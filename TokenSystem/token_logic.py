"""
FURBX Token Logic - Core Tokenization System
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Advanced Token Management
"""

import json
import datetime
import uuid
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from decimal import Decimal, getcontext
import logging

# Set decimal precision for financial calculations
getcontext().prec = 18

logger = logging.getLogger(__name__)

@dataclass
class Transaction:
    """Represents a token transaction"""
    id: str
    from_user: str
    to_user: str
    amount: Decimal
    transaction_type: str  # 'transfer', 'mint', 'burn', 'reward', 'purchase', 'stake', 'unstake'
    description: str
    timestamp: datetime.datetime
    fee: Decimal = Decimal('0')
    block_height: int = 0
    confirmation_status: str = 'confirmed'
    metadata: Dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

@dataclass
class TokenBalance:
    """Represents user token balance and stats"""
    user_id: str
    available_balance: Decimal
    staked_balance: Decimal
    locked_balance: Decimal
    total_earned: Decimal
    total_spent: Decimal
    last_activity: datetime.datetime
    referral_count: int = 0
    premium_status: bool = False

    @property
    def total_balance(self) -> Decimal:
        return self.available_balance + self.staked_balance + self.locked_balance

class FurbyToken:
    """
    Core FURBX Token Management System
    Handles all token operations, economics, and business logic
    """
    
    def __init__(self, config_path: str = "TokenSystem/token_config.json"):
        self.config = self._load_config(config_path)
        self.balances: Dict[str, TokenBalance] = {}
        self.transactions: List[Transaction] = []
        self.total_supply = Decimal(str(self.config['token_info']['initial_supply']))
        self.circulating_supply = Decimal('0')
        self.burned_supply = Decimal('0')
        self.current_block = 1
        
        # Initialize system wallets
        self._initialize_system_wallets()
        
        logger.info(f"🪙 FURBX Token System initialized with {self.total_supply} FBX total supply")
    
    def _load_config(self, config_path: str) -> Dict:
        """Load token configuration"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """Default configuration if file not found"""
        return {
            "token_info": {
                "initial_supply": 1000000,
                "max_supply": 10000000
            },
            "exchange_rates": {
                "fantasy_credits_per_fbx": 100,
                "usd_per_fbx": 0.10
            },
            "economic_parameters": {
                "transfer_fee": 0.01,
                "daily_mint_limit": 1000
            }
        }
    
    def _initialize_system_wallets(self):
        """Initialize system wallets for platform operations"""
        system_wallets = [
            'treasury',
            'rewards_pool', 
            'staking_pool',
            'marketplace_fees',
            'burn_address',
            'development_fund'
        ]
        
        for wallet in system_wallets:
            if wallet not in self.balances:
                self.balances[wallet] = TokenBalance(
                    user_id=wallet,
                    available_balance=Decimal('0'),
                    staked_balance=Decimal('0'),
                    locked_balance=Decimal('0'),
                    total_earned=Decimal('0'),
                    total_spent=Decimal('0'),
                    last_activity=datetime.datetime.now()
                )
        
        # Allocate initial distribution
        initial_allocations = {
            'treasury': Decimal('500000'),      # 50% - Treasury
            'rewards_pool': Decimal('200000'),  # 20% - User rewards
            'staking_pool': Decimal('150000'),  # 15% - Staking rewards
            'marketplace_fees': Decimal('50000'), # 5% - Marketplace operations
            'development_fund': Decimal('100000') # 10% - Development
        }
        
        for wallet, amount in initial_allocations.items():
            self.balances[wallet].available_balance = amount
            self.circulating_supply += amount
    
    def create_user_wallet(self, user_id: str) -> TokenBalance:
        """Create a new user wallet"""
        if user_id in self.balances:
            return self.balances[user_id]
        
        wallet = TokenBalance(
            user_id=user_id,
            available_balance=Decimal('0'),
            staked_balance=Decimal('0'),
            locked_balance=Decimal('0'),
            total_earned=Decimal('0'),
            total_spent=Decimal('0'),
            last_activity=datetime.datetime.now()
        )
        
        self.balances[user_id] = wallet
        
        # Welcome bonus for new users
        welcome_bonus = Decimal('10')
        self._internal_transfer('rewards_pool', user_id, welcome_bonus, 'welcome_bonus', 'Welcome bonus for new user')
        
        logger.info(f"🎁 Created new wallet for {user_id} with {welcome_bonus} FBX welcome bonus")
        return wallet
    
    def get_balance(self, user_id: str) -> TokenBalance:
        """Get user balance information"""
        if user_id not in self.balances:
            return self.create_user_wallet(user_id)
        return self.balances[user_id]
    
    def transfer(self, from_user: str, to_user: str, amount: Decimal, description: str = "Transfer") -> Tuple[bool, str]:
        """Transfer tokens between users"""
        try:
            amount = Decimal(str(amount))
            
            # Validation
            if from_user not in self.balances:
                return False, "Sender wallet not found"
            
            if to_user not in self.balances:
                self.create_user_wallet(to_user)
            
            # Calculate fee
            fee = amount * Decimal(str(self.config['economic_parameters']['transfer_fee']))
            total_deduction = amount + fee
            
            if self.balances[from_user].available_balance < total_deduction:
                return False, "Insufficient balance"
            
            # Execute transfer
            self.balances[from_user].available_balance -= total_deduction
            self.balances[to_user].available_balance += amount
            self.balances['treasury'].available_balance += fee  # Fees go to treasury
            
            # Record transaction
            transaction = Transaction(
                id=str(uuid.uuid4()),
                from_user=from_user,
                to_user=to_user,
                amount=amount,
                transaction_type='transfer',
                description=description,
                timestamp=datetime.datetime.now(),
                fee=fee,
                block_height=self.current_block
            )
            
            self.transactions.append(transaction)
            self.current_block += 1
            
            # Update user stats
            self.balances[from_user].total_spent += amount
            self.balances[to_user].total_earned += amount
            self.balances[from_user].last_activity = datetime.datetime.now()
            self.balances[to_user].last_activity = datetime.datetime.now()
            
            logger.info(f"💰 Transfer: {amount} FBX from {from_user} to {to_user} (fee: {fee})")
            return True, f"Successfully transferred {amount} FBX"
            
        except Exception as e:
            logger.error(f"Transfer error: {e}")
            return False, f"Transfer failed: {str(e)}"
    
    def _internal_transfer(self, from_wallet: str, to_wallet: str, amount: Decimal, tx_type: str, description: str) -> bool:
        """Internal transfer without fees (for system operations)"""
        try:
            amount = Decimal(str(amount))
            
            if from_wallet not in self.balances or to_wallet not in self.balances:
                if to_wallet not in self.balances:
                    self.create_user_wallet(to_wallet)
                if from_wallet not in self.balances:
                    return False
            
            if self.balances[from_wallet].available_balance < amount:
                return False
            
            self.balances[from_wallet].available_balance -= amount
            self.balances[to_wallet].available_balance += amount
            
            # Record transaction
            transaction = Transaction(
                id=str(uuid.uuid4()),
                from_user=from_wallet,
                to_user=to_wallet,
                amount=amount,
                transaction_type=tx_type,
                description=description,
                timestamp=datetime.datetime.now(),
                block_height=self.current_block
            )
            
            self.transactions.append(transaction)
            self.current_block += 1
            
            # Update stats for user wallets (not system wallets)
            if not from_wallet.startswith(('treasury', 'rewards_pool', 'staking_pool', 'marketplace_fees', 'burn_address', 'development_fund')):
                self.balances[from_wallet].total_spent += amount
                self.balances[from_wallet].last_activity = datetime.datetime.now()
            
            if not to_wallet.startswith(('treasury', 'rewards_pool', 'staking_pool', 'marketplace_fees', 'burn_address', 'development_fund')):
                self.balances[to_wallet].total_earned += amount
                self.balances[to_wallet].last_activity = datetime.datetime.now()
            
            return True
            
        except Exception as e:
            logger.error(f"Internal transfer error: {e}")
            return False
    
    def mint_tokens(self, to_user: str, amount: Decimal, reason: str) -> Tuple[bool, str]:
        """Mint new tokens (admin function)"""
        try:
            amount = Decimal(str(amount))
            
            # Check daily mint limit
            today = datetime.date.today()
            daily_minted = sum(
                tx.amount for tx in self.transactions 
                if tx.transaction_type == 'mint' and tx.timestamp.date() == today
            )
            
            daily_limit = Decimal(str(self.config['economic_parameters']['daily_mint_limit']))
            if daily_minted + amount > daily_limit:
                return False, f"Daily mint limit exceeded ({daily_limit} FBX)"
            
            # Check max supply
            if self.total_supply + amount > Decimal(str(self.config['token_info']['max_supply'])):
                return False, "Max supply exceeded"
            
            # Create wallet if needed
            if to_user not in self.balances:
                self.create_user_wallet(to_user)
            
            # Mint tokens
            self.balances[to_user].available_balance += amount
            self.total_supply += amount
            self.circulating_supply += amount
            
            # Record transaction
            transaction = Transaction(
                id=str(uuid.uuid4()),
                from_user='system',
                to_user=to_user,
                amount=amount,
                transaction_type='mint',
                description=f"Minted tokens: {reason}",
                timestamp=datetime.datetime.now(),
                block_height=self.current_block
            )
            
            self.transactions.append(transaction)
            self.current_block += 1
            
            # Update user stats
            self.balances[to_user].total_earned += amount
            self.balances[to_user].last_activity = datetime.datetime.now()
            
            logger.info(f"🏭 Minted {amount} FBX to {to_user}: {reason}")
            return True, f"Successfully minted {amount} FBX"
            
        except Exception as e:
            logger.error(f"Mint error: {e}")
            return False, f"Mint failed: {str(e)}"
    
    def burn_tokens(self, from_user: str, amount: Decimal, reason: str) -> Tuple[bool, str]:
        """Burn tokens (remove from circulation)"""
        try:
            amount = Decimal(str(amount))
            
            if from_user not in self.balances:
                return False, "User wallet not found"
            
            if self.balances[from_user].available_balance < amount:
                return False, "Insufficient balance"
            
            # Burn tokens
            self.balances[from_user].available_balance -= amount
            self.burned_supply += amount
            self.circulating_supply -= amount
            
            # Record transaction
            transaction = Transaction(
                id=str(uuid.uuid4()),
                from_user=from_user,
                to_user='burn_address',
                amount=amount,
                transaction_type='burn',
                description=f"Burned tokens: {reason}",
                timestamp=datetime.datetime.now(),
                block_height=self.current_block
            )
            
            self.transactions.append(transaction)
            self.current_block += 1
            
            # Update user stats
            self.balances[from_user].total_spent += amount
            self.balances[from_user].last_activity = datetime.datetime.now()
            
            logger.info(f"🔥 Burned {amount} FBX from {from_user}: {reason}")
            return True, f"Successfully burned {amount} FBX"
            
        except Exception as e:
            logger.error(f"Burn error: {e}")
            return False, f"Burn failed: {str(e)}"
    
    def reward_user(self, user_id: str, reward_type: str, multiplier: Decimal = Decimal('1')) -> Tuple[bool, str]:
        """Reward user with tokens based on activity"""
        try:
            if reward_type not in self.config['reward_tiers']:
                return False, f"Unknown reward type: {reward_type}"
            
            base_amount = Decimal(str(self.config['reward_tiers'][reward_type]))
            amount = base_amount * multiplier
            
            # Check if rewards pool has enough balance
            if self.balances['rewards_pool'].available_balance < amount:
                return False, "Rewards pool insufficient"
            
            success = self._internal_transfer(
                'rewards_pool', 
                user_id, 
                amount, 
                'reward', 
                f"Reward for {reward_type}"
            )
            
            if success:
                return True, f"Rewarded {amount} FBX for {reward_type}"
            else:
                return False, "Reward transfer failed"
                
        except Exception as e:
            logger.error(f"Reward error: {e}")
            return False, f"Reward failed: {str(e)}"
    
    def purchase_premium_feature(self, user_id: str, feature: str) -> Tuple[bool, str]:
        """Purchase premium features with FBX"""
        try:
            if feature not in self.config['premium_features']:
                return False, f"Unknown premium feature: {feature}"
            
            cost = Decimal(str(self.config['premium_features'][feature]))
            
            if user_id not in self.balances:
                return False, "User wallet not found"
            
            if self.balances[user_id].available_balance < cost:
                return False, f"Insufficient balance. Need {cost} FBX"
            
            # Process purchase
            success = self._internal_transfer(
                user_id,
                'treasury',
                cost,
                'purchase',
                f"Purchased {feature}"
            )
            
            if success:
                # Mark user as premium if applicable
                if feature in ['vip_access', 'custom_furby']:
                    self.balances[user_id].premium_status = True
                
                return True, f"Successfully purchased {feature} for {cost} FBX"
            else:
                return False, "Purchase transaction failed"
                
        except Exception as e:
            logger.error(f"Purchase error: {e}")
            return False, f"Purchase failed: {str(e)}"
    
    def get_user_transactions(self, user_id: str, limit: int = 50) -> List[Dict]:
        """Get user transaction history"""
        user_txs = [
            tx for tx in self.transactions 
            if tx.from_user == user_id or tx.to_user == user_id
        ]
        
        # Sort by timestamp (newest first) and limit
        user_txs.sort(key=lambda x: x.timestamp, reverse=True)
        return [asdict(tx) for tx in user_txs[:limit]]
    
    def get_system_stats(self) -> Dict:
        """Get overall system statistics"""
        active_users = len([
            user_id for user_id, balance in self.balances.items()
            if not user_id.startswith(('treasury', 'rewards_pool', 'staking_pool', 'marketplace_fees', 'burn_address', 'development_fund'))
            and balance.total_balance > 0
        ])
        
        total_user_balance = sum(
            balance.total_balance for user_id, balance in self.balances.items()
            if not user_id.startswith(('treasury', 'rewards_pool', 'staking_pool', 'marketplace_fees', 'burn_address', 'development_fund'))
        )
        
        return {
            'total_supply': float(self.total_supply),
            'circulating_supply': float(self.circulating_supply),
            'burned_supply': float(self.burned_supply),
            'active_users': active_users,
            'total_user_balance': float(total_user_balance),
            'total_transactions': len(self.transactions),
            'current_block': self.current_block,
            'treasury_balance': float(self.balances['treasury'].available_balance),
            'rewards_pool_balance': float(self.balances['rewards_pool'].available_balance),
            'staking_pool_balance': float(self.balances['staking_pool'].available_balance),
            'exchange_rate_usd': self.config['exchange_rates']['usd_per_fbx'],
            'last_transaction': self.transactions[-1].timestamp.isoformat() if self.transactions else None
        }
    
    def export_balances(self) -> Dict:
        """Export all user balances"""
        return {
            user_id: asdict(balance) 
            for user_id, balance in self.balances.items()
        }
    
    def save_state(self, filepath: str = "TokenSystem/token_state.json"):
        """Save current token system state"""
        try:
            state = {
                'balances': {user_id: asdict(balance) for user_id, balance in self.balances.items()},
                'transactions': [asdict(tx) for tx in self.transactions],
                'total_supply': float(self.total_supply),
                'circulating_supply': float(self.circulating_supply),
                'burned_supply': float(self.burned_supply),
                'current_block': self.current_block,
                'last_saved': datetime.datetime.now().isoformat()
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, default=str)
            
            logger.info(f"💾 Token system state saved to {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Save state error: {e}")
            return False
    
    def load_state(self, filepath: str = "TokenSystem/token_state.json"):
        """Load token system state"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            # Restore balances
            self.balances = {}
            for user_id, balance_data in state.get('balances', {}).items():
                balance_data['last_activity'] = datetime.datetime.fromisoformat(balance_data['last_activity'])
                self.balances[user_id] = TokenBalance(**balance_data)
            
            # Restore transactions
            self.transactions = []
            for tx_data in state.get('transactions', []):
                tx_data['timestamp'] = datetime.datetime.fromisoformat(tx_data['timestamp'])
                tx_data['amount'] = Decimal(str(tx_data['amount']))
                tx_data['fee'] = Decimal(str(tx_data['fee']))
                self.transactions.append(Transaction(**tx_data))
            
            # Restore system state
            self.total_supply = Decimal(str(state.get('total_supply', 1000000)))
            self.circulating_supply = Decimal(str(state.get('circulating_supply', 0)))
            self.burned_supply = Decimal(str(state.get('burned_supply', 0)))
            self.current_block = state.get('current_block', 1)
            
            logger.info(f"📂 Token system state loaded from {filepath}")
            return True
            
        except FileNotFoundError:
            logger.info("No saved state found, starting fresh")
            return False
        except Exception as e:
            logger.error(f"Load state error: {e}")
            return False

# Global token system instance
token_system = None

def get_token_system() -> FurbyToken:
    """Get global token system instance"""
    global token_system
    if token_system is None:
        token_system = FurbyToken()
        # Try to load saved state
        token_system.load_state()
    return token_system

def initialize_token_system():
    """Initialize the global token system"""
    global token_system
    token_system = FurbyToken()
    token_system.load_state()
    return token_system

if __name__ == "__main__":
    # Test the token system
    logging.basicConfig(level=logging.INFO)
    
    token = FurbyToken()
    
    # Create test users
    user1 = "user_alice"
    user2 = "user_bob"
    
    # Test basic operations
    print("=== FURBX Token System Test ===")
    
    # Create wallets
    wallet1 = token.create_user_wallet(user1)
    wallet2 = token.create_user_wallet(user2)
    
    print(f"Alice balance: {wallet1.total_balance} FBX")
    print(f"Bob balance: {wallet2.total_balance} FBX")
    
    # Test rewards
    success, msg = token.reward_user(user1, "daily_login")
    print(f"Daily login reward: {msg}")
    
    # Test transfer
    success, msg = token.transfer(user1, user2, Decimal('5'), "Test transfer")
    print(f"Transfer result: {msg}")
    
    # Test premium purchase
    success, msg = token.purchase_premium_feature(user1, "voice_packs")
    print(f"Premium purchase: {msg}")
    
    # Show final balances
    print(f"\nFinal balances:")
    print(f"Alice: {token.get_balance(user1).total_balance} FBX")
    print(f"Bob: {token.get_balance(user2).total_balance} FBX")
    
    # Show system stats
    stats = token.get_system_stats()
    print(f"\nSystem stats: {stats}")
    
    # Save state
    token.save_state()
    print("\n💾 State saved successfully")