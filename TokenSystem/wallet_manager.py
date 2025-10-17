"""
FURBX Wallet Manager - User Balance and Transaction Management
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Advanced Wallet Interface
"""

import json
import datetime
from typing import Dict, List, Tuple
from decimal import Decimal
import logging
from dataclasses import asdict

from token_logic import get_token_system, TokenBalance, Transaction

logger = logging.getLogger(__name__)

class WalletManager:
    """
    Advanced Wallet Management System for FURBX Tokens
    Handles user wallets, transactions, and balance operations
    """
    
    def __init__(self):
        self.token_system = get_token_system()
        logger.info("🏦 Wallet Manager initialized")
    
    def create_wallet(self, user_id: str, initial_data: Dict = None) -> Dict:
        """Create new user wallet with optional initial data"""
        try:
            # Create wallet in token system
            wallet = self.token_system.create_user_wallet(user_id)
            
            # Process initial data if provided
            if initial_data:
                if 'referral_code' in initial_data:
                    self._process_referral(user_id, initial_data['referral_code'])
                
                if 'welcome_bonus' in initial_data and initial_data['welcome_bonus']:
                    self._apply_welcome_bonus(user_id)
            
            return {
                'success': True,
                'wallet': self._format_wallet_data(wallet),
                'message': f'Wallet created for {user_id}'
            }
            
        except Exception as e:
            logger.error(f"Wallet creation error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to create wallet'
            }
    
    def get_wallet_info(self, user_id: str) -> Dict:
        """Get comprehensive wallet information"""
        try:
            wallet = self.token_system.get_balance(user_id)
            recent_transactions = self.token_system.get_user_transactions(user_id, limit=10)
            
            # Calculate additional stats
            stats = self._calculate_wallet_stats(user_id, wallet)
            
            return {
                'success': True,
                'wallet': self._format_wallet_data(wallet),
                'recent_transactions': recent_transactions,
                'stats': stats,
                'exchange_rates': self.token_system.config['exchange_rates']
            }
            
        except Exception as e:
            logger.error(f"Wallet info error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve wallet information'
            }
    
    def transfer_tokens(self, from_user: str, to_user: str, amount: float, description: str = "") -> Dict:
        """Transfer tokens between users with validation"""
        try:
            amount_decimal = Decimal(str(amount))
            
            # Validation
            if amount_decimal <= 0:
                return {
                    'success': False,
                    'error': 'Amount must be positive',
                    'message': 'Invalid transfer amount'
                }
            
            if from_user == to_user:
                return {
                    'success': False,
                    'error': 'Cannot transfer to yourself',
                    'message': 'Invalid transfer recipient'
                }
            
            # Check minimum transfer amount
            min_transfer = Decimal('0.01')
            if amount_decimal < min_transfer:
                return {
                    'success': False,
                    'error': f'Minimum transfer amount is {min_transfer} FBX',
                    'message': 'Transfer amount too small'
                }
            
            # Execute transfer
            success, message = self.token_system.transfer(from_user, to_user, amount_decimal, description)
            
            if success:
                # Log transfer for analytics
                self._log_transfer_activity(from_user, to_user, amount_decimal)
                
                return {
                    'success': True,
                    'message': message,
                    'transaction_id': self.token_system.transactions[-1].id,
                    'fee': float(self.token_system.transactions[-1].fee)
                }
            else:
                return {
                    'success': False,
                    'error': message,
                    'message': 'Transfer failed'
                }
                
        except Exception as e:
            logger.error(f"Transfer error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Transfer processing failed'
            }
    
    def get_transaction_history(self, user_id: str, page: int = 1, limit: int = 20, tx_type: str = None) -> Dict:
        """Get paginated transaction history with filtering"""
        try:
            # Get all user transactions
            all_transactions = self.token_system.get_user_transactions(user_id, limit=1000)
            
            # Filter by transaction type if specified
            if tx_type:
                all_transactions = [
                    tx for tx in all_transactions 
                    if tx['transaction_type'] == tx_type
                ]
            
            # Pagination
            start_index = (page - 1) * limit
            end_index = start_index + limit
            transactions = all_transactions[start_index:end_index]
            
            # Format transactions
            formatted_transactions = []
            for tx in transactions:
                formatted_tx = self._format_transaction(tx, user_id)
                formatted_transactions.append(formatted_tx)
            
            return {
                'success': True,
                'transactions': formatted_transactions,
                'pagination': {
                    'current_page': page,
                    'total_pages': (len(all_transactions) + limit - 1) // limit,
                    'total_transactions': len(all_transactions),
                    'has_next': end_index < len(all_transactions),
                    'has_previous': page > 1
                }
            }
            
        except Exception as e:
            logger.error(f"Transaction history error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve transaction history'
            }
    
    def convert_to_fantasy_credits(self, user_id: str, fbx_amount: float) -> Dict:
        """Convert FBX to Fantasy Credits"""
        try:
            fbx_decimal = Decimal(str(fbx_amount))
            
            if fbx_decimal <= 0:
                return {
                    'success': False,
                    'error': 'Amount must be positive',
                    'message': 'Invalid conversion amount'
                }
            
            # Check balance
            wallet = self.token_system.get_balance(user_id)
            if wallet.available_balance < fbx_decimal:
                return {
                    'success': False,
                    'error': 'Insufficient FBX balance',
                    'message': 'Cannot convert more than available balance'
                }
            
            # Calculate conversion
            conversion_rate = Decimal(str(self.token_system.config['exchange_rates']['fantasy_credits_per_fbx']))
            fantasy_credits = fbx_decimal * conversion_rate
            
            # Process conversion (burn FBX)
            success, message = self.token_system.burn_tokens(
                user_id, 
                fbx_decimal, 
                f"Converted to {fantasy_credits} Fantasy Credits"
            )
            
            if success:
                # In a real system, you would credit the fantasy credits to their game account
                # For now, we'll just record the conversion
                
                return {
                    'success': True,
                    'message': f'Converted {fbx_amount} FBX to {float(fantasy_credits)} Fantasy Credits',
                    'fbx_burned': float(fbx_decimal),
                    'fantasy_credits_received': float(fantasy_credits),
                    'conversion_rate': float(conversion_rate)
                }
            else:
                return {
                    'success': False,
                    'error': message,
                    'message': 'Conversion failed'
                }
                
        except Exception as e:
            logger.error(f"Conversion error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Conversion processing failed'
            }
    
    def get_wallet_analytics(self, user_id: str, days: int = 30) -> Dict:
        """Get wallet analytics and insights"""
        try:
            wallet = self.token_system.get_balance(user_id)
            
            # Get transactions in date range
            cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
            recent_transactions = [
                tx for tx in self.token_system.get_user_transactions(user_id, limit=1000)
                if datetime.datetime.fromisoformat(tx['timestamp']) > cutoff_date
            ]
            
            # Calculate analytics
            analytics = {
                'period_days': days,
                'total_transactions': len(recent_transactions),
                'incoming_transactions': len([tx for tx in recent_transactions if tx['to_user'] == user_id]),
                'outgoing_transactions': len([tx for tx in recent_transactions if tx['from_user'] == user_id]),
                'total_received': sum(
                    float(tx['amount']) for tx in recent_transactions 
                    if tx['to_user'] == user_id and tx['transaction_type'] != 'transfer'
                ),
                'total_sent': sum(
                    float(tx['amount']) for tx in recent_transactions 
                    if tx['from_user'] == user_id
                ),
                'total_fees_paid': sum(
                    float(tx['fee']) for tx in recent_transactions 
                    if tx['from_user'] == user_id
                ),
                'reward_earnings': sum(
                    float(tx['amount']) for tx in recent_transactions 
                    if tx['to_user'] == user_id and tx['transaction_type'] == 'reward'
                ),
                'premium_purchases': sum(
                    float(tx['amount']) for tx in recent_transactions 
                    if tx['from_user'] == user_id and tx['transaction_type'] == 'purchase'
                )
            }
            
            # Calculate trends
            if len(recent_transactions) > 0:
                # Daily activity
                daily_activity = {}
                for tx in recent_transactions:
                    date = datetime.datetime.fromisoformat(tx['timestamp']).date().isoformat()
                    if date not in daily_activity:
                        daily_activity[date] = 0
                    daily_activity[date] += 1
                
                analytics['daily_activity'] = daily_activity
                analytics['most_active_day'] = max(daily_activity.items(), key=lambda x: x[1])
                analytics['average_daily_transactions'] = len(recent_transactions) / days
            
            # Transaction type breakdown
            tx_types = {}
            for tx in recent_transactions:
                tx_type = tx['transaction_type']
                if tx_type not in tx_types:
                    tx_types[tx_type] = 0
                tx_types[tx_type] += 1
            
            analytics['transaction_types'] = tx_types
            
            # Wallet health score (0-100)
            health_score = self._calculate_wallet_health(wallet, analytics)
            analytics['wallet_health_score'] = health_score
            
            return {
                'success': True,
                'analytics': analytics,
                'current_balance': self._format_wallet_data(wallet)
            }
            
        except Exception as e:
            logger.error(f"Analytics error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to generate analytics'
            }
    
    def _format_wallet_data(self, wallet: TokenBalance) -> Dict:
        """Format wallet data for API response"""
        return {
            'user_id': wallet.user_id,
            'available_balance': float(wallet.available_balance),
            'staked_balance': float(wallet.staked_balance),
            'locked_balance': float(wallet.locked_balance),
            'total_balance': float(wallet.total_balance),
            'total_earned': float(wallet.total_earned),
            'total_spent': float(wallet.total_spent),
            'last_activity': wallet.last_activity.isoformat(),
            'referral_count': wallet.referral_count,
            'premium_status': wallet.premium_status,
            'usd_value': float(wallet.total_balance) * self.token_system.config['exchange_rates']['usd_per_fbx']
        }
    
    def _format_transaction(self, tx: Dict, user_id: str) -> Dict:
        """Format transaction for user display"""
        is_incoming = tx['to_user'] == user_id
        
        return {
            'id': tx['id'],
            'type': tx['transaction_type'],
            'direction': 'incoming' if is_incoming else 'outgoing',
            'amount': float(tx['amount']),
            'fee': float(tx['fee']) if not is_incoming else 0,
            'description': tx['description'],
            'timestamp': tx['timestamp'],
            'confirmation_status': tx['confirmation_status'],
            'other_party': tx['from_user'] if is_incoming else tx['to_user'],
            'block_height': tx['block_height']
        }
    
    def _calculate_wallet_stats(self, user_id: str, wallet: TokenBalance) -> Dict:
        """Calculate additional wallet statistics"""
        # Get all transactions
        all_transactions = self.token_system.get_user_transactions(user_id, limit=1000)
        
        # Calculate stats
        total_transactions = len(all_transactions)
        incoming_count = len([tx for tx in all_transactions if tx['to_user'] == user_id])
        outgoing_count = len([tx for tx in all_transactions if tx['from_user'] == user_id])
        
        # Account age
        if all_transactions:
            first_transaction = min(all_transactions, key=lambda x: x['timestamp'])
            account_age_days = (
                datetime.datetime.now() - 
                datetime.datetime.fromisoformat(first_transaction['timestamp'])
            ).days
        else:
            account_age_days = 0
        
        return {
            'total_transactions': total_transactions,
            'incoming_transactions': incoming_count,
            'outgoing_transactions': outgoing_count,
            'account_age_days': account_age_days,
            'average_balance': float(wallet.total_balance) / max(account_age_days, 1),
            'transaction_frequency': total_transactions / max(account_age_days, 1)
        }
    
    def _calculate_wallet_health(self, wallet: TokenBalance, analytics: Dict) -> int:
        """Calculate wallet health score (0-100)"""
        score = 50  # Base score
        
        # Balance score (0-25)
        if wallet.total_balance > 100:
            score += 25
        elif wallet.total_balance > 50:
            score += 20
        elif wallet.total_balance > 10:
            score += 15
        elif wallet.total_balance > 0:
            score += 10
        
        # Activity score (0-25)
        if analytics.get('total_transactions', 0) > 50:
            score += 25
        elif analytics.get('total_transactions', 0) > 20:
            score += 20
        elif analytics.get('total_transactions', 0) > 10:
            score += 15
        elif analytics.get('total_transactions', 0) > 0:
            score += 10
        
        # Diversification score (0-25)
        tx_types = len(analytics.get('transaction_types', {}))
        if tx_types >= 4:
            score += 25
        elif tx_types >= 3:
            score += 20
        elif tx_types >= 2:
            score += 15
        elif tx_types >= 1:
            score += 10
        
        # Premium features usage (0-25)
        if wallet.premium_status:
            score += 25
        elif analytics.get('premium_purchases', 0) > 0:
            score += 15
        
        return min(100, max(0, score))
    
    def _process_referral(self, user_id: str, referral_code: str):
        """Process referral bonus"""
        try:
            # In a real system, you would validate the referral code
            # For now, we'll assume it's valid and give both users a bonus
            
            referrer_id = f"referrer_{referral_code}"  # Simplified for demo
            
            # Bonus for new user
            self.token_system.reward_user(user_id, "referral_signup")
            
            # Bonus for referrer (if they exist)
            if referrer_id in self.token_system.balances:
                self.token_system.reward_user(referrer_id, "successful_referral")
                self.token_system.balances[referrer_id].referral_count += 1
            
            logger.info(f"🤝 Processed referral: {user_id} referred by {referral_code}")
            
        except Exception as e:
            logger.error(f"Referral processing error: {e}")
    
    def _apply_welcome_bonus(self, user_id: str):
        """Apply additional welcome bonus"""
        try:
            # Additional welcome bonus beyond the standard one
            bonus_amount = Decimal('5')
            success = self.token_system._internal_transfer(
                'rewards_pool',
                user_id,
                bonus_amount,
                'welcome_bonus',
                'Additional welcome bonus'
            )
            
            if success:
                logger.info(f"🎁 Applied welcome bonus: {bonus_amount} FBX to {user_id}")
            
        except Exception as e:
            logger.error(f"Welcome bonus error: {e}")
    
    def _log_transfer_activity(self, from_user: str, to_user: str, amount: Decimal):
        """Log transfer activity for analytics"""
        try:
            # In a real system, you would log this to an analytics database
            logger.info(f"📊 Transfer activity: {from_user} -> {to_user}, {amount} FBX")
            
        except Exception as e:
            logger.error(f"Activity logging error: {e}")

# Global wallet manager instance
wallet_manager = None

def get_wallet_manager() -> WalletManager:
    """Get global wallet manager instance"""
    global wallet_manager
    if wallet_manager is None:
        wallet_manager = WalletManager()
    return wallet_manager

if __name__ == "__main__":
    # Test the wallet manager
    logging.basicConfig(level=logging.INFO)
    
    wm = WalletManager()
    
    # Test wallet creation
    print("=== FURBX Wallet Manager Test ===")
    
    result = wm.create_wallet("test_user_1", {'welcome_bonus': True})
    print(f"Wallet creation: {result}")
    
    # Test wallet info
    info = wm.get_wallet_info("test_user_1")
    print(f"Wallet info: {info}")
    
    # Test transfer
    wm.create_wallet("test_user_2")
    transfer_result = wm.transfer_tokens("test_user_1", "test_user_2", 5.0, "Test transfer")
    print(f"Transfer result: {transfer_result}")
    
    # Test analytics
    analytics = wm.get_wallet_analytics("test_user_1")
    print(f"Analytics: {analytics}")
    
    print("\n💼 Wallet Manager test completed")