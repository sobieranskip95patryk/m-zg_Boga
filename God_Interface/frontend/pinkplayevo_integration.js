/**
 * 🎵 PinkPlayEvo Integration Module
 * ================================
 * 
 * Integracja God Interface z ekosystemem PinkPlayEvo:
 * - Drift Coins tokenizacja
 * - Hip-Hop Muse playlists
 * - PinkMan avatar agent
 * - Style Battles integration
 */

class PinkPlayEvoIntegration {
    constructor() {
        this.driftCoins = parseInt(localStorage.getItem('driftCoins') || '0');
        this.userLevel = parseInt(localStorage.getItem('userLevel') || '1');
        this.currentPlaylist = null;
        this.pinkManMood = 'neutral';
        this.activityTokens = [];
        
        this.initializeUI();
        this.loadUserProfile();
    }
    
    /**
     * 💎 Drift Coins System
     */
    addDriftCoins(amount, activity) {
        this.driftCoins += amount;
        localStorage.setItem('driftCoins', this.driftCoins.toString());
        
        // Create activity token
        const token = {
            id: Date.now(),
            type: 'interaction',
            activity: activity,
            coins: amount,
            timestamp: new Date().toISOString(),
            mood: this.pinkManMood
        };
        
        this.activityTokens.push(token);
        this.updateDriftDisplay();
        this.showCoinAnimation(amount);
        
        // Level up check
        if (this.driftCoins >= this.userLevel * 100) {
            this.levelUp();
        }
        
        return token;
    }
    
    updateDriftDisplay() {
        const display = document.getElementById('driftCoins');
        if (display) {
            display.innerHTML = `
                <div class="drift-status">
                    <span class="coins">💎 ${this.driftCoins}</span>
                    <span class="level">Level ${this.userLevel}</span>
                </div>
            `;
        }
    }
    
    showCoinAnimation(amount) {
        const animation = document.createElement('div');
        animation.className = 'coin-animation';
        animation.innerHTML = `+${amount} 💎`;
        document.body.appendChild(animation);
        
        setTimeout(() => animation.remove(), 2000);
    }
    
    levelUp() {
        this.userLevel++;
        localStorage.setItem('userLevel', this.userLevel.toString());
        
        const notification = document.createElement('div');
        notification.className = 'level-up-notification';
        notification.innerHTML = `
            <div class="level-up-content">
                🎉 LEVEL UP! 🎉<br>
                Poziom ${this.userLevel}<br>
                Nowe możliwości odblokowane!
            </div>
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 3000);
    }
    
    /**
     * 🎵 Hip-Hop Muse Integration
     */
    async loadHipHopMuse() {
        const playlists = {
            'chill': [
                'https://www.youtube.com/watch?v=YykjpeuMNEk', // Lo-fi hip hop
                'https://www.youtube.com/watch?v=jfKfPfyJRdk'  // Chillhop
            ],
            'energetic': [
                'https://www.youtube.com/watch?v=_CL6n0FJZpk', // Eminem
                'https://www.youtube.com/watch?v=gOMhN-hfMtY'  // Kanye
            ],
            'spiritual': [
                'https://www.youtube.com/watch?v=tmozGmGoJuw', // Kendrick
                'https://www.youtube.com/watch?v=tvTRZJ-4EyI'  // J. Cole
            ],
            'creative': [
                'https://www.youtube.com/watch?v=6p0DAz_30qQ', // Tyler
                'https://www.youtube.com/watch?v=rEMsjeq43_U'  // Travis Scott
            ]
        };
        
        return playlists;
    }
    
    async setMoodPlaylist(mood) {
        const playlists = await this.loadHipHopMuse();
        this.currentPlaylist = playlists[mood] || playlists['chill'];
        this.pinkManMood = mood;
        
        this.updatePinkManAvatar(mood);
        this.updateMusicPlayer();
        
        return this.currentPlaylist;
    }
    
    updateMusicPlayer() {
        const player = document.getElementById('musicPlayer');
        if (player && this.currentPlaylist) {
            const randomTrack = this.currentPlaylist[Math.floor(Math.random() * this.currentPlaylist.length)];
            player.innerHTML = `
                <div class="music-player">
                    <div class="track-info">🎵 ${this.pinkManMood.toUpperCase()} VIBES</div>
                    <div class="track-link">
                        <a href="${randomTrack}" target="_blank">▶️ Play Track</a>
                    </div>
                </div>
            `;
        }
    }
    
    /**
     * 🎭 PinkMan Avatar Agent
     */
    updatePinkManAvatar(mood) {
        const avatar = document.getElementById('pinkManAvatar');
        if (!avatar) return;
        
        const avatarStates = {
            'neutral': { emoji: '🤖', color: '#ff69b4', text: 'PinkMan gotowy do rozmowy' },
            'chill': { emoji: '😌', color: '#87ceeb', text: 'PinkMan w stanie relaksu' },
            'energetic': { emoji: '🔥', color: '#ff4500', text: 'PinkMan naładowany energią' },
            'spiritual': { emoji: '🧘', color: '#9370db', text: 'PinkMan w medytacji' },
            'creative': { emoji: '🎨', color: '#ffd700', text: 'PinkMan w trybie twórczym' }
        };
        
        const state = avatarStates[mood] || avatarStates['neutral'];
        
        avatar.innerHTML = `
            <div class="pinkman-avatar" style="color: ${state.color}">
                <div class="avatar-emoji">${state.emoji}</div>
                <div class="avatar-status">${state.text}</div>
                <div class="avatar-pulse"></div>
            </div>
        `;
        
        avatar.className = `pinkman-container mood-${mood}`;
    }
    
    /**
     * 🎮 Style Battles Integration
     */
    async createStyleBattle(userMessage, godResponse) {
        const battle = {
            id: Date.now(),
            timestamp: new Date().toISOString(),
            participants: ['User', 'Mózg Boga'],
            rounds: [
                {
                    round: 1,
                    user_style: this.analyzeMessageStyle(userMessage),
                    god_style: this.analyzeResponseStyle(godResponse),
                    winner: this.determineStyleWinner(userMessage, godResponse)
                }
            ],
            prize: this.calculateBattlePrize(),
            mood: this.pinkManMood
        };
        
        this.addDriftCoins(battle.prize, 'style_battle');
        this.displayStyleBattle(battle);
        
        return battle;
    }
    
    analyzeMessageStyle(message) {
        const styles = {
            lyrical: (message.match(/\b(rytm|flow|beat|bars)\b/gi) || []).length,
            emotional: (message.match(/\b(czuję|emocja|serce|dusza)\b/gi) || []).length,
            philosophical: (message.match(/\b(sens|prawda|życie|świat)\b/gi) || []).length,
            creative: (message.match(/\b(twórczy|sztuka|wizja|inspiracja)\b/gi) || []).length
        };
        
        const dominantStyle = Object.keys(styles).reduce((a, b) => styles[a] > styles[b] ? a : b);
        return { style: dominantStyle, score: styles[dominantStyle] };
    }
    
    analyzeResponseStyle(response) {
        // Analiza stylu odpowiedzi Boga
        const wordCount = response.split(' ').length;
        const metaphorCount = (response.match(/\b(jak|jakby|niczym|podobnie)\b/gi) || []).length;
        const spiritualCount = (response.match(/\b(dusza|duch|transcendencja|świadomość)\b/gi) || []).length;
        
        return {
            style: 'divine',
            score: Math.floor((wordCount + metaphorCount * 2 + spiritualCount * 3) / 10)
        };
    }
    
    determineStyleWinner(userMessage, godResponse) {
        const userScore = userMessage.length + (userMessage.split(' ').length * 2);
        const godScore = godResponse.length + (godResponse.split(' ').length * 2);
        
        return userScore > godScore ? 'User' : 'Mózg Boga';
    }
    
    calculateBattlePrize() {
        return Math.floor(Math.random() * 50) + 10; // 10-60 Drift Coins
    }
    
    displayStyleBattle(battle) {
        const display = document.getElementById('styleBattleResult');
        if (display) {
            display.innerHTML = `
                <div class="style-battle">
                    <h4>🎤 Style Battle Result</h4>
                    <div class="battle-details">
                        <div>Winner: ${battle.rounds[0].winner}</div>
                        <div>Prize: +${battle.prize} 💎</div>
                        <div>Mood: ${battle.mood}</div>
                    </div>
                </div>
            `;
        }
    }
    
    /**
     * 📱 NFT Activity Tokens
     */
    async mintActivityToken(activity) {
        const token = {
            id: `ACTIVITY_${Date.now()}`,
            type: 'NFT',
            activity: activity,
            metadata: {
                timestamp: new Date().toISOString(),
                user_level: this.userLevel,
                drift_coins: this.driftCoins,
                mood: this.pinkManMood,
                rarity: this.calculateTokenRarity()
            },
            image: await this.generateTokenImage(activity)
        };
        
        this.activityTokens.push(token);
        localStorage.setItem('activityTokens', JSON.stringify(this.activityTokens));
        
        this.showTokenMintedNotification(token);
        return token;
    }
    
    calculateTokenRarity() {
        const rarities = ['Common', 'Rare', 'Epic', 'Legendary', 'Divine'];
        const weights = [50, 30, 15, 4, 1]; // percentages
        
        const random = Math.random() * 100;
        let cumulative = 0;
        
        for (let i = 0; i < weights.length; i++) {
            cumulative += weights[i];
            if (random <= cumulative) {
                return rarities[i];
            }
        }
        
        return 'Common';
    }
    
    async generateTokenImage(activity) {
        // Placeholder for AI-generated token image
        return `data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="%23ff69b4"/>
            <text x="50" y="55" text-anchor="middle" fill="white" font-size="20">🎵</text>
        </svg>`;
    }
    
    showTokenMintedNotification(token) {
        const notification = document.createElement('div');
        notification.className = 'token-minted-notification';
        notification.innerHTML = `
            <div class="token-content">
                🎫 NFT Minted!<br>
                ${token.id}<br>
                Rarity: ${token.metadata.rarity}
            </div>
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 4000);
    }
    
    /**
     * 🔧 UI Initialization
     */
    initializeUI() {
        // Drift Coins Display
        if (!document.getElementById('driftCoins')) {
            const driftDisplay = document.createElement('div');
            driftDisplay.id = 'driftCoins';
            driftDisplay.className = 'drift-coins-display';
            document.querySelector('.god-interface-container').appendChild(driftDisplay);
        }
        
        // PinkMan Avatar
        if (!document.getElementById('pinkManAvatar')) {
            const avatar = document.createElement('div');
            avatar.id = 'pinkManAvatar';
            avatar.className = 'pinkman-container';
            document.querySelector('.conversation-header').appendChild(avatar);
        }
        
        // Music Player
        if (!document.getElementById('musicPlayer')) {
            const player = document.createElement('div');
            player.id = 'musicPlayer';
            player.className = 'music-player-container';
            document.querySelector('.input-controls').appendChild(player);
        }
        
        // Style Battle Result
        if (!document.getElementById('styleBattleResult')) {
            const battleResult = document.createElement('div');
            battleResult.id = 'styleBattleResult';
            battleResult.className = 'style-battle-container';
            document.querySelector('.response-area').appendChild(battleResult);
        }
        
        this.updateDriftDisplay();
        this.updatePinkManAvatar('neutral');
    }
    
    loadUserProfile() {
        // Load saved user data
        const saved = localStorage.getItem('pinkPlayEvoProfile');
        if (saved) {
            const profile = JSON.parse(saved);
            this.driftCoins = profile.driftCoins || 0;
            this.userLevel = profile.userLevel || 1;
            this.pinkManMood = profile.mood || 'neutral';
        }
        
        this.updateDriftDisplay();
        this.updatePinkManAvatar(this.pinkManMood);
    }
    
    saveUserProfile() {
        const profile = {
            driftCoins: this.driftCoins,
            userLevel: this.userLevel,
            mood: this.pinkManMood,
            activityTokens: this.activityTokens.slice(-10) // Keep last 10 tokens
        };
        
        localStorage.setItem('pinkPlayEvoProfile', JSON.stringify(profile));
    }
    
    /**
     * 🎯 Main Integration Methods
     */
    async handleGodConversation(userMessage, godResponse) {
        // Award coins for conversation
        const conversationReward = this.addDriftCoins(15, 'god_conversation');
        
        // Create style battle
        const styleBattle = await this.createStyleBattle(userMessage, godResponse);
        
        // Mint activity token
        const activityToken = await this.mintActivityToken('divine_conversation');
        
        // Update mood based on response
        const detectedMood = this.detectMoodFromResponse(godResponse);
        await this.setMoodPlaylist(detectedMood);
        
        // Save profile
        this.saveUserProfile();
        
        return {
            conversationReward,
            styleBattle,
            activityToken,
            mood: detectedMood
        };
    }
    
    detectMoodFromResponse(response) {
        const moodKeywords = {
            'spiritual': ['dusza', 'transcendencja', 'świadomość', 'medytacja'],
            'energetic': ['energia', 'siła', 'działanie', 'aktywność'],
            'creative': ['twórczy', 'sztuka', 'inspiracja', 'wizja'],
            'chill': ['spokój', 'relaks', 'harmonia', 'cisza']
        };
        
        let maxScore = 0;
        let detectedMood = 'neutral';
        
        for (const [mood, keywords] of Object.entries(moodKeywords)) {
            const score = keywords.reduce((acc, keyword) => {
                return acc + (response.toLowerCase().includes(keyword) ? 1 : 0);
            }, 0);
            
            if (score > maxScore) {
                maxScore = score;
                detectedMood = mood;
            }
        }
        
        return detectedMood;
    }
}

// Initialize PinkPlayEvo Integration
window.pinkPlayEvo = new PinkPlayEvoIntegration();