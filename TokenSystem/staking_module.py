"""
FURBX Staking & Rewards System - Advanced Token Staking Engine
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Staking Pool Management
"""

import datetime
from typing import Dict, List
from decimal import Decimal, getcontext
import logging
from dataclasses import dataclass, asdict
import uuid

from token_logic import get_token_system

# Set decimal precision for financial calculations
getcontext().prec = 18

logger = logging.getLogger(__name__)

@dataclass
class StakePosition:
    """Represents a user's staking position"""
    id: str
    user_id: str
    pool_type: str  # 'basic', 'premium', 'vip'
    amount: Decimal
    start_date: datetime.datetime
    last_reward_claim: datetime.datetime
    accumulated_rewards: Decimal
    is_active: bool = True
    lock_duration: int = 0  # days
    multiplier: Decimal = Decimal('1.0')

    @property
    def days_staked(self) -> int:
        return (datetime.datetime.now() - self.start_date).days

    @property
    def is_locked(self) -> bool:
        if self.lock_duration == 0:
            return False
        return self.days_staked < self.lock_duration

class StakingSystem:
    """
    Advanced FURBX Staking System
    Manages staking pools, rewards calculation, and user positions
    """
    
    def __init__(self):
        self.token_system = get_token_system()
        self.stake_positions: Dict[str, StakePosition] = {}
        self.last_reward_distribution = datetime.datetime.now()
        
        # Load staking configuration
        self.pools_config = self.token_system.config.get('staking_pools', {})
        
        logger.info("🥩 Staking System initialized")
    
    def get_available_pools(self) -> Dict:
        """Get information about available staking pools"""
        try:
            pools = {}
            for pool_name, config in self.pools_config.items():
                # Calculate current statistics
                active_stakes = [
                    stake for stake in self.stake_positions.values()
                    if stake.pool_type == pool_name and stake.is_active
                ]
                
                total_staked = sum(stake.amount for stake in active_stakes)
                total_stakers = len(active_stakes)
                
                pools[pool_name] = {
                    'name': pool_name,
                    'apy': config['apy'],
                    'min_stake': config['minimum_stake'],
                    'lock_duration': config.get('lock_duration', 0),
                    'rewards_frequency': config.get('rewards_frequency', 'daily'),
                    'total_staked': float(total_staked),
                    'total_stakers': total_stakers,
                    'is_active': config.get('is_active', True),
                    'special_benefits': config.get('special_benefits', []),
                    'multiplier_bonus': config.get('multiplier_bonus', 1.0)
                }
            
            return {
                'success': True,
                'pools': pools,
                'total_staked_across_all_pools': float(sum(
                    stake.amount for stake in self.stake_positions.values() 
                    if stake.is_active
                )),
                'total_active_stakers': len(set(
                    stake.user_id for stake in self.stake_positions.values() 
                    if stake.is_active
                ))
            }
            
        except Exception as e:
            logger.error(f"Get pools error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve pool information'
            }
    
    def stake_tokens(self, user_id: str, pool_type: str, amount: float, lock_duration: int = 0) -> Dict:
        """Stake tokens in specified pool"""
        try:
            amount_decimal = Decimal(str(amount))
            
            # Validation
            if pool_type not in self.pools_config:
                return {
                    'success': False,
                    'error': f'Unknown pool type: {pool_type}',
                    'message': 'Invalid staking pool'
                }
            
            pool_config = self.pools_config[pool_type]
            
            # Check minimum stake amount
            min_stake = Decimal(str(pool_config['minimum_stake']))
            if amount_decimal < min_stake:
                return {
                    'success': False,
                    'error': f'Minimum stake for {pool_type} pool is {min_stake} FBX',
                    'message': 'Stake amount too low'
                }
            
            # Check user balance
            wallet = self.token_system.get_balance(user_id)
            if wallet.available_balance < amount_decimal:
                return {
                    'success': False,
                    'error': 'Insufficient available balance',
                    'message': 'Cannot stake more than available balance'
                }
            
            # Check pool requirements
            if pool_type == 'premium' and not wallet.premium_status:
                return {
                    'success': False,
                    'error': 'Premium pool requires premium status',
                    'message': 'Upgrade to premium to access this pool'
                }
            
            if pool_type == 'vip' and wallet.total_balance < Decimal('1000'):
                return {
                    'success': False,
                    'error': 'VIP pool requires minimum 1000 FBX total balance',
                    'message': 'Insufficient balance for VIP pool'
                }
            
            # Move tokens from available to staked
            self.token_system.balances[user_id].available_balance -= amount_decimal
            self.token_system.balances[user_id].staked_balance += amount_decimal
            
            # Calculate multiplier
            multiplier = Decimal(str(pool_config.get('multiplier_bonus', 1.0)))
            if lock_duration > 0:
                # Additional bonus for locking
                lock_bonus = Decimal('0.1') * Decimal(str(lock_duration)) / Decimal('365')  # 10% per year
                multiplier += lock_bonus
            
            # Create stake position
            stake_position = StakePosition(
                id=str(uuid.uuid4()),
                user_id=user_id,
                pool_type=pool_type,
                amount=amount_decimal,
                start_date=datetime.datetime.now(),
                last_reward_claim=datetime.datetime.now(),
                accumulated_rewards=Decimal('0'),
                lock_duration=lock_duration,
                multiplier=multiplier
            )
            
            self.stake_positions[stake_position.id] = stake_position
            
            # Record staking transaction
            self.token_system._internal_transfer(
                user_id,
                'staking_pool',
                amount_decimal,
                'stake',
                f'Staked in {pool_type} pool'
            )
            
            logger.info(f"🥩 Staked {amount_decimal} FBX: {user_id} -> {pool_type} pool")
            
            return {
                'success': True,
                'message': f'Successfully staked {amount} FBX in {pool_type} pool',
                'stake_id': stake_position.id,
                'pool_type': pool_type,
                'amount_staked': float(amount_decimal),
                'estimated_daily_rewards': float(self._calculate_daily_rewards(stake_position)),
                'multiplier': float(multiplier),
                'lock_duration': lock_duration
            }
            
        except Exception as e:
            logger.error(f"Staking error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Staking operation failed'
            }
    
    def unstake_tokens(self, user_id: str, stake_id: str, partial_amount: float = None) -> Dict:
        """Unstake tokens from a position"""
        try:
            if stake_id not in self.stake_positions:
                return {
                    'success': False,
                    'error': 'Stake position not found',
                    'message': 'Invalid stake ID'
                }
            
            stake = self.stake_positions[stake_id]
            
            if stake.user_id != user_id:
                return {
                    'success': False,
                    'error': 'Unauthorized access to stake position',
                    'message': 'Access denied'
                }
            
            if not stake.is_active:
                return {
                    'success': False,
                    'error': 'Stake position is not active',
                    'message': 'Cannot unstake inactive position'
                }
            
            # Check lock period
            if stake.is_locked:
                remaining_days = stake.lock_duration - stake.days_staked
                return {
                    'success': False,
                    'error': f'Position is locked for {remaining_days} more days',
                    'message': 'Cannot unstake during lock period'
                }
            
            # Determine unstake amount
            if partial_amount is None:
                unstake_amount = stake.amount
                is_full_unstake = True
            else:
                unstake_amount = Decimal(str(partial_amount))
                is_full_unstake = False
                
                if unstake_amount > stake.amount:
                    return {
                        'success': False,
                        'error': 'Cannot unstake more than staked amount',
                        'message': 'Invalid unstake amount'
                    }
            
            # Calculate and claim pending rewards first
            pending_rewards = self._calculate_pending_rewards(stake)
            if pending_rewards > 0:
                self._distribute_rewards_to_user(user_id, pending_rewards, 'staking_rewards')
            
            # Move tokens back to available balance
            self.token_system.balances[user_id].available_balance += unstake_amount
            self.token_system.balances[user_id].staked_balance -= unstake_amount
            
            # Update or remove stake position
            if is_full_unstake:
                stake.is_active = False
                stake.accumulated_rewards += pending_rewards
            else:
                stake.amount -= unstake_amount
                stake.last_reward_claim = datetime.datetime.now()
            
            # Record unstaking transaction
            self.token_system._internal_transfer(
                'staking_pool',
                user_id,
                unstake_amount,
                'unstake',
                f'Unstaked from {stake.pool_type} pool'
            )
            
            logger.info(f"📤 Unstaked {unstake_amount} FBX: {user_id} from {stake.pool_type} pool")
            
            return {
                'success': True,
                'message': f'Successfully unstaked {float(unstake_amount)} FBX',
                'unstaked_amount': float(unstake_amount),
                'rewards_claimed': float(pending_rewards),
                'remaining_staked': float(stake.amount) if not is_full_unstake else 0,
                'position_closed': is_full_unstake
            }
            
        except Exception as e:
            logger.error(f"Unstaking error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Unstaking operation failed'
            }
    
    def claim_rewards(self, user_id: str, stake_id: str = None) -> Dict:
        """Claim staking rewards"""
        try:
            if stake_id:
                # Claim rewards for specific stake
                if stake_id not in self.stake_positions:
                    return {
                        'success': False,
                        'error': 'Stake position not found',
                        'message': 'Invalid stake ID'
                    }
                
                stake = self.stake_positions[stake_id]
                if stake.user_id != user_id or not stake.is_active:
                    return {
                        'success': False,
                        'error': 'Invalid stake position',
                        'message': 'Cannot claim rewards for this position'
                    }
                
                positions_to_claim = [stake]
            else:
                # Claim rewards for all user's active stakes
                positions_to_claim = [
                    stake for stake in self.stake_positions.values()
                    if stake.user_id == user_id and stake.is_active
                ]
            
            if not positions_to_claim:
                return {
                    'success': False,
                    'error': 'No active stake positions found',
                    'message': 'Nothing to claim'
                }
            
            total_rewards = Decimal('0')
            claimed_positions = []
            
            for stake in positions_to_claim:
                pending_rewards = self._calculate_pending_rewards(stake)
                if pending_rewards > 0:
                    total_rewards += pending_rewards
                    stake.accumulated_rewards += pending_rewards
                    stake.last_reward_claim = datetime.datetime.now()
                    
                    claimed_positions.append({
                        'stake_id': stake.id,
                        'pool_type': stake.pool_type,
                        'rewards': float(pending_rewards)
                    })
            
            if total_rewards > 0:
                # Distribute rewards
                self._distribute_rewards_to_user(user_id, total_rewards, 'staking_rewards')
                
                logger.info(f"💰 Claimed {total_rewards} FBX rewards: {user_id}")
                
                return {
                    'success': True,
                    'message': f'Successfully claimed {float(total_rewards)} FBX in rewards',
                    'total_rewards': float(total_rewards),
                    'claimed_positions': claimed_positions
                }
            else:
                return {
                    'success': False,
                    'error': 'No rewards available to claim',
                    'message': 'All rewards are up to date'
                }
            
        except Exception as e:
            logger.error(f"Claim rewards error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Reward claiming failed'
            }
    
    def get_user_stakes(self, user_id: str) -> Dict:
        """Get all stake positions for a user"""
        try:
            user_stakes = [
                stake for stake in self.stake_positions.values()
                if stake.user_id == user_id
            ]
            
            # Format stake data
            stakes_data = []
            total_staked = Decimal('0')
            total_pending_rewards = Decimal('0')
            
            for stake in user_stakes:
                pending_rewards = self._calculate_pending_rewards(stake) if stake.is_active else Decimal('0')
                if stake.is_active:
                    total_staked += stake.amount
                    total_pending_rewards += pending_rewards
                
                estimated_daily = self._calculate_daily_rewards(stake) if stake.is_active else Decimal('0')
                
                stakes_data.append({
                    'stake_id': stake.id,
                    'pool_type': stake.pool_type,
                    'amount': float(stake.amount),
                    'start_date': stake.start_date.isoformat(),
                    'days_staked': stake.days_staked,
                    'is_active': stake.is_active,
                    'is_locked': stake.is_locked,
                    'lock_duration': stake.lock_duration,
                    'pending_rewards': float(pending_rewards),
                    'accumulated_rewards': float(stake.accumulated_rewards),
                    'estimated_daily_rewards': float(estimated_daily),
                    'multiplier': float(stake.multiplier),
                    'last_reward_claim': stake.last_reward_claim.isoformat()
                })
            
            return {
                'success': True,
                'stakes': stakes_data,
                'summary': {
                    'total_active_stakes': len([s for s in user_stakes if s.is_active]),
                    'total_staked': float(total_staked),
                    'total_pending_rewards': float(total_pending_rewards),
                    'total_accumulated_rewards': float(sum(stake.accumulated_rewards for stake in user_stakes)),
                    'estimated_daily_rewards': float(sum(
                        self._calculate_daily_rewards(stake) for stake in user_stakes if stake.is_active
                    ))
                }
            }
            
        except Exception as e:
            logger.error(f"Get user stakes error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to retrieve stake positions'
            }
    
    def compound_rewards(self, user_id: str, stake_id: str) -> Dict:
        """Compound rewards by restaking them"""
        try:
            if stake_id not in self.stake_positions:
                return {
                    'success': False,
                    'error': 'Stake position not found',
                    'message': 'Invalid stake ID'
                }
            
            stake = self.stake_positions[stake_id]
            
            if stake.user_id != user_id or not stake.is_active:
                return {
                    'success': False,
                    'error': 'Invalid stake position',
                    'message': 'Cannot compound this position'
                }
            
            # Calculate pending rewards
            pending_rewards = self._calculate_pending_rewards(stake)
            
            if pending_rewards <= 0:
                return {
                    'success': False,
                    'error': 'No rewards to compound',
                    'message': 'No pending rewards available'
                }
            
            # Add rewards to stake amount
            stake.amount += pending_rewards
            stake.accumulated_rewards += pending_rewards
            stake.last_reward_claim = datetime.datetime.now()
            
            # Update user's staked balance
            self.token_system.balances[user_id].staked_balance += pending_rewards
            
            # Move rewards from staking pool (this maintains the pool balance)
            self.token_system._internal_transfer(
                'staking_pool',
                'staking_pool',  # Self-transfer to maintain balance
                pending_rewards,
                'compound',
                f'Compounded rewards in {stake.pool_type} pool'
            )
            
            logger.info(f"🔄 Compounded {pending_rewards} FBX: {user_id} in {stake.pool_type} pool")
            
            return {
                'success': True,
                'message': f'Successfully compounded {float(pending_rewards)} FBX',
                'compounded_amount': float(pending_rewards),
                'new_stake_amount': float(stake.amount),
                'new_daily_rewards': float(self._calculate_daily_rewards(stake))
            }
            
        except Exception as e:
            logger.error(f"Compound error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Compounding operation failed'
            }
    
    def _calculate_pending_rewards(self, stake: StakePosition) -> Decimal:
        """Calculate pending rewards for a stake position"""
        if not stake.is_active:
            return Decimal('0')
        
        now = datetime.datetime.now()
        time_since_last_claim = now - stake.last_reward_claim
        hours_elapsed = Decimal(str(time_since_last_claim.total_seconds())) / Decimal('3600')
        
        # Get pool APY
        pool_config = self.pools_config.get(stake.pool_type, {})
        apy = Decimal(str(pool_config.get('apy', 0))) / Decimal('100')  # Convert percentage to decimal
        
        # Calculate hourly rate
        hourly_rate = apy / Decimal('365') / Decimal('24')
        
        # Calculate rewards with multiplier
        base_rewards = stake.amount * hourly_rate * hours_elapsed
        final_rewards = base_rewards * stake.multiplier
        
        return final_rewards
    
    def _calculate_daily_rewards(self, stake: StakePosition) -> Decimal:
        """Calculate estimated daily rewards for a stake position"""
        if not stake.is_active:
            return Decimal('0')
        
        pool_config = self.pools_config.get(stake.pool_type, {})
        apy = Decimal(str(pool_config.get('apy', 0))) / Decimal('100')
        
        daily_rate = apy / Decimal('365')
        daily_rewards = stake.amount * daily_rate * stake.multiplier
        
        return daily_rewards
    
    def _distribute_rewards_to_user(self, user_id: str, amount: Decimal, reward_type: str):
        """Distribute rewards to user"""
        success = self.token_system._internal_transfer(
            'staking_pool',
            user_id,
            amount,
            'reward',
            f'Staking rewards: {reward_type}'
        )
        
        if not success:
            logger.error(f"Failed to distribute {amount} FBX rewards to {user_id}")
        
        return success
    
    def run_daily_reward_distribution(self) -> Dict:
        """Run daily reward distribution for all active stakes"""
        try:
            distributed_rewards = Decimal('0')
            updated_positions = 0
            
            for stake in self.stake_positions.values():
                if stake.is_active:
                    pending_rewards = self._calculate_pending_rewards(stake)
                    if pending_rewards > 0:
                        # Auto-distribute daily rewards
                        success = self._distribute_rewards_to_user(
                            stake.user_id, 
                            pending_rewards, 
                            'daily_distribution'
                        )
                        
                        if success:
                            stake.accumulated_rewards += pending_rewards
                            stake.last_reward_claim = datetime.datetime.now()
                            distributed_rewards += pending_rewards
                            updated_positions += 1
            
            self.last_reward_distribution = datetime.datetime.now()
            
            logger.info(f"📅 Daily reward distribution: {distributed_rewards} FBX to {updated_positions} positions")
            
            return {
                'success': True,
                'total_distributed': float(distributed_rewards),
                'positions_updated': updated_positions,
                'distribution_time': self.last_reward_distribution.isoformat()
            }
            
        except Exception as e:
            logger.error(f"Daily distribution error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Daily reward distribution failed'
            }
    
    def get_staking_analytics(self) -> Dict:
        """Get comprehensive staking system analytics"""
        try:
            analytics = {
                'total_positions': len(self.stake_positions),
                'active_positions': len([s for s in self.stake_positions.values() if s.is_active]),
                'total_staked': float(sum(s.amount for s in self.stake_positions.values() if s.is_active)),
                'total_rewards_distributed': float(sum(s.accumulated_rewards for s in self.stake_positions.values())),
                'unique_stakers': len(set(s.user_id for s in self.stake_positions.values() if s.is_active)),
                'last_distribution': self.last_reward_distribution.isoformat(),
                'pool_breakdown': {}
            }
            
            # Pool-specific analytics
            for pool_type in self.pools_config.keys():
                pool_stakes = [s for s in self.stake_positions.values() if s.pool_type == pool_type and s.is_active]
                
                analytics['pool_breakdown'][pool_type] = {
                    'active_stakes': len(pool_stakes),
                    'total_staked': float(sum(s.amount for s in pool_stakes)),
                    'average_stake': float(sum(s.amount for s in pool_stakes) / len(pool_stakes)) if pool_stakes else 0,
                    'total_rewards': float(sum(s.accumulated_rewards for s in pool_stakes)),
                    'unique_stakers': len(set(s.user_id for s in pool_stakes))
                }
            
            return {
                'success': True,
                'analytics': analytics
            }
            
        except Exception as e:
            logger.error(f"Staking analytics error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to generate analytics'
            }

# Global staking system instance
staking_system = None

def get_staking_system() -> StakingSystem:
    """Get global staking system instance"""
    global staking_system
    if staking_system is None:
        staking_system = StakingSystem()
    return staking_system

if __name__ == "__main__":
    # Test the staking system
    logging.basicConfig(level=logging.INFO)
    
    staking = StakingSystem()
    
    print("=== FURBX Staking System Test ===")
    
    # Test pool information
    pools = staking.get_available_pools()
    print(f"Available pools: {pools}")
    
    # Test staking
    stake_result = staking.stake_tokens("test_user_1", "basic", 50.0)
    print(f"Staking result: {stake_result}")
    
    # Test user stakes
    user_stakes = staking.get_user_stakes("test_user_1")
    print(f"User stakes: {user_stakes}")
    
    # Test analytics
    analytics = staking.get_staking_analytics()
    print(f"Staking analytics: {analytics}")
    
    print("\n🥩 Staking System test completed")