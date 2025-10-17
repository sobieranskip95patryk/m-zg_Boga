"""
FURBX Marketplace Integration - Economic Ecosystem Interface
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Marketplace Token Integration
"""

import datetime
from typing import Dict
from decimal import Decimal
import logging
import uuid

from token_logic import get_token_system
from wallet_manager import get_wallet_manager

logger = logging.getLogger(__name__)

class MarketplaceIntegration:
    """
    FURBX Marketplace Integration System
    Handles marketplace transactions, creator payments, and platform economics
    """
    
    def __init__(self):
        self.token_system = get_token_system()
        self.wallet_manager = get_wallet_manager()
        
        # Load marketplace configuration
        self.marketplace_config = self.token_system.config.get('marketplace', {})
        
        # Transaction tracking
        self.marketplace_transactions = []
        
        logger.info("🛒 Marketplace Integration initialized")
    
    def purchase_premium_content(self, user_id: str, content_type: str, creator_id: str, price: float) -> Dict:
        """Purchase premium content with FBX tokens"""
        try:
            price_decimal = Decimal(str(price))
            
            # Validation
            if price_decimal <= 0:
                return {
                    'success': False,
                    'error': 'Price must be positive',
                    'message': 'Invalid purchase price'
                }
            
            # Check user balance
            wallet = self.token_system.get_balance(user_id)
            if wallet.available_balance < price_decimal:
                return {
                    'success': False,
                    'error': 'Insufficient FBX balance',
                    'message': f'Need {float(price_decimal)} FBX to purchase'
                }
            
            # Calculate distribution
            platform_fee = price_decimal * Decimal(str(self.marketplace_config.get('platform_fee_rate', 0.30)))
            creator_share = price_decimal * Decimal(str(self.marketplace_config.get('creator_revenue_share', 0.70)))
            
            # Process payment
            # 1. User pays total amount
            success = self.token_system._internal_transfer(
                user_id,
                'marketplace_fees',
                price_decimal,
                'purchase',
                f'Purchased {content_type} from {creator_id}'
            )
            
            if not success:
                return {
                    'success': False,
                    'error': 'Payment processing failed',
                    'message': 'Transaction could not be completed'
                }
            
            # 2. Distribute to creator
            creator_payment_success = self.token_system._internal_transfer(
                'marketplace_fees',
                creator_id,
                creator_share,
                'creator_payment',
                f'Creator payment for {content_type}'
            )
            
            # 3. Keep platform fee in marketplace_fees wallet
            # (Already there from step 1, just need to account for it)
            
            # Record marketplace transaction
            transaction_record = {
                'id': str(uuid.uuid4()),
                'type': 'content_purchase',
                'buyer_id': user_id,
                'creator_id': creator_id,
                'content_type': content_type,
                'total_price': float(price_decimal),
                'creator_share': float(creator_share),
                'platform_fee': float(platform_fee),
                'timestamp': datetime.datetime.now().isoformat(),
                'status': 'completed' if creator_payment_success else 'partial'
            }
            
            self.marketplace_transactions.append(transaction_record)
            
            logger.info(f"🛒 Purchase: {user_id} bought {content_type} from {creator_id} for {price_decimal} FBX")
            
            return {
                'success': True,
                'message': f'Successfully purchased {content_type}',
                'transaction_id': transaction_record['id'],
                'total_paid': float(price_decimal),
                'creator_received': float(creator_share),
                'platform_fee': float(platform_fee)
            }
            
        except Exception as e:
            logger.error(f"Purchase error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Purchase processing failed'
            }
    
    def list_premium_content(self, creator_id: str, content_info: Dict) -> Dict:
        """List premium content for sale"""
        try:
            # Validation
            required_fields = ['title', 'description', 'price', 'content_type']
            for field in required_fields:
                if field not in content_info:
                    return {
                        'success': False,
                        'error': f'Missing required field: {field}',
                        'message': 'Invalid content listing'
                    }
            
            price = Decimal(str(content_info['price']))
            if price <= 0:
                return {
                    'success': False,
                    'error': 'Price must be positive',
                    'message': 'Invalid content price'
                }
            
            # Check if creator has premium status for certain content types
            creator_wallet = self.token_system.get_balance(creator_id)
            premium_content_types = ['custom_furby', 'exclusive_voice_pack', 'special_animation']
            
            if content_info['content_type'] in premium_content_types and not creator_wallet.premium_status:
                return {
                    'success': False,
                    'error': 'Premium status required to list this content type',
                    'message': 'Upgrade to premium to list premium content'
                }
            
            # Create content listing
            listing = {
                'id': str(uuid.uuid4()),
                'creator_id': creator_id,
                'title': content_info['title'],
                'description': content_info['description'],
                'content_type': content_info['content_type'],
                'price': float(price),
                'created_at': datetime.datetime.now().isoformat(),
                'status': 'active',
                'sales_count': 0,
                'total_revenue': 0.0,
                'tags': content_info.get('tags', []),
                'preview_url': content_info.get('preview_url'),
                'difficulty_level': content_info.get('difficulty_level', 'beginner')
            }
            
            logger.info(f"📝 Listed content: {creator_id} - {content_info['title']} ({price} FBX)")
            
            return {
                'success': True,
                'message': 'Content listed successfully',
                'listing_id': listing['id'],
                'listing': listing
            }
            
        except Exception as e:
            logger.error(f"Content listing error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Content listing failed'
            }
    
    def tip_creator(self, tipper_id: str, creator_id: str, amount: float, message: str = "") -> Dict:
        """Send tips to content creators"""
        try:
            tip_amount = Decimal(str(amount))
            
            # Validation
            if tip_amount <= 0:
                return {
                    'success': False,
                    'error': 'Tip amount must be positive',
                    'message': 'Invalid tip amount'
                }
            
            if tipper_id == creator_id:
                return {
                    'success': False,
                    'error': 'Cannot tip yourself',
                    'message': 'Invalid tip recipient'
                }
            
            # Check minimum tip
            min_tip = Decimal(str(self.marketplace_config.get('minimum_tip', 0.10)))
            if tip_amount < min_tip:
                return {
                    'success': False,
                    'error': f'Minimum tip is {min_tip} FBX',
                    'message': 'Tip amount too small'
                }
            
            # Check balance
            tipper_wallet = self.token_system.get_balance(tipper_id)
            if tipper_wallet.available_balance < tip_amount:
                return {
                    'success': False,
                    'error': 'Insufficient balance for tip',
                    'message': 'Cannot tip more than available balance'
                }
            
            # Calculate platform fee for tips (smaller than purchases)
            tip_fee_rate = Decimal(str(self.marketplace_config.get('tip_fee_rate', 0.05)))  # 5% for tips
            platform_fee = tip_amount * tip_fee_rate
            creator_receives = tip_amount - platform_fee
            
            # Process tip
            success = self.token_system.transfer(
                tipper_id,
                creator_id,
                creator_receives,
                f'Tip: {message}' if message else 'Creator tip'
            )
            
            if success[0]:
                # Additional platform fee
                fee_success = self.token_system._internal_transfer(
                    tipper_id,
                    'marketplace_fees',
                    platform_fee,
                    'tip_fee',
                    'Platform tip fee'
                )
                
                # Record tip transaction
                tip_record = {
                    'id': str(uuid.uuid4()),
                    'type': 'creator_tip',
                    'tipper_id': tipper_id,
                    'creator_id': creator_id,
                    'tip_amount': float(tip_amount),
                    'creator_received': float(creator_receives),
                    'platform_fee': float(platform_fee),
                    'message': message,
                    'timestamp': datetime.datetime.now().isoformat()
                }
                
                self.marketplace_transactions.append(tip_record)
                
                logger.info(f"💝 Tip: {tipper_id} tipped {creator_id} {tip_amount} FBX")
                
                return {
                    'success': True,
                    'message': f'Successfully tipped {float(creator_receives)} FBX to creator',
                    'transaction_id': tip_record['id'],
                    'tip_amount': float(tip_amount),
                    'creator_received': float(creator_receives),
                    'platform_fee': float(platform_fee)
                }
            else:
                return {
                    'success': False,
                    'error': success[1],
                    'message': 'Tip processing failed'
                }
            
        except Exception as e:
            logger.error(f"Tip error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Tip processing failed'
            }
    
    def get_creator_earnings(self, creator_id: str, days: int = 30) -> Dict:
        """Get creator earnings summary"""
        try:
            # Get creator transactions from token system
            creator_transactions = self.token_system.get_user_transactions(creator_id, limit=1000)
            
            # Filter earnings in date range
            cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
            earnings_transactions = [
                tx for tx in creator_transactions
                if datetime.datetime.fromisoformat(tx['timestamp']) > cutoff_date
                and tx['to_user'] == creator_id
                and tx['transaction_type'] in ['creator_payment', 'reward']
            ]
            
            # Get marketplace transactions for this creator
            marketplace_earnings = [
                tx for tx in self.marketplace_transactions
                if tx['creator_id'] == creator_id
                and datetime.datetime.fromisoformat(tx['timestamp']) > cutoff_date
            ]
            
            # Calculate earnings breakdown
            total_earnings = sum(float(tx['amount']) for tx in earnings_transactions)
            content_sales = sum(tx['creator_share'] for tx in marketplace_earnings if tx['type'] == 'content_purchase')
            tips_received = sum(tx['creator_received'] for tx in marketplace_earnings if tx['type'] == 'creator_tip')
            
            # Calculate statistics
            unique_buyers = len(set(
                tx['buyer_id'] if 'buyer_id' in tx else tx['tipper_id']
                for tx in marketplace_earnings
            ))
            
            total_sales = len([tx for tx in marketplace_earnings if tx['type'] == 'content_purchase'])
            total_tips = len([tx for tx in marketplace_earnings if tx['type'] == 'creator_tip'])
            
            earnings_summary = {
                'period_days': days,
                'total_earnings': total_earnings,
                'content_sales_revenue': content_sales,
                'tips_received': tips_received,
                'other_earnings': total_earnings - content_sales - tips_received,
                'total_transactions': len(earnings_transactions),
                'content_sales_count': total_sales,
                'tips_count': total_tips,
                'unique_supporters': unique_buyers,
                'average_transaction': total_earnings / len(earnings_transactions) if earnings_transactions else 0,
                'average_sale_price': content_sales / total_sales if total_sales > 0 else 0,
                'average_tip': tips_received / total_tips if total_tips > 0 else 0
            }
            
            # Daily breakdown
            daily_earnings = {}
            for tx in earnings_transactions:
                date = datetime.datetime.fromisoformat(tx['timestamp']).date().isoformat()
                if date not in daily_earnings:
                    daily_earnings[date] = 0
                daily_earnings[date] += float(tx['amount'])
            
            return {
                'success': True,
                'creator_id': creator_id,
                'earnings_summary': earnings_summary,
                'daily_earnings': daily_earnings,
                'recent_transactions': earnings_transactions[:10]  # Last 10 earnings
            }
            
        except Exception as e:
            logger.error(f"Creator earnings error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve creator earnings'
            }
    
    def process_referral_bonus(self, referrer_id: str, referred_id: str, purchase_amount: float) -> Dict:
        """Process referral bonus when referred user makes purchase"""
        try:
            purchase_decimal = Decimal(str(purchase_amount))
            
            # Calculate referral bonus (5% of purchase amount)
            bonus_rate = Decimal(str(self.marketplace_config.get('referral_bonus_rate', 0.05)))
            referral_bonus = purchase_decimal * bonus_rate
            
            # Minimum and maximum bonus limits
            min_bonus = Decimal(str(self.marketplace_config.get('min_referral_bonus', 0.01)))
            max_bonus = Decimal(str(self.marketplace_config.get('max_referral_bonus', 10.0)))
            
            referral_bonus = max(min_bonus, min(referral_bonus, max_bonus))
            
            # Give bonus to referrer
            success = self.token_system._internal_transfer(
                'rewards_pool',
                referrer_id,
                referral_bonus,
                'referral_bonus',
                f'Referral bonus for {referred_id} purchase'
            )
            
            if success:
                # Update referrer stats
                if referrer_id in self.token_system.balances:
                    self.token_system.balances[referrer_id].referral_count += 1
                
                logger.info(f"🤝 Referral bonus: {referral_bonus} FBX to {referrer_id} for {referred_id}")
                
                return {
                    'success': True,
                    'message': f'Referral bonus of {float(referral_bonus)} FBX awarded',
                    'bonus_amount': float(referral_bonus),
                    'referrer_id': referrer_id,
                    'referred_id': referred_id
                }
            else:
                return {
                    'success': False,
                    'error': 'Bonus transfer failed',
                    'message': 'Could not process referral bonus'
                }
            
        except Exception as e:
            logger.error(f"Referral bonus error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Referral bonus processing failed'
            }
    
    def get_marketplace_analytics(self) -> Dict:
        """Get comprehensive marketplace analytics"""
        try:
            # Calculate analytics from transactions
            total_transactions = len(self.marketplace_transactions)
            total_volume = sum(tx.get('total_price', 0) for tx in self.marketplace_transactions)
            
            content_purchases = [tx for tx in self.marketplace_transactions if tx['type'] == 'content_purchase']
            tips = [tx for tx in self.marketplace_transactions if tx['type'] == 'creator_tip']
            
            # Creator analytics
            unique_creators = len(set(tx['creator_id'] for tx in self.marketplace_transactions))
            unique_buyers = len(set(
                tx.get('buyer_id') or tx.get('tipper_id') for tx in self.marketplace_transactions
            ))
            
            # Revenue analytics
            total_creator_revenue = sum(tx.get('creator_share', 0) + tx.get('creator_received', 0) for tx in self.marketplace_transactions)
            total_platform_fees = sum(tx.get('platform_fee', 0) for tx in self.marketplace_transactions)
            
            analytics = {
                'total_transactions': total_transactions,
                'total_volume_fbx': total_volume,
                'total_volume_usd': total_volume * self.token_system.config['exchange_rates']['usd_per_fbx'],
                'content_purchases': {
                    'count': len(content_purchases),
                    'volume': sum(tx['total_price'] for tx in content_purchases),
                    'average_price': sum(tx['total_price'] for tx in content_purchases) / len(content_purchases) if content_purchases else 0
                },
                'tips': {
                    'count': len(tips),
                    'volume': sum(tx['tip_amount'] for tx in tips),
                    'average_tip': sum(tx['tip_amount'] for tx in tips) / len(tips) if tips else 0
                },
                'creators': {
                    'unique_creators': unique_creators,
                    'total_revenue': total_creator_revenue,
                    'average_revenue_per_creator': total_creator_revenue / unique_creators if unique_creators > 0 else 0
                },
                'buyers': {
                    'unique_buyers': unique_buyers,
                    'average_spend_per_buyer': total_volume / unique_buyers if unique_buyers > 0 else 0
                },
                'platform': {
                    'total_fees_collected': total_platform_fees,
                    'fee_percentage_of_volume': (total_platform_fees / total_volume * 100) if total_volume > 0 else 0
                }
            }
            
            # Top content types
            content_type_sales = {}
            for tx in content_purchases:
                content_type = tx.get('content_type', 'unknown')
                if content_type not in content_type_sales:
                    content_type_sales[content_type] = {'count': 0, 'revenue': 0}
                content_type_sales[content_type]['count'] += 1
                content_type_sales[content_type]['revenue'] += tx['total_price']
            
            analytics['top_content_types'] = dict(sorted(
                content_type_sales.items(),
                key=lambda x: x[1]['revenue'],
                reverse=True
            )[:5])
            
            return {
                'success': True,
                'analytics': analytics,
                'last_updated': datetime.datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Marketplace analytics error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to generate marketplace analytics'
            }

# Global marketplace integration instance
marketplace_integration = None

def get_marketplace_integration() -> MarketplaceIntegration:
    """Get global marketplace integration instance"""
    global marketplace_integration
    if marketplace_integration is None:
        marketplace_integration = MarketplaceIntegration()
    return marketplace_integration

if __name__ == "__main__":
    # Test the marketplace integration
    logging.basicConfig(level=logging.INFO)
    
    marketplace = MarketplaceIntegration()
    
    print("=== FURBX Marketplace Integration Test ===")
    
    # Test content listing
    listing_result = marketplace.list_premium_content("creator_1", {
        'title': 'Custom Furby Voice Pack',
        'description': 'Unique voice pack for your AI Furby',
        'price': 15.0,
        'content_type': 'voice_pack',
        'tags': ['voice', 'premium', 'custom']
    })
    print(f"Content listing: {listing_result}")
    
    # Test purchase
    purchase_result = marketplace.purchase_premium_content(
        "buyer_1", 
        "voice_pack", 
        "creator_1", 
        15.0
    )
    print(f"Purchase: {purchase_result}")
    
    # Test creator earnings
    earnings = marketplace.get_creator_earnings("creator_1")
    print(f"Creator earnings: {earnings}")
    
    # Test analytics
    analytics = marketplace.get_marketplace_analytics()
    print(f"Marketplace analytics: {analytics}")
    
    print("\n🛒 Marketplace Integration test completed")