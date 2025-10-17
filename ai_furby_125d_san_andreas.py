#!/usr/bin/env python3
"""
🎮 AI FURBY 1.25D: SAN ANDREAS EROTIC EDITION 🎮
==============================================

Innowacyjna gra 1.25D łącząca tekstową rozgrywę z pseudo-grafiką:
- ASCII art vehicles & NPCs
- Progress bary i visual HUD
- Liniowa mapa z kamerą
- San Andreas atmosphere
- Heat progression system
- Multiple endings

Author: Meta-Geniusz-mózg_Boga
Version: 1.25D Enhanced Edition
Date: 2024
"""

import random
import time
import os
import sys
from datetime import datetime
from typing import Dict, List, Any

class FurbyGameEngine125D:
    """
    🚗 Enhanced 1.25D Game Engine 
    Pseudo-graphics + immersive gameplay
    """
    
    def __init__(self):
        # Player Stats
        self.player = {
            "name": "", 
            "cash": 1000, 
            "energy": 100, 
            "heat": 0,
            "level": 1,
            "xp": 0,
            "car": "Rusty_Lowrider", 
            "reputation": 0,
            "style_points": 0,
            "achievements": [],
            "inventory": ["Gold_Chain", "Fake_Rolex"]
        }
        
        # World Map (Linear progression)
        self.position = 0
        self.world = [
            {
                "name": "Ghetto", 
                "type": "danger", 
                "icon": "🏚️", 
                "encounters": ["Hustler", "Gangsta", "Street_Girl"],
                "mood": "gritty",
                "music": "🎵 Hip-hop beats echo from abandoned buildings..."
            },
            {
                "name": "Downtown", 
                "type": "city", 
                "icon": "🏙️", 
                "encounters": ["Club_Girl", "Pimp", "Business_Woman"],
                "mood": "urban",
                "music": "🎶 Neon lights flash with electronic music..."
            },
            {
                "name": "Beach", 
                "type": "relax", 
                "icon": "🏖️", 
                "encounters": ["Bikini_Girl", "Surfer", "Tourist"],
                "mood": "chill",
                "music": "🌊 Ocean waves mix with reggae vibes..."
            },
            {
                "name": "Vegas_Strip", 
                "type": "luxury", 
                "icon": "🎰", 
                "encounters": ["VIP_Girl", "Casino_Hostess", "High_Roller"],
                "mood": "glamour",
                "music": "💎 Jazz and slot machine sounds fill the air..."
            },
            {
                "name": "Hollywood_Hills", 
                "type": "elite", 
                "icon": "🏰", 
                "encounters": ["Sugar_Mama", "Pool_Party_Girl", "Celebrity"],
                "mood": "exclusive",
                "music": "🍾 Champagne corks and exclusive party music..."
            }
        ]
        
        # NPC Database
        self.npcs = {
            "Hustler": {
                "name": "Tina", 
                "style": "street smart rebel", 
                "heat_reward": 15,
                "cash_cost": 100,
                "description": "Tough girl from the block",
                "ascii": "👩‍🦱💪"
            },
            "Club_Girl": {
                "name": "Velvet", 
                "style": "seductive dancer", 
                "heat_reward": 25,
                "cash_cost": 200,
                "description": "Professional club dancer",
                "ascii": "💃✨"
            },
            "Bikini_Girl": {
                "name": "Sunny", 
                "style": "beach goddess", 
                "heat_reward": 20,
                "cash_cost": 150,
                "description": "California beach beauty",
                "ascii": "👙🌺"
            },
            "VIP_Girl": {
                "name": "Lola", 
                "style": "high-end escort", 
                "heat_reward": 35,
                "cash_cost": 500,
                "description": "Elite companion",
                "ascii": "👠💎"
            },
            "Sugar_Mama": {
                "name": "Madame X", 
                "style": "wealthy cougar", 
                "heat_reward": 50,
                "cash_cost": 0,  # She pays YOU
                "description": "Rich older woman",
                "ascii": "👑💰"
            },
            "Celebrity": {
                "name": "Starlet", 
                "style": "A-list actress", 
                "heat_reward": 75,
                "cash_cost": 1000,
                "description": "Hollywood superstar",
                "ascii": "⭐🎬"
            }
        }
        
        # Vehicle Upgrades
        self.cars = {
            "Rusty_Lowrider": {
                "name": "Rusty Lowrider", 
                "icon": "🚗💨", 
                "style_bonus": 5,
                "ascii_art": [
                    "   🚗💨 LOWRIDER 💨🚗",
                    "    ____",
                    "  _/    \\_",
                    " /  [] []  \\",
                    " |__________|",
                    "    ||  ||"
                ]
            },
            "Pimped_Ride": {
                "name": "Pimped Ride", 
                "icon": "🚘✨", 
                "style_bonus": 15,
                "cost": 2000,
                "ascii_art": [
                    "  🚘✨ PIMPED RIDE ✨🚘",
                    "     ______",
                    "   _/      \\_",
                    "  /  💎 💎  \\",
                    "  |__________|",
                    "     ||  ||"
                ]
            },
            "Luxury_Convertible": {
                "name": "Luxury Drop-Top", 
                "icon": "🏎️💎", 
                "style_bonus": 30,
                "cost": 5000,
                "ascii_art": [
                    " 🏎️💎 LUXURY RIDE 💎🏎️",
                    "      ________",
                    "    _/        \\_",
                    "   /  🔥 ⭐ 🔥  \\",
                    "   |____________|",
                    "      ||    ||"
                ]
            }
        }
        
        # Game state
        self.achievements_unlocked = []
        self.high_scores = {"max_heat": 0, "max_cash": 0, "max_rep": 0}
        self.game_time = 0
        self.encounters_total = 0
        
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw_title_screen(self):
        """Epic ASCII title screen"""
        title_art = [
            "╔══════════════════════════════════════════════════╗",
            "║  🎮 AI FURBY 1.25D: SAN ANDREAS EROTIC 🎮      ║",
            "║                                                  ║",
            "║     ░█▀▀▀█ ░█▀▀█ ░█▄─░█   ░█▀▀█ ░█▄─░█ ░█▀▀▄   ║",
            "║     ─▀▀▀▄▄ ░█▄▄█ ░█░█░█   ░█▄▄█ ░█░█░█ ░█─░█   ║",
            "║     ░█▄▄▄█ ░█─░█ ░█──▀█   ░█─░█ ░█──▀█ ░█▄▄▀   ║",
            "║                                                  ║",
            "║          🚗💨 CRUISE • FLIRT • CONQUER 💨🚗      ║",
            "║                                                  ║",
            "╚══════════════════════════════════════════════════╝"
        ]
        
        for line in title_art:
            print(line)
        
        print("\n🌆 Welcome to San Andreas, gdzie każda noc może być legendary...")
        print("💋 Twoją misją jest zostać królem nocy, zdobywając hearts i heat!")
        print("🎯 Cruisuj po mieście, poznawaj gorące laski, buduj reputację!")
    
    def draw_hud(self):
        """Enhanced HUD with visual progress bars"""
        current_loc = self.world[self.position]
        
        # Progress bars
        energy_bar = "█" * (self.player['energy'] // 10) + "░" * (10 - (self.player['energy'] // 10))
        heat_bar = "🔥" * (self.player['heat'] // 10) + "░" * (10 - (self.player['heat'] // 10))
        
        # Level progress
        xp_needed = self.player['level'] * 100
        xp_progress = "⭐" * (self.player['xp'] // 20) + "☆" * (5 - (self.player['xp'] // 20))
        
        print(f"\n{'='*60}")
        print(f"💋 FURBY 1.25D: SAN ANDREAS NIGHTS 💋")
        print(f"{'='*60}")
        print(f"👤 {self.player['name']} (Level {self.player['level']})  | 💰 ${self.player['cash']:,}")
        print(f"⚡ Energy: [{energy_bar}] {self.player['energy']}/100")
        print(f"🔥 Heat:   [{heat_bar}] {self.player['heat']}/100")
        print(f"⭐ XP:     [{xp_progress}] {self.player['xp']}/{xp_needed}")
        print(f"🚗 Ride: {self.cars[self.player['car']]['name']} | 🌟 Rep: {self.player['reputation']}")
        print(f"📍 Location: {current_loc['icon']} {current_loc['name']}")
        
        # Map visualization
        map_view = ""
        for i, location in enumerate(self.world):
            if i == self.position:
                map_view += f"[{location['icon']}]"
            else:
                map_view += f" {location['icon']} "
            if i < len(self.world) - 1:
                map_view += "━"
        
        print(f"🗺️  Map: {map_view}")
        print(f"🎵 Atmosphere: {current_loc['music']}")
        print(f"{'='*60}")
    
    def draw_car_ascii(self):
        """Display current car ASCII art"""
        car_data = self.cars[self.player['car']]
        print("\n🚗 YOUR RIDE:")
        for line in car_data['ascii_art']:
            print(f"   {line}")
        print(f"   Style Bonus: +{car_data['style_bonus']}")
    
    def show_encounter_screen(self, npc_type):
        """Enhanced encounter screen with ASCII NPC"""
        npc = self.npcs[npc_type]
        location = self.world[self.position]
        
        print(f"\n🎯 ENCOUNTER IN {location['name'].upper()}")
        print("━" * 50)
        print(f"{npc['ascii']} {npc['name']} - {npc['style']}")
        print(f"💬 \"{npc['description']}\"")
        print("━" * 50)
        
        # Encounter options with style
        options = [
            "1️⃣  😘 Sweet Talk    (Charm & Flirt)",
            "2️⃣  💰 Flash Cash    (Show your wealth)",  
            "3️⃣  🔥 Get Physical  (Intimate approach)",
            "4️⃣  🎁 Give Gift     (Use inventory item)",
            "5️⃣  🎲 Risky Move    (High risk/reward)",
            "6️⃣  🚗 Drive Away    (Leave immediately)"
        ]
        
        for option in options:
            print(option)
        
        # Show cost/reward preview
        if npc['cash_cost'] > 0:
            print(f"\n💸 Estimated cost: ${npc['cash_cost']}")
        else:
            print(f"\n💰 She might pay YOU!")
        print(f"🔥 Heat reward: +{npc['heat_reward']}")
    
    def travel_system(self):
        """Enhanced travel with random events"""
        print("\n🛣️  CITY NAVIGATION 🛣️")
        print("━" * 40)
        
        # Show available directions
        directions = []
        if self.position > 0:
            directions.append("⬅️  [L] LEFT - " + self.world[self.position - 1]['name'])
        if self.position < len(self.world) - 1:
            directions.append("➡️  [R] RIGHT - " + self.world[self.position + 1]['name'])
        directions.append("⬆️  [S] STAY - Look around current area")
        
        for direction in directions:
            print(direction)
        
        choice = input("\n🚗 Direction (L/R/S): ").upper().strip()
        
        # Movement logic
        if choice == "L" and self.position > 0:
            self.position -= 1
            print(f"⬅️  Cruising to {self.world[self.position]['name']}...")
            self.driving_event()
        elif choice == "R" and self.position < len(self.world) - 1:
            self.position += 1
            print(f"➡️  Cruising to {self.world[self.position]['name']}...")
            self.driving_event()
        elif choice == "S":
            print("🔄  You park and observe the scene...")
            self.location_event()
        else:
            print("❌  Invalid choice! You rev the engine but stay put.")
            return
        
        # Energy consumption
        energy_cost = random.randint(5, 15)
        self.player["energy"] -= energy_cost
        self.game_time += 1
        
        time.sleep(1.5)
    
    def driving_event(self):
        """Random events while driving"""
        events = [
            {
                "text": "👮 Police patrol spotted ahead! You slow down and act cool.",
                "effect": {"reputation": -2}
            },
            {
                "text": "💨 Your ride turns heads - everyone's checking out your style!",
                "effect": {"style_points": 5, "reputation": 3}
            },
            {
                "text": "🎵 Perfect song comes on the radio - you're feeling confident!",
                "effect": {"energy": 10}
            },
            {
                "text": "💰 You spot cash blowing in the wind and grab it!",
                "effect": {"cash": random.randint(50, 200)}
            },
            {
                "text": "🔥 Hot girl at red light gives you her number!",
                "effect": {"heat": 5, "reputation": 2}
            }
        ]
        
        # 70% chance of random event
        if random.random() < 0.7:
            event = random.choice(events)
            print(f"🎲 ROAD EVENT: {event['text']}")
            
            # Apply effects
            for stat, value in event['effect'].items():
                if stat in self.player:
                    self.player[stat] += value
                    if value > 0:
                        print(f"   ↗️  +{value} {stat}")
                    else:
                        print(f"   ↘️  {value} {stat}")
    
    def location_event(self):
        """Events when staying in current location"""
        location = self.world[self.position]
        
        events = {
            "danger": [
                "👀 You notice some shady characters eyeing your ride...",
                "🎲 Local hustlers approach with a 'business opportunity'...",
                "💊 Someone offers to sell you something 'special'..."
            ],
            "city": [
                "🏙️ Bright neon lights reflect off your car's chrome...",
                "🎭 Club promoters hand you VIP passes...",
                "📱 Your phone buzzes with party invitations..."
            ],
            "relax": [
                "🌊 Ocean breeze refreshes your mind and spirit...",
                "🏄 Surfers wave as they recognize your legendary status...",
                "🍹 Beach bar owner offers you a complimentary drink..."
            ],
            "luxury": [
                "💎 High-rollers nod with respect as you pass...",
                "🎰 Casino host offers you exclusive gaming opportunities...",
                "🥂 VIP lounge sends over champagne and their finest girls..."
            ],
            "elite": [
                "🏰 Security guards actually recognize you and step aside...",
                "🍾 Hollywood elite invite you to exclusive after-party...",
                "⭐ Paparazzi want photos with the legendary night king..."
            ]
        }
        
        event_text = random.choice(events[location['type']])
        print(f"🎭 {event_text}")
        
        # Small energy recovery for observing
        self.player['energy'] += random.randint(2, 8)
        if self.player['energy'] > 100:
            self.player['energy'] = 100
    
    def encounter_system(self):
        """Enhanced encounter with multiple resolution paths"""
        current_loc = self.world[self.position]
        available_npcs = current_loc["encounters"]
        
        # Filter NPCs based on player level/reputation
        accessible_npcs = []
        for npc_type in available_npcs:
            npc = self.npcs[npc_type]
            if npc['cash_cost'] <= self.player['cash'] * 2:  # Can at least attempt
                accessible_npcs.append(npc_type)
        
        if not accessible_npcs:
            print("💸 No suitable encounters at your current status level...")
            return
        
        npc_type = random.choice(accessible_npcs)
        
        self.clear_screen()
        self.draw_hud()
        self.draw_car_ascii()
        self.show_encounter_screen(npc_type)
        
        choice = input("\n💬 Your move (1-6): ").strip()
        npc = self.npcs[npc_type]
        
        # Track encounter
        self.encounters_total += 1
        
        # Process choice
        success_rate = 0.5  # Base success rate
        
        if choice == "1":  # Sweet Talk
            success_rate = self.flirt_encounter(npc)
        elif choice == "2":  # Flash Cash
            success_rate = self.money_encounter(npc)
        elif choice == "3":  # Get Physical
            success_rate = self.physical_encounter(npc)
        elif choice == "4":  # Give Gift
            success_rate = self.gift_encounter(npc)
        elif choice == "5":  # Risky Move
            success_rate = self.risky_encounter(npc)
        elif choice == "6":  # Drive Away
            print("💨 You hit the gas and speed away with style!")
            self.player['energy'] -= 5
            return
        else:
            print("❓ Invalid choice! She walks away confused...")
            return
        
        # Determine outcome
        success = random.random() < success_rate
        self.resolve_encounter(npc, success, choice)
        
        # Level up check
        self.check_level_up()
    
    def flirt_encounter(self, npc) -> float:
        """Flirting approach - charm based"""
        dialogues = [
            f"😘 'Hey {npc['name']}, that smile could light up the whole strip...'",
            f"💋 'I've been cruising all night, but you're the view I was looking for...'",
            f"🔥 'Want to see how this lowrider handles on the open road?'"
        ]
        
        player_line = random.choice(dialogues)
        print(f"\n💭 You: {player_line}")
        
        # Success based on reputation and style
        base_rate = 0.4
        rep_bonus = min(self.player['reputation'] / 100, 0.3)
        style_bonus = self.cars[self.player['car']]['style_bonus'] / 100
        
        return base_rate + rep_bonus + style_bonus
    
    def money_encounter(self, npc) -> float:
        """Money approach - wealth based"""
        cost = npc['cash_cost']
        
        if self.player['cash'] < cost:
            print(f"💸 You try to impress with ${self.player['cash']}, but she wants ${cost}...")
            return 0.2  # Low success if insufficient funds
        
        print(f"💵 You flash ${cost} cash: 'Let's make this night unforgettable...'")
        self.player['cash'] -= cost
        
        return 0.8  # High success with money
    
    def physical_encounter(self, npc) -> float:
        """Physical approach - energy and heat based"""
        if self.player['energy'] < 30:
            print("😴 You're too tired to be smooth... She notices your exhaustion.")
            return 0.2
        
        intensity_options = ["gentle", "passionate", "wild"]
        intensity = random.choice(intensity_options)
        
        print(f"🔥 You make a {intensity} move...")
        
        self.player['energy'] -= 20
        
        # Success based on current heat level
        heat_factor = self.player['heat'] / 100
        return 0.3 + (heat_factor * 0.4)
    
    def gift_encounter(self, npc) -> float:
        """Gift approach - inventory based"""
        if not self.player['inventory']:
            print("🎁 You reach for a gift... but your pockets are empty!")
            return 0.1
        
        gift = random.choice(self.player['inventory'])
        print(f"🎁 You offer her your {gift}...")
        self.player['inventory'].remove(gift)
        
        # Different gifts have different success rates
        gift_values = {
            "Gold_Chain": 0.6,
            "Fake_Rolex": 0.4,
            "Diamond_Ring": 0.9,
            "Perfume": 0.5
        }
        
        return gift_values.get(gift, 0.3)
    
    def risky_encounter(self, npc) -> float:
        """Risky move - high risk/reward"""
        risky_moves = [
            "You challenge her to a spontaneous race through the city...",
            "You invite her to an exclusive underground party...",
            "You offer to show her your 'secret spot' in the hills..."
        ]
        
        move = random.choice(risky_moves)
        print(f"🎲 RISKY MOVE: {move}")
        
        # 50/50 but with extreme outcomes
        return 0.5
    
    def resolve_encounter(self, npc, success: bool, choice: str):
        """Resolve encounter outcome"""
        if success:
            # Success outcomes
            heat_gain = npc['heat_reward']
            rep_gain = random.randint(3, 8)
            xp_gain = random.randint(10, 25)
            
            # Bonus for risky moves
            if choice == "5":  # Risky move
                heat_gain *= 1.5
                rep_gain *= 2
                cash_bonus = random.randint(200, 800)
                self.player['cash'] += cash_bonus
                print(f"🎰 JACKPOT! Your risky move pays off massively!")
                print(f"💰 +${cash_bonus} cash bonus!")
            
            # Apply rewards
            self.player['heat'] += int(heat_gain)
            self.player['reputation'] += rep_gain
            self.player['xp'] += xp_gain
            
            # Success messages
            success_messages = [
                f"💋 {npc['name']}: 'You're something special... I like that...'",
                f"🔥 {npc['name']}: 'That was... intense. You've got skills.'",
                f"❤️ {npc['name']}: 'I haven't felt this way in a long time...'"
            ]
            
            print(f"\n✅ SUCCESS!")
            print(random.choice(success_messages))
            print(f"🔥 +{int(heat_gain)} Heat")
            print(f"🌟 +{rep_gain} Reputation") 
            print(f"⭐ +{xp_gain} XP")
            
        else:
            # Failure outcomes
            print(f"\n❌ REJECTED!")
            
            failure_messages = [
                f"😒 {npc['name']}: 'Not interested, try someone else...'",
                f"💔 {npc['name']}: 'You're not my type, sorry...'",
                f"🙄 {npc['name']}: 'Maybe work on your game first...'"
            ]
            
            print(random.choice(failure_messages))
            
            # Small penalties
            rep_loss = random.randint(1, 3)
            self.player['reputation'] -= rep_loss
            print(f"📉 -{rep_loss} Reputation")
            
            # Risky move failures are worse
            if choice == "5":
                cash_loss = random.randint(100, 400)
                self.player['cash'] -= cash_loss
                print(f"💸 -{cash_loss} Cash (risky move backfired)")
        
        time.sleep(3)
    
    def check_level_up(self):
        """Check and handle level progression"""
        xp_needed = self.player['level'] * 100
        
        if self.player['xp'] >= xp_needed:
            self.player['level'] += 1
            self.player['xp'] -= xp_needed
            
            print(f"\n🌟 LEVEL UP! You're now Level {self.player['level']}!")
            
            # Level up rewards
            rewards = [
                "🎁 New inventory item: Diamond Ring",
                "💰 Cash bonus: $500",
                "⚡ Energy boost: +20",
                "🔥 Heat multiplier increased!"
            ]
            
            reward = random.choice(rewards)
            print(f"🎁 Level up reward: {reward}")
            
            if "Diamond Ring" in reward:
                self.player['inventory'].append("Diamond_Ring")
            elif "Cash bonus" in reward:
                self.player['cash'] += 500
            elif "Energy boost" in reward:
                self.player['energy'] += 20
                if self.player['energy'] > 100:
                    self.player['energy'] = 100
    
    def rest_system(self):
        """Enhanced rest with location-based benefits"""
        location = self.world[self.position]
        
        print(f"\n😴 RESTING IN {location['name']}...")
        
        # Location-based rest benefits
        rest_benefits = {
            "Ghetto": {"energy": 60, "description": "Sleep in your car - not comfortable but safe"},
            "Downtown": {"energy": 80, "description": "Hotel room - decent rest with city views"},
            "Beach": {"energy": 90, "description": "Beach house - ocean breeze rejuvenates you"},
            "Vegas_Strip": {"energy": 85, "description": "Casino suite - luxury but noisy"},
            "Hollywood_Hills": {"energy": 100, "description": "Mansion bedroom - ultimate comfort"}
        }
        
        rest_data = rest_benefits[location['name']]
        
        print(f"🏠 {rest_data['description']}")
        
        # Restore energy
        self.player['energy'] = rest_data['energy']
        
        # Small benefits
        if location['type'] == 'luxury' or location['type'] == 'elite':
            self.player['cash'] += random.randint(50, 200)  # Tips/winnings
            print("💰 You wake up with some extra cash in your pocket...")
        
        print(f"⚡ Energy restored to {self.player['energy']}/100")
        time.sleep(2)
    
    def car_shop(self):
        """Vehicle upgrade system"""
        print("\n🚗 VEHICLE UPGRADES 🚗")
        print("━" * 40)
        
        available_cars = []
        for car_id, car_data in self.cars.items():
            if car_id != self.player['car'] and 'cost' in car_data:
                if self.player['cash'] >= car_data['cost']:
                    available_cars.append((car_id, car_data))
        
        if not available_cars:
            print("💸 No vehicle upgrades available at your budget...")
            print("💰 Keep earning cash to unlock better rides!")
            return
        
        print("Available upgrades:")
        for i, (car_id, car_data) in enumerate(available_cars):
            print(f"{i+1}. {car_data['name']} - ${car_data['cost']:,}")
            print(f"   Style Bonus: +{car_data['style_bonus']}")
            print()
        
        choice = input("Choose upgrade (number) or 'exit': ").strip()
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(available_cars):
                car_id, car_data = available_cars[choice_idx]
                
                # Purchase car
                self.player['cash'] -= car_data['cost']
                self.player['car'] = car_id
                
                print(f"🎉 Purchased {car_data['name']}!")
                print("Your new ride commands respect on the streets!")
                
        except (ValueError, IndexError):
            if choice.lower() != 'exit':
                print("❌ Invalid selection")
    
    def check_game_over(self) -> bool:
        """Check various game ending conditions"""
        # Energy depletion
        if self.player["energy"] <= 0:
            print("\n😴 EXHAUSTED! You need to rest...")
            self.player["energy"] = 20  # Emergency energy
            return False
        
        # Heat victory
        if self.player["heat"] >= 100:
            self.heat_victory()
            return True
        
        # Cash bankruptcy (with some tolerance)
        if self.player["cash"] <= -1000:
            print("\n💸 BANKRUPTCY! Game Over - You're broke!")
            return True
        
        # Level 10 achievement victory
        if self.player["level"] >= 10:
            self.legend_victory()
            return True
        
        return False
    
    def heat_victory(self):
        """Heat meter maxed out victory"""
        print("\n🔥🔥🔥 ULTRA HOT VICTORY! 🔥🔥🔥")
        print("You've reached maximum heat level!")
        print("The streets know your name - you're the undisputed KING OF THE NIGHT!")
        
        final_score = (self.player['heat'] * 10 + 
                      self.player['reputation'] * 5 + 
                      self.player['cash'] // 100)
        
        print(f"🏆 Final Score: {final_score:,} points")
        
        # Update high scores
        self.high_scores['max_heat'] = max(self.high_scores['max_heat'], self.player['heat'])
        self.high_scores['max_cash'] = max(self.high_scores['max_cash'], self.player['cash'])
        self.high_scores['max_rep'] = max(self.high_scores['max_rep'], self.player['reputation'])
    
    def legend_victory(self):
        """Level 10 legend victory"""
        print("\n⭐⭐⭐ LEGEND STATUS ACHIEVED! ⭐⭐⭐")
        print("You've reached Level 10 - LEGENDARY NIGHT KING!")
        print("Your name will be whispered in the streets forever!")
        
        final_score = (self.player['level'] * 100 +
                      self.player['reputation'] * 10 +
                      self.player['cash'] // 50)
        
        print(f"🏆 Legendary Score: {final_score:,} points")
    
    def main_menu(self):
        """Enhanced main menu"""
        while True:
            self.clear_screen()
            self.draw_hud()
            
            if self.check_game_over():
                break
            
            # Current location info
            location = self.world[self.position]
            print(f"\n🌆 Current vibe: {location['mood'].upper()}")
            print(f"🎵 {location['music']}")
            
            print("\n🎯 WHAT'S YOUR MOVE?")
            print("━" * 30)
            print("1️⃣  🚗 Cruise City     (Travel between locations)")
            print("2️⃣  👀 Hunt Encounters (Look for action)")
            print("3️⃣  💤 Rest & Recover  (Restore energy)")
            print("4️⃣  🛠️  Vehicle Shop    (Upgrade your ride)")
            print("5️⃣  📊 View Stats      (Check progress)")
            print("6️⃣  🏆 Achievements    (View unlocked)")
            print("7️⃣  💾 Save & Quit     (End session)")
            
            choice = input("\n🎮 Your choice (1-7): ").strip()
            
            if choice == "1":
                self.travel_system()
            elif choice == "2":
                self.encounter_system()
            elif choice == "3":
                self.rest_system()
            elif choice == "4":
                self.car_shop()
            elif choice == "5":
                self.show_detailed_stats()
            elif choice == "6":
                self.show_achievements()
            elif choice == "7":
                self.save_and_quit()
                break
            else:
                print("❓ Invalid choice! Try again...")
                time.sleep(1)
    
    def show_detailed_stats(self):
        """Detailed statistics screen"""
        print("\n📊 DETAILED STATISTICS")
        print("=" * 50)
        print(f"🏆 Player: {self.player['name']}")
        print(f"⭐ Level: {self.player['level']} (XP: {self.player['xp']})")
        print(f"💰 Cash: ${self.player['cash']:,}")
        print(f"🔥 Heat: {self.player['heat']}/100")
        print(f"⚡ Energy: {self.player['energy']}/100")
        print(f"🌟 Reputation: {self.player['reputation']}")
        print(f"🚗 Vehicle: {self.cars[self.player['car']]['name']}")
        print(f"🎒 Inventory: {', '.join(self.player['inventory']) if self.player['inventory'] else 'Empty'}")
        print(f"⏰ Game Time: {self.game_time} hours")
        print(f"💋 Total Encounters: {self.encounters_total}")
        print("\n🏆 HIGH SCORES:")
        print(f"   Max Heat: {self.high_scores['max_heat']}")
        print(f"   Max Cash: ${self.high_scores['max_cash']:,}")
        print(f"   Max Rep: {self.high_scores['max_rep']}")
        
        input("\nPress Enter to continue...")
    
    def show_achievements(self):
        """Achievement system"""
        achievements = [
            {"name": "First Contact", "desc": "Complete your first encounter", "unlocked": self.encounters_total >= 1},
            {"name": "Player", "desc": "Reach 50 Heat points", "unlocked": self.player['heat'] >= 50},
            {"name": "High Roller", "desc": "Accumulate $5,000", "unlocked": self.player['cash'] >= 5000},
            {"name": "Legend", "desc": "Reach Level 5", "unlocked": self.player['level'] >= 5},
            {"name": "King of Streets", "desc": "100+ Reputation", "unlocked": self.player['reputation'] >= 100},
            {"name": "Vehicle Collector", "desc": "Own a luxury car", "unlocked": self.player['car'] == 'Luxury_Convertible'},
            {"name": "Marathon Man", "desc": "20+ encounters", "unlocked": self.encounters_total >= 20},
            {"name": "Elite Access", "desc": "Reach Hollywood Hills", "unlocked": self.position >= 4}
        ]
        
        print("\n🏆 ACHIEVEMENTS")
        print("=" * 40)
        
        unlocked_count = 0
        for achievement in achievements:
            status = "✅" if achievement['unlocked'] else "🔒"
            print(f"{status} {achievement['name']}")
            print(f"   {achievement['desc']}")
            print()
            if achievement['unlocked']:
                unlocked_count += 1
        
        print(f"Progress: {unlocked_count}/{len(achievements)} achievements unlocked")
        input("\nPress Enter to continue...")
    
    def save_and_quit(self):
        """Save game and exit"""
        print("\n💾 SAVING GAME...")
        
        # In a full implementation, this would save to file
        print("🎮 Game session summary:")
        print(f"   Level reached: {self.player['level']}")
        print(f"   Heat gained: {self.player['heat']}")
        print(f"   Cash earned: ${self.player['cash']:,}")
        print(f"   Reputation: {self.player['reputation']}")
        print(f"   Encounters: {self.encounters_total}")
        
        print("\n👋 Thanks for playing AI Furby 1.25D!")
        print("💋 Your legend lives on in San Andreas...")
    
    def start_game(self):
        """Main game initialization"""
        self.clear_screen()
        self.draw_title_screen()
        
        print("\n🎮 GAME SETUP")
        print("━" * 20)
        
        # Player name
        self.player["name"] = input("💎 Enter your Furby player name: ").strip() or "Night_King"
        
        # Difficulty selection
        print("\n🎯 Select your starting difficulty:")
        print("1. Easy Mode    (More cash, higher success rates)")
        print("2. Normal Mode  (Balanced gameplay)")
        print("3. Hard Mode    (Less cash, lower success rates)")
        
        difficulty = input("Choose (1-3): ").strip()
        
        if difficulty == "1":
            self.player["cash"] = 2000
            print("💰 Easy mode: Starting with extra cash!")
        elif difficulty == "3":
            self.player["cash"] = 500
            print("💸 Hard mode: Tougher financial start!")
        else:
            print("⚖️ Normal mode selected!")
        
        print(f"\n🌟 Welcome {self.player['name']} to San Andreas!")
        print("🚗 Your journey to become the Night King begins...")
        print("💋 Remember: Charm, cash, and style rule these streets!")
        
        input("\nPress Enter to start your adventure...")
        
        # Start main game loop
        self.main_menu()

def main():
    """Game entry point"""
    try:
        print("🎮 Initializing AI Furby 1.25D: San Andreas Edition...")
        time.sleep(1)
        
        game = FurbyGameEngine125D()
        game.start_game()
        
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted by user. See you later!")
    except Exception as e:
        print(f"\n💥 Game error: {e}")
        print("Please restart the game.")

if __name__ == "__main__":
    main()