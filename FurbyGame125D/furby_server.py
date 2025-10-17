"""
AI Furby 1.25D: San Andreas Edition - Server Integration
Complete Flask server endpoints for web gameplay integration
MTAQuestWebsideX.com platform integration
"""

from flask import Flask, request, jsonify, render_template_string, session
from typing import Dict, Any
import json
import logging
import os
import time
from datetime import datetime

# Import game components
from furby_san_andreas import get_furby_game, active_games, FurbyGame125D
from furby_web_interface import get_furby_web_interface

logger = logging.getLogger(__name__)

class FurbyGameServer:
    """
    Flask server for AI Furby 1.25D: San Andreas Edition
    Provides REST API endpoints for web gameplay
    """
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "furby_san_andreas_1.25d_secret_key_2024"
        self.web_interface = get_furby_web_interface()
        self.setup_routes()
        logger.info("🚀 Furby Game Server initialized")
    
    def setup_routes(self):
        """Setup all API routes"""
        
        @self.app.route('/')
        def home():
            """Main game dashboard"""
            try:
                user_id = session.get('user_id', f"web_user_{int(time.time())}")
                session['user_id'] = user_id
                
                html = self.web_interface.render_game_dashboard(user_id)
                return html
                
            except Exception as e:
                logger.error(f"Home route error: {e}")
                return self.render_error_response(f"Failed to load game: {str(e)}")
        
        @self.app.route('/api/game/status')
        def get_game_status():
            """Get current game status"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                game.load_game_state()
                
                status = {
                    "user_id": user_id,
                    "player": {
                        "name": game.player.name,
                        "level": game.player.level,
                        "experience": game.player.experience,
                        "energy": game.player.energy,
                        "heat": game.player.heat,
                        "reputation": game.player.reputation,
                        "cash_usd": game.player.cash_usd,
                        "fbx_tokens": game.player.fbx_tokens,
                        "current_vehicle": game.player.current_vehicle,
                        "playtime_hours": game.player.playtime_hours
                    },
                    "game": {
                        "position": game.position,
                        "current_location": game.locations[game.position].name,
                        "game_time": game.game_time,
                        "difficulty": game.difficulty,
                        "animations_enabled": game.animations_enabled,
                        "sound_effects_enabled": game.sound_effects_enabled
                    },
                    "timestamp": datetime.now().isoformat()
                }
                
                return jsonify(status)
                
            except Exception as e:
                logger.error(f"Game status error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/encounter', methods=['POST'])
        def create_encounter():
            """Generate new encounter"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                
                # Generate encounter
                encounter_result = game.generate_encounter()
                
                if encounter_result:
                    npc, interaction_text = encounter_result
                    
                    response = {
                        "success": True,
                        "encounter": {
                            "npc": {
                                "id": npc.npc_id,
                                "name": npc.name,
                                "style": npc.style,
                                "personality": npc.personality,
                                "heat_potential": npc.heat_potential,
                                "cash_requirement": npc.cash_requirement,
                                "reputation_requirement": npc.reputation_requirement
                            },
                            "interaction_text": interaction_text,
                            "available_actions": [
                                {"id": "sweet_talk", "name": "😘 Sweet Talk", "description": "Use charm and smooth words"},
                                {"id": "flash_cash", "name": "💰 Flash Cash", "description": "Show off your wealth"},
                                {"id": "physical", "name": "🔥 Physical Seduction", "description": "Use physical appeal"},
                                {"id": "rev_engine", "name": "🚗 Rev Engine", "description": "Show off your ride"},
                                {"id": "risky_gamble", "name": "🎲 Risky Gamble", "description": "Take a big risk"},
                                {"id": "premium_fbx", "name": "🪙 Use FBX Tokens", "description": "Premium experience with tokens"},
                                {"id": "drive_away", "name": "💨 Drive Away", "description": "Leave the encounter"}
                            ]
                        }
                    }
                    
                    return jsonify(response)
                else:
                    return jsonify({
                        "success": False,
                        "message": "No encounters available right now. Try again later."
                    })
                
            except Exception as e:
                logger.error(f"Encounter creation error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/encounter/action', methods=['POST'])
        def handle_encounter_action():
            """Handle encounter action choice"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                data = request.get_json()
                action = data.get('action')
                npc_id = data.get('npc_id')
                
                if not action or not npc_id:
                    return jsonify({"error": "Missing action or npc_id"}), 400
                
                game = get_furby_game(user_id)
                
                # Find NPC
                npc = game.npcs.get(npc_id)
                if not npc:
                    return jsonify({"error": "NPC not found"}), 404
                
                # Handle encounter action
                result = game.handle_encounter_action(npc, action)
                
                return jsonify({
                    "success": True,
                    "result": result,
                    "player_status": {
                        "energy": game.player.energy,
                        "heat": game.player.heat,
                        "reputation": game.player.reputation,
                        "cash_usd": game.player.cash_usd,
                        "fbx_tokens": game.player.fbx_tokens,
                        "experience": game.player.experience
                    }
                })
                
            except Exception as e:
                logger.error(f"Encounter action error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/travel', methods=['POST'])
        def travel_to_location():
            """Travel to different location"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                data = request.get_json()
                target_position = data.get('position')
                direction = data.get('direction')  # 'left', 'right', or specific position
                
                game = get_furby_game(user_id)
                
                if direction == 'left':
                    if game.position > 0:
                        game.position -= 1
                        success = True
                        message = "Moved to previous location"
                    else:
                        success = False
                        message = "Already at the first location"
                        
                elif direction == 'right':
                    if game.position < len(game.locations) - 1:
                        game.position += 1
                        success = True
                        message = "Moved to next location"
                    else:
                        success = False
                        message = "Already at the last location"
                        
                elif target_position is not None:
                    if 0 <= target_position < len(game.locations):
                        target_location = game.locations[target_position]
                        
                        # Check if location is unlocked
                        if target_location.name in game.player.unlocked_locations:
                            # Check entry cost
                            if game.player.cash_usd >= target_location.entry_cost:
                                game.player.cash_usd -= target_location.entry_cost
                                game.position = target_position
                                success = True
                                message = f"Traveled to {target_location.name}"
                                
                                if target_location.entry_cost > 0:
                                    message += f" (Cost: ${target_location.entry_cost})"
                            else:
                                success = False
                                message = f"Not enough cash for {target_location.name} (${target_location.entry_cost} required)"
                        else:
                            success = False
                            message = f"{target_location.name} is locked"
                    else:
                        success = False
                        message = "Invalid location"
                else:
                    success = False
                    message = "Invalid travel parameters"
                
                if success:
                    # Save game after travel
                    game.save_game_state()
                    
                    current_location = game.locations[game.position]
                    
                    return jsonify({
                        "success": True,
                        "message": message,
                        "current_location": {
                            "position": game.position,
                            "name": current_location.name,
                            "icon": current_location.icon,
                            "danger_level": current_location.danger_level,
                            "luxury_level": current_location.luxury_level,
                            "ascii_art": current_location.ascii_art
                        },
                        "player_status": {
                            "cash_usd": game.player.cash_usd
                        }
                    })
                else:
                    return jsonify({
                        "success": False,
                        "message": message
                    })
                
            except Exception as e:
                logger.error(f"Travel error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/explore')
        def explore_area():
            """Explore current area"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                
                # Generate random exploration event
                current_location = game.locations[game.position]
                
                exploration_events = [
                    {
                        "type": "cash_find",
                        "message": "💰 You found some cash dropped by someone!",
                        "reward": {"type": "cash", "amount": 200}
                    },
                    {
                        "type": "heat_boost",
                        "message": "🔥 Your impressive ride caught attention from admirers!",
                        "reward": {"type": "heat", "amount": 5}
                    },
                    {
                        "type": "police_warning",
                        "message": "👮 Police patrol spotted - better lay low for a while.",
                        "reward": {"type": "heat", "amount": -10}
                    },
                    {
                        "type": "energy_boost",
                        "message": "🎵 Street music and good vibes lift your spirits!",
                        "reward": {"type": "energy", "amount": 10}
                    },
                    {
                        "type": "reputation_gain",
                        "message": "⭐ Locals recognize your style and show respect!",
                        "reward": {"type": "reputation", "amount": 3}
                    }
                ]
                
                # Higher danger areas have more intense events
                if current_location.danger_level > 7:
                    exploration_events.extend([
                        {
                            "type": "big_risk",
                            "message": "⚠️ You stumbled into a dangerous situation but handled it smoothly!",
                            "reward": {"type": "reputation", "amount": 10}
                        },
                        {
                            "type": "underground_tip",
                            "message": "🤫 Someone whispered about a secret location...",
                            "reward": {"type": "special", "amount": "location_hint"}
                        }
                    ])
                
                # Random event selection
                import random
                event = random.choice(exploration_events)
                
                # Apply rewards
                reward = event["reward"]
                if reward["type"] == "cash":
                    game.player.cash_usd += reward["amount"]
                elif reward["type"] == "heat":
                    game.player.heat = max(0, min(100, game.player.heat + reward["amount"]))
                elif reward["type"] == "energy":
                    game.player.energy = max(0, min(100, game.player.energy + reward["amount"]))
                elif reward["type"] == "reputation":
                    game.player.reputation += reward["amount"]
                
                # Add experience for exploring
                game.player.experience += 5
                game.player.check_level_up()
                
                # Reduce energy slightly
                game.player.energy = max(0, game.player.energy - 3)
                
                # Save game
                game.save_game_state()
                
                return jsonify({
                    "success": True,
                    "event": event,
                    "player_status": {
                        "energy": game.player.energy,
                        "heat": game.player.heat,
                        "reputation": game.player.reputation,
                        "cash_usd": game.player.cash_usd,
                        "experience": game.player.experience,
                        "level": game.player.level
                    }
                })
                
            except Exception as e:
                logger.error(f"Exploration error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/rest', methods=['POST'])
        def rest_player():
            """Rest and recover energy"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                
                rest_cost = 50
                
                if game.player.cash_usd >= rest_cost:
                    game.player.cash_usd -= rest_cost
                    game.player.energy = min(100, game.player.energy + 25)
                    game.player.heat = max(0, game.player.heat - 5)  # Reduce heat slightly
                    
                    # Save game
                    game.save_game_state()
                    
                    return jsonify({
                        "success": True,
                        "message": f"Rested and recovered energy! (-${rest_cost})",
                        "player_status": {
                            "energy": game.player.energy,
                            "heat": game.player.heat,
                            "cash_usd": game.player.cash_usd
                        }
                    })
                else:
                    return jsonify({
                        "success": False,
                        "message": f"Not enough cash to rest (${rest_cost} required)"
                    })
                
            except Exception as e:
                logger.error(f"Rest error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/vehicle/purchase', methods=['POST'])
        def purchase_vehicle():
            """Purchase a vehicle"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                data = request.get_json()
                vehicle_id = data.get('vehicle_id')
                
                if not vehicle_id:
                    return jsonify({"error": "Missing vehicle_id"}), 400
                
                game = get_furby_game(user_id)
                
                vehicle = game.vehicles.get(vehicle_id)
                if not vehicle:
                    return jsonify({"error": "Vehicle not found"}), 404
                
                if game.player.fbx_tokens >= vehicle.cost_fbx:
                    game.player.fbx_tokens -= vehicle.cost_fbx
                    game.player.current_vehicle = vehicle_id
                    game.player.style_points += vehicle.style_points
                    
                    # Add experience for purchase
                    game.player.experience += 20
                    game.player.check_level_up()
                    
                    # Save game
                    game.save_game_state()
                    
                    return jsonify({
                        "success": True,
                        "message": f"Purchased {vehicle.name}! Style points increased!",
                        "vehicle": {
                            "id": vehicle_id,
                            "name": vehicle.name,
                            "type": vehicle.type,
                            "style_points": vehicle.style_points,
                            "special_ability": vehicle.special_ability
                        },
                        "player_status": {
                            "fbx_tokens": game.player.fbx_tokens,
                            "style_points": game.player.style_points,
                            "experience": game.player.experience,
                            "level": game.player.level,
                            "current_vehicle": game.player.current_vehicle
                        }
                    })
                else:
                    return jsonify({
                        "success": False,
                        "message": f"Not enough FBX tokens (need {vehicle.cost_fbx}, have {game.player.fbx_tokens:.2f})"
                    })
                
            except Exception as e:
                logger.error(f"Vehicle purchase error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/save', methods=['POST'])
        def save_game():
            """Save game state"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                game.save_game_state()
                
                return jsonify({
                    "success": True,
                    "message": "Game saved successfully!",
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                logger.error(f"Save error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/load', methods=['POST'])
        def load_game():
            """Load game state"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                game = get_furby_game(user_id)
                
                if game.load_game_state():
                    return jsonify({
                        "success": True,
                        "message": "Game loaded successfully!",
                        "player_status": {
                            "name": game.player.name,
                            "level": game.player.level,
                            "experience": game.player.experience,
                            "energy": game.player.energy,
                            "heat": game.player.heat,
                            "reputation": game.player.reputation,
                            "cash_usd": game.player.cash_usd,
                            "fbx_tokens": game.player.fbx_tokens,
                            "current_vehicle": game.player.current_vehicle
                        }
                    })
                else:
                    return jsonify({
                        "success": False,
                        "message": "No save file found"
                    })
                
            except Exception as e:
                logger.error(f"Load error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/settings', methods=['POST'])
        def update_settings():
            """Update game settings"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                data = request.get_json()
                setting = data.get('setting')
                value = data.get('value')
                
                if not setting:
                    return jsonify({"error": "Missing setting"}), 400
                
                game = get_furby_game(user_id)
                
                if setting == 'animations':
                    game.animations_enabled = bool(value)
                elif setting == 'sounds':
                    game.sound_effects_enabled = bool(value)
                elif setting == 'difficulty':
                    if value in ['easy', 'normal', 'hard', 'insane']:
                        game.difficulty = value
                    else:
                        return jsonify({"error": "Invalid difficulty"}), 400
                else:
                    return jsonify({"error": "Unknown setting"}), 400
                
                # Save game
                game.save_game_state()
                
                return jsonify({
                    "success": True,
                    "message": f"Setting '{setting}' updated to {value}",
                    "settings": {
                        "animations_enabled": game.animations_enabled,
                        "sound_effects_enabled": game.sound_effects_enabled,
                        "difficulty": game.difficulty
                    }
                })
                
            except Exception as e:
                logger.error(f"Settings error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/game/reset', methods=['POST'])
        def reset_game():
            """Reset game save data"""
            try:
                user_id = session.get('user_id')
                if not user_id:
                    return jsonify({"error": "No active session"}), 400
                
                # Remove from active games
                if user_id in active_games:
                    del active_games[user_id]
                
                # Delete save file
                save_file = f"game_save_{user_id}.json"
                if os.path.exists(save_file):
                    os.remove(save_file)
                
                return jsonify({
                    "success": True,
                    "message": "Game data reset successfully!"
                })
                
            except Exception as e:
                logger.error(f"Reset error: {e}")
                return jsonify({"error": str(e)}), 500
        
        # Error handlers
        @self.app.errorhandler(404)
        def not_found(error):
            return jsonify({"error": "Endpoint not found"}), 404
        
        @self.app.errorhandler(500)
        def internal_error(error):
            return jsonify({"error": "Internal server error"}), 500
    
    def render_error_response(self, message: str) -> str:
        """Render error response HTML"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Furby Game Error</title>
            <style>
                body {{ font-family: monospace; background: #2d1b69; color: white; 
                       display: flex; align-items: center; justify-content: center; 
                       min-height: 100vh; margin: 0; }}
                .error {{ background: rgba(0,0,0,0.8); padding: 40px; border-radius: 15px; 
                        text-align: center; border: 2px solid #ef4444; }}
                .error h1 {{ color: #ef4444; }}
                .retry {{ background: #8b5cf6; color: white; border: none; 
                        padding: 12px 24px; border-radius: 8px; margin-top: 20px; 
                        cursor: pointer; }}
            </style>
        </head>
        <body>
            <div class="error">
                <h1>💥 Game Error</h1>
                <p>{message}</p>
                <button class="retry" onclick="location.reload()">🔄 Retry</button>
            </div>
        </body>
        </html>
        """
    
    def run(self, host='127.0.0.1', port=5000, debug=True):
        """Run the Flask server"""
        print(f"🚀 AI Furby 1.25D Server starting...")
        print(f"🌐 Game URL: http://{host}:{port}")
        print(f"🎮 Ready for web gameplay!")
        
        self.app.run(host=host, port=port, debug=debug)

# Global server instance
furby_server = None

def get_furby_server() -> FurbyGameServer:
    """Get global server instance"""
    global furby_server
    if furby_server is None:
        furby_server = FurbyGameServer()
    return furby_server

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Start server
    server = FurbyGameServer()
    server.run(host='0.0.0.0', port=5000, debug=True)