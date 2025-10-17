"""
AI Furby 1.25D Web Interface - Browser-based Gaming Platform
MTAQuestWebsideX.com - HTML5 Game Interface with FURBX Integration
Complete web dashboard for Furby San Andreas Edition
"""

from typing import Dict
import json
import datetime
import logging

from furby_san_andreas import get_furby_game, active_games

logger = logging.getLogger(__name__)

class FurbyGameWebInterface:
    """
    Web interface for AI Furby 1.25D: San Andreas Edition
    Provides HTML dashboard and API endpoints for browser gameplay
    """
    
    def __init__(self):
        self.active_sessions = {}
        logger.info("🌐 Furby Game Web Interface initialized")
    
    def render_game_dashboard(self, user_id: str) -> str:
        """Render complete game dashboard for web browser"""
        try:
            # Get or create game instance
            game = get_furby_game(user_id)
            
            # Try to load existing save
            game.load_game_state()
            
            # Get current game state
            current_location = game.locations[game.position]
            current_vehicle = game.vehicles[game.player.current_vehicle]
            
            # Generate HTML
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>AI Furby 1.25D: San Andreas Edition - Web Dashboard</title>
                <style>
                    {self._get_game_css()}
                </style>
            </head>
            <body>
                <div class="game-container">
                    <header class="game-header">
                        <div class="header-content">
                            <h1>🎮 AI FURBY 1.25D: SAN ANDREAS EDITION 🎮</h1>
                            <div class="player-info">
                                <span class="player-name">👤 {game.player.name or 'New Player'}</span>
                                <span class="level-badge">🎯 Level {game.player.level}</span>
                            </div>
                        </div>
                    </header>
                    
                    <div class="game-dashboard">
                        {self._render_player_hud(game)}
                        {self._render_location_view(game, current_location)}
                        {self._render_vehicle_display(current_vehicle)}
                        {self._render_action_panel()}
                    </div>
                    
                    <div class="game-tabs">
                        <div class="tab-buttons">
                            <button class="tab-button active" onclick="showGameTab('main')">🎮 Main Game</button>
                            <button class="tab-button" onclick="showGameTab('travel')">🗺️ Travel</button>
                            <button class="tab-button" onclick="showGameTab('shop')">🏪 Vehicle Shop</button>
                            <button class="tab-button" onclick="showGameTab('stats')">📊 Statistics</button>
                            <button class="tab-button" onclick="showGameTab('settings')">⚙️ Settings</button>
                        </div>
                        
                        <div id="main-tab" class="tab-content active">
                            {self._render_main_game_tab(game)}
                        </div>
                        
                        <div id="travel-tab" class="tab-content">
                            {self._render_travel_tab(game)}
                        </div>
                        
                        <div id="shop-tab" class="tab-content">
                            {self._render_vehicle_shop_tab(game)}
                        </div>
                        
                        <div id="stats-tab" class="tab-content">
                            {self._render_statistics_tab(game)}
                        </div>
                        
                        <div id="settings-tab" class="tab-content">
                            {self._render_settings_tab(game)}
                        </div>
                    </div>
                </div>
                
                <!-- Modals -->
                {self._render_encounter_modal()}
                {self._render_results_modal()}
                
                <script>
                    {self._get_game_javascript(user_id)}
                </script>
            </body>
            </html>
            """
            
            return html
            
        except Exception as e:
            logger.error(f"Game dashboard error: {e}")
            return self._render_error_page(f"Failed to load game: {str(e)}")
    
    def _render_player_hud(self, game) -> str:
        """Render player HUD with stats and progress bars"""
        return f"""
        <div class="player-hud">
            <div class="hud-section finances">
                <h3>💰 Finances</h3>
                <div class="stat-row">
                    <span class="stat-label">Cash USD:</span>
                    <span class="stat-value">${game.player.cash_usd:,}</span>
                </div>
                <div class="stat-row">
                    <span class="stat-label">FBX Tokens:</span>
                    <span class="stat-value">{game.player.fbx_tokens:.2f} FBX</span>
                </div>
            </div>
            
            <div class="hud-section stats">
                <h3>📈 Player Stats</h3>
                <div class="progress-bars">
                    <div class="progress-item">
                        <label>⚡ Energy</label>
                        <div class="progress-bar">
                            <div class="progress-fill energy" style="width: {game.player.energy}%"></div>
                            <span class="progress-text">{game.player.energy}/100</span>
                        </div>
                    </div>
                    
                    <div class="progress-item">
                        <label>🔥 Heat</label>
                        <div class="progress-bar">
                            <div class="progress-fill heat" style="width: {game.player.heat}%"></div>
                            <span class="progress-text">{game.player.heat}/100</span>
                        </div>
                    </div>
                    
                    <div class="progress-item">
                        <label>⭐ Reputation</label>
                        <div class="progress-bar">
                            <div class="progress-fill reputation" style="width: {min(game.player.reputation, 100)}%"></div>
                            <span class="progress-text">{game.player.reputation}</span>
                        </div>
                    </div>
                    
                    <div class="progress-item">
                        <label>🎯 Experience</label>
                        <div class="progress-bar">
                            <div class="progress-fill experience" style="width: {(game.player.experience % 100)}%"></div>
                            <span class="progress-text">{game.player.experience}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_location_view(self, game, location) -> str:
        """Render current location with ASCII art and info"""
        ascii_art = '\\n'.join(location.ascii_art)
        
        return f"""
        <div class="location-view">
            <div class="location-header">
                <h2>{location.icon} {location.name}</h2>
                <div class="location-stats">
                    <span class="danger-level">💀 Danger: {location.danger_level}/10</span>
                    <span class="luxury-level">💎 Luxury: {location.luxury_level}/10</span>
                </div>
            </div>
            
            <div class="ascii-art">
                <pre>{ascii_art}</pre>
            </div>
            
            <div class="location-info">
                <p class="background-music">{location.background_music}</p>
                {f'<p class="entry-cost">💰 Entry Cost: ${location.entry_cost}</p>' if location.entry_cost > 0 else ''}
            </div>
            
            <div class="location-actions">
                <button onclick="lookForEncounter()" class="action-btn encounter-btn">
                    👀 Look for Encounters
                </button>
                <button onclick="exploreArea()" class="action-btn explore-btn">
                    🔍 Explore Area
                </button>
            </div>
        </div>
        """
    
    def _render_vehicle_display(self, vehicle) -> str:
        """Render current vehicle with ASCII art"""
        ascii_art = '\\n'.join(vehicle.ascii_art)
        
        return f"""
        <div class="vehicle-display">
            <h3>🚗 Current Vehicle</h3>
            <div class="vehicle-info">
                <h4>{vehicle.name}</h4>
                <div class="vehicle-stats">
                    <span>🏃 Speed: {vehicle.speed}/10</span>
                    <span>✨ Style: {vehicle.style_points}/10</span>
                    <span>⚡ Special: {vehicle.special_ability}</span>
                </div>
            </div>
            
            <div class="vehicle-ascii">
                <pre>{ascii_art}</pre>
            </div>
            
            <div class="engine-sound">
                {vehicle.engine_sound}
            </div>
        </div>
        """
    
    def _render_action_panel(self) -> str:
        """Render main action panel"""
        return """
        <div class="action-panel">
            <h3>⚡ Quick Actions</h3>
            <div class="action-grid">
                <button onclick="restPlayer()" class="action-btn rest-btn">
                    💤 Rest & Recover
                </button>
                <button onclick="saveGame()" class="action-btn save-btn">
                    💾 Save Game
                </button>
                <button onclick="showGameTab('travel')" class="action-btn travel-btn">
                    🗺️ Travel
                </button>
                <button onclick="showGameTab('shop')" class="action-btn shop-btn">
                    🏪 Vehicle Shop
                </button>
            </div>
        </div>
        """
    
    def _render_main_game_tab(self, game) -> str:
        """Render main game interaction tab"""
        return f"""
        <div class="main-game-content">
            <div class="game-section">
                <h3>🎯 Game Status</h3>
                <div class="status-info">
                    <p><strong>Current Location:</strong> {game.locations[game.position].name}</p>
                    <p><strong>Game Time:</strong> {game.game_time:.1f} hours</p>
                    <p><strong>Playtime:</strong> {game.player.playtime_hours:.1f} hours</p>
                </div>
            </div>
            
            <div class="game-section">
                <h3>🎮 Game Actions</h3>
                <div class="game-actions">
                    <button onclick="lookForEncounter()" class="game-action-btn">
                        👀 Look for Encounters
                    </button>
                    <button onclick="exploreArea()" class="game-action-btn">
                        🔍 Explore Current Area
                    </button>
                    <button onclick="restPlayer()" class="game-action-btn">
                        💤 Rest (Restore Energy)
                    </button>
                </div>
            </div>
            
            <div class="game-section">
                <h3>📜 Recent Activity</h3>
                <div id="activity-log" class="activity-log">
                    <p>🎮 Welcome to AI Furby 1.25D: San Andreas Edition!</p>
                    <p>🌟 Start your adventure by looking for encounters or exploring the area.</p>
                </div>
            </div>
        </div>
        """
    
    def _render_travel_tab(self, game) -> str:
        """Render travel/navigation tab"""
        locations_html = ""
        for i, location in enumerate(game.locations):
            current_marker = "🔸" if i == game.position else "⚪"
            locked = "🔒" if location.name not in game.player.unlocked_locations else "✅"
            
            locations_html += f"""
            <div class="location-item {'current' if i == game.position else ''}">
                <span class="location-marker">{current_marker}</span>
                <span class="location-icon">{location.icon}</span>
                <span class="location-name">{location.name}</span>
                <span class="location-status">{locked}</span>
                {f'<span class="entry-cost">${location.entry_cost}</span>' if location.entry_cost > 0 else ''}
                <button onclick="travelTo({i})" class="travel-btn" 
                        {'disabled' if location.name not in game.player.unlocked_locations else ''}>
                    {'🚫 Locked' if location.name not in game.player.unlocked_locations else '🚗 Travel'}
                </button>
            </div>
            """
        
        return f"""
        <div class="travel-content">
            <div class="travel-section">
                <h3>🗺️ Available Locations</h3>
                <div class="locations-list">
                    {locations_html}
                </div>
            </div>
            
            <div class="travel-section">
                <h3>🚗 Travel Options</h3>
                <div class="travel-actions">
                    <button onclick="moveLeft()" class="travel-action-btn" 
                            {'disabled' if game.position <= 0 else ''}>
                        ⬅️ Move Left
                    </button>
                    <button onclick="moveRight()" class="travel-action-btn"
                            {'disabled' if game.position >= len(game.locations) - 1 else ''}>
                        ➡️ Move Right
                    </button>
                    <button onclick="exploreArea()" class="travel-action-btn">
                        🔍 Explore Current Area
                    </button>
                </div>
            </div>
        </div>
        """
    
    def _render_vehicle_shop_tab(self, game) -> str:
        """Render vehicle shop tab"""
        vehicles_html = ""
        for vehicle_id, vehicle in game.vehicles.items():
            owned = vehicle_id == game.player.current_vehicle
            can_afford = game.player.fbx_tokens >= vehicle.cost_fbx
            
            vehicles_html += f"""
            <div class="vehicle-item {'owned' if owned else ''}">
                <div class="vehicle-header">
                    <h4>{vehicle.name}</h4>
                    <span class="vehicle-type">{vehicle.type.title()}</span>
                </div>
                
                <div class="vehicle-ascii-mini">
                    <pre>{'\\n'.join(vehicle.ascii_art[:3])}</pre>
                </div>
                
                <div class="vehicle-stats-grid">
                    <div class="stat-item">
                        <span class="stat-label">🏃 Speed:</span>
                        <span class="stat-value">{vehicle.speed}/10</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">✨ Style:</span>
                        <span class="stat-value">{vehicle.style_points}/10</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-label">💰 Price:</span>
                        <span class="stat-value">{vehicle.cost_fbx} FBX</span>
                    </div>
                </div>
                
                <div class="vehicle-special">
                    <strong>⚡ Special Ability:</strong> {vehicle.special_ability}
                </div>
                
                <div class="vehicle-action">
                    {'<button class="vehicle-btn owned-btn">✅ Owned</button>' if owned else 
                     f'<button onclick="purchaseVehicle(\\'{{vehicle_id}}\\')" class="vehicle-btn purchase-btn" {{\"disabled\" if not can_afford else \"\"}}>{"💸 Can\\'t Afford" if not can_afford else f"🛒 Buy for {vehicle.cost_fbx} FBX"}</button>'}
                </div>
            </div>
            """
        
        return f"""
        <div class="shop-content">
            <div class="shop-header">
                <h3>🏪 Premium Vehicle Dealership</h3>
                <div class="player-balance">
                    <span>💰 Your Balance: {game.player.fbx_tokens:.2f} FBX</span>
                </div>
            </div>
            
            <div class="vehicles-grid">
                {vehicles_html}
            </div>
        </div>
        """
    
    def _render_statistics_tab(self, game) -> str:
        """Render detailed statistics tab"""
        relationships_html = ""
        for npc_id, encounters in game.player.npc_relationships.items():
            npc = game.npcs.get(npc_id)
            if npc:
                relationships_html += f"""
                <div class="relationship-item">
                    <span class="npc-name">{npc.name}</span>
                    <span class="encounter-count">{encounters} encounters</span>
                    <div class="relationship-bar">
                        <div class="relationship-fill" style="width: {min(encounters * 20, 100)}%"></div>
                    </div>
                </div>
                """
        
        achievements_html = ""
        for achievement in game.player.achievements:
            achievements_html += f'<li class="achievement-item">🏆 {achievement}</li>'
        
        return f"""
        <div class="stats-content">
            <div class="stats-grid">
                <div class="stats-section">
                    <h4>📊 General Stats</h4>
                    <div class="stats-list">
                        <div class="stat-row">
                            <span>🎯 Level:</span>
                            <span>{game.player.level}</span>
                        </div>
                        <div class="stat-row">
                            <span>⚡ Experience:</span>
                            <span>{game.player.experience}</span>
                        </div>
                        <div class="stat-row">
                            <span>⏰ Playtime:</span>
                            <span>{game.player.playtime_hours:.1f} hours</span>
                        </div>
                        <div class="stat-row">
                            <span>✨ Style Points:</span>
                            <span>{game.player.style_points}</span>
                        </div>
                    </div>
                </div>
                
                <div class="stats-section">
                    <h4>🗺️ Progress</h4>
                    <div class="stats-list">
                        <div class="stat-row">
                            <span>📍 Unlocked Locations:</span>
                            <span>{len(game.player.unlocked_locations)}/{len(game.locations)}</span>
                        </div>
                        <div class="stat-row">
                            <span>✅ Completed Missions:</span>
                            <span>{len(game.player.completed_missions)}</span>
                        </div>
                        <div class="stat-row">
                            <span>🚗 Current Vehicle:</span>
                            <span>{game.vehicles[game.player.current_vehicle].name}</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="relationships-section">
                <h4>💕 NPC Relationships</h4>
                <div class="relationships-list">
                    {relationships_html if relationships_html else '<p class="no-data">No relationships established yet.</p>'}
                </div>
            </div>
            
            <div class="achievements-section">
                <h4>🏆 Achievements</h4>
                <ul class="achievements-list">
                    {achievements_html if achievements_html else '<li class="no-data">No achievements yet.</li>'}
                </ul>
            </div>
        </div>
        """
    
    def _render_settings_tab(self, game) -> str:
        """Render game settings tab"""
        return f"""
        <div class="settings-content">
            <div class="settings-section">
                <h4>⚙️ Game Settings</h4>
                <div class="settings-list">
                    <div class="setting-item">
                        <label>🎬 Animations:</label>
                        <button onclick="toggleSetting('animations')" class="setting-toggle {'on' if game.animations_enabled else 'off'}">
                            {'ON' if game.animations_enabled else 'OFF'}
                        </button>
                    </div>
                    
                    <div class="setting-item">
                        <label>🔊 Sound Effects:</label>
                        <button onclick="toggleSetting('sounds')" class="setting-toggle {'on' if game.sound_effects_enabled else 'off'}">
                            {'ON' if game.sound_effects_enabled else 'OFF'}
                        </button>
                    </div>
                    
                    <div class="setting-item">
                        <label>🎯 Difficulty:</label>
                        <select onchange="changeDifficulty(this.value)" class="difficulty-select">
                            <option value="easy" {'selected' if game.difficulty == 'easy' else ''}>Easy</option>
                            <option value="normal" {'selected' if game.difficulty == 'normal' else ''}>Normal</option>
                            <option value="hard" {'selected' if game.difficulty == 'hard' else ''}>Hard</option>
                            <option value="insane" {'selected' if game.difficulty == 'insane' else ''}>Insane</option>
                        </select>
                    </div>
                </div>
            </div>
            
            <div class="settings-section">
                <h4>💾 Game Data</h4>
                <div class="data-actions">
                    <button onclick="saveGame()" class="data-btn save-btn">
                        💾 Save Game
                    </button>
                    <button onclick="loadGame()" class="data-btn load-btn">
                        📂 Load Game
                    </button>
                    <button onclick="resetGame()" class="data-btn reset-btn">
                        🗑️ Reset Save Data
                    </button>
                </div>
            </div>
            
            <div class="settings-section">
                <h4>ℹ️ Game Info</h4>
                <div class="game-info">
                    <p><strong>Version:</strong> AI Furby 1.25D v1.0</p>
                    <p><strong>Platform:</strong> MTAQuestWebsideX.com</p>
                    <p><strong>Integration:</strong> FURBX Token System</p>
                    <p><strong>Save File:</strong> game_save_{game.user_id}.json</p>
                </div>
            </div>
        </div>
        """
    
    def _render_encounter_modal(self) -> str:
        """Render encounter modal dialog"""
        return """
        <div id="encounter-modal" class="modal">
            <div class="modal-content encounter-modal">
                <div class="modal-header">
                    <h3 id="encounter-title">💫 Encounter</h3>
                    <span class="close" onclick="closeModal('encounter-modal')">&times;</span>
                </div>
                
                <div class="modal-body">
                    <div id="npc-profile" class="npc-profile">
                        <!-- NPC profile will be inserted here -->
                    </div>
                    
                    <div id="encounter-dialogue" class="encounter-dialogue">
                        <!-- Dialogue will be inserted here -->
                    </div>
                    
                    <div class="encounter-actions">
                        <button onclick="chooseAction('sweet_talk')" class="encounter-btn sweet-talk">
                            😘 Sweet Talk
                        </button>
                        <button onclick="chooseAction('flash_cash')" class="encounter-btn flash-cash">
                            💰 Flash Cash
                        </button>
                        <button onclick="chooseAction('physical')" class="encounter-btn physical">
                            🔥 Physical Seduction
                        </button>
                        <button onclick="chooseAction('rev_engine')" class="encounter-btn rev-engine">
                            🚗 Rev Engine
                        </button>
                        <button onclick="chooseAction('risky_gamble')" class="encounter-btn risky-gamble">
                            🎲 Risky Gamble
                        </button>
                        <button onclick="chooseAction('premium_fbx')" class="encounter-btn premium-fbx">
                            🪙 Use FBX Tokens
                        </button>
                        <button onclick="chooseAction('drive_away')" class="encounter-btn drive-away">
                            💨 Drive Away
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _render_results_modal(self) -> str:
        """Render results modal dialog"""
        return """
        <div id="results-modal" class="modal">
            <div class="modal-content results-modal">
                <div class="modal-header">
                    <h3 id="results-title">📊 Results</h3>
                    <span class="close" onclick="closeModal('results-modal')">&times;</span>
                </div>
                
                <div class="modal-body">
                    <div id="results-content" class="results-content">
                        <!-- Results will be inserted here -->
                    </div>
                    
                    <div class="results-actions">
                        <button onclick="closeModal('results-modal')" class="results-btn continue-btn">
                            ⏭️ Continue
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _get_game_css(self) -> str:
        """Get CSS styles for the game interface"""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            background: linear-gradient(135deg, #2d1b69 0%, #8b5cf6 50%, #ef4444 100%);
            min-height: 100vh;
            color: #fff;
            line-height: 1.6;
        }
        
        .game-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .game-header {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            border: 2px solid #8b5cf6;
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header-content h1 {
            color: #8b5cf6;
            font-size: 2.2em;
            font-weight: bold;
            text-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
        }
        
        .player-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .player-name {
            font-size: 1.2em;
            font-weight: bold;
            color: #fbbf24;
        }
        
        .level-badge {
            background: linear-gradient(45deg, #8b5cf6, #ef4444);
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
        }
        
        .game-dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .player-hud, .location-view, .vehicle-display, .action-panel {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #8b5cf6;
            box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
        }
        
        .player-hud h3, .location-view h2, .vehicle-display h3, .action-panel h3 {
            color: #8b5cf6;
            margin-bottom: 15px;
            font-size: 1.4em;
        }
        
        .hud-section {
            margin-bottom: 20px;
        }
        
        .stat-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }
        
        .stat-label {
            color: #cbd5e1;
        }
        
        .stat-value {
            color: #fbbf24;
            font-weight: bold;
        }
        
        .progress-item {
            margin-bottom: 12px;
        }
        
        .progress-item label {
            display: block;
            margin-bottom: 4px;
            color: #cbd5e1;
            font-size: 0.9em;
        }
        
        .progress-bar {
            position: relative;
            width: 100%;
            height: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            transition: width 0.3s ease;
            border-radius: 10px;
        }
        
        .progress-fill.energy {
            background: linear-gradient(90deg, #10b981, #34d399);
        }
        
        .progress-fill.heat {
            background: linear-gradient(90deg, #ef4444, #f87171);
        }
        
        .progress-fill.reputation {
            background: linear-gradient(90deg, #8b5cf6, #a78bfa);
        }
        
        .progress-fill.experience {
            background: linear-gradient(90deg, #fbbf24, #fcd34d);
        }
        
        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 0.8em;
            font-weight: bold;
            color: #fff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }
        
        .location-header {
            margin-bottom: 15px;
        }
        
        .location-stats {
            display: flex;
            gap: 15px;
            margin-top: 8px;
        }
        
        .location-stats span {
            background: rgba(139, 92, 246, 0.2);
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.9em;
        }
        
        .ascii-art {
            background: rgba(0, 0, 0, 0.6);
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
        }
        
        .ascii-art pre {
            color: #8b5cf6;
            font-size: 0.9em;
            line-height: 1.2;
        }
        
        .location-actions, .action-grid {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .action-btn, .game-action-btn, .travel-action-btn {
            padding: 10px 16px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .encounter-btn {
            background: #ef4444;
            color: white;
        }
        
        .explore-btn {
            background: #8b5cf6;
            color: white;
        }
        
        .rest-btn {
            background: #10b981;
            color: white;
        }
        
        .save-btn {
            background: #fbbf24;
            color: black;
        }
        
        .travel-btn, .shop-btn {
            background: #6366f1;
            color: white;
        }
        
        .action-btn:hover, .game-action-btn:hover, .travel-action-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        .vehicle-info h4 {
            color: #fbbf24;
            margin-bottom: 8px;
        }
        
        .vehicle-stats {
            display: flex;
            gap: 15px;
            margin-bottom: 10px;
        }
        
        .vehicle-stats span {
            background: rgba(139, 92, 246, 0.2);
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.8em;
        }
        
        .engine-sound {
            text-align: center;
            color: #8b5cf6;
            font-weight: bold;
            margin-top: 10px;
        }
        
        .game-tabs {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #8b5cf6;
        }
        
        .tab-buttons {
            display: flex;
            background: rgba(139, 92, 246, 0.2);
        }
        
        .tab-button {
            flex: 1;
            padding: 15px 20px;
            border: none;
            background: transparent;
            color: #cbd5e1;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .tab-button.active {
            background: #8b5cf6;
            color: white;
        }
        
        .tab-button:hover:not(.active) {
            background: rgba(139, 92, 246, 0.4);
            color: white;
        }
        
        .tab-content {
            display: none;
            padding: 30px;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .locations-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .location-item {
            display: grid;
            grid-template-columns: auto auto 1fr auto auto auto;
            gap: 15px;
            align-items: center;
            padding: 12px;
            background: rgba(139, 92, 246, 0.1);
            border-radius: 8px;
            border: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        .location-item.current {
            border-color: #8b5cf6;
            background: rgba(139, 92, 246, 0.2);
        }
        
        .location-item:hover {
            background: rgba(139, 92, 246, 0.15);
        }
        
        .travel-btn {
            padding: 6px 12px;
            font-size: 0.9em;
        }
        
        .travel-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .vehicles-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .vehicle-item {
            background: rgba(139, 92, 246, 0.1);
            border: 2px solid transparent;
            border-radius: 12px;
            padding: 20px;
            transition: all 0.3s ease;
        }
        
        .vehicle-item:hover {
            border-color: #8b5cf6;
            transform: translateY(-5px);
        }
        
        .vehicle-item.owned {
            border-color: #10b981;
            background: rgba(16, 185, 129, 0.1);
        }
        
        .vehicle-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .vehicle-header h4 {
            color: #fbbf24;
        }
        
        .vehicle-type {
            background: #8b5cf6;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.8em;
        }
        
        .vehicle-ascii-mini {
            margin: 15px 0;
        }
        
        .vehicle-ascii-mini pre {
            color: #8b5cf6;
            font-size: 0.8em;
            text-align: center;
        }
        
        .vehicle-stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin: 15px 0;
        }
        
        .vehicle-special {
            margin: 15px 0;
            padding: 10px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 6px;
            font-size: 0.9em;
        }
        
        .vehicle-btn {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .purchase-btn {
            background: #8b5cf6;
            color: white;
        }
        
        .purchase-btn:disabled {
            background: #6b7280;
            cursor: not-allowed;
        }
        
        .owned-btn {
            background: #10b981;
            color: white;
            cursor: default;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .stats-section {
            background: rgba(139, 92, 246, 0.1);
            padding: 20px;
            border-radius: 10px;
        }
        
        .stats-section h4 {
            color: #8b5cf6;
            margin-bottom: 15px;
        }
        
        .relationships-list, .achievements-list {
            margin-top: 15px;
        }
        
        .relationship-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding: 8px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 6px;
        }
        
        .relationship-bar {
            width: 60px;
            height: 8px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
            overflow: hidden;
        }
        
        .relationship-fill {
            height: 100%;
            background: linear-gradient(90deg, #ef4444, #fbbf24);
        }
        
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
        }
        
        .modal-content {
            background: linear-gradient(135deg, #1f2937, #374151);
            margin: 5% auto;
            padding: 0;
            border-radius: 15px;
            width: 80%;
            max-width: 600px;
            border: 2px solid #8b5cf6;
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
        }
        
        .modal-header {
            background: #8b5cf6;
            padding: 20px;
            border-radius: 13px 13px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .modal-header h3 {
            margin: 0;
            color: white;
        }
        
        .close {
            color: white;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }
        
        .close:hover {
            opacity: 0.7;
        }
        
        .modal-body {
            padding: 20px;
        }
        
        .encounter-actions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 20px;
        }
        
        .encounter-btn {
            padding: 12px 16px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            background: #8b5cf6;
            color: white;
        }
        
        .encounter-btn:hover {
            background: #7c3aed;
            transform: translateY(-2px);
        }
        
        .no-data {
            color: #6b7280;
            font-style: italic;
        }
        
        @media (max-width: 768px) {
            .game-dashboard {
                grid-template-columns: 1fr;
            }
            
            .header-content {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }
            
            .header-content h1 {
                font-size: 1.8em;
            }
            
            .tab-buttons {
                flex-wrap: wrap;
            }
            
            .tab-button {
                font-size: 0.9em;
                padding: 12px 15px;
            }
            
            .vehicles-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
        """
    
    def _get_game_javascript(self, user_id: str) -> str:
        """Get JavaScript for game functionality"""
        return f"""
        // Game JavaScript
        let currentUser = '{user_id}';
        let gameState = {{}};
        
        // Tab management
        function showGameTab(tabName) {{
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
        }}
        
        // Modal management
        function showModal(modalId) {{
            document.getElementById(modalId).style.display = 'block';
        }}
        
        function closeModal(modalId) {{
            document.getElementById(modalId).style.display = 'none';
        }}
        
        // Game actions
        function lookForEncounter() {{
            addToActivityLog('🔍 Looking for encounters...');
            
            // Simulate encounter
            setTimeout(() => {{
                const encounters = ['Street Hustler', 'Club Dancer', 'Beach Babe'];
                const encounter = encounters[Math.floor(Math.random() * encounters.length)];
                showEncounterModal(encounter);
            }}, 1000);
        }}
        
        function exploreArea() {{
            addToActivityLog('🗺️ Exploring the current area...');
            
            // Simulate random event
            setTimeout(() => {{
                const events = [
                    '💰 You found some cash on the ground! (+$200)',
                    '🔥 Your ride attracted admirers! (+5 heat)',
                    '👮 Police patrol spotted - lay low!',
                    '🎵 Street music lifts your spirits! (+10 energy)'
                ];
                const event = events[Math.floor(Math.random() * events.length)];
                addToActivityLog(event);
            }}, 1500);
        }}
        
        function restPlayer() {{
            addToActivityLog('😴 Resting to recover energy...');
            
            // Simulate rest
            setTimeout(() => {{
                addToActivityLog('⚡ Energy restored! (-$50 cash)');
                updatePlayerStats();
            }}, 1000);
        }}
        
        function saveGame() {{
            addToActivityLog('💾 Saving game...');
            
            // Simulate save
            setTimeout(() => {{
                addToActivityLog('✅ Game saved successfully!');
            }}, 500);
        }}
        
        function showEncounterModal(npcName) {{
            const modal = document.getElementById('encounter-modal');
            const title = document.getElementById('encounter-title');
            const profile = document.getElementById('npc-profile');
            const dialogue = document.getElementById('encounter-dialogue');
            
            title.textContent = `💫 Encounter with ${{npcName}}`;
            
            profile.innerHTML = `
                <div class="npc-card">
                    <h4>${{npcName}}</h4>
                    <p><strong>Style:</strong> Sultry and mysterious</p>
                    <p><strong>Heat Potential:</strong> 40 points</p>
                    <p><strong>Requirements:</strong> $300 cash, 25 rep</p>
                </div>
            `;
            
            dialogue.innerHTML = `
                <div class="dialogue-box">
                    <p>💋 "${{npcName}} looks at you with interest..."</p>
                    <p>"You've got that dangerous charm... Tell me more about yourself..."</p>
                </div>
            `;
            
            showModal('encounter-modal');
        }}
        
        function chooseAction(action) {{
            const actionNames = {{
                'sweet_talk': 'Sweet Talk',
                'flash_cash': 'Flash Cash',
                'physical': 'Physical Seduction',
                'rev_engine': 'Rev Engine',
                'risky_gamble': 'Risky Gamble',
                'premium_fbx': 'Use FBX Tokens',
                'drive_away': 'Drive Away'
            }};
            
            addToActivityLog(`🎭 You chose: ${{actionNames[action]}}`);
            
            closeModal('encounter-modal');
            
            // Simulate encounter result
            setTimeout(() => {{
                showEncounterResult(action);
            }}, 1000);
        }}
        
        function showEncounterResult(action) {{
            const results = {{
                'sweet_talk': {{
                    success: true,
                    message: '😘 Your charm worked! She is impressed by your smooth talk.',
                    rewards: '+20 heat, +3 reputation'
                }},
                'flash_cash': {{
                    success: true,
                    message: '💰 Money talks! She is very interested now.',
                    rewards: '+30 heat, +5 reputation, -$300 cash'
                }},
                'premium_fbx': {{
                    success: true,
                    message: '💎 PREMIUM EXPERIENCE! She gives you the VIP treatment!',
                    rewards: '+60 heat, +15 reputation, -2.5 FBX'
                }}
            }};
            
            const result = results[action] || {{
                success: false,
                message: '💥 That didn\\'t work out as planned...',
                rewards: 'No rewards'
            }};
            
            const modal = document.getElementById('results-modal');
            const content = document.getElementById('results-content');
            
            content.innerHTML = `
                <div class="result-card ${{result.success ? 'success' : 'failure'}}">
                    <h4>${{result.success ? '🎉 Success!' : '❌ Failed!'}}</h4>
                    <p>${{result.message}}</p>
                    <div class="rewards">
                        <strong>Rewards:</strong> ${{result.rewards}}
                    </div>
                </div>
            `;
            
            showModal('results-modal');
            
            addToActivityLog(`${{result.success ? '✅' : '❌'}} ${{result.message}}`);
            
            if (result.success) {{
                updatePlayerStats();
            }}
        }}
        
        // Travel functions
        function moveLeft() {{
            addToActivityLog('⬅️ Moving to previous location...');
            updateLocation();
        }}
        
        function moveRight() {{
            addToActivityLog('➡️ Moving to next location...');
            updateLocation();
        }}
        
        function travelTo(locationIndex) {{
            addToActivityLog(`🚁 Fast traveling to location ${{locationIndex + 1}}...`);
            updateLocation();
        }}
        
        // Vehicle functions
        function purchaseVehicle(vehicleId) {{
            addToActivityLog(`🛒 Attempting to purchase vehicle: ${{vehicleId}}...`);
            
            setTimeout(() => {{
                addToActivityLog('🎉 Vehicle purchased successfully!');
                addToActivityLog('✨ Your style points have increased!');
                updatePlayerStats();
            }}, 1000);
        }}
        
        // Settings functions
        function toggleSetting(setting) {{
            addToActivityLog(`⚙️ Toggled ${{setting}} setting`);
        }}
        
        function changeDifficulty(difficulty) {{
            addToActivityLog(`🎯 Difficulty changed to ${{difficulty}}`);
        }}
        
        function resetGame() {{
            if (confirm('⚠️ Are you sure you want to reset ALL save data?')) {{
                addToActivityLog('💥 Game data reset!');
                location.reload();
            }}
        }}
        
        function loadGame() {{
            addToActivityLog('📂 Loading saved game...');
            setTimeout(() => {{
                addToActivityLog('✅ Game loaded successfully!');
                updatePlayerStats();
            }}, 500);
        }}
        
        // Utility functions
        function addToActivityLog(message) {{
            const log = document.getElementById('activity-log');
            if (log) {{
                const timestamp = new Date().toLocaleTimeString();
                const logEntry = document.createElement('p');
                logEntry.innerHTML = `<span class="timestamp">[${{timestamp}}]</span> ${{message}}`;
                log.insertBefore(logEntry, log.firstChild);
                
                // Keep only last 10 entries
                while (log.children.length > 10) {{
                    log.removeChild(log.lastChild);
                }}
            }}
        }}
        
        function updatePlayerStats() {{
            // Simulate stat updates
            const energy = Math.floor(Math.random() * 100);
            const heat = Math.floor(Math.random() * 100);
            const reputation = Math.floor(Math.random() * 100);
            
            // Update progress bars
            updateProgressBar('energy', energy);
            updateProgressBar('heat', heat);
            updateProgressBar('reputation', reputation);
        }}
        
        function updateProgressBar(type, value) {{
            const bar = document.querySelector(`.progress-fill.${{type}}`);
            const text = bar?.nextElementSibling;
            
            if (bar) {{
                bar.style.width = `${{value}}%`;
            }}
            
            if (text && type !== 'reputation') {{
                text.textContent = `${{value}}/100`;
            }} else if (text) {{
                text.textContent = value.toString();
            }}
        }}
        
        function updateLocation() {{
            setTimeout(() => {{
                addToActivityLog('📍 Arrived at new location!');
                // Refresh page or update location display
            }}, 1000);
        }}
        
        // Initialize game
        document.addEventListener('DOMContentLoaded', function() {{
            addToActivityLog('🎮 Welcome to AI Furby 1.25D: San Andreas Edition!');
            addToActivityLog('🌟 Use the action buttons to start your adventure.');
            
            // Auto-update stats every 30 seconds
            setInterval(updatePlayerStats, 30000);
        }});
        
        // Close modals when clicking outside
        window.onclick = function(event) {{
            const modals = document.querySelectorAll('.modal');
            modals.forEach(modal => {{
                if (event.target === modal) {{
                    modal.style.display = 'none';
                }}
            }});
        }}
        """
    
    def _render_error_page(self, error_message: str) -> str:
        """Render error page"""
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>AI Furby 1.25D - Error</title>
            <style>
                body {{
                    font-family: 'Consolas', monospace;
                    background: linear-gradient(135deg, #2d1b69 0%, #8b5cf6 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }}
                .error-container {{
                    background: rgba(0, 0, 0, 0.8);
                    padding: 40px;
                    border-radius: 15px;
                    text-align: center;
                    max-width: 500px;
                    border: 2px solid #ef4444;
                }}
                .error-icon {{
                    font-size: 4em;
                    margin-bottom: 20px;
                }}
                .error-title {{
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #ef4444;
                    margin-bottom: 15px;
                }}
                .error-message {{
                    color: #cbd5e1;
                    margin-bottom: 25px;
                }}
                .retry-btn {{
                    padding: 12px 24px;
                    background: #8b5cf6;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    font-weight: bold;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <div class="error-icon">💥</div>
                <div class="error-title">Game Error</div>
                <div class="error-message">{error_message}</div>
                <button class="retry-btn" onclick="location.reload()">🔄 Retry</button>
            </div>
        </body>
        </html>
        """

# Global web interface instance
furby_web_interface = None

def get_furby_web_interface() -> FurbyGameWebInterface:
    """Get global web interface instance"""
    global furby_web_interface
    if furby_web_interface is None:
        furby_web_interface = FurbyGameWebInterface()
    return furby_web_interface

if __name__ == "__main__":
    # Test web interface
    logging.basicConfig(level=logging.INFO)
    
    web_interface = FurbyGameWebInterface()
    
    print("🌐 AI Furby 1.25D Web Interface Test")
    
    # Generate test HTML
    test_html = web_interface.render_game_dashboard("test_web_player")
    
    # Save to file
    with open("furby_game_web_test.html", "w", encoding="utf-8") as f:
        f.write(test_html)
    
    print("✅ Web interface HTML generated: furby_game_web_test.html")
    print("🎮 Open the file in a browser to test the interface!")