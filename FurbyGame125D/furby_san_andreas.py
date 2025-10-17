"""
AI Furby 1.25D: San Andreas Edition - Core Game Engine
MTAQuestWebsideX.com - Advanced Pseudo-3D Gaming Experience
Integracja z FURBX Token System dla kompletnej ekonomii gry
"""

import random
import time
import os
import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import logging

# Import our token system for economic integration
import sys
sys.path.append('../TokenSystem')
from token_logic import get_token_system
from wallet_manager import get_wallet_manager

logger = logging.getLogger(__name__)

@dataclass
class NPCCharacter:
    """Represents an NPC character in the game"""
    name: str
    style: str
    personality: str
    heat_reward: int
    cash_requirement: int
    reputation_needed: int
    location_preference: str
    dialogue_lines: List[str]
    special_ability: str
    rarity: str  # common, rare, legendary

@dataclass
class GameLocation:
    """Represents a location in the 1.25D world"""
    name: str
    type: str
    icon: str
    danger_level: int
    luxury_level: int
    encounters: List[str]
    special_events: List[str]
    ascii_art: List[str]
    background_music: str
    entry_cost: int

@dataclass
class Vehicle:
    """Represents a vehicle in the game"""
    name: str
    type: str
    speed: int
    style_points: int
    fuel_consumption: int
    special_ability: str
    cost_fbx: float
    ascii_art: List[str]
    engine_sound: str

@dataclass
class PlayerStats:
    """Complete player statistics"""
    name: str
    cash_usd: int
    fbx_tokens: float
    energy: int
    heat: int
    reputation: int
    style_points: int
    experience: int
    level: int
    current_vehicle: str
    unlocked_locations: List[str]
    completed_missions: List[str]
    npc_relationships: Dict[str, int]
    achievements: List[str]
    playtime_hours: float

class FurbyGame125D:
    """
    AI Furby 1.25D: San Andreas Edition
    Complete pseudo-3D gaming experience with FURBX token integration
    """
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.token_system = get_token_system()
        self.wallet_manager = get_wallet_manager()
        
        # Initialize game systems
        self.player = self._create_default_player()
        self.position = 0
        self.game_time = 0  # Game hours
        self.current_mission = None
        self.game_state = "menu"  # menu, playing, paused, mission
        
        # Load game data
        self._initialize_locations()
        self._initialize_npcs()
        self._initialize_vehicles()
        self._initialize_missions()
        
        # Game settings
        self.animations_enabled = True
        self.sound_effects_enabled = True
        self.difficulty = "normal"  # easy, normal, hard, insane
        
        logger.info(f"🎮 AI Furby 1.25D initialized for user: {user_id}")
    
    def _create_default_player(self) -> PlayerStats:
        """Create default player with FURBX integration"""
        # Get real wallet balance
        wallet = self.token_system.get_balance(self.user_id)
        
        return PlayerStats(
            name="",
            cash_usd=1000,
            fbx_tokens=float(wallet.available_balance),
            energy=100,
            heat=0,
            reputation=0,
            style_points=0,
            experience=0,
            level=1,
            current_vehicle="stolen_civic",
            unlocked_locations=["ghetto"],
            completed_missions=[],
            npc_relationships={},
            achievements=[],
            playtime_hours=0.0
        )
    
    def _initialize_locations(self):
        """Initialize all game locations with detailed ASCII art"""
        self.locations = [
            GameLocation(
                name="Ghetto Streets",
                type="danger",
                icon="🏚️",
                danger_level=8,
                luxury_level=1,
                encounters=["Street_Hustler", "Gang_Girl", "Crack_Head"],
                special_events=["police_chase", "gang_shootout", "drug_deal"],
                ascii_art=[
                    "🏚️🏚️🏚️ GHETTO 🏚️🏚️🏚️",
                    "│  ╔═══╗  ╔═══╗  ╔═══╗  │",
                    "│  ║💀 ║  ║🔫 ║  ║💊 ║  │",
                    "│  ╚═══╝  ╚═══╝  ╚═══╝  │",
                    "════════════════════════════"
                ],
                background_music="🎵 Heavy Bass 🎵",
                entry_cost=0
            ),
            GameLocation(
                name="Downtown Club District",
                type="nightlife",
                icon="🏙️",
                danger_level=4,
                luxury_level=6,
                encounters=["Club_Dancer", "VIP_Hostess", "Rich_Cougar"],
                special_events=["vip_party", "dance_contest", "celebrity_sighting"],
                ascii_art=[
                    "🏙️✨🏙️ DOWNTOWN 🏙️✨🏙️",
                    "│  ╔═══╗  ╔═══╗  ╔═══╗  │",
                    "│  ║🍸 ║  ║💃 ║  ║🎭 ║  │",
                    "│  ╚═══╝  ╚═══╝  ╚═══╝  │",
                    "════════════════════════════"
                ],
                background_music="🎵 House Music 🎵",
                entry_cost=50
            ),
            GameLocation(
                name="Venice Beach",
                type="relax",
                icon="🏖️",
                danger_level=2,
                luxury_level=5,
                encounters=["Beach_Babe", "Surfer_Girl", "Yoga_Instructor"],
                special_events=["beach_party", "volleyball_game", "sunset_romance"],
                ascii_art=[
                    "🏖️🌊🏖️ BEACH 🏖️🌊🏖️",
                    "│  ╔═══╗  ╔═══╗  ╔═══╗  │",
                    "│  ║🏄 ║  ║🏐 ║  ║🌺 ║  │",
                    "│  ╚═══╝  ╚═══╝  ╚═══╝  │",
                    "════════════════════════════"
                ],
                background_music="🎵 Chill Wave 🎵",
                entry_cost=20
            ),
            GameLocation(
                name="Las Vegas Strip",
                type="luxury",
                icon="🎰",
                danger_level=3,
                luxury_level=9,
                encounters=["Casino_Hostess", "High_Roller", "Showgirl"],
                special_events=["jackpot_win", "private_show", "high_stakes_poker"],
                ascii_art=[
                    "🎰💎🎰 VEGAS 🎰💎🎰",
                    "│  ╔═══╗  ╔═══╗  ╔═══╗  │",
                    "│  ║💰 ║  ║🎲 ║  ║👑 ║  │",
                    "│  ╚═══╝  ╚═══╝  ╚═══╝  │",
                    "════════════════════════════"
                ],
                background_music="🎵 Jazz Lounge 🎵",
                entry_cost=200
            ),
            GameLocation(
                name="Hollywood Hills Mansion",
                type="elite",
                icon="🏰",
                danger_level=1,
                luxury_level=10,
                encounters=["Sugar_Mama", "Celebrity", "Trophy_Wife"],
                special_events=["pool_party", "exclusive_auction", "celebrity_scandal"],
                ascii_art=[
                    "🏰👑🏰 MANSION 🏰👑🏰",
                    "│  ╔═══╗  ╔═══╗  ╔═══╗  │",
                    "│  ║💎 ║  ║🍾 ║  ║🦄 ║  │",
                    "│  ╚═══╝  ╚═══╝  ╚═══╝  │",
                    "════════════════════════════"
                ],
                background_music="🎵 Classical Remix 🎵",
                entry_cost=1000
            )
        ]
    
    def _initialize_npcs(self):
        """Initialize all NPCs with rich personalities"""
        self.npcs = {
            "Street_Hustler": NPCCharacter(
                name="Tina 'Razor' Rodriguez",
                style="street smart badass",
                personality="tough exterior, soft heart",
                heat_reward=25,
                cash_requirement=100,
                reputation_needed=0,
                location_preference="ghetto",
                dialogue_lines=[
                    "😏 'You look like trouble... I like that.'",
                    "🔥 'This street ain't safe, but I am...'",
                    "💋 'Show me what you got, pretty boy.'"
                ],
                special_ability="street_knowledge",
                rarity="common"
            ),
            "Club_Dancer": NPCCharacter(
                name="Velvet 'Diamond' Jones",
                style="sultry club goddess",
                personality="confident performer",
                heat_reward=40,
                cash_requirement=300,
                reputation_needed=25,
                location_preference="downtown",
                dialogue_lines=[
                    "💃 'I dance for money, but stay for passion...'",
                    "✨ 'You've got that VIP energy...'",
                    "🍸 'Buy me a drink and I'll show you magic.'"
                ],
                special_ability="dance_magic",
                rarity="rare"
            ),
            "Beach_Babe": NPCCharacter(
                name="Sunny 'Wave' Martinez",
                style="californian goddess",
                personality="free spirit beach lover",
                heat_reward=35,
                cash_requirement=200,
                reputation_needed=15,
                location_preference="beach",
                dialogue_lines=[
                    "🌊 'Life's a wave, ride it with me...'",
                    "☀️ 'Your vibe is so golden...'",
                    "🏄 'Want to catch something bigger than waves?'"
                ],
                special_ability="zen_healing",
                rarity="common"
            ),
            "Casino_Hostess": NPCCharacter(
                name="Lola 'Fortune' Kim",
                style="high-stakes temptress",
                personality="sophisticated risk-taker",
                heat_reward=60,
                cash_requirement=500,
                reputation_needed=50,
                location_preference="vegas",
                dialogue_lines=[
                    "🎰 'Luck favors the bold... and the rich.'",
                    "💎 'I'm the jackpot you've been chasing...'",
                    "🍾 'High stakes, higher rewards...'"
                ],
                special_ability="luck_boost",
                rarity="rare"
            ),
            "Sugar_Mama": NPCCharacter(
                name="Madame X 'Dynasty' Chen",
                style="wealthy power player",
                personality="dominant luxury lover",
                heat_reward=100,
                cash_requirement=2000,
                reputation_needed=100,
                location_preference="mansion",
                dialogue_lines=[
                    "👑 'Money talks, but passion screams...'",
                    "💸 'I collect beautiful things... like you.'",
                    "🦄 'Welcome to my world of infinite pleasure...'"
                ],
                special_ability="wealth_magic",
                rarity="legendary"
            )
        }
    
    def _initialize_vehicles(self):
        """Initialize all available vehicles"""
        self.vehicles = {
            "stolen_civic": Vehicle(
                name="Stolen Honda Civic",
                type="starter",
                speed=3,
                style_points=1,
                fuel_consumption=5,
                special_ability="invisible_to_cops",
                cost_fbx=0.0,
                ascii_art=[
                    "🚗💨 CIVIC 💨🚗",
                    "   ╔════╗",
                    " ╔═╣    ╠═╗",
                    "╔╣  ████  ╠╗",
                    "╚═╗ ○  ○ ╔═╝",
                    "  ╚══════╝"
                ],
                engine_sound="🎵 *put put put* 🎵"
            ),
            "lowrider_impala": Vehicle(
                name="Hydraulic Lowrider",
                type="style",
                speed=4,
                style_points=8,
                fuel_consumption=8,
                special_ability="bounce_charm",
                cost_fbx=25.0,
                ascii_art=[
                    "🚗✨ LOWRIDER ✨🚗",
                    "   ╔═══════╗",
                    " ╔═╣ ♫ ♫ ♫ ╠═╗",
                    "╔╣  ████████  ╠╗",
                    "╚═╗ ◉    ◉ ╔═╝",
                    "  ╚═════════╝"
                ],
                engine_sound="🎵 *BOOM BOOM* 🎵"
            ),
            "ferrari_spider": Vehicle(
                name="Ferrari Spider",
                type="supercar",
                speed=10,
                style_points=9,
                fuel_consumption=15,
                special_ability="speed_demon",
                cost_fbx=100.0,
                ascii_art=[
                    "🏎️🔥 FERRARI 🔥🏎️",
                    "    ╔═══════╗",
                    "  ╔═╣ ⚡ ⚡ ⚡ ╠═╗",
                    "╔═╣  ████████  ╠═╗",
                    "╚══╗ ◉    ◉ ╔══╝",
                    "   ╚═════════╝"
                ],
                engine_sound="🎵 *VROOOOOM* 🎵"
            ),
            "golden_lambo": Vehicle(
                name="Golden Lamborghini",
                type="legendary",
                speed=10,
                style_points=10,
                fuel_consumption=20,
                special_ability="instant_attraction",
                cost_fbx=250.0,
                ascii_art=[
                    "🚗👑 GOLDEN LAMBO 👑🚗",
                    "     ╔═════════╗",
                    "   ╔═╣ 💎 💎 💎 ╠═╗",
                    "╔══╣  ██████████  ╠══╗",
                    "╚═══╗ ◉      ◉ ╔═══╝",
                    "    ╚═══════════╝"
                ],
                engine_sound="🎵 *GOLDEN ROAR* 🎵"
            )
        }
    
    def _initialize_missions(self):
        """Initialize story missions"""
        self.missions = {
            "tutorial": {
                "name": "Welcome to San Andreas",
                "description": "Learn the basics of cruising and charm",
                "objectives": ["Talk to 3 NPCs", "Earn 50 heat points"],
                "reward_fbx": 5.0,
                "reward_cash": 500,
                "unlock_location": "downtown"
            },
            "first_ride": {
                "name": "Get Your First Ride",
                "description": "Upgrade from stolen civic to lowrider",
                "objectives": ["Earn 25 FBX tokens", "Buy lowrider"],
                "reward_fbx": 10.0,
                "reward_cash": 1000,
                "unlock_location": "beach"
            },
            "vegas_baby": {
                "name": "What Happens in Vegas...",
                "description": "Make it big in Las Vegas",
                "objectives": ["Reach reputation 50", "Win 1000$ gambling"],
                "reward_fbx": 25.0,
                "reward_cash": 5000,
                "unlock_location": "mansion"
            }
        }
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def typewriter_effect(self, text: str, delay: float = 0.03):
        """Create typewriter effect for text"""
        if not self.animations_enabled:
            print(text)
            return
        
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # New line at the end
    
    def draw_enhanced_hud(self):
        """Draw advanced HUD with all player stats"""
        current_loc = self.locations[self.position]
        vehicle = self.vehicles[self.player.current_vehicle]
        
        # Update FBX from real wallet
        wallet = self.token_system.get_balance(self.user_id)
        self.player.fbx_tokens = float(wallet.available_balance)
        
        print(f"\n{'='*70}")
        print(f"💋 AI FURBY 1.25D: SAN ANDREAS NIGHTS 💋")
        print(f"{'='*70}")
        
        # Player info line
        print(f"👤 {self.player.name} | Level {self.player.level} | XP: {self.player.experience}")
        
        # Money line
        print(f"💰 Cash: ${self.player.cash_usd:,} | 🪙 FBX: {self.player.fbx_tokens:.2f}")
        
        # Stats bars
        energy_bar = self._create_progress_bar(self.player.energy, 100, "⚡")
        heat_bar = self._create_progress_bar(self.player.heat, 100, "🔥")
        rep_bar = self._create_progress_bar(min(self.player.reputation, 100), 100, "⭐")
        
        print(f"⚡ Energy: {energy_bar} {self.player.energy}/100")
        print(f"🔥 Heat: {heat_bar} {self.player.heat}/100")
        print(f"⭐ Rep: {rep_bar} {self.player.reputation}/100")
        
        # Vehicle and location
        print(f"🚗 {vehicle.name} | Style: {vehicle.style_points}/10")
        print(f"📍 {current_loc.icon} {current_loc.name}")
        
        # Location progress bar
        location_progress = "█" * (self.position + 1) + "░" * (len(self.locations) - self.position - 1)
        print(f"🗺️  Progress: [{location_progress}]")
        
        print(f"{'='*70}")
    
    def _create_progress_bar(self, current: int, maximum: int, icon: str, length: int = 10) -> str:
        """Create a visual progress bar"""
        filled = int((current / maximum) * length)
        empty = length - filled
        return f"{icon}[{'█' * filled}{'░' * empty}]"
    
    def draw_location_scene(self):
        """Draw current location with ASCII art"""
        current_loc = self.locations[self.position]
        
        print(f"\n{current_loc.background_music}")
        for line in current_loc.ascii_art:
            print(f"  {line}")
        
        # Show location info
        print(f"\n📍 {current_loc.name}")
        print(f"💀 Danger: {current_loc.danger_level}/10 | 💎 Luxury: {current_loc.luxury_level}/10")
        
        if current_loc.entry_cost > 0 and self.player.cash_usd < current_loc.entry_cost:
            print(f"💸 Entry cost: ${current_loc.entry_cost} (You need more cash!)")
    
    def draw_vehicle(self):
        """Draw current vehicle ASCII art"""
        vehicle = self.vehicles[self.player.current_vehicle]
        
        print(f"\n🚗 {vehicle.name} 🚗")
        for line in vehicle.ascii_art:
            print(f"  {line}")
        
        print(f"  {vehicle.engine_sound}")
        print(f"  Speed: {vehicle.speed}/10 | Style: {vehicle.style_points}/10")
    
    def show_encounter_screen(self, npc_name: str):
        """Enhanced encounter screen with NPC details"""
        npc = self.npcs[npc_name]
        current_loc = self.locations[self.position]
        
        self.clear_screen()
        self.draw_enhanced_hud()
        
        # NPC introduction
        print(f"\n💫 ENCOUNTER AT {current_loc.name.upper()} 💫")
        print(f"{'='*50}")
        
        # NPC profile card
        print(f"👤 {npc.name}")
        print(f"💅 Style: {npc.style}")
        print(f"💭 Personality: {npc.personality}")
        print(f"🔥 Heat Potential: {npc.heat_reward} points")
        print(f"💰 Cash Needed: ${npc.cash_requirement}")
        print(f"⭐ Rep Required: {npc.reputation_needed}")
        print(f"✨ Rarity: {npc.rarity.upper()}")
        
        # Show random dialogue
        dialogue = random.choice(npc.dialogue_lines)
        print(f"\n💬 {dialogue}")
        
        print(f"\n{'='*50}")
        print("💋 CHOOSE YOUR APPROACH 💋")
        print("1️⃣  😘 Sweet Talk (Charisma-based)")
        print("2️⃣  💰 Flash Cash (Money talks)")
        print("3️⃣  🔥 Physical Seduction (Risky but rewarding)")
        print("4️⃣  🚗 Rev Engine (Show off your ride)")
        print("5️⃣  🎲 Risky Gamble (High risk, high reward)")
        print("6️⃣  🎁 Use FURBX Tokens (Premium experience)")
        print("7️⃣  💨 Drive Away (Leave gracefully)")
    
    def handle_encounter_choice(self, npc_name: str, choice: str) -> Dict:
        """Handle player choice in encounter with detailed outcomes"""
        npc = self.npcs[npc_name]
        result = {
            "success": False,
            "heat_gained": 0,
            "cash_spent": 0,
            "fbx_spent": 0.0,
            "reputation_change": 0,
            "special_reward": None,
            "message": ""
        }
        
        # Check requirements
        if npc.cash_requirement > self.player.cash_usd and choice in ["2", "3", "5"]:
            result["message"] = f"💸 You need ${npc.cash_requirement} to impress {npc.name}!"
            return result
        
        if npc.reputation_needed > self.player.reputation and choice != "7":
            result["message"] = f"⭐ You need {npc.reputation_needed} reputation to approach {npc.name}!"
            return result
        
        if choice == "1":  # Sweet Talk
            success_chance = min(0.8, 0.4 + (self.player.reputation * 0.01))
            if random.random() < success_chance:
                result["success"] = True
                result["heat_gained"] = npc.heat_reward // 2
                result["reputation_change"] = random.randint(1, 3)
                result["message"] = f"😘 Your charm worked! {npc.name} is impressed by your smooth talk."
            else:
                result["message"] = f"😬 {npc.name} wasn't convinced by your lines. Need more style!"
        
        elif choice == "2":  # Flash Cash
            cost = npc.cash_requirement
            if self.player.cash_usd >= cost:
                result["success"] = True
                result["cash_spent"] = cost
                result["heat_gained"] = int(npc.heat_reward * 0.8)
                result["reputation_change"] = random.randint(2, 5)
                result["message"] = f"💰 Money talks! {npc.name} is very interested now."
            
        elif choice == "3":  # Physical Seduction
            risk_factor = npc.danger_level if hasattr(npc, 'danger_level') else 5
            success_chance = max(0.3, 0.7 - (risk_factor * 0.05))
            
            if random.random() < success_chance:
                result["success"] = True
                result["heat_gained"] = int(npc.heat_reward * 1.5)
                result["cash_spent"] = npc.cash_requirement // 2
                result["reputation_change"] = random.randint(3, 8)
                result["message"] = f"🔥 Intense chemistry! {npc.name} can't resist your physical appeal."
            else:
                result["cash_spent"] = npc.cash_requirement // 4
                result["reputation_change"] = -random.randint(1, 3)
                result["message"] = f"💥 Too aggressive! {npc.name} pushed you away."
        
        elif choice == "4":  # Rev Engine
            vehicle = self.vehicles[self.player.current_vehicle]
            style_bonus = vehicle.style_points
            
            if style_bonus >= 7:
                result["success"] = True
                result["heat_gained"] = npc.heat_reward + (style_bonus * 5)
                result["reputation_change"] = style_bonus
                result["message"] = f"🚗 Your {vehicle.name} is absolutely stunning! {npc.name} is mesmerized."
            else:
                result["message"] = f"😐 {npc.name} isn't impressed by your {vehicle.name}. Need a better ride!"
        
        elif choice == "5":  # Risky Gamble
            if random.random() < 0.4:  # 40% success rate
                result["success"] = True
                result["heat_gained"] = npc.heat_reward * 2
                result["cash_spent"] = 0
                result["reputation_change"] = random.randint(5, 15)
                result["special_reward"] = "jackpot"
                result["message"] = f"🎰 JACKPOT! Your bold move paid off big time with {npc.name}!"
            else:
                result["cash_spent"] = npc.cash_requirement
                result["reputation_change"] = -random.randint(5, 10)
                result["message"] = f"💥 Epic fail! Your risky move backfired with {npc.name}."
        
        elif choice == "6":  # Use FURBX Tokens
            fbx_cost = 2.0 + (npc.heat_reward * 0.05)
            wallet = self.token_system.get_balance(self.user_id)
            
            if wallet.available_balance >= fbx_cost:
                # Spend FURBX tokens
                success, message = self.token_system.burn_tokens(
                    self.user_id, 
                    fbx_cost, 
                    f"Premium encounter with {npc.name}"
                )
                
                if success:
                    result["success"] = True
                    result["fbx_spent"] = fbx_cost
                    result["heat_gained"] = npc.heat_reward * 3  # Triple reward!
                    result["reputation_change"] = random.randint(10, 20)
                    result["special_reward"] = "premium_experience"
                    result["message"] = f"💎 PREMIUM EXPERIENCE! {npc.name} gives you the VIP treatment!"
                else:
                    result["message"] = f"❌ Token transaction failed: {message}"
            else:
                result["message"] = f"💸 You need {fbx_cost:.2f} FBX tokens for the premium experience!"
        
        elif choice == "7":  # Drive Away
            result["message"] = f"💨 You drive away smoothly. {npc.name} watches with interest..."
            result["reputation_change"] = 1  # Slight rep gain for being cool
        
        return result
    
    def apply_encounter_result(self, result: Dict):
        """Apply the encounter result to player stats"""
        self.player.heat += result["heat_gained"]
        self.player.cash_usd -= result["cash_spent"]
        self.player.reputation += result["reputation_change"]
        self.player.fbx_tokens -= result["fbx_spent"]
        
        # Cap stats
        self.player.heat = min(self.player.heat, 100)
        self.player.reputation = max(0, self.player.reputation)
        self.player.cash_usd = max(0, self.player.cash_usd)
        
        # Experience gain
        exp_gain = (result["heat_gained"] + abs(result["reputation_change"])) * 2
        self.player.experience += exp_gain
        
        # Level up check
        required_exp = self.player.level * 100
        if self.player.experience >= required_exp:
            self.level_up()
        
        # Special rewards
        if result["special_reward"] == "jackpot":
            bonus_cash = random.randint(1000, 5000)
            self.player.cash_usd += bonus_cash
            print(f"🎰 BONUS! You won ${bonus_cash} extra!")
        
        elif result["special_reward"] == "premium_experience":
            # Grant premium status temporarily
            print("👑 You've unlocked temporary VIP status!")
            # Could integrate with actual premium system
    
    def level_up(self):
        """Handle player level up"""
        self.player.level += 1
        self.player.energy = 100  # Full energy restore
        
        # Level up rewards
        fbx_reward = self.player.level * 0.5
        cash_reward = self.player.level * 200
        
        # Give actual FURBX tokens
        success, message = self.token_system.mint_tokens(
            self.user_id,
            fbx_reward,
            f"Level {self.player.level} achievement"
        )
        
        if success:
            self.player.cash_usd += cash_reward
            
            print(f"\n🎉 LEVEL UP! Welcome to Level {self.player.level}!")
            print(f"💰 Rewards: ${cash_reward} cash + {fbx_reward} FBX tokens")
            print(f"⚡ Energy fully restored!")
        
        # Unlock new locations or vehicles based on level
        if self.player.level == 5:
            print("🏖️ Venice Beach unlocked!")
        elif self.player.level == 10:
            print("🎰 Las Vegas Strip unlocked!")
        elif self.player.level == 20:
            print("🏰 Hollywood Hills Mansion unlocked!")
    
    def travel_system(self):
        """Enhanced travel system with costs and requirements"""
        print("\n🗺️  NAVIGATION SYSTEM 🗺️")
        print("=" * 40)
        
        for i, location in enumerate(self.locations):
            current_marker = "👉" if i == self.position else "  "
            locked = "🔒" if location.name not in self.player.unlocked_locations else ""
            
            print(f"{current_marker} {i+1}. {location.icon} {location.name} {locked}")
            if location.entry_cost > 0:
                print(f"      💰 Entry: ${location.entry_cost}")
        
        print("\n⬅️  A - Move Left | ➡️  D - Move Right")
        print("🔢 [1-5] - Jump to location (costs energy)")
        print("🔄 S - Stay and explore current area")
        
        choice = input("\n🎯 Your move: ").upper()
        
        if choice == "A" and self.position > 0:
            self.position -= 1
            energy_cost = 5
            self.player.energy -= energy_cost
            print(f"⬅️  Moving left... (-{energy_cost} energy)")
            
        elif choice == "D" and self.position < len(self.locations) - 1:
            new_location = self.locations[self.position + 1]
            if new_location.name in self.player.unlocked_locations:
                if self.player.cash_usd >= new_location.entry_cost:
                    self.position += 1
                    self.player.cash_usd -= new_location.entry_cost
                    energy_cost = 5
                    self.player.energy -= energy_cost
                    print(f"➡️  Moving right... (-${new_location.entry_cost}, -{energy_cost} energy)")
                else:
                    print(f"💸 You need ${new_location.entry_cost} to enter {new_location.name}!")
            else:
                print(f"🔒 {new_location.name} is locked! Complete missions to unlock.")
        
        elif choice == "S":
            print("🔍 Exploring current area...")
            self.random_event()
        
        elif choice.isdigit():
            target = int(choice) - 1
            if 0 <= target < len(self.locations):
                target_location = self.locations[target]
                if target_location.name in self.player.unlocked_locations:
                    energy_cost = abs(target - self.position) * 10
                    if self.player.energy >= energy_cost and self.player.cash_usd >= target_location.entry_cost:
                        self.position = target
                        self.player.energy -= energy_cost
                        self.player.cash_usd -= target_location.entry_cost
                        print(f"🚁 Fast travel to {target_location.name}! (-${target_location.entry_cost}, -{energy_cost} energy)")
                    else:
                        print(f"❌ Need {energy_cost} energy and ${target_location.entry_cost} cash!")
                else:
                    print(f"🔒 {target_location.name} is locked!")
        
        else:
            print("❓ Invalid choice!")
        
        time.sleep(1)
    
    def random_event(self):
        """Enhanced random events with FURBX integration"""
        current_loc = self.locations[self.position]
        
        events = [
            {
                "text": "👮 Police patrol spotted! Lay low...",
                "effect": {"reputation": -2},
                "type": "danger"
            },
            {
                "text": "💋 Gorgeous stranger winks at you from across the street!",
                "effect": {"heat": 5},
                "type": "romance"
            },
            {
                "text": "💰 You find a wallet on the ground with cash inside!",
                "effect": {"cash_usd": random.randint(100, 500)},
                "type": "luck"
            },
            {
                "text": "🔥 Your ride attracts a crowd of admirers!",
                "effect": {"reputation": 3, "heat": 10},
                "type": "fame"
            },
            {
                "text": "🎵 Street musician plays your favorite song - feeling inspired!",
                "effect": {"energy": 20},
                "type": "inspiration"
            },
            {
                "text": "🪙 Crypto trader tips you about FURBX! You earn bonus tokens!",
                "effect": {"fbx_bonus": 1.0},
                "type": "crypto"
            }
        ]
        
        # Filter events by location type
        if current_loc.type == "danger":
            events = [e for e in events if e["type"] in ["danger", "luck"]]
        elif current_loc.type == "luxury":
            events = [e for e in events if e["type"] in ["fame", "crypto"]]
        
        event = random.choice(events)
        
        print(f"\n🎲 RANDOM EVENT:")
        self.typewriter_effect(event["text"])
        
        # Apply effects
        for effect, value in event["effect"].items():
            if effect == "cash_usd":
                self.player.cash_usd += value
                print(f"💰 +${value} cash!")
            elif effect == "reputation":
                self.player.reputation += value
                print(f"⭐ {'+' if value > 0 else ''}{value} reputation!")
            elif effect == "heat":
                self.player.heat += value
                print(f"🔥 +{value} heat!")
            elif effect == "energy":
                self.player.energy = min(100, self.player.energy + value)
                print(f"⚡ +{value} energy!")
            elif effect == "fbx_bonus":
                # Give actual FURBX tokens
                success, message = self.token_system.mint_tokens(
                    self.user_id,
                    value,
                    "Random event bonus"
                )
                if success:
                    print(f"🪙 +{value} FBX tokens!")
    
    def encounter_system(self):
        """Main encounter system"""
        current_loc = self.locations[self.position]
        
        if not current_loc.encounters:
            print("👻 This area seems empty...")
            return
        
        # Random encounter selection
        npc_type = random.choice(current_loc.encounters)
        
        self.show_encounter_screen(npc_type)
        choice = input("\n💫 Your choice (1-7): ")
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            result = self.handle_encounter_choice(npc_type, choice)
            
            print(f"\n{result['message']}")
            
            if result["success"]:
                print(f"🔥 +{result['heat_gained']} heat points!")
                if result["reputation_change"] > 0:
                    print(f"⭐ +{result['reputation_change']} reputation!")
                
                # Apply results
                self.apply_encounter_result(result)
                
                # Relationship tracking
                if npc_type not in self.player.npc_relationships:
                    self.player.npc_relationships[npc_type] = 0
                
                self.player.npc_relationships[npc_type] += 1
                
                if self.player.npc_relationships[npc_type] >= 3:
                    print(f"💕 {self.npcs[npc_type].name} remembers you fondly!")
            
            input("\n⏳ Press Enter to continue...")
        else:
            print("❓ Invalid choice!")
    
    def vehicle_shop(self):
        """Vehicle purchasing system with FURBX integration"""
        print("\n🚗 PREMIUM VEHICLE DEALERSHIP 🚗")
        print("=" * 50)
        
        for vehicle_id, vehicle in self.vehicles.items():
            owned = "✅" if vehicle_id == self.player.current_vehicle else "🛒"
            
            print(f"\n{owned} {vehicle.name}")
            print(f"    💎 Price: {vehicle.cost_fbx} FBX")
            print(f"    🏃 Speed: {vehicle.speed}/10")
            print(f"    ✨ Style: {vehicle.style_points}/10")
            print(f"    ⚡ Special: {vehicle.special_ability}")
        
        print(f"\n💰 Your Balance: {self.player.fbx_tokens:.2f} FBX")
        
        choice = input("\nEnter vehicle name to purchase (or 'back'): ").lower().replace(" ", "_")
        
        if choice == "back":
            return
        
        if choice in self.vehicles:
            vehicle = self.vehicles[choice]
            
            if choice == self.player.current_vehicle:
                print("🚗 You already own this vehicle!")
                return
            
            if self.player.fbx_tokens >= vehicle.cost_fbx:
                # Use actual FURBX token system
                wallet = self.token_system.get_balance(self.user_id)
                
                if wallet.available_balance >= vehicle.cost_fbx:
                    success, message = self.token_system.burn_tokens(
                        self.user_id,
                        vehicle.cost_fbx,
                        f"Purchased {vehicle.name}"
                    )
                    
                    if success:
                        self.player.current_vehicle = choice
                        self.player.fbx_tokens -= vehicle.cost_fbx
                        
                        print(f"🎉 Congratulations! You now own the {vehicle.name}!")
                        self.draw_vehicle()
                        
                        # Style points bonus
                        self.player.style_points = vehicle.style_points * 10
                        print(f"✨ Style points increased to {self.player.style_points}!")
                    else:
                        print(f"❌ Purchase failed: {message}")
                else:
                    print(f"💸 Insufficient FBX tokens! Need {vehicle.cost_fbx} FBX")
            else:
                print(f"💸 Insufficient FBX tokens! Need {vehicle.cost_fbx} FBX")
        else:
            print("❓ Vehicle not found!")
        
        input("\n⏳ Press Enter to continue...")
    
    def save_game_state(self):
        """Save game state to file"""
        save_data = {
            "player": asdict(self.player),
            "position": self.position,
            "game_time": self.game_time,
            "current_mission": self.current_mission,
            "last_save": datetime.datetime.now().isoformat()
        }
        
        save_file = f"game_save_{self.user_id}.json"
        
        try:
            with open(save_file, 'w') as f:
                json.dump(save_data, f, indent=2)
            print(f"💾 Game saved successfully!")
        except Exception as e:
            print(f"❌ Save failed: {e}")
    
    def load_game_state(self):
        """Load game state from file"""
        save_file = f"game_save_{self.user_id}.json"
        
        try:
            with open(save_file, 'r') as f:
                save_data = json.load(f)
            
            # Restore player data
            player_data = save_data["player"]
            self.player = PlayerStats(**player_data)
            
            self.position = save_data.get("position", 0)
            self.game_time = save_data.get("game_time", 0)
            self.current_mission = save_data.get("current_mission", None)
            
            print(f"📂 Game loaded successfully!")
            return True
            
        except FileNotFoundError:
            print("💾 No save file found. Starting new game...")
            return False
        except Exception as e:
            print(f"❌ Load failed: {e}")
            return False
    
    def check_game_over_conditions(self) -> bool:
        """Check various game over conditions"""
        if self.player.energy <= 0:
            print("\n😴 EXHAUSTION! You collapse from fatigue...")
            print("💤 Rest at your safe house to recover energy.")
            return True
        
        if self.player.heat >= 100:
            print("\n🔥🔥 ULTIMATE HEAT! You've become the LEGEND of San Andreas!")
            print("👑 You are now the undisputed King of the Night!")
            print(f"🏆 Final Stats:")
            print(f"   💰 Cash: ${self.player.cash_usd:,}")
            print(f"   🪙 FBX: {self.player.fbx_tokens:.2f}")
            print(f"   ⭐ Reputation: {self.player.reputation}")
            print(f"   🎯 Level: {self.player.level}")
            return True
        
        if self.player.reputation < -50:
            print("\n💀 GAME OVER! Your reputation is ruined...")
            print("🚫 No one wants to associate with you anymore.")
            return True
        
        return False
    
    def main_game_loop(self):
        """Main game loop"""
        # Try to load save file
        if not self.load_game_state():
            # New game setup
            self.clear_screen()
            print("🎮 AI FURBY 1.25D: SAN ANDREAS EDITION 🎮")
            print("=" * 50)
            self.typewriter_effect("Welcome to the hottest adventure in gaming...")
            
            self.player.name = input("💎 Enter your Furby Pimp name: ")
            if not self.player.name:
                self.player.name = f"Player_{self.user_id}"
            
            self.typewriter_effect(f"Welcome to San Andreas, {self.player.name}!")
            self.typewriter_effect("Build your reputation, collect heat, and become the ultimate player...")
            
            input("\n⏳ Press Enter to start your journey...")
        
        # Main game loop
        while True:
            try:
                self.clear_screen()
                self.draw_enhanced_hud()
                self.draw_location_scene()
                
                # Check game over conditions
                if self.check_game_over_conditions():
                    break
                
                print("\n🎯 WHAT'S YOUR MOVE?")
                print("=" * 30)
                print("1️⃣  🚗 Travel/Navigate")
                print("2️⃣  👀 Look for encounters")
                print("3️⃣  💤 Rest (restore energy)")
                print("4️⃣  🏪 Vehicle shop")
                print("5️⃣  📊 View detailed stats")
                print("6️⃣  💾 Save game")
                print("7️⃣  ⚙️  Settings")
                print("8️⃣  🚪 Exit game")
                
                choice = input("\n💫 Your choice (1-8): ")
                
                if choice == "1":
                    self.travel_system()
                
                elif choice == "2":
                    if random.random() < 0.7:  # 70% chance of encounter
                        self.encounter_system()
                    else:
                        print("\n👻 The area is quiet right now...")
                        self.random_event()
                        input("⏳ Press Enter to continue...")
                
                elif choice == "3":
                    rest_cost = 50
                    if self.player.cash_usd >= rest_cost:
                        self.player.cash_usd -= rest_cost
                        self.player.energy = 100
                        print(f"😴 You rest at a hotel. Full energy restored! (-${rest_cost})")
                    else:
                        self.player.energy = min(100, self.player.energy + 25)
                        print("😴 You rest in your car. Partial energy restored...")
                    
                    input("⏳ Press Enter to continue...")
                
                elif choice == "4":
                    self.vehicle_shop()
                
                elif choice == "5":
                    self.show_detailed_stats()
                
                elif choice == "6":
                    self.save_game_state()
                    input("⏳ Press Enter to continue...")
                
                elif choice == "7":
                    self.settings_menu()
                
                elif choice == "8":
                    print("💨 Thanks for playing AI Furby 1.25D!")
                    self.save_game_state()
                    break
                
                else:
                    print("❓ Invalid choice! Try again...")
                    time.sleep(1)
                
                # Increment game time
                self.game_time += 0.5
                self.player.playtime_hours += 0.5
                
                # Random energy decrease
                if random.random() < 0.3:
                    energy_loss = random.randint(1, 3)
                    self.player.energy = max(0, self.player.energy - energy_loss)
                
            except KeyboardInterrupt:
                print("\n\n💾 Auto-saving before exit...")
                self.save_game_state()
                print("👋 Game saved. See you next time!")
                break
            except Exception as e:
                logger.error(f"Game loop error: {e}")
                print(f"❌ Game error: {e}")
                input("⏳ Press Enter to continue...")
    
    def show_detailed_stats(self):
        """Show comprehensive player statistics"""
        self.clear_screen()
        print("📊 DETAILED PLAYER STATISTICS 📊")
        print("=" * 50)
        
        print(f"👤 Player: {self.player.name}")
        print(f"🎯 Level: {self.player.level}")
        print(f"⚡ Experience: {self.player.experience}")
        print(f"⏰ Playtime: {self.player.playtime_hours:.1f} hours")
        
        print(f"\n💰 FINANCES:")
        print(f"   Cash USD: ${self.player.cash_usd:,}")
        print(f"   FBX Tokens: {self.player.fbx_tokens:.2f}")
        
        print(f"\n📈 STATS:")
        print(f"   Energy: {self.player.energy}/100")
        print(f"   Heat: {self.player.heat}/100")
        print(f"   Reputation: {self.player.reputation}")
        print(f"   Style Points: {self.player.style_points}")
        
        print(f"\n🚗 VEHICLE:")
        vehicle = self.vehicles[self.player.current_vehicle]
        print(f"   Current: {vehicle.name}")
        print(f"   Speed: {vehicle.speed}/10")
        print(f"   Style: {vehicle.style_points}/10")
        
        print(f"\n🗺️  PROGRESS:")
        print(f"   Unlocked Locations: {len(self.player.unlocked_locations)}")
        print(f"   Completed Missions: {len(self.player.completed_missions)}")
        
        print(f"\n💕 RELATIONSHIPS:")
        for npc, level in self.player.npc_relationships.items():
            npc_name = self.npcs[npc].name
            print(f"   {npc_name}: {level} encounters")
        
        print(f"\n🏆 ACHIEVEMENTS:")
        for achievement in self.player.achievements:
            print(f"   ✅ {achievement}")
        
        input("\n⏳ Press Enter to continue...")
    
    def settings_menu(self):
        """Game settings menu"""
        while True:
            self.clear_screen()
            print("⚙️  GAME SETTINGS ⚙️")
            print("=" * 30)
            
            print(f"1️⃣  Animations: {'ON' if self.animations_enabled else 'OFF'}")
            print(f"2️⃣  Sound Effects: {'ON' if self.sound_effects_enabled else 'OFF'}")
            print(f"3️⃣  Difficulty: {self.difficulty.upper()}")
            print("4️⃣  Reset save data")
            print("5️⃣  Back to game")
            
            choice = input("\n⚙️  Setting to change (1-5): ")
            
            if choice == "1":
                self.animations_enabled = not self.animations_enabled
                print(f"✅ Animations {'enabled' if self.animations_enabled else 'disabled'}!")
                
            elif choice == "2":
                self.sound_effects_enabled = not self.sound_effects_enabled
                print(f"✅ Sound effects {'enabled' if self.sound_effects_enabled else 'disabled'}!")
                
            elif choice == "3":
                difficulties = ["easy", "normal", "hard", "insane"]
                current_idx = difficulties.index(self.difficulty)
                self.difficulty = difficulties[(current_idx + 1) % len(difficulties)]
                print(f"✅ Difficulty set to {self.difficulty.upper()}!")
                
            elif choice == "4":
                confirm = input("⚠️  Reset ALL save data? (yes/no): ").lower()
                if confirm == "yes":
                    try:
                        os.remove(f"game_save_{self.user_id}.json")
                        print("💥 Save data deleted!")
                    except FileNotFoundError:
                        print("💾 No save data found!")
                
            elif choice == "5":
                break
            
            else:
                print("❓ Invalid choice!")
            
            if choice != "5":
                input("⏳ Press Enter to continue...")

# Global game instance management
active_games = {}

def get_furby_game(user_id: str) -> FurbyGame125D:
    """Get or create game instance for user"""
    if user_id not in active_games:
        active_games[user_id] = FurbyGame125D(user_id)
    return active_games[user_id]

def start_game_for_user(user_id: str):
    """Start game for specific user"""
    try:
        game = get_furby_game(user_id)
        game.main_game_loop()
    except Exception as e:
        logger.error(f"Game error for user {user_id}: {e}")
        print(f"❌ Game error: {e}")

if __name__ == "__main__":
    # Test game with default user
    logging.basicConfig(level=logging.INFO)
    
    print("🎮 AI FURBY 1.25D: SAN ANDREAS EDITION 🎮")
    test_user = input("Enter test user ID (or press Enter for 'test_player'): ").strip()
    
    if not test_user:
        test_user = "test_player"
    
    start_game_for_user(test_user)