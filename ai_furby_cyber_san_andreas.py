"""
🎮 AI FURBY 1.25D: CYBER SAN ANDREAS EDITION
============================================

Innowacyjna gra erotyczna dla dorosłych łącząca:
- San Andreas open-world atmosphere
- Cyber banking & trading system  
- 1.25D pseudo-graphics (ASCII + HUD)
- Heat progression system
- Global market simulation

Author: Meta-Geniusz-mózg_Boga
Version: 1.0 Cyber Edition
"""

import random
import time
import os

class FurbyCyberSanAndreas:
    def __init__(self):
        self.player = {
            "name": "", 
            "cash": 1000, 
            "energy": 100, 
            "heat": 0, 
            "car": "Cyber Lowrider", 
            "reputation": 0,
            "bank_balance": 500, 
            "investments": 0, 
            "items": [],
            "insurance": False,
            "cyber_crimes": 0,
            "vip_status": False
        }
        self.position = 0  # Pozycja na mapie liniowej
        self.turn_counter = 0
        
        # Mapa świata San Andreas style
        self.world = [
            {"name": "Cyber Ghetto", "type": "danger", "icon": "🏚️💻", "encounters": ["Cyber_Hustler", "Digital_Gangsta"], "risk": 0.3},
            {"name": "Neon Downtown", "type": "city", "icon": "🏙️✨", "encounters": ["VR_Club_Girl", "Holo_Pimp"], "risk": 0.1},
            {"name": "Virtual Beach", "type": "relax", "icon": "🏖️🌐", "encounters": ["AI_Bikini_Babe", "Quantum_Surfer"], "risk": 0.05},
            {"name": "Crypto Vegas", "type": "luxury", "icon": "🎰💎", "encounters": ["Blockchain_VIP", "Smart_Contract_Hostess"], "risk": 0.2},
            {"name": "Meta Mansion", "type": "elite", "icon": "🏰🔮", "encounters": ["NFT_Sugar_Mama", "Cyber_Pool_Party"], "risk": 0.0}
        ]
        
        # Rozszerzeni NPC z cyber tematyką
        self.npcs = {
            "Cyber_Hustler": {"name": "CyberTina", "style": "underground hacker", "heat_reward": 25, "price_modifier": 0.8},
            "Digital_Gangsta": {"name": "Big_Data", "style": "data lord", "heat_reward": 20, "price_modifier": 1.2},
            "VR_Club_Girl": {"name": "HoloVelvet", "style": "virtual dancer", "heat_reward": 35, "price_modifier": 1.0},
            "Holo_Pimp": {"name": "QuantumSlick", "style": "digital dealer", "heat_reward": 15, "price_modifier": 1.5},
            "AI_Bikini_Babe": {"name": "SunnAI", "style": "synthetic beach queen", "heat_reward": 30, "price_modifier": 0.9},
            "Quantum_Surfer": {"name": "WaveRider_X", "style": "dimensional traveler", "heat_reward": 25, "price_modifier": 1.1},
            "Blockchain_VIP": {"name": "CryptoLola", "style": "decentralized goddess", "heat_reward": 45, "price_modifier": 2.0},
            "Smart_Contract_Hostess": {"name": "EthGlitz", "style": "automated seduction", "heat_reward": 40, "price_modifier": 1.8},
            "NFT_Sugar_Mama": {"name": "MetaMadame", "style": "virtual reality mogul", "heat_reward": 60, "price_modifier": 3.0},
            "Cyber_Pool_Party": {"name": "VirtualOrgy_Host", "style": "collective consciousness", "heat_reward": 55, "price_modifier": 2.5}
        }
        
        # Przedmioty do handlu cybernetycznego
        self.market_items = [
            {"name": "Quantum Vibrator", "base_price": 400, "value": 25, "category": "gadget", "rarity": "common"},
            {"name": "Neural Link Stimulator", "base_price": 800, "value": 40, "category": "tech", "rarity": "rare"},
            {"name": "Holographic Lingerie", "base_price": 600, "value": 35, "category": "fashion", "rarity": "uncommon"},
            {"name": "AI Companion Premium", "base_price": 1200, "value": 60, "category": "ai", "rarity": "epic"},
            {"name": "Virtual Reality Fantasy Suite", "base_price": 2000, "value": 80, "category": "experience", "rarity": "legendary"},
            {"name": "Cyber Furby Skin Ultra", "base_price": 1500, "value": 70, "category": "avatar", "rarity": "epic"},
            {"name": "Blockchain Dildo", "base_price": 500, "value": 30, "category": "gadget", "rarity": "uncommon"},
            {"name": "Smart Contract Condom", "base_price": 50, "value": 5, "category": "protection", "rarity": "common"},
            {"name": "Metaverse Orgy Token", "base_price": 3000, "value": 100, "category": "experience", "rarity": "mythic"},
            {"name": "Quantum Entangled Toy", "base_price": 900, "value": 45, "category": "gadget", "rarity": "rare"}
        ]
        
        # Cyber zagrożenia i eventy
        self.cyber_events = [
            {"name": "DDoS Attack", "effect": "bank_loss", "severity": 0.15, "message": "💥 DDoS atakuje Twój bank! Strata 15% salda!"},
            {"name": "Phishing Scam", "effect": "cash_loss", "severity": 0.10, "message": "🎣 Padłeś na phishing! Strata 10% gotówki!"},
            {"name": "Ransomware", "effect": "item_lock", "severity": 1.0, "message": "🔒 Ransomware blokuje Twoje itemy! Zapłać 500$ lub strać losowy item!"},
            {"name": "Crypto Boom", "effect": "investment_gain", "severity": 0.25, "message": "📈 Boom krypto! Inwestycje rosną o 25%!"},
            {"name": "Market Crash", "effect": "investment_loss", "severity": 0.20, "message": "📉 Krach rynku! Inwestycje spadają o 20%!"},
            {"name": "Hacker Bounty", "effect": "cash_gain", "severity": 500, "message": "💰 Złapałeś hackera! Nagroda +500$!"},
            {"name": "NFT Airdrop", "effect": "free_item", "severity": 1.0, "message": "🎁 Darmowy NFT airdrop! Otrzymujesz losowy item!"},
            {"name": "Smart Contract Bug", "effect": "energy_drain", "severity": 30, "message": "🐛 Bug w smart contract! Tracisz 30 energii!"}
        ]
        
        # Mission system
        self.missions = [
            {"name": "Cyber Heist", "description": "Hakuj bank przeciwnika", "reward": 1000, "risk": 0.4, "type": "criminal"},
            {"name": "VIP Escort", "description": "Obsłuż VIP klienta", "reward": 800, "risk": 0.1, "type": "service"},
            {"name": "Market Manipulation", "description": "Manipuluj ceną itemu", "reward": 600, "risk": 0.3, "type": "trading"},
            {"name": "Data Mining", "description": "Wykradnij dane osobowe", "reward": 400, "risk": 0.2, "type": "hacking"},
            {"name": "Underground Tournament", "description": "Weź udział w cyber-turnieju", "reward": 1500, "risk": 0.5, "type": "competition"}
        ]
        
        self.update_market_prices()
        
    def update_market_prices(self):
        """Aktualizuj ceny rynkowe z globalną fluktuacją"""
        for item in self.market_items:
            # Większa volatility dla wyższych rarity
            volatility = {
                "common": 0.1, "uncommon": 0.15, "rare": 0.25, 
                "epic": 0.35, "legendary": 0.45, "mythic": 0.60
            }
            
            base_volatility = volatility.get(item["rarity"], 0.2)
            fluctuation = random.uniform(-base_volatility, base_volatility)
            
            item["price"] = max(50, int(item["base_price"] * (1 + fluctuation)))
            
            # Market events
            if random.random() < 0.05:  # 5% szansy na market event
                if random.random() < 0.5:
                    item["price"] = int(item["price"] * 1.5)  # Boom
                else:
                    item["price"] = int(item["price"] * 0.7)  # Crash
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw_hud(self):
        current_loc = self.world[self.position]
        insurance_status = "🛡️ ON" if self.player["insurance"] else "❌ OFF"
        vip_status = "👑 VIP" if self.player["vip_status"] else "🔰 REG"
        
        print(f"\n{'='*70}")
        print(f"💋 AI FURBY 1.25D: CYBER SAN ANDREAS EMPIRE 💋")
        print(f"👤 {self.player['name']} | 💰 ${self.player['cash']} | 🔥 Heat: {self.player['heat']}/100 | {vip_status}")
        print(f"🏦 Bank: ${self.player['bank_balance']} | 📈 Investments: ${self.player['investments']} | {insurance_status}")
        
        # Progress bars
        energy_bar = '█' * (self.player['energy']//10) + '░' * (10 - self.player['energy']//10)
        heat_bar = '🔥' * (self.player['heat']//20) + '❄️' * (5 - self.player['heat']//20)
        
        print(f"⚡ Energy: [{energy_bar}] {self.player['energy']}/100 | 🚗 {self.player['car']}")
        print(f"🔥 Heat: [{heat_bar}] | ⭐ Rep: {self.player['reputation']} | 📦 Items: {len(self.player['items'])}")
        print(f"📍 {current_loc['icon']} {current_loc['name']} | Turn: {self.turn_counter} | Crimes: {self.player['cyber_crimes']}")
        
        # Mini-map
        map_display = ""
        for i, location in enumerate(self.world):
            if i == self.position:
                map_display += f"[{location['icon']}]"
            else:
                map_display += f" {location['icon']} "
        print(f"🗺️  Map: {map_display}")
        print(f"{'='*70}")
    
    def draw_ascii_cyber_car(self):
        car_art = [
            "🚗💨 CYBER LOWRIDER CRUISING THE NET 💨🚗",
            "    ╔══════════╗",
            "  ╔═╣ ◉    ◉  ╠═╗",
            " ╔╝ ╚══╤══╤══╝ ╚╗",
            " ║▓▓▓▓██████▓▓▓▓║",
            " ╚═══╧══════╧═══╝",
            "   💎 NEON WHEELS 💎"
        ]
        for line in car_art:
            print(line.center(70))
    
    def draw_ascii_cyber_bank(self):
        bank_art = [
            "🏦 CYBERNETIC GLOBAL TRADE BANK 🏦",
            "    ╔═══════════════════╗",
            "    ║  💰 BLOCKCHAIN  💰 ║",
            "    ║    CYBER TRADE     ║",
            "    ║   ₿  $  Ξ  NFT     ║",
            "    ╚═══════════════════╝",
            "        🌐 GLOBAL 🌐"
        ]
        for line in bank_art:
            print(line.center(70))
    
    def draw_ascii_mission_hq(self):
        hq_art = [
            "🏢 UNDERGROUND MISSION HQ 🏢",
            "    ░▒▓█ DARKNET █▓▒░",
            "       ┌─── ⚡ ───┐",
            "       │ HIRE HERE │",
            "       │  RISKY    │",
            "       │  REWARDS  │",
            "       └───────────┘"
        ]
        for line in hq_art:
            print(line.center(70))
    
    def show_encounter(self, npc_type):
        npc = self.npcs.get(npc_type, {"name": "Unknown", "style": "mysterious", "heat_reward": 10})
        current_loc = self.world[self.position]
        
        print(f"\n🎯 CYBER ENCOUNTER: {npc['name']} 💃")
        print(f"Style: {npc['style']} | Location: {current_loc['name']} | Risk Level: {current_loc['risk']*100:.0f}%")
        print("\n💫 INTERACTION OPTIONS:")
        print("1️⃣ 😘 Cyber Flirt (Sweet digital talk)")
        print("2️⃣ 💰 Flex Assets (Show cash/items/rep)")
        print("3️⃣ 🔥 Physical Interface (Intimate + item boost)")
        print("4️⃣ 🚗 Quantum Drive Away")
        print("5️⃣ 🎲 Risky Cyber Deal (High risk/reward)")
        print("6️⃣ 💳 Direct Payment (Pay for guaranteed action)")
        
        # Item boost preview
        if self.player["items"]:
            relevant_items = [item for item in self.player["items"] if item["value"] > 30]
            if relevant_items:
                print(f"💎 Power Items Detected: {len(relevant_items)} high-value items will boost this encounter!")
    
    def travel(self):
        print(f"\n🛣️ CYBER HIGHWAY NAVIGATION 🛣️")
        print("Your position on the San Andreas cyber-net:")
        
        # Show available moves
        moves = []
        if self.position > 0:
            moves.append(f"⬅️  L: {self.world[self.position-1]['name']}")
        if self.position < len(self.world) - 1:
            moves.append(f"➡️  R: {self.world[self.position+1]['name']}")
        moves.append("⬆️  N: Stay and trigger event")
        
        for move in moves:
            print(move)
        
        choice = input("\nDirection (L/R/N): ").upper()
        energy_cost = random.randint(8, 15)
        
        if choice == "L" and self.position > 0:
            self.position -= 1
            print(f"⬅️ Cruising to {self.world[self.position]['name']}...")
            self.trigger_travel_event()
        elif choice == "R" and self.position < len(self.world) - 1:
            self.position += 1
            print(f"➡️ Heading to {self.world[self.position]['name']}...")
            self.trigger_travel_event()
        elif choice == "N":
            print("🔄 Staying local, scanning for opportunities...")
            self.trigger_location_event()
        else:
            print("❌ Invalid route! GPS recalculating...")
            energy_cost = 5
        
        self.player["energy"] = max(0, self.player["energy"] - energy_cost)
        self.update_market_prices()
        self.turn_counter += 1
        time.sleep(1.5)
    
    def trigger_travel_event(self):
        travel_events = [
            "🚓 Cyber Police checkpoint! Hide your illegal items or pay fine.",
            "💰 Found a data cache on the highway! +200$",
            "🔥 Street race challenge! Win for heat and rep boost.",
            "💋 Hitchhiker signals for ride - potential encounter!",
            "⚡ EMP blast damages your systems - energy drain!",
            "🎰 Popup crypto casino ad - feeling lucky?",
            "📱 Encrypted message: New mission available!"
        ]
        
        event = random.choice(travel_events)
        print(f"🌐 Travel Event: {event}")
        
        if "fine" in event and self.player["items"]:
            illegal_items = [item for item in self.player["items"] if "hack" in item["name"].lower()]
            if illegal_items and random.random() < 0.3:
                fine = random.randint(100, 300)
                self.player["cash"] = max(0, self.player["cash"] - fine)
                print(f"💸 Paid fine: ${fine}")
        elif "+200$" in event:
            self.player["cash"] += 200
        elif "energy drain" in event:
            self.player["energy"] = max(0, self.player["energy"] - 20)
    
    def trigger_location_event(self):
        current_loc = self.world[self.position]
        
        location_events = {
            "danger": [
                "🥊 Gang challenge - fight or pay protection!",
                "💊 Underground drug deal opportunity",
                "🔫 Cyber warfare - choose side for rewards"
            ],
            "city": [
                "🏪 New cyber shop opened - rare items available!",
                "📻 Club promotion - VIP access for heat boost",
                "🎭 Underground auction - bid on exclusive items"
            ],
            "relax": [
                "🧘 Meditation app ads - restore energy for $50",
                "🏄 Virtual surfing competition - skill challenge",
                "☀️ Solar charging station - free energy boost"
            ],
            "luxury": [
                "🎲 High-stakes crypto gambling",
                "💍 Elite escort service advertisement",
                "🍾 VIP party invitation - networking opportunity"
            ],
            "elite": [
                "👑 Exclusive NFT mint opportunity",
                "🎪 Private billionaire party",
                "🔬 Experimental tech beta testing"
            ]
        }
        
        events = location_events.get(current_loc["type"], ["Nothing special happens."])
        event = random.choice(events)
        print(f"📍 {current_loc['name']} Event: {event}")
        
        # Handle event consequences
        if "energy boost" in event:
            if "free" in event:
                self.player["energy"] = min(100, self.player["energy"] + 25)
            elif self.player["cash"] >= 50:
                self.player["cash"] -= 50
                self.player["energy"] = min(100, self.player["energy"] + 40)
                print("💚 Energy restored!")
        elif "VIP access" in event and self.player["cash"] >= 200:
            choice = input("Pay $200 for VIP access? (y/n): ")
            if choice.lower() == 'y':
                self.player["cash"] -= 200
                self.player["heat"] += 15
                self.player["reputation"] += 5
                print("🔥 VIP heat boost gained!")
    
    def encounter(self):
        current_loc = self.world[self.position]
        npc_type = random.choice(current_loc["encounters"])
        
        self.clear_screen()
        self.draw_hud()
        self.draw_ascii_cyber_car()
        self.show_encounter(npc_type)
        
        choice = input("\n💬 Your choice (1-6): ")
        npc = self.npcs[npc_type]
        base_heat = npc["heat_reward"]
        
        if choice == "1":
            self.cyber_flirt(npc)
        elif choice == "2":
            self.flex_assets(npc)
        elif choice == "3":
            self.physical_interface(npc)
        elif choice == "4":
            print("💨 Quantum drive activated! Escaped in a flash of neon...")
            return
        elif choice == "5":
            self.risky_cyber_deal(npc)
        elif choice == "6":
            self.direct_payment(npc)
        else:
            print("❓ Invalid choice - standing there confused...")
            return
        
        # Apply base heat reward
        heat_gained = base_heat
        
        # Item bonuses
        item_bonus = sum(item["value"] for item in self.player["items"]) // 10
        heat_gained += item_bonus
        
        # VIP bonus
        if self.player["vip_status"]:
            heat_gained = int(heat_gained * 1.2)
        
        self.player["heat"] += heat_gained
        self.player["reputation"] += random.randint(2, 8)
        
        if item_bonus > 0:
            print(f"💎 Item boost: +{item_bonus} heat from your collection!")
        
        # Random cyber event check
        if random.random() < 0.15:
            self.trigger_cyber_event()
        
        time.sleep(2)
    
    def cyber_flirt(self, npc):
        flirt_lines = [
            f"😘 {npc['name']}: 'Your digital aura is intoxicating... Tell me your deepest cyber fantasies.'",
            f"💋 {npc['name']}: 'I love how your neural implants glow when you're excited...'",
            f"🔥 {npc['name']}: 'In this digital realm, we can be anything... What's your secret desire?'"
        ]
        
        print(random.choice(flirt_lines))
        player_line = input("💭 Your flirt response: ")
        
        response_quality = len(player_line) + random.randint(-5, 5)
        
        if response_quality > 15:
            print(f"❤️ {npc['name']}: 'Mmm, that's incredibly hot... I'm getting wet just thinking about it.'")
            self.player["heat"] += 10
        elif response_quality > 8:
            print(f"😊 {npc['name']}: 'Sweet... I like your style. Want to get more intimate?'")
            self.player["heat"] += 5
        else:
            print(f"😐 {npc['name']}: 'Okay... maybe try being more creative next time.'")
    
    def flex_assets(self, npc):
        total_assets = self.player["cash"] + self.player["bank_balance"] + self.player["investments"]
        item_value = sum(item["value"] for item in self.player["items"])
        
        print(f"💵 Flexing: ${total_assets} total wealth, {len(self.player['items'])} premium items")
        print(f"⭐ Reputation: {self.player['reputation']} | Cyber Crimes: {self.player['cyber_crimes']}")
        
        if total_assets > 5000 or item_value > 200:
            print(f"💎 {npc['name']}: 'Wow! You're clearly a major player in this game... I'm impressed.'")
            self.player["heat"] += 20
            if random.random() < 0.3:
                print(f"🎁 {npc['name']} gives you a special item for being so impressive!")
                bonus_item = random.choice(self.market_items).copy()
                self.player["items"].append(bonus_item)
        elif total_assets > 2000:
            print(f"😊 {npc['name']}: 'Nice setup! You've got potential...'")
            self.player["heat"] += 10
        else:
            print(f"😏 {npc['name']}: 'Cute, but I need to see more zeros in those numbers.'")
    
    def physical_interface(self, npc):
        print(f"🔥 {npc['name']} moves closer: 'I can feel the electricity between us...'")
        
        intensity_options = {
            "light": {"name": "Gentle touch", "heat": 15, "energy": 5},
            "medium": {"name": "Passionate embrace", "heat": 25, "energy": 10},
            "hot": {"name": "Intense action", "heat": 40, "energy": 15},
            "wild": {"name": "Explosive encounter", "heat": 60, "energy": 25}
        }
        
        print("\nIntensity levels:")
        for key, value in intensity_options.items():
            print(f"• {key}: {value['name']} (+{value['heat']} heat, -{value['energy']} energy)")
        
        intensity = input("Choose intensity (light/medium/hot/wild): ").lower()
        
        if intensity in intensity_options:
            option = intensity_options[intensity]
            print(f"🌶️ {option['name']} selected!")
            
            if self.player["energy"] >= option["energy"]:
                self.player["energy"] -= option["energy"]
                heat_gain = option["heat"]
                
                # Item bonuses for physical encounters
                relevant_items = [item for item in self.player["items"] 
                                if "vibrator" in item["name"].lower() or "stimulator" in item["name"].lower()]
                
                if relevant_items:
                    bonus = len(relevant_items) * 10
                    heat_gain += bonus
                    print(f"💎 Item synergy bonus: +{bonus} heat!")
                
                self.player["heat"] += heat_gain
                print(f"❤️ {npc['name']}: 'That was... incredible. I've never felt anything like it.'")
            else:
                print("😴 You're too tired for that intensity! Rest first.")
        else:
            print("❓ Invalid intensity level.")
    
    def risky_cyber_deal(self, npc):
        print(f"🎲 {npc['name']}: 'I've got a proposition... High risk, but the rewards...'")
        
        deals = [
            {"name": "Data theft job", "success_rate": 0.6, "reward": 800, "penalty": 400},
            {"name": "Illegal item smuggling", "success_rate": 0.5, "reward": 1200, "penalty": 600},
            {"name": "Insider trading info", "success_rate": 0.7, "reward": 600, "penalty": 300},
            {"name": "Identity forgery", "success_rate": 0.4, "reward": 1500, "penalty": 800}
        ]
        
        deal = random.choice(deals)
        print(f"💼 Deal: {deal['name']}")
        print(f"📊 Success rate: {deal['success_rate']*100:.0f}%")
        print(f"💰 Reward: ${deal['reward']} | Penalty: ${deal['penalty']}")
        
        if input("Accept deal? (y/n): ").lower() == 'y':
            if random.random() < deal["success_rate"]:
                print(f"🎉 SUCCESS! Earned ${deal['reward']}")
                self.player["cash"] += deal["reward"]
                self.player["reputation"] += 15
                self.player["cyber_crimes"] += 1
                self.player["heat"] += 20
            else:
                print(f"💥 BUSTED! Lost ${deal['penalty']}")
                self.player["cash"] = max(0, self.player["cash"] - deal["penalty"])
                self.player["reputation"] = max(0, self.player["reputation"] - 10)
        else:
            print(f"{npc['name']}: 'Your loss... maybe next time.'")
    
    def direct_payment(self, npc):
        base_price = int(npc["heat_reward"] * npc.get("price_modifier", 1.0) * 10)
        vip_discount = 0.2 if self.player["vip_status"] else 0.0
        final_price = int(base_price * (1 - vip_discount))
        
        print(f"💳 {npc['name']}: 'For ${final_price}, I'll give you the premium experience...'")
        
        if self.player["vip_status"]:
            print(f"👑 VIP Discount Applied: {vip_discount*100:.0f}% off!")
        
        if self.player["cash"] >= final_price:
            if input(f"Pay ${final_price}? (y/n): ").lower() == 'y':
                self.player["cash"] -= final_price
                heat_bonus = npc["heat_reward"] + 20
                self.player["heat"] += heat_bonus
                print(f"💖 Premium service delivered! +{heat_bonus} heat")
                print(f"🔥 {npc['name']}: 'You definitely got your money's worth... and then some.'")
        else:
            print(f"💸 Not enough cash! Need ${final_price - self.player['cash']} more.")
    
    def trigger_cyber_event(self):
        event = random.choice(self.cyber_events)
        print(f"\n🌐 CYBER EVENT: {event['message']}")
        
        if event["effect"] == "bank_loss":
            loss = int(self.player["bank_balance"] * event["severity"])
            if self.player["insurance"]:
                loss = int(loss * 0.5)
                print("🛡️ Insurance reduced the damage by 50%!")
            self.player["bank_balance"] = max(0, self.player["bank_balance"] - loss)
            
        elif event["effect"] == "cash_loss":
            loss = int(self.player["cash"] * event["severity"])
            self.player["cash"] = max(0, self.player["cash"] - loss)
            
        elif event["effect"] == "item_lock":
            if self.player["items"]:
                if self.player["cash"] >= 500:
                    if input("Pay $500 ransom? (y/n): ").lower() == 'y':
                        self.player["cash"] -= 500
                        print("🔓 Items unlocked!")
                    else:
                        lost_item = self.player["items"].pop(random.randint(0, len(self.player["items"])-1))
                        print(f"💔 Lost {lost_item['name']}!")
                else:
                    if self.player["items"]:
                        lost_item = self.player["items"].pop(random.randint(0, len(self.player["items"])-1))
                        print(f"💔 Can't pay ransom! Lost {lost_item['name']}!")
                        
        elif event["effect"] == "investment_gain":
            gain = int(self.player["investments"] * event["severity"])
            self.player["investments"] += gain
            
        elif event["effect"] == "investment_loss":
            loss = int(self.player["investments"] * event["severity"])
            self.player["investments"] = max(0, self.player["investments"] - loss)
            
        elif event["effect"] == "cash_gain":
            self.player["cash"] += int(event["severity"])
            
        elif event["effect"] == "free_item":
            free_item = random.choice(self.market_items).copy()
            self.player["items"].append(free_item)
            print(f"🎁 Received: {free_item['name']}!")
            
        elif event["effect"] == "energy_drain":
            self.player["energy"] = max(0, self.player["energy"] - int(event["severity"]))
        
        time.sleep(2)
    
    def cyber_bank_menu(self):
        while True:
            self.clear_screen()
            self.draw_hud()
            self.draw_ascii_cyber_bank()
            
            print("\n💳 CYBER BANK: GLOBAL TRADING EMPIRE 💳")
            print("🌐 Creating trade on a massive scale!")
            print("\n📊 BANKING SERVICES:")
            print("1️⃣ 📥 Deposit Cash to Bank")
            print("2️⃣ 📤 Withdraw from Bank")
            print("3️⃣ 📈 Invest (Growth + Risk)")
            print("4️⃣ 🛒 Global Item Market")
            print("5️⃣ 🛡️ Buy Cyber Insurance ($300)")
            print("6️⃣ 👑 Upgrade to VIP Status ($2000)")
            print("7️⃣ 💎 Mint Personal NFT")
            print("8️⃣ 📊 Market Analysis")
            print("9️⃣ 🎯 Trading Missions")
            print("0️⃣ 🚪 Exit Bank")
            
            choice = input("\nSelect service: ")
            
            if choice == "1":
                self.bank_deposit()
            elif choice == "2":
                self.bank_withdraw()
            elif choice == "3":
                self.bank_invest()
            elif choice == "4":
                self.global_market()
            elif choice == "5":
                self.buy_insurance()
            elif choice == "6":
                self.upgrade_vip()
            elif choice == "7":
                self.mint_personal_nft()
            elif choice == "8":
                self.market_analysis()
            elif choice == "9":
                self.trading_missions()
            elif choice == "0":
                break
            else:
                print("❓ Invalid option!")
                time.sleep(1)
    
    def bank_deposit(self):
        print(f"\n💰 Current Cash: ${self.player['cash']}")
        try:
            amount = int(input("Amount to deposit: $") or 0)
            if 0 < amount <= self.player["cash"]:
                self.player["cash"] -= amount
                self.player["bank_balance"] += amount
                print(f"✅ Deposited ${amount} to secure cyber-vault!")
            else:
                print("❌ Invalid amount!")
        except ValueError:
            print("❌ Enter a valid number!")
        time.sleep(1.5)
    
    def bank_withdraw(self):
        print(f"\n🏦 Bank Balance: ${self.player['bank_balance']}")
        try:
            amount = int(input("Amount to withdraw: $") or 0)
            if 0 < amount <= self.player["bank_balance"]:
                self.player["bank_balance"] -= amount
                self.player["cash"] += amount
                print(f"✅ Withdrew ${amount} to your wallet!")
            else:
                print("❌ Insufficient bank funds!")
        except ValueError:
            print("❌ Enter a valid number!")
        time.sleep(1.5)
    
    def bank_invest(self):
        print(f"\n📈 Bank Balance: ${self.player['bank_balance']}")
        print(f"📊 Current Investments: ${self.player['investments']}")
        print("💡 Investments grow 5-15% per turn, but have 20% risk of loss!")
        
        try:
            amount = int(input("Amount to invest: $") or 0)
            if 0 < amount <= self.player["bank_balance"]:
                self.player["bank_balance"] -= amount
                self.player["investments"] += amount
                
                # Immediate growth/loss
                growth_rate = random.uniform(-0.20, 0.25)  # -20% to +25%
                growth = int(amount * growth_rate)
                self.player["investments"] += growth
                
                if growth > 0:
                    print(f"📈 Investment grew by ${growth}! Total investments: ${self.player['investments']}")
                else:
                    print(f"📉 Market loss: ${abs(growth)}. Total investments: ${self.player['investments']}")
            else:
                print("❌ Insufficient bank funds!")
        except ValueError:
            print("❌ Enter a valid number!")
        time.sleep(2)
    
    def global_market(self):
        while True:
            self.clear_screen()
            self.draw_hud()
            print("\n🛒 GLOBAL CYBER MARKET 🛒")
            print("💹 Prices fluctuate in real-time!")
            
            print("\n📦 AVAILABLE ITEMS:")
            for i, item in enumerate(self.market_items):
                rarity_symbols = {
                    "common": "⚪", "uncommon": "🟢", "rare": "🔵", 
                    "epic": "🟣", "legendary": "🟡", "mythic": "🔴"
                }
                symbol = rarity_symbols.get(item["rarity"], "⚫")
                price_change = item["price"] - item["base_price"]
                trend = "📈" if price_change > 0 else "📉" if price_change < 0 else "➡️"
                
                print(f"{i+1:2d}: {symbol} {item['name']:<25} ${item['price']:>6} {trend} (Heat: +{item['value']})")
            
            print("\n🎒 YOUR ITEMS:")
            if self.player["items"]:
                for i, item in enumerate(self.player["items"]):
                    sell_price = item["price"] // 2
                    print(f"   {item['name']} (Sell for ${sell_price})")
            else:
                print("   No items owned")
            
            print("\n💰 ACTIONS:")
            print("1-9: Buy item | S: Sell items | R: Refresh market | B: Back")
            
            choice = input("\nAction: ").upper()
            
            if choice.isdigit():
                self.buy_item(int(choice) - 1)
            elif choice == "S":
                self.sell_items()
            elif choice == "R":
                self.update_market_prices()
                print("🔄 Market refreshed!")
                time.sleep(1)
            elif choice == "B":
                break
            else:
                print("❓ Invalid choice!")
                time.sleep(1)
    
    def buy_item(self, index):
        if 0 <= index < len(self.market_items):
            item = self.market_items[index]
            
            print(f"\n🛍️ Purchasing: {item['name']}")
            print(f"💰 Price: ${item['price']}")
            print(f"🔥 Heat Value: +{item['value']}")
            print(f"💎 Rarity: {item['rarity']}")
            
            payment_source = "cash"
            if item["price"] > self.player["cash"]:
                if item["price"] <= self.player["bank_balance"]:
                    payment_source = "bank"
                else:
                    print("❌ Insufficient funds!")
                    time.sleep(1.5)
                    return
            
            if input(f"Buy with {payment_source}? (y/n): ").lower() == "y":
                if payment_source == "cash":
                    self.player["cash"] -= item["price"]
                else:
                    self.player["bank_balance"] -= item["price"]
                
                purchased_item = item.copy()
                self.player["items"].append(purchased_item)
                self.player["heat"] += item["value"]
                
                print(f"✅ Purchased {item['name']}! +{item['value']} heat boost!")
                time.sleep(1.5)
        else:
            print("❌ Invalid item number!")
            time.sleep(1)
    
    def sell_items(self):
        if not self.player["items"]:
            print("❌ No items to sell!")
            time.sleep(1.5)
            return
        
        print("\n💰 SELL ITEMS:")
        for i, item in enumerate(self.player["items"]):
            sell_price = item["price"] // 2
            print(f"{i+1}: {item['name']} - Sell for ${sell_price}")
        
        try:
            choice = int(input("Item to sell (number): ")) - 1
            if 0 <= choice < len(self.player["items"]):
                sold_item = self.player["items"].pop(choice)
                profit = sold_item["price"] // 2
                self.player["cash"] += profit
                print(f"✅ Sold {sold_item['name']} for ${profit}!")
            else:
                print("❌ Invalid item number!")
        except ValueError:
            print("❌ Enter a valid number!")
        time.sleep(1.5)
    
    def buy_insurance(self):
        if self.player["insurance"]:
            print("🛡️ You already have active cyber insurance!")
        elif self.player["cash"] >= 300:
            if input("Buy cyber insurance for $300? (y/n): ").lower() == "y":
                self.player["cash"] -= 300
                self.player["insurance"] = True
                print("🛡️ Cyber insurance activated! 50% damage reduction for 10 turns.")
        else:
            print("❌ Need $300 for insurance!")
        time.sleep(1.5)
    
    def upgrade_vip(self):
        if self.player["vip_status"]:
            print("👑 You're already VIP!")
        elif self.player["cash"] >= 2000:
            if input("Upgrade to VIP for $2000? (20% heat bonus, discounts) (y/n): ").lower() == "y":
                self.player["cash"] -= 2000
                self.player["vip_status"] = True
                print("👑 VIP status activated! Enjoy premium benefits!")
        else:
            print("❌ Need $2000 for VIP upgrade!")
        time.sleep(1.5)
    
    def mint_personal_nft(self):
        print("\n🎨 MINT YOUR PERSONAL NFT")
        nft_name = input("NFT Name: ") or "Custom Furby"
        
        base_cost = 800
        print(f"💰 Minting cost: ${base_cost}")
        
        if self.player["bank_balance"] >= base_cost:
            if input("Mint NFT? (y/n): ").lower() == "y":
                self.player["bank_balance"] -= base_cost
                
                # Create unique NFT
                nft_value = random.randint(50, 150)
                nft_price = random.randint(1000, 3000)
                
                personal_nft = {
                    "name": f"{nft_name} NFT",
                    "price": nft_price,
                    "value": nft_value,
                    "category": "personal",
                    "rarity": "unique"
                }
                
                self.player["items"].append(personal_nft)
                self.player["reputation"] += 25
                
                print(f"✨ Minted {personal_nft['name']}!")
                print(f"💎 Value: +{nft_value} heat, Market price: ${nft_price}")
        else:
            print("❌ Insufficient bank funds!")
        time.sleep(2)
    
    def market_analysis(self):
        print("\n📊 MARKET ANALYSIS REPORT")
        print("="*50)
        
        # Calculate market trends
        total_market_value = sum(item["price"] for item in self.market_items)
        average_price = total_market_value // len(self.market_items)
        
        print(f"📈 Total Market Cap: ${total_market_value}")
        print(f"💰 Average Item Price: ${average_price}")
        print(f"📦 Your Portfolio Value: ${sum(item['price'] for item in self.player['items'])}")
        
        # Show trends by category
        categories = {}
        for item in self.market_items:
            cat = item["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item["price"])
        
        print(f"\n📊 CATEGORY TRENDS:")
        for category, prices in categories.items():
            avg_price = sum(prices) // len(prices)
            print(f"   {category.capitalize()}: ${avg_price} avg")
        
        # Investment advice
        print(f"\n💡 INVESTMENT ADVICE:")
        if self.player["investments"] < 1000:
            print("   • Consider increasing your investment portfolio")
        if len(self.player["items"]) < 3:
            print("   • Diversify with more items for heat bonuses")
        if not self.player["insurance"]:
            print("   • Cyber insurance recommended for asset protection")
        
        input("\nPress Enter to continue...")
    
    def trading_missions(self):
        print("\n🎯 TRADING MISSIONS HQ")
        self.draw_ascii_mission_hq()
        
        print("\n💼 AVAILABLE MISSIONS:")
        for i, mission in enumerate(self.missions):
            risk_level = "🟢" if mission["risk"] < 0.2 else "🟡" if mission["risk"] < 0.4 else "🔴"
            print(f"{i+1}: {mission['name']} - ${mission['reward']} {risk_level}")
            print(f"    {mission['description']} (Risk: {mission['risk']*100:.0f}%)")
        
        try:
            choice = int(input("\nSelect mission (number): ")) - 1
            if 0 <= choice < len(self.missions):
                self.execute_mission(self.missions[choice])
            else:
                print("❌ Invalid mission!")
        except ValueError:
            print("❌ Enter a valid number!")
        time.sleep(2)
    
    def execute_mission(self, mission):
        print(f"\n🎯 Executing: {mission['name']}")
        print(f"📋 {mission['description']}")
        
        # Check if player wants to proceed
        if input("Accept mission? (y/n): ").lower() != 'y':
            return
        
        # Mission execution
        success = random.random() > mission["risk"]
        
        if success:
            print(f"✅ MISSION SUCCESS!")
            print(f"💰 Earned ${mission['reward']}")
            self.player["cash"] += mission["reward"]
            self.player["reputation"] += 10
            
            if mission["type"] == "criminal":
                self.player["cyber_crimes"] += 1
                print("⚖️ Cyber crime record updated")
                
        else:
            print(f"💥 MISSION FAILED!")
            penalty = mission["reward"] // 3
            print(f"💸 Lost ${penalty} in resources")
            self.player["cash"] = max(0, self.player["cash"] - penalty)
            
            if mission["type"] == "criminal":
                print("🚓 Authorities are now aware of your activities")
                self.player["reputation"] = max(0, self.player["reputation"] - 5)
    
    def check_game_over(self):
        # Victory conditions
        if self.player["heat"] >= 100:
            self.show_victory_screen("HEAT_MASTER")
            return True
        
        if self.player["cash"] + self.player["bank_balance"] + self.player["investments"] >= 50000:
            self.show_victory_screen("CYBER_MOGUL")
            return True
        
        if self.player["reputation"] >= 1000:
            self.show_victory_screen("LEGEND")
            return True
        
        # Defeat conditions
        if self.player["energy"] <= 0 and self.player["cash"] < 100:
            self.show_game_over_screen("EXHAUSTED")
            return True
        
        if self.player["cash"] <= 0 and self.player["bank_balance"] <= 0 and not self.player["items"]:
            self.show_game_over_screen("BANKRUPT")
            return True
        
        return False
    
    def show_victory_screen(self, victory_type):
        self.clear_screen()
        
        victory_messages = {
            "HEAT_MASTER": {
                "title": "🔥 HEAT MASTER ACHIEVED 🔥",
                "message": "You've become the ultimate seducer of the cyber realm!",
                "bonus": "You can make anyone fall for your digital charm!"
            },
            "CYBER_MOGUL": {
                "title": "💰 CYBER MOGUL STATUS 💰", 
                "message": "Your trading empire spans the entire digital world!",
                "bonus": "You control the cyber economy!"
            },
            "LEGEND": {
                "title": "⭐ LEGENDARY REPUTATION ⭐",
                "message": "Everyone in the cyber realm knows your name!",
                "bonus": "You're a living legend in San Andreas!"
            }
        }
        
        victory = victory_messages[victory_type]
        
        print("="*70)
        print(victory["title"].center(70))
        print("="*70)
        print()
        print(victory["message"].center(70))
        print(victory["bonus"].center(70))
        print()
        print(f"FINAL STATS:".center(70))
        print(f"Heat: {self.player['heat']}/100 | Wealth: ${self.player['cash'] + self.player['bank_balance'] + self.player['investments']}".center(70))
        print(f"Reputation: {self.player['reputation']} | Items: {len(self.player['items'])}".center(70))
        print(f"Turns Played: {self.turn_counter} | Cyber Crimes: {self.player['cyber_crimes']}".center(70))
        print()
        print("🎉 CONGRATULATIONS! YOU'VE WON THE CYBER GAME! 🎉".center(70))
        print("="*70)
    
    def show_game_over_screen(self, defeat_type):
        self.clear_screen()
        
        defeat_messages = {
            "EXHAUSTED": {
                "title": "😴 ENERGY DEPLETED 😴",
                "message": "You've burned out in the cyber world..."
            },
            "BANKRUPT": {
                "title": "💸 TOTAL BANKRUPTCY 💸",
                "message": "You've lost everything in the digital realm..."
            }
        }
        
        defeat = defeat_messages[defeat_type]
        
        print("="*70)
        print(defeat["title"].center(70))
        print("="*70)
        print()
        print(defeat["message"].center(70))
        print()
        print("GAME OVER - Better luck next time in the cyber realm!".center(70))
        print("="*70)
    
    def rest_and_recover(self):
        """Rest to restore energy and process passive income"""
        energy_gain = random.randint(40, 60)
        self.player["energy"] = min(100, self.player["energy"] + energy_gain)
        
        # Passive investment growth
        if self.player["investments"] > 0:
            growth = int(self.player["investments"] * random.uniform(0.02, 0.08))
            self.player["investments"] += growth
            print(f"📈 Investments grew by ${growth} while you rested!")
        
        # Insurance countdown
        if self.player["insurance"]:
            print("🛡️ Cyber insurance still active!")
        
        print(f"😴 Rested well! Energy restored to {self.player['energy']}/100")
        self.turn_counter += 1
        time.sleep(2)
    
    def start_game(self):
        self.clear_screen()
        
        # Game intro
        intro_art = [
            "🎮 AI FURBY 1.25D: CYBER SAN ANDREAS EDITION 🎮",
            "",
            "💋 Welcome to the ultimate adult cyber adventure! 💋",
            "",
            "🌐 Build your empire through:",
            "   • Seductive encounters in 5 unique locations",
            "   • Global cyber trading & banking",
            "   • High-risk missions & deals", 
            "   • Heat progression & reputation building",
            "",
            "⚠️  This game contains adult content ⚠️",
            "🔞 Players must be 18+ years old 🔞"
        ]
        
        for line in intro_art:
            print(line.center(70))
        print("\n" + "="*70)
        
        self.player["name"] = input("💎 Enter your Cyber Furby name: ") or "Anonymous_Player"
        
        print(f"\nWelcome to the game, {self.player['name']}!")
        print("🚗 Starting your journey in the Cyber Ghetto...")
        time.sleep(2)
        
        # Main game loop
        while not self.check_game_over():
            self.clear_screen()
            self.draw_hud()
            
            print("\n🎯 MAIN ACTIONS:")
            print("1️⃣ 🚗 Travel & Cruise")
            print("2️⃣ 💋 Seek Erotic Encounters") 
            print("3️⃣ 🏦 Enter Cyber Bank")
            print("4️⃣ 😴 Rest & Recover")
            print("5️⃣ 📊 View Full Stats")
            print("6️⃣ 🎯 Quick Mission")
            print("0️⃣ 🚪 Quit Game")
            
            choice = input("\nYour choice: ")
            
            if choice == "1":
                self.travel()
            elif choice == "2":
                self.encounter()
            elif choice == "3":
                self.cyber_bank_menu()
            elif choice == "4":
                self.rest_and_recover()
            elif choice == "5":
                self.show_full_stats()
            elif choice == "6":
                if self.missions:
                    quick_mission = random.choice(self.missions)
                    print(f"🎯 Quick Mission: {quick_mission['name']}")
                    self.execute_mission(quick_mission)
            elif choice == "0":
                if input("Really quit? (y/n): ").lower() == "y":
                    print("👋 Thanks for playing Cyber San Andreas!")
                    break
            else:
                print("❓ Invalid choice!")
                time.sleep(1)
            
            # Auto-save simulation
            if self.turn_counter % 10 == 0:
                print("💾 Auto-saving your progress...")
                time.sleep(1)
        
        print("\n🎮 Game ended! Thanks for playing!")
        print(f"Final score: Heat {self.player['heat']}, Wealth ${self.player['cash'] + self.player['bank_balance']}")
    
    def show_full_stats(self):
        self.clear_screen()
        self.draw_hud()
        
        print("\n📊 DETAILED STATISTICS")
        print("="*50)
        print(f"💰 Financial Status:")
        print(f"   Cash: ${self.player['cash']}")
        print(f"   Bank: ${self.player['bank_balance']}")
        print(f"   Investments: ${self.player['investments']}")
        print(f"   Total Wealth: ${self.player['cash'] + self.player['bank_balance'] + self.player['investments']}")
        
        print(f"\n🔥 Performance:")
        print(f"   Heat Level: {self.player['heat']}/100")
        print(f"   Reputation: {self.player['reputation']}")
        print(f"   Energy: {self.player['energy']}/100")
        
        print(f"\n📦 Inventory:")
        print(f"   Items Owned: {len(self.player['items'])}")
        if self.player["items"]:
            print(f"   Total Item Value: ${sum(item['price'] for item in self.player['items'])}")
            print(f"   Heat Bonus: +{sum(item['value'] for item in self.player['items'])}")
        
        print(f"\n🎮 Game Progress:")
        print(f"   Turns Played: {self.turn_counter}")
        print(f"   Current Location: {self.world[self.position]['name']}")
        print(f"   Cyber Crimes: {self.player['cyber_crimes']}")
        print(f"   VIP Status: {'Active' if self.player['vip_status'] else 'Inactive'}")
        print(f"   Insurance: {'Protected' if self.player['insurance'] else 'Unprotected'}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("🔞 AGE VERIFICATION REQUIRED 🔞")
    age_confirm = input("Are you 18+ years old? (yes/no): ").lower()
    
    if age_confirm in ['yes', 'y']:
        game = FurbyCyberSanAndreas()
        game.start_game()
    else:
        print("❌ This game is for adults only. Goodbye!")