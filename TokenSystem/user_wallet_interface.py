"""
FURBX User Wallet Interface - Interactive Dashboard
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Complete Wallet Management Interface
"""

from typing import Dict
import datetime
from decimal import Decimal
import logging

from token_logic import get_token_system
from wallet_manager import get_wallet_manager
from staking_module import get_staking_system
from marketplace_integration import get_marketplace_integration

logger = logging.getLogger(__name__)

class UserWalletInterface:
    """
    Complete User Wallet Interface for FURBX Token System
    Provides unified access to all wallet, staking, and marketplace functions
    """
    
    def __init__(self):
        self.token_system = get_token_system()
        self.wallet_manager = get_wallet_manager()
        self.staking_system = get_staking_system()
        self.marketplace = get_marketplace_integration()
        
        logger.info("👛 User Wallet Interface initialized")
    
    def get_dashboard_data(self, user_id: str) -> Dict:
        """Get complete dashboard data for user wallet interface"""
        try:
            # Get basic wallet information
            wallet_info = self.wallet_manager.get_wallet_info(user_id)
            
            if not wallet_info['success']:
                return wallet_info
            
            # Get staking information
            staking_info = self.staking_system.get_user_stakes(user_id)
            
            # Get marketplace earnings (for creators)
            creator_earnings = self.marketplace.get_creator_earnings(user_id, days=30)
            
            # Calculate portfolio overview
            wallet_data = wallet_info['wallet']
            portfolio = {
                'total_portfolio_value': {
                    'fbx': wallet_data['total_balance'],
                    'usd': wallet_data['usd_value']
                },
                'available_balance': {
                    'fbx': wallet_data['available_balance'],
                    'usd': wallet_data['available_balance'] * self.token_system.config['exchange_rates']['usd_per_fbx']
                },
                'staked_balance': {
                    'fbx': wallet_data['staked_balance'],
                    'usd': wallet_data['staked_balance'] * self.token_system.config['exchange_rates']['usd_per_fbx']
                },
                'pending_rewards': {
                    'fbx': staking_info.get('summary', {}).get('total_pending_rewards', 0) if staking_info.get('success') else 0,
                    'usd': (staking_info.get('summary', {}).get('total_pending_rewards', 0) * 
                           self.token_system.config['exchange_rates']['usd_per_fbx']) if staking_info.get('success') else 0
                }
            }
            
            # Recent activity summary
            recent_activity = self._format_recent_activity(
                wallet_info.get('recent_transactions', []),
                limit=5
            )
            
            # Quick stats
            quick_stats = {
                'total_transactions': wallet_info.get('stats', {}).get('total_transactions', 0),
                'account_age_days': wallet_info.get('stats', {}).get('account_age_days', 0),
                'premium_status': wallet_data['premium_status'],
                'referral_count': wallet_data['referral_count'],
                'active_stakes': staking_info.get('summary', {}).get('total_active_stakes', 0) if staking_info.get('success') else 0,
                'creator_earnings_30d': creator_earnings.get('earnings_summary', {}).get('total_earnings', 0) if creator_earnings.get('success') else 0
            }
            
            # Staking overview
            staking_overview = {
                'active_positions': staking_info.get('summary', {}).get('total_active_stakes', 0) if staking_info.get('success') else 0,
                'total_staked': staking_info.get('summary', {}).get('total_staked', 0) if staking_info.get('success') else 0,
                'estimated_daily_rewards': staking_info.get('summary', {}).get('estimated_daily_rewards', 0) if staking_info.get('success') else 0,
                'total_rewards_earned': staking_info.get('summary', {}).get('total_accumulated_rewards', 0) if staking_info.get('success') else 0
            }
            
            return {
                'success': True,
                'user_id': user_id,
                'portfolio': portfolio,
                'quick_stats': quick_stats,
                'staking_overview': staking_overview,
                'recent_activity': recent_activity,
                'exchange_rates': self.token_system.config['exchange_rates'],
                'last_updated': datetime.datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Dashboard data error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to load dashboard data'
            }
    
    def transfer_interface(self, from_user: str, to_user: str, amount: float, description: str = "") -> Dict:
        """Process token transfer with enhanced interface feedback"""
        try:
            # Pre-transfer validation and fee calculation
            amount_decimal = Decimal(str(amount))
            fee = amount_decimal * Decimal(str(self.token_system.config['economic_parameters']['transfer_fee']))
            total_cost = amount_decimal + fee
            
            # Check balance
            sender_wallet = self.token_system.get_balance(from_user)
            if sender_wallet.available_balance < total_cost:
                return {
                    'success': False,
                    'error': 'Insufficient balance',
                    'details': {
                        'required': float(total_cost),
                        'available': float(sender_wallet.available_balance),
                        'shortage': float(total_cost - sender_wallet.available_balance)
                    },
                    'message': f'Need {float(total_cost)} FBX total (including {float(fee)} FBX fee)'
                }
            
            # Execute transfer
            result = self.wallet_manager.transfer_tokens(from_user, to_user, amount, description)
            
            if result['success']:
                # Get updated balances
                sender_balance = self.token_system.get_balance(from_user)
                recipient_balance = self.token_system.get_balance(to_user)
                
                result['balance_updates'] = {
                    'sender_new_balance': float(sender_balance.available_balance),
                    'recipient_new_balance': float(recipient_balance.available_balance)
                }
            
            return result
            
        except Exception as e:
            logger.error(f"Transfer interface error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Transfer processing failed'
            }
    
    def staking_interface(self, user_id: str, action: str, **kwargs) -> Dict:
        """Unified staking interface for all staking operations"""
        try:
            if action == 'get_pools':
                return self.staking_system.get_available_pools()
            
            elif action == 'stake':
                pool_type = kwargs.get('pool_type')
                amount = kwargs.get('amount')
                lock_duration = kwargs.get('lock_duration', 0)
                
                if not all([pool_type, amount]):
                    return {
                        'success': False,
                        'error': 'Missing required parameters',
                        'message': 'Pool type and amount are required'
                    }
                
                return self.staking_system.stake_tokens(user_id, pool_type, amount, lock_duration)
            
            elif action == 'unstake':
                stake_id = kwargs.get('stake_id')
                partial_amount = kwargs.get('partial_amount')
                
                if not stake_id:
                    return {
                        'success': False,
                        'error': 'Missing stake ID',
                        'message': 'Stake ID is required for unstaking'
                    }
                
                return self.staking_system.unstake_tokens(user_id, stake_id, partial_amount)
            
            elif action == 'claim_rewards':
                stake_id = kwargs.get('stake_id')  # Optional - if None, claims all
                return self.staking_system.claim_rewards(user_id, stake_id)
            
            elif action == 'compound':
                stake_id = kwargs.get('stake_id')
                
                if not stake_id:
                    return {
                        'success': False,
                        'error': 'Missing stake ID',
                        'message': 'Stake ID is required for compounding'
                    }
                
                return self.staking_system.compound_rewards(user_id, stake_id)
            
            elif action == 'get_positions':
                return self.staking_system.get_user_stakes(user_id)
            
            else:
                return {
                    'success': False,
                    'error': f'Unknown action: {action}',
                    'message': 'Invalid staking action'
                }
            
        except Exception as e:
            logger.error(f"Staking interface error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Staking operation failed'
            }
    
    def marketplace_interface(self, user_id: str, action: str, **kwargs) -> Dict:
        """Unified marketplace interface for all marketplace operations"""
        try:
            if action == 'purchase_content':
                content_type = kwargs.get('content_type')
                creator_id = kwargs.get('creator_id')
                price = kwargs.get('price')
                
                if not all([content_type, creator_id, price]):
                    return {
                        'success': False,
                        'error': 'Missing required parameters',
                        'message': 'Content type, creator ID, and price are required'
                    }
                
                return self.marketplace.purchase_premium_content(user_id, content_type, creator_id, price)
            
            elif action == 'tip_creator':
                creator_id = kwargs.get('creator_id')
                amount = kwargs.get('amount')
                message = kwargs.get('message', '')
                
                if not all([creator_id, amount]):
                    return {
                        'success': False,
                        'error': 'Missing required parameters',
                        'message': 'Creator ID and amount are required'
                    }
                
                return self.marketplace.tip_creator(user_id, creator_id, amount, message)
            
            elif action == 'list_content':
                content_info = kwargs.get('content_info')
                
                if not content_info:
                    return {
                        'success': False,
                        'error': 'Missing content information',
                        'message': 'Content info is required for listing'
                    }
                
                return self.marketplace.list_premium_content(user_id, content_info)
            
            elif action == 'get_earnings':
                days = kwargs.get('days', 30)
                return self.marketplace.get_creator_earnings(user_id, days)
            
            else:
                return {
                    'success': False,
                    'error': f'Unknown action: {action}',
                    'message': 'Invalid marketplace action'
                }
            
        except Exception as e:
            logger.error(f"Marketplace interface error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Marketplace operation failed'
            }
    
    def convert_tokens(self, user_id: str, conversion_type: str, amount: float) -> Dict:
        """Convert FBX tokens to other currencies or credits"""
        try:
            if conversion_type == 'to_fantasy_credits':
                return self.wallet_manager.convert_to_fantasy_credits(user_id, amount)
            
            elif conversion_type == 'to_usd_estimate':
                # This would integrate with external exchange in real system
                fbx_amount = Decimal(str(amount))
                usd_rate = Decimal(str(self.token_system.config['exchange_rates']['usd_per_fbx']))
                usd_value = fbx_amount * usd_rate
                
                return {
                    'success': True,
                    'conversion_type': 'usd_estimate',
                    'fbx_amount': float(fbx_amount),
                    'usd_value': float(usd_value),
                    'exchange_rate': float(usd_rate),
                    'note': 'This is an estimated value. Actual exchange rates may vary.'
                }
            
            else:
                return {
                    'success': False,
                    'error': f'Unknown conversion type: {conversion_type}',
                    'message': 'Invalid conversion type'
                }
            
        except Exception as e:
            logger.error(f"Token conversion error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Token conversion failed'
            }
    
    def get_transaction_history(self, user_id: str, filters: Dict = None) -> Dict:
        """Get formatted transaction history with filtering options"""
        try:
            filters = filters or {}
            
            page = filters.get('page', 1)
            limit = filters.get('limit', 20)
            tx_type = filters.get('type')
            date_from = filters.get('date_from')
            date_to = filters.get('date_to')
            
            # Get transactions from wallet manager
            history = self.wallet_manager.get_transaction_history(user_id, page, limit, tx_type)
            
            if not history['success']:
                return history
            
            # Apply additional date filtering if specified
            if date_from or date_to:
                filtered_transactions = []
                
                for tx in history['transactions']:
                    tx_date = datetime.datetime.fromisoformat(tx['timestamp']).date()
                    
                    include_tx = True
                    if date_from:
                        from_date = datetime.datetime.fromisoformat(date_from).date()
                        if tx_date < from_date:
                            include_tx = False
                    
                    if date_to:
                        to_date = datetime.datetime.fromisoformat(date_to).date()
                        if tx_date > to_date:
                            include_tx = False
                    
                    if include_tx:
                        filtered_transactions.append(tx)
                
                history['transactions'] = filtered_transactions
                history['pagination']['total_transactions'] = len(filtered_transactions)
            
            # Add enhanced formatting
            for tx in history['transactions']:
                tx['formatted_timestamp'] = datetime.datetime.fromisoformat(tx['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
                tx['usd_value'] = tx['amount'] * self.token_system.config['exchange_rates']['usd_per_fbx']
                
                # Add transaction category
                tx['category'] = self._categorize_transaction(tx)
            
            return history
            
        except Exception as e:
            logger.error(f"Transaction history error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve transaction history'
            }
    
    def get_analytics_dashboard(self, user_id: str) -> Dict:
        """Get comprehensive user analytics dashboard"""
        try:
            # Get wallet analytics
            wallet_analytics = self.wallet_manager.get_wallet_analytics(user_id, days=30)
            
            # Get marketplace earnings if creator
            creator_data = self.marketplace.get_creator_earnings(user_id, days=30)
            
            # Get staking analytics
            staking_data = self.staking_system.get_user_stakes(user_id)
            
            # Compile comprehensive analytics
            analytics = {
                'wallet_health': wallet_analytics.get('analytics', {}).get('wallet_health_score', 0),
                'transaction_trends': wallet_analytics.get('analytics', {}).get('daily_activity', {}),
                'earning_breakdown': {
                    'staking_rewards': staking_data.get('summary', {}).get('total_accumulated_rewards', 0) if staking_data.get('success') else 0,
                    'creator_earnings': creator_data.get('earnings_summary', {}).get('total_earnings', 0) if creator_data.get('success') else 0,
                    'referral_bonuses': 0,  # Would calculate from transaction history
                    'other_rewards': 0
                },
                'spending_breakdown': {
                    'transfers': 0,
                    'premium_purchases': 0,
                    'marketplace_tips': 0,
                    'staking_fees': 0
                }
            }
            
            # Calculate spending breakdown from transaction history
            recent_transactions = self.token_system.get_user_transactions(user_id, limit=100)
            for tx in recent_transactions:
                if tx['from_user'] == user_id:
                    tx_type = tx['transaction_type']
                    amount = float(tx['amount'])
                    
                    if tx_type == 'transfer':
                        analytics['spending_breakdown']['transfers'] += amount
                    elif tx_type == 'purchase':
                        analytics['spending_breakdown']['premium_purchases'] += amount
                    elif 'tip' in tx.get('description', '').lower():
                        analytics['spending_breakdown']['marketplace_tips'] += amount
            
            return {
                'success': True,
                'user_id': user_id,
                'analytics': analytics,
                'generated_at': datetime.datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Analytics dashboard error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to generate analytics dashboard'
            }
    
    def _format_recent_activity(self, transactions, limit: int = 5) -> list:
        """Format recent transactions for dashboard display"""
        formatted_activity = []
        
        for tx in transactions[:limit]:
            activity = {
                'id': tx.get('id', ''),
                'type': tx.get('type', ''),
                'direction': tx.get('direction', ''),
                'amount': tx.get('amount', 0),
                'description': tx.get('description', ''),
                'timestamp': tx.get('formatted_timestamp', tx.get('timestamp', '')),
                'status': tx.get('confirmation_status', 'confirmed'),
                'icon': self._get_transaction_icon(tx.get('type', '')),
                'color': self._get_transaction_color(tx.get('direction', ''))
            }
            formatted_activity.append(activity)
        
        return formatted_activity
    
    def _categorize_transaction(self, tx: Dict) -> str:
        """Categorize transaction for better user understanding"""
        tx_type = tx.get('type', '')
        description = tx.get('description', '').lower()
        
        if tx_type == 'reward':
            return 'Rewards'
        elif tx_type == 'transfer':
            return 'Transfer'
        elif tx_type == 'purchase':
            return 'Purchase'
        elif tx_type == 'stake':
            return 'Staking'
        elif tx_type == 'unstake':
            return 'Unstaking'
        elif 'tip' in description:
            return 'Creator Tip'
        elif 'referral' in description:
            return 'Referral Bonus'
        elif 'welcome' in description:
            return 'Welcome Bonus'
        else:
            return 'Other'
    
    def _get_transaction_icon(self, tx_type: str) -> str:
        """Get appropriate icon for transaction type"""
        icon_map = {
            'reward': '🎁',
            'transfer': '↔️',
            'purchase': '🛒',
            'stake': '🥩',
            'unstake': '📤',
            'mint': '🏭',
            'burn': '🔥'
        }
        return icon_map.get(tx_type, '💰')
    
    def _get_transaction_color(self, direction: str) -> str:
        """Get appropriate color for transaction direction"""
        color_map = {
            'incoming': 'green',
            'outgoing': 'red',
            'neutral': 'blue'
        }
        return color_map.get(direction, 'gray')

# Global user wallet interface instance
user_wallet_interface = None

def get_user_wallet_interface() -> UserWalletInterface:
    """Get global user wallet interface instance"""
    global user_wallet_interface
    if user_wallet_interface is None:
        user_wallet_interface = UserWalletInterface()
    return user_wallet_interface

if __name__ == "__main__":
    # Test the user wallet interface
    logging.basicConfig(level=logging.INFO)
    
    wallet_ui = UserWalletInterface()
    
    print("=== FURBX User Wallet Interface Test ===")
    
    # Test dashboard
    dashboard = wallet_ui.get_dashboard_data("test_user_1")
    print(f"Dashboard: {dashboard}")
    
    # Test staking interface
    pools = wallet_ui.staking_interface("test_user_1", "get_pools")
    print(f"Staking pools: {pools}")
    
    # Test analytics
    analytics = wallet_ui.get_analytics_dashboard("test_user_1")
    print(f"Analytics: {analytics}")
    
    print("\n👛 User Wallet Interface test completed")