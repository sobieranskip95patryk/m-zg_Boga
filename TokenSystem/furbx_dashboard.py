"""
FURBX Dashboard Web Interface - Complete Token Management UI
AI Furby Platform Economic Engine
MTAQuestWebsideX.com - Interactive Token Dashboard
"""

from typing import Dict
import datetime
import logging

from user_wallet_interface import get_user_wallet_interface
from token_logic import get_token_system
from staking_module import get_staking_system
from marketplace_integration import get_marketplace_integration

logger = logging.getLogger(__name__)

class FURBXDashboard:
    """
    Complete FURBX Dashboard Web Interface
    Provides all wallet, staking, and marketplace functionality through web UI
    """
    
    def __init__(self):
        self.wallet_interface = get_user_wallet_interface()
        self.token_system = get_token_system()
        self.staking_system = get_staking_system()
        self.marketplace = get_marketplace_integration()
        
        # Dashboard state
        self.current_user = None
        self.last_refresh = datetime.datetime.now()
        
        logger.info("🎛️ FURBX Dashboard initialized")
    
    def render_main_dashboard(self, user_id: str) -> str:
        """Render main dashboard HTML"""
        self.current_user = user_id
        
        # Get dashboard data
        dashboard_data = self.wallet_interface.get_dashboard_data(user_id)
        
        if not dashboard_data['success']:
            return self._render_error_page(dashboard_data.get('message', 'Dashboard load failed'))
        
        # Get additional data
        staking_pools = self.staking_system.get_available_pools()
        system_stats = self.token_system.get_system_stats()
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FURBX Token Dashboard - AI Furby Platform</title>
            <style>
                {self._get_dashboard_css()}
            </style>
        </head>
        <body>
            <div class="dashboard-container">
                <header class="dashboard-header">
                    <div class="header-content">
                        <h1>🪙 FURBX Token Dashboard</h1>
                        <div class="user-info">
                            <span class="user-id">👤 {user_id}</span>
                            <span class="premium-badge {'premium' if dashboard_data['quick_stats']['premium_status'] else 'basic'}">
                                {'👑 PREMIUM' if dashboard_data['quick_stats']['premium_status'] else '🔹 BASIC'}
                            </span>
                        </div>
                    </div>
                </header>
                
                <div class="dashboard-grid">
                    {self._render_portfolio_card(dashboard_data['portfolio'])}
                    {self._render_quick_stats_card(dashboard_data['quick_stats'])}
                    {self._render_staking_card(dashboard_data['staking_overview'], staking_pools)}
                    {self._render_recent_activity_card(dashboard_data['recent_activity'])}
                    {self._render_system_info_card(system_stats)}
                    {self._render_actions_card()}
                </div>
                
                <div class="dashboard-tabs">
                    <div class="tab-buttons">
                        <button class="tab-button active" onclick="showTab('wallet')">💼 Wallet</button>
                        <button class="tab-button" onclick="showTab('staking')">🥩 Staking</button>
                        <button class="tab-button" onclick="showTab('marketplace')">🛒 Marketplace</button>
                        <button class="tab-button" onclick="showTab('analytics')">📊 Analytics</button>
                    </div>
                    
                    <div id="wallet-tab" class="tab-content active">
                        {self._render_wallet_tab(user_id)}
                    </div>
                    
                    <div id="staking-tab" class="tab-content">
                        {self._render_staking_tab(user_id)}
                    </div>
                    
                    <div id="marketplace-tab" class="tab-content">
                        {self._render_marketplace_tab(user_id)}
                    </div>
                    
                    <div id="analytics-tab" class="tab-content">
                        {self._render_analytics_tab(user_id)}
                    </div>
                </div>
            </div>
            
            <script>
                {self._get_dashboard_javascript()}
            </script>
        </body>
        </html>
        """
        
        return html
    
    def _render_portfolio_card(self, portfolio: Dict) -> str:
        """Render portfolio overview card"""
        return f"""
        <div class="card portfolio-card">
            <h3>💰 Portfolio Overview</h3>
            <div class="portfolio-stats">
                <div class="stat-item main-balance">
                    <div class="stat-value">{portfolio['total_portfolio_value']['fbx']:.2f} FBX</div>
                    <div class="stat-label">Total Portfolio</div>
                    <div class="stat-usd">${portfolio['total_portfolio_value']['usd']:.2f} USD</div>
                </div>
                
                <div class="portfolio-breakdown">
                    <div class="breakdown-item">
                        <span class="breakdown-label">💵 Available</span>
                        <span class="breakdown-value">{portfolio['available_balance']['fbx']:.2f} FBX</span>
                        <span class="breakdown-usd">${portfolio['available_balance']['usd']:.2f}</span>
                    </div>
                    
                    <div class="breakdown-item">
                        <span class="breakdown-label">🥩 Staked</span>
                        <span class="breakdown-value">{portfolio['staked_balance']['fbx']:.2f} FBX</span>
                        <span class="breakdown-usd">${portfolio['staked_balance']['usd']:.2f}</span>
                    </div>
                    
                    <div class="breakdown-item pending-rewards">
                        <span class="breakdown-label">⏰ Pending Rewards</span>
                        <span class="breakdown-value">{portfolio['pending_rewards']['fbx']:.4f} FBX</span>
                        <span class="breakdown-usd">${portfolio['pending_rewards']['usd']:.4f}</span>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_quick_stats_card(self, stats: Dict) -> str:
        """Render quick statistics card"""
        return f"""
        <div class="card stats-card">
            <h3>📈 Quick Stats</h3>
            <div class="quick-stats">
                <div class="stat-row">
                    <div class="stat-item">
                        <span class="stat-icon">📊</span>
                        <div class="stat-info">
                            <div class="stat-value">{stats['total_transactions']}</div>
                            <div class="stat-label">Total Transactions</div>
                        </div>
                    </div>
                    
                    <div class="stat-item">
                        <span class="stat-icon">📅</span>
                        <div class="stat-info">
                            <div class="stat-value">{stats['account_age_days']}</div>
                            <div class="stat-label">Account Age (Days)</div>
                        </div>
                    </div>
                </div>
                
                <div class="stat-row">
                    <div class="stat-item">
                        <span class="stat-icon">🤝</span>
                        <div class="stat-info">
                            <div class="stat-value">{stats['referral_count']}</div>
                            <div class="stat-label">Referrals</div>
                        </div>
                    </div>
                    
                    <div class="stat-item">
                        <span class="stat-icon">🎯</span>
                        <div class="stat-info">
                            <div class="stat-value">{stats['active_stakes']}</div>
                            <div class="stat-label">Active Stakes</div>
                        </div>
                    </div>
                </div>
                
                <div class="creator-earnings">
                    <span class="earnings-label">💎 Creator Earnings (30d)</span>
                    <span class="earnings-value">{stats['creator_earnings_30d']:.2f} FBX</span>
                </div>
            </div>
        </div>
        """
    
    def _render_staking_card(self, staking: Dict, pools: Dict) -> str:
        """Render staking overview card"""
        pools_info = pools.get('pools', {}) if pools.get('success') else {}
        
        return f"""
        <div class="card staking-card">
            <h3>🥩 Staking Overview</h3>
            <div class="staking-summary">
                <div class="staking-stat">
                    <div class="stat-value">{staking['total_staked']:.2f} FBX</div>
                    <div class="stat-label">Total Staked</div>
                </div>
                
                <div class="staking-stat">
                    <div class="stat-value">{staking['estimated_daily_rewards']:.4f} FBX</div>
                    <div class="stat-label">Daily Rewards</div>
                </div>
                
                <div class="staking-stat">
                    <div class="stat-value">{staking['total_rewards_earned']:.2f} FBX</div>
                    <div class="stat-label">Total Earned</div>
                </div>
            </div>
            
            <div class="available-pools">
                <h4>Available Pools</h4>
                <div class="pools-list">
                    {''.join([f'''
                    <div class="pool-item">
                        <span class="pool-name">{pool_name.title()}</span>
                        <span class="pool-apy">{pool_info["apy"]}% APY</span>
                        <span class="pool-min">Min: {pool_info["min_stake"]} FBX</span>
                    </div>
                    ''' for pool_name, pool_info in pools_info.items()])}
                </div>
            </div>
        </div>
        """
    
    def _render_recent_activity_card(self, activity: list) -> str:
        """Render recent activity card"""
        activity_html = ""
        for tx in activity[:5]:
            activity_html += f"""
            <div class="activity-item">
                <span class="activity-icon">{tx.get('icon', '💰')}</span>
                <div class="activity-info">
                    <div class="activity-desc">{tx.get('description', 'Transaction')}</div>
                    <div class="activity-time">{tx.get('timestamp', '')}</div>
                </div>
                <div class="activity-amount {tx.get('color', 'gray')}">
                    {'+' if tx.get('direction') == 'incoming' else '-'}{tx.get('amount', 0):.2f} FBX
                </div>
            </div>
            """
        
        return f"""
        <div class="card activity-card">
            <h3>⚡ Recent Activity</h3>
            <div class="activity-list">
                {activity_html if activity_html else '<div class="no-activity">No recent activity</div>'}
            </div>
            <button class="view-all-btn" onclick="showTab('wallet')">View All Transactions</button>
        </div>
        """
    
    def _render_system_info_card(self, stats: Dict) -> str:
        """Render system information card"""
        return f"""
        <div class="card system-card">
            <h3>🌐 System Info</h3>
            <div class="system-stats">
                <div class="system-stat">
                    <span class="stat-label">Total Supply</span>
                    <span class="stat-value">{stats.get('total_supply', 0):,.0f} FBX</span>
                </div>
                
                <div class="system-stat">
                    <span class="stat-label">Active Users</span>
                    <span class="stat-value">{stats.get('active_users', 0):,}</span>
                </div>
                
                <div class="system-stat">
                    <span class="stat-label">Exchange Rate</span>
                    <span class="stat-value">${stats.get('exchange_rate_usd', 0):.3f} USD</span>
                </div>
                
                <div class="system-stat">
                    <span class="stat-label">Treasury Balance</span>
                    <span class="stat-value">{stats.get('treasury_balance', 0):,.0f} FBX</span>
                </div>
            </div>
        </div>
        """
    
    def _render_actions_card(self) -> str:
        """Render quick actions card"""
        return f"""
        <div class="card actions-card">
            <h3>⚡ Quick Actions</h3>
            <div class="action-buttons">
                <button class="action-btn transfer-btn" onclick="showTransferModal()">
                    💸 Transfer Tokens
                </button>
                
                <button class="action-btn stake-btn" onclick="showStakeModal()">
                    🥩 Stake Tokens
                </button>
                
                <button class="action-btn claim-btn" onclick="claimAllRewards()">
                    💰 Claim Rewards
                </button>
                
                <button class="action-btn convert-btn" onclick="showConvertModal()">
                    🔄 Convert Tokens
                </button>
                
                <button class="action-btn premium-btn" onclick="showPremiumModal()">
                    👑 Upgrade Premium
                </button>
                
                <button class="action-btn refresh-btn" onclick="refreshDashboard()">
                    🔄 Refresh Data
                </button>
            </div>
        </div>
        """
    
    def _render_wallet_tab(self, user_id: str) -> str:
        """Render wallet management tab"""
        return f"""
        <div class="wallet-tab-content">
            <div class="tab-section">
                <h3>💼 Wallet Management</h3>
                
                <div class="wallet-actions">
                    <div class="action-section">
                        <h4>💸 Transfer Tokens</h4>
                        <form class="transfer-form" onsubmit="return transferTokens(event)">
                            <input type="text" id="transfer-recipient" placeholder="Recipient User ID" required>
                            <input type="number" id="transfer-amount" placeholder="Amount (FBX)" step="0.01" min="0.01" required>
                            <input type="text" id="transfer-description" placeholder="Description (optional)">
                            <button type="submit" class="submit-btn">Send Transfer</button>
                        </form>
                    </div>
                    
                    <div class="action-section">
                        <h4>🔄 Convert Tokens</h4>
                        <form class="convert-form" onsubmit="return convertTokens(event)">
                            <select id="conversion-type" required>
                                <option value="">Select Conversion Type</option>
                                <option value="to_fantasy_credits">FBX → Fantasy Credits</option>
                                <option value="to_usd_estimate">FBX → USD (Estimate)</option>
                            </select>
                            <input type="number" id="convert-amount" placeholder="Amount (FBX)" step="0.01" min="0.01" required>
                            <button type="submit" class="submit-btn">Convert</button>
                        </form>
                    </div>
                </div>
                
                <div class="transaction-history">
                    <h4>📊 Transaction History</h4>
                    <div class="history-filters">
                        <select id="history-type">
                            <option value="">All Types</option>
                            <option value="transfer">Transfers</option>
                            <option value="reward">Rewards</option>
                            <option value="stake">Staking</option>
                            <option value="purchase">Purchases</option>
                        </select>
                        <input type="date" id="history-from">
                        <input type="date" id="history-to">
                        <button onclick="filterTransactions()">Filter</button>
                    </div>
                    <div id="transaction-list" class="transaction-list">
                        Loading transactions...
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_staking_tab(self, user_id: str) -> str:
        """Render staking management tab"""
        return f"""
        <div class="staking-tab-content">
            <div class="tab-section">
                <h3>🥩 Staking Management</h3>
                
                <div class="staking-actions">
                    <div class="action-section">
                        <h4>📈 Stake Tokens</h4>
                        <form class="stake-form" onsubmit="return stakeTokens(event)">
                            <select id="stake-pool" required>
                                <option value="">Select Pool</option>
                                <option value="basic">Basic (30% APY)</option>
                                <option value="premium">Premium (60% APY)</option>
                                <option value="vip">VIP (120% APY)</option>
                            </select>
                            <input type="number" id="stake-amount" placeholder="Amount (FBX)" step="0.01" min="1" required>
                            <input type="number" id="lock-duration" placeholder="Lock Duration (days, 0=flexible)" min="0" value="0">
                            <button type="submit" class="submit-btn">Stake Tokens</button>
                        </form>
                    </div>
                    
                    <div class="action-section">
                        <h4>💰 Claim All Rewards</h4>
                        <button onclick="claimAllStakingRewards()" class="claim-all-btn">Claim All Pending Rewards</button>
                    </div>
                </div>
                
                <div class="user-stakes">
                    <h4>🎯 Your Stake Positions</h4>
                    <div id="stakes-list" class="stakes-list">
                        Loading stake positions...
                    </div>
                </div>
                
                <div class="staking-pools">
                    <h4>🏊 Available Pools</h4>
                    <div id="pools-list" class="pools-list">
                        Loading staking pools...
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_marketplace_tab(self, user_id: str) -> str:
        """Render marketplace tab"""
        return f"""
        <div class="marketplace-tab-content">
            <div class="tab-section">
                <h3>🛒 Marketplace</h3>
                
                <div class="marketplace-actions">
                    <div class="action-section">
                        <h4>🎁 Tip Creator</h4>
                        <form class="tip-form" onsubmit="return tipCreator(event)">
                            <input type="text" id="tip-creator-id" placeholder="Creator User ID" required>
                            <input type="number" id="tip-amount" placeholder="Tip Amount (FBX)" step="0.01" min="0.10" required>
                            <input type="text" id="tip-message" placeholder="Message (optional)">
                            <button type="submit" class="submit-btn">Send Tip</button>
                        </form>
                    </div>
                    
                    <div class="action-section">
                        <h4>👑 Premium Features</h4>
                        <div class="premium-features">
                            <div class="feature-item">
                                <span class="feature-name">Voice Packs</span>
                                <span class="feature-price">2.5 FBX</span>
                                <button onclick="purchasePremiumFeature('voice_packs', 2.5)">Purchase</button>
                            </div>
                            <div class="feature-item">
                                <span class="feature-name">Custom Furby</span>
                                <span class="feature-price">25.0 FBX</span>
                                <button onclick="purchasePremiumFeature('custom_furby', 25.0)">Purchase</button>
                            </div>
                            <div class="feature-item">
                                <span class="feature-name">VIP Access</span>
                                <span class="feature-price">50.0 FBX</span>
                                <button onclick="purchasePremiumFeature('vip_access', 50.0)">Purchase</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="action-section">
                        <h4>📝 List Content (Creators)</h4>
                        <form class="list-content-form" onsubmit="return listContent(event)">
                            <input type="text" id="content-title" placeholder="Content Title" required>
                            <textarea id="content-description" placeholder="Description" rows="3" required></textarea>
                            <select id="content-type" required>
                                <option value="">Select Content Type</option>
                                <option value="voice_pack">Voice Pack</option>
                                <option value="custom_furby">Custom Furby</option>
                                <option value="animation">Animation</option>
                                <option value="skin">Skin/Theme</option>
                            </select>
                            <input type="number" id="content-price" placeholder="Price (FBX)" step="0.01" min="0.01" required>
                            <button type="submit" class="submit-btn">List Content</button>
                        </form>
                    </div>
                </div>
                
                <div class="creator-earnings">
                    <h4>💎 Creator Earnings</h4>
                    <div id="earnings-summary" class="earnings-summary">
                        Loading creator earnings...
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_analytics_tab(self, user_id: str) -> str:
        """Render analytics tab"""
        return f"""
        <div class="analytics-tab-content">
            <div class="tab-section">
                <h3>📊 Analytics Dashboard</h3>
                
                <div class="analytics-overview">
                    <div id="wallet-health" class="analytics-card">
                        <h4>💪 Wallet Health Score</h4>
                        <div class="health-score">
                            <div class="score-circle">
                                <span class="score-value">Loading...</span>
                            </div>
                        </div>
                    </div>
                    
                    <div id="earning-breakdown" class="analytics-card">
                        <h4>💰 Earning Breakdown</h4>
                        <div class="breakdown-chart">
                            Loading earning data...
                        </div>
                    </div>
                    
                    <div id="spending-breakdown" class="analytics-card">
                        <h4>💸 Spending Breakdown</h4>
                        <div class="breakdown-chart">
                            Loading spending data...
                        </div>
                    </div>
                    
                    <div id="transaction-trends" class="analytics-card">
                        <h4>📈 Transaction Trends</h4>
                        <div class="trends-chart">
                            Loading trends data...
                        </div>
                    </div>
                </div>
                
                <div class="analytics-actions">
                    <button onclick="refreshAnalytics()">🔄 Refresh Analytics</button>
                    <button onclick="exportAnalytics()">📤 Export Data</button>
                </div>
            </div>
        </div>
        """
    
    def _get_dashboard_css(self) -> str:
        """Get CSS styles for dashboard"""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .dashboard-header {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header-content h1 {
            color: #4a5568;
            font-size: 2.5em;
            font-weight: 700;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .user-id {
            font-size: 1.1em;
            font-weight: 600;
            color: #2d3748;
        }
        
        .premium-badge {
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9em;
        }
        
        .premium-badge.premium {
            background: linear-gradient(45deg, #f6ad55, #ed8936);
            color: white;
        }
        
        .premium-badge.basic {
            background: #e2e8f0;
            color: #4a5568;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);
        }
        
        .card h3 {
            color: #2d3748;
            margin-bottom: 20px;
            font-size: 1.3em;
            font-weight: 700;
        }
        
        .portfolio-card {
            grid-column: span 2;
        }
        
        .main-balance {
            text-align: center;
            margin-bottom: 25px;
            padding: 20px;
            background: linear-gradient(45deg, #4299e1, #3182ce);
            border-radius: 12px;
            color: white;
        }
        
        .main-balance .stat-value {
            font-size: 2.5em;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .main-balance .stat-label {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .main-balance .stat-usd {
            font-size: 1.2em;
            margin-top: 8px;
            opacity: 0.8;
        }
        
        .portfolio-breakdown {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .breakdown-item {
            padding: 15px;
            background: #f7fafc;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        .breakdown-label {
            font-weight: 600;
            color: #4a5568;
            font-size: 0.9em;
        }
        
        .breakdown-value {
            font-size: 1.2em;
            font-weight: 700;
            color: #2d3748;
        }
        
        .breakdown-usd {
            font-size: 0.9em;
            color: #718096;
        }
        
        .pending-rewards {
            background: linear-gradient(45deg, #48bb78, #38a169);
            color: white;
        }
        
        .pending-rewards .breakdown-label,
        .pending-rewards .breakdown-usd {
            color: rgba(255, 255, 255, 0.9);
        }
        
        .quick-stats {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .stat-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        
        .stat-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #f7fafc;
            border-radius: 10px;
        }
        
        .stat-icon {
            font-size: 1.5em;
        }
        
        .stat-info .stat-value {
            font-size: 1.3em;
            font-weight: 700;
            color: #2d3748;
        }
        
        .stat-info .stat-label {
            font-size: 0.8em;
            color: #718096;
        }
        
        .creator-earnings {
            padding: 15px;
            background: linear-gradient(45deg, #ed64a6, #d53f8c);
            border-radius: 10px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .action-buttons {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px;
        }
        
        .action-btn {
            padding: 12px 16px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9em;
        }
        
        .action-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        .transfer-btn {
            background: #4299e1;
            color: white;
        }
        
        .stake-btn {
            background: #48bb78;
            color: white;
        }
        
        .claim-btn {
            background: #ed8936;
            color: white;
        }
        
        .convert-btn {
            background: #9f7aea;
            color: white;
        }
        
        .premium-btn {
            background: linear-gradient(45deg, #f6ad55, #ed8936);
            color: white;
        }
        
        .refresh-btn {
            background: #718096;
            color: white;
        }
        
        .dashboard-tabs {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .tab-buttons {
            display: flex;
            background: #edf2f7;
        }
        
        .tab-button {
            flex: 1;
            padding: 15px 20px;
            border: none;
            background: transparent;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .tab-button.active {
            background: white;
            color: #4299e1;
        }
        
        .tab-content {
            display: none;
            padding: 30px;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .action-section {
            margin-bottom: 30px;
            padding: 20px;
            background: #f7fafc;
            border-radius: 10px;
        }
        
        .action-section h4 {
            margin-bottom: 15px;
            color: #2d3748;
        }
        
        .transfer-form,
        .convert-form,
        .stake-form,
        .tip-form,
        .list-content-form {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            align-items: end;
        }
        
        .transfer-form input,
        .convert-form input,
        .convert-form select,
        .stake-form input,
        .stake-form select,
        .tip-form input,
        .list-content-form input,
        .list-content-form select,
        .list-content-form textarea {
            padding: 10px;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            font-size: 0.9em;
        }
        
        .submit-btn {
            padding: 10px 20px;
            background: #4299e1;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        
        .submit-btn:hover {
            background: #3182ce;
        }
        
        .transaction-list,
        .stakes-list,
        .pools-list {
            max-height: 400px;
            overflow-y: auto;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            background: white;
        }
        
        .activity-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .activity-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #f7fafc;
            border-radius: 8px;
        }
        
        .activity-icon {
            font-size: 1.3em;
        }
        
        .activity-info {
            flex: 1;
        }
        
        .activity-desc {
            font-weight: 600;
            color: #2d3748;
            font-size: 0.9em;
        }
        
        .activity-time {
            font-size: 0.8em;
            color: #718096;
        }
        
        .activity-amount {
            font-weight: 700;
            font-size: 0.9em;
        }
        
        .activity-amount.green {
            color: #48bb78;
        }
        
        .activity-amount.red {
            color: #f56565;
        }
        
        .view-all-btn {
            width: 100%;
            padding: 10px;
            background: #edf2f7;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            color: #4a5568;
            margin-top: 15px;
        }
        
        .system-stats {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .system-stat {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background: #f7fafc;
            border-radius: 6px;
        }
        
        .system-stat .stat-label {
            color: #718096;
            font-size: 0.9em;
        }
        
        .system-stat .stat-value {
            font-weight: 700;
            color: #2d3748;
        }
        
        @media (max-width: 768px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
            
            .portfolio-card {
                grid-column: span 1;
            }
            
            .header-content {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }
            
            .header-content h1 {
                font-size: 2em;
            }
            
            .tab-buttons {
                flex-wrap: wrap;
            }
            
            .tab-button {
                font-size: 0.8em;
                padding: 12px 15px;
            }
        }
        """
    
    def _get_dashboard_javascript(self) -> str:
        """Get JavaScript for dashboard functionality"""
        return f"""
        // Dashboard JavaScript Functions
        let currentUser = '{self.current_user}';
        
        function showTab(tabName) {{
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(tab => {{
                tab.classList.remove('active');
            }});
            
            // Remove active class from all buttons
            document.querySelectorAll('.tab-button').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            // Show selected tab
            document.getElementById(tabName + '-tab').classList.add('active');
            
            // Activate button
            event.target.classList.add('active');
            
            // Load tab-specific data
            loadTabData(tabName);
        }}
        
        function loadTabData(tabName) {{
            switch(tabName) {{
                case 'wallet':
                    loadTransactionHistory();
                    break;
                case 'staking':
                    loadStakingData();
                    break;
                case 'marketplace':
                    loadMarketplaceData();
                    break;
                case 'analytics':
                    loadAnalyticsData();
                    break;
            }}
        }}
        
        function transferTokens(event) {{
            event.preventDefault();
            
            const recipient = document.getElementById('transfer-recipient').value;
            const amount = document.getElementById('transfer-amount').value;
            const description = document.getElementById('transfer-description').value;
            
            // API call would go here
            alert(`Transfer: ${{amount}} FBX to ${{recipient}} - ${{description}}`);
            
            return false;
        }}
        
        function convertTokens(event) {{
            event.preventDefault();
            
            const type = document.getElementById('conversion-type').value;
            const amount = document.getElementById('convert-amount').value;
            
            // API call would go here
            alert(`Convert: ${{amount}} FBX to ${{type}}`);
            
            return false;
        }}
        
        function stakeTokens(event) {{
            event.preventDefault();
            
            const pool = document.getElementById('stake-pool').value;
            const amount = document.getElementById('stake-amount').value;
            const lockDuration = document.getElementById('lock-duration').value;
            
            // API call would go here
            alert(`Stake: ${{amount}} FBX in ${{pool}} pool for ${{lockDuration}} days`);
            
            return false;
        }}
        
        function tipCreator(event) {{
            event.preventDefault();
            
            const creatorId = document.getElementById('tip-creator-id').value;
            const amount = document.getElementById('tip-amount').value;
            const message = document.getElementById('tip-message').value;
            
            // API call would go here
            alert(`Tip: ${{amount}} FBX to ${{creatorId}} - ${{message}}`);
            
            return false;
        }}
        
        function listContent(event) {{
            event.preventDefault();
            
            const title = document.getElementById('content-title').value;
            const description = document.getElementById('content-description').value;
            const type = document.getElementById('content-type').value;
            const price = document.getElementById('content-price').value;
            
            // API call would go here
            alert(`List Content: ${{title}} (${{type}}) for ${{price}} FBX`);
            
            return false;
        }}
        
        function claimAllRewards() {{
            // API call would go here
            alert('Claiming all pending rewards...');
        }}
        
        function claimAllStakingRewards() {{
            // API call would go here
            alert('Claiming all staking rewards...');
        }}
        
        function purchasePremiumFeature(feature, price) {{
            if (confirm(`Purchase ${{feature}} for ${{price}} FBX?`)) {{
                // API call would go here
                alert(`Purchased ${{feature}} for ${{price}} FBX`);
            }}
        }}
        
        function refreshDashboard() {{
            location.reload();
        }}
        
        function loadTransactionHistory() {{
            // Simulate loading transaction history
            const transactionList = document.getElementById('transaction-list');
            if (transactionList) {{
                transactionList.innerHTML = `
                    <div style="padding: 20px; text-align: center;">
                        <p>📊 Transaction history would be loaded here via API</p>
                        <p>Features: Filtering, pagination, detailed view</p>
                    </div>
                `;
            }}
        }}
        
        function loadStakingData() {{
            // Load stakes list
            const stakesList = document.getElementById('stakes-list');
            if (stakesList) {{
                stakesList.innerHTML = `
                    <div style="padding: 20px; text-align: center;">
                        <p>🎯 User stake positions would be loaded here</p>
                        <p>Features: Unstake, claim rewards, compound</p>
                    </div>
                `;
            }}
            
            // Load pools list
            const poolsList = document.getElementById('pools-list');
            if (poolsList) {{
                poolsList.innerHTML = `
                    <div style="padding: 20px; text-align: center;">
                        <p>🏊 Available staking pools information</p>
                        <p>Features: APY details, requirements, statistics</p>
                    </div>
                `;
            }}
        }}
        
        function loadMarketplaceData() {{
            // Load creator earnings
            const earningsSummary = document.getElementById('earnings-summary');
            if (earningsSummary) {{
                earningsSummary.innerHTML = `
                    <div style="padding: 20px; text-align: center;">
                        <p>💎 Creator earnings summary would be displayed here</p>
                        <p>Features: Revenue breakdown, top content, trends</p>
                    </div>
                `;
            }}
        }}
        
        function loadAnalyticsData() {{
            // Load wallet health
            const walletHealth = document.getElementById('wallet-health');
            if (walletHealth) {{
                const scoreValue = walletHealth.querySelector('.score-value');
                if (scoreValue) {{
                    scoreValue.textContent = '85/100';
                }}
            }}
            
            // Load other analytics components
            ['earning-breakdown', 'spending-breakdown', 'transaction-trends'].forEach(id => {{
                const element = document.getElementById(id);
                if (element) {{
                    const chart = element.querySelector('.breakdown-chart, .trends-chart');
                    if (chart) {{
                        chart.innerHTML = `
                            <div style="padding: 20px; text-align: center; color: #666;">
                                📊 ${{id.replace('-', ' ').toUpperCase()}} chart would be displayed here
                            </div>
                        `;
                    }}
                }}
            }});
        }}
        
        function filterTransactions() {{
            const type = document.getElementById('history-type').value;
            const from = document.getElementById('history-from').value;
            const to = document.getElementById('history-to').value;
            
            // API call would filter transactions
            console.log('Filter transactions:', {{ type, from, to }});
        }}
        
        function refreshAnalytics() {{
            loadAnalyticsData();
            alert('Analytics refreshed!');
        }}
        
        function exportAnalytics() {{
            alert('Analytics data would be exported to CSV/PDF');
        }}
        
        // Initialize dashboard on load
        document.addEventListener('DOMContentLoaded', function() {{
            loadTabData('wallet');
        }});
        
        // Auto-refresh dashboard every 30 seconds
        setInterval(function() {{
            console.log('Auto-refreshing dashboard data...');
            // Refresh data without full page reload
        }}, 30000);
        """
    
    def _render_error_page(self, error_message: str) -> str:
        """Render error page"""
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FURBX Dashboard - Error</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                .error-container {{
                    background: white;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 500px;
                }}
                .error-icon {{
                    font-size: 4em;
                    margin-bottom: 20px;
                }}
                .error-title {{
                    font-size: 1.5em;
                    font-weight: 700;
                    color: #e53e3e;
                    margin-bottom: 15px;
                }}
                .error-message {{
                    color: #666;
                    margin-bottom: 25px;
                }}
                .retry-btn {{
                    padding: 12px 24px;
                    background: #4299e1;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    font-weight: 600;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <div class="error-icon">⚠️</div>
                <div class="error-title">Dashboard Error</div>
                <div class="error-message">{error_message}</div>
                <button class="retry-btn" onclick="location.reload()">Retry</button>
            </div>
        </body>
        </html>
        """

# Global dashboard instance
furbx_dashboard = None

def get_furbx_dashboard() -> FURBXDashboard:
    """Get global FURBX dashboard instance"""
    global furbx_dashboard
    if furbx_dashboard is None:
        furbx_dashboard = FURBXDashboard()
    return furbx_dashboard

if __name__ == "__main__":
    # Test the dashboard
    logging.basicConfig(level=logging.INFO)
    
    dashboard = FURBXDashboard()
    
    print("=== FURBX Dashboard Test ===")
    
    # Generate dashboard HTML for test user
    html_output = dashboard.render_main_dashboard("test_user_dashboard")
    
    # Save to file for testing
    with open("furbx_dashboard_test.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    
    print("Dashboard HTML generated and saved to furbx_dashboard_test.html")
    print("🎛️ FURBX Dashboard test completed")