/**
 * 🎬 GOK: MIXTAPE Integration Module
 * ==================================
 * 
 * Integracja God Interface z GOK: MIXTAPE system:
 * - Kompozycja narracji (temat, analiza, muzyka, emocja)
 * - Suwak MIXTAPE jako kontrola AI
 * - Eksport wpisu do bloga MetaGeniuszPL
 * - Generowanie grafik na podstawie nastroju
 * - Blog post creation i content management
 */

class GOKMixtapeIntegration {
    constructor() {
        this.currentMixtape = null;
        this.narrativeComposition = {
            theme: '',
            analysis: '',
            music: '',
            emotion: '',
            graphics: []
        };
        this.mixtapeLevel = 50; // 0-100 slider
        this.blogPosts = [];
        this.contentTemplates = {};
        
        this.initializeUI();
        this.loadTemplates();
    }
    
    /**
     * 🎬 MIXTAPE Composition System
     */
    createMixtapeFromConversation(userMessage, godResponse, emotion, mode) {
        const mixtape = {
            id: `MIXTAPE_${Date.now()}`,
            timestamp: new Date().toISOString(),
            mode: mode,
            composition: {
                theme: this.extractTheme(userMessage, godResponse),
                analysis: this.createAnalysis(userMessage, godResponse),
                music: this.suggestMusic(emotion, mode),
                emotion: emotion,
                user_input: userMessage,
                god_response: godResponse,
                mixtape_level: this.mixtapeLevel
            },
            graphics: [],
            exportable: true
        };
        
        this.currentMixtape = mixtape;
        this.updateMixtapeDisplay();
        
        return mixtape;
    }
    
    extractTheme(userMessage, godResponse) {
        // AI-powered theme extraction
        const themes = {
            'spiritual': ['dusza', 'duch', 'świadomość', 'medytacja', 'transcendencja'],
            'creative': ['twórczy', 'sztuka', 'inspiracja', 'wizja', 'kreatywność'],
            'philosophical': ['sens', 'prawda', 'życie', 'istnienie', 'mądrość'],
            'emotional': ['uczucia', 'emocje', 'serce', 'miłość', 'radość'],
            'technological': ['AI', 'technologia', 'przyszłość', 'innowacja', 'cyfrowy'],
            'musical': ['muzyka', 'dźwięk', 'rytm', 'harmonia', 'kompozycja']
        };
        
        const combinedText = (userMessage + ' ' + godResponse).toLowerCase();
        let maxScore = 0;
        let dominantTheme = 'universal';
        
        for (const [theme, keywords] of Object.entries(themes)) {
            const score = keywords.reduce((acc, keyword) => {
                return acc + (combinedText.includes(keyword) ? 1 : 0);
            }, 0);
            
            if (score > maxScore) {
                maxScore = score;
                dominantTheme = theme;
            }
        }
        
        return {
            primary: dominantTheme,
            score: maxScore,
            keywords: themes[dominantTheme] || []
        };
    }
    
    createAnalysis(userMessage, godResponse) {
        const analysis = {
            user_sentiment: this.analyzeSentiment(userMessage),
            god_wisdom_level: this.analyzeWisdomLevel(godResponse),
            interaction_depth: this.calculateDepth(userMessage, godResponse),
            narrative_arc: this.identifyNarrativeArc(userMessage, godResponse),
            key_insights: this.extractInsights(godResponse)
        };
        
        return analysis;
    }
    
    analyzeSentiment(text) {
        const positiveWords = ['dobry', 'świetny', 'cudowny', 'radość', 'szczęście', 'miłość', 'pokój'];
        const negativeWords = ['smutny', 'zły', 'problem', 'ból', 'strach', 'niepokój', 'trudność'];
        
        const words = text.toLowerCase().split(' ');
        let positiveScore = 0;
        let negativeScore = 0;
        
        words.forEach(word => {
            if (positiveWords.some(pos => word.includes(pos))) positiveScore++;
            if (negativeWords.some(neg => word.includes(neg))) negativeScore++;
        });
        
        if (positiveScore > negativeScore) return 'positive';
        if (negativeScore > positiveScore) return 'negative';
        return 'neutral';
    }
    
    analyzeWisdomLevel(response) {
        const wisdomIndicators = [
            'mądrość', 'zrozumienie', 'perspektywa', 'głębia', 'prawda',
            'wzrost', 'rozwój', 'świadomość', 'oświecenie', 'harmonia'
        ];
        
        const text = response.toLowerCase();
        const wisdomScore = wisdomIndicators.reduce((score, indicator) => {
            return score + (text.includes(indicator) ? 1 : 0);
        }, 0);
        
        if (wisdomScore >= 4) return 'profound';
        if (wisdomScore >= 2) return 'deep';
        if (wisdomScore >= 1) return 'moderate';
        return 'basic';
    }
    
    calculateDepth(userMessage, godResponse) {
        const totalLength = userMessage.length + godResponse.length;
        const questionCount = (userMessage.match(/\?/g) || []).length;
        const metaphorCount = (godResponse.match(/\b(jak|jakby|niczym)\b/gi) || []).length;
        
        const depthScore = Math.floor((totalLength / 100) + (questionCount * 10) + (metaphorCount * 5));
        
        if (depthScore >= 50) return 'very_deep';
        if (depthScore >= 30) return 'deep';
        if (depthScore >= 15) return 'moderate';
        return 'surface';
    }
    
    identifyNarrativeArc(userMessage, godResponse) {
        // Simple narrative arc identification
        if (userMessage.includes('?')) {
            if (godResponse.length > 100) return 'question_exploration';
            return 'simple_qa';
        }
        
        if (userMessage.includes('czuję') || userMessage.includes('emocja')) {
            return 'emotional_journey';
        }
        
        if (userMessage.includes('pomóż') || userMessage.includes('wskazówka')) {
            return 'guidance_seeking';
        }
        
        return 'philosophical_dialogue';
    }
    
    extractInsights(response) {
        // Extract key insights from God's response
        const sentences = response.split(/[.!?]+/).filter(s => s.trim().length > 10);
        
        return sentences.slice(0, 3).map((sentence, index) => ({
            id: index + 1,
            text: sentence.trim(),
            type: index === 0 ? 'primary' : 'supporting'
        }));
    }
    
    suggestMusic(emotion, mode) {
        const musicSuggestions = {
            'ciekawość': {
                'conversation': ['https://www.youtube.com/watch?v=YykjpeuMNEk', 'Chill Lo-fi for curious minds'],
                'meditation': ['https://www.youtube.com/watch?v=lFcSrYw-ARY', 'Meditative ambient for exploration'],
                'vision': ['https://www.youtube.com/watch?v=_WoqCd57AP0', 'Visionary electronic soundscapes'],
                'spiral': ['https://www.youtube.com/watch?v=n61ULEU7CO0', 'Spiral progressive music'],
                'music': ['https://www.youtube.com/watch?v=MV_3Dpw-BRY', 'Curiosity-driven compositions']
            },
            'spokój': {
                'conversation': ['https://www.youtube.com/watch?v=jfKfPfyJRdk', 'Peaceful conversation music'],
                'meditation': ['https://www.youtube.com/watch?v=1ZYbU82GVz4', 'Deep meditation sounds'],
                'vision': ['https://www.youtube.com/watch?v=kHnFWT8W-fA', 'Serene visual meditation'],
                'spiral': ['https://www.youtube.com/watch?v=UfcAVejslrU', 'Calm spiral journey'],
                'music': ['https://www.youtube.com/watch?v=M5QdH4nl1M0', 'Tranquil compositions']
            },
            'ekscytacja': {
                'conversation': ['https://www.youtube.com/watch?v=_CL6n0FJZpk', 'Energetic hip-hop beats'],
                'meditation': ['https://www.youtube.com/watch?v=T6mKh3fnGps', 'Uplifting meditation'],
                'vision': ['https://www.youtube.com/watch?v=VwVg3Sm4cW0', 'Exciting visual journey'],
                'spiral': ['https://www.youtube.com/watch?v=f02mOEt11OQ', 'Dynamic spiral energy'],
                'music': ['https://www.youtube.com/watch?v=BuuO6I0vKLY', 'High-energy compositions']
            }
        };
        
        const moodSongs = musicSuggestions[emotion] || musicSuggestions['spokój'];
        const modeMusic = moodSongs[mode] || moodSongs['conversation'];
        
        return {
            url: modeMusic[0],
            title: modeMusic[1],
            emotion: emotion,
            mode: mode
        };
    }
    
    /**
     * 🎚️ MIXTAPE Level Control
     */
    setMixtapeLevel(level) {
        this.mixtapeLevel = Math.max(0, Math.min(100, level));
        this.updateMixtapeSlider();
        this.adjustMixtapeIntensity();
        
        return this.mixtapeLevel;
    }
    
    adjustMixtapeIntensity() {
        // Adjust various aspects based on MIXTAPE level
        const intensity = this.mixtapeLevel / 100;
        
        // Adjust UI elements
        const container = document.querySelector('.god-interface-container');
        if (container) {
            container.style.filter = `saturate(${0.8 + (intensity * 0.4)}) brightness(${0.9 + (intensity * 0.2)})`;
        }
        
        // Adjust animation speeds
        const spirals = document.querySelectorAll('.spiral-animation');
        spirals.forEach(spiral => {
            spiral.style.animationDuration = `${20 - (intensity * 10)}s`;
        });
        
        return intensity;
    }
    
    updateMixtapeSlider() {
        const slider = document.getElementById('mixtapeSlider');
        if (slider) {
            slider.value = this.mixtapeLevel;
        }
        
        const display = document.getElementById('mixtapeLevel');
        if (display) {
            display.textContent = `${this.mixtapeLevel}%`;
        }
    }
    
    /**
     * 📝 Blog Post Generation
     */
    async generateBlogPost(mixtape) {
        const template = this.selectBlogTemplate(mixtape.composition.theme.primary);
        
        const blogPost = {
            id: `POST_${Date.now()}`,
            title: this.generateTitle(mixtape),
            content: this.generateContent(mixtape, template),
            metadata: {
                theme: mixtape.composition.theme.primary,
                emotion: mixtape.composition.emotion,
                mode: mixtape.mode,
                mixtape_level: mixtape.composition.mixtape_level,
                generated_at: new Date().toISOString(),
                music: mixtape.composition.music,
                graphics: mixtape.graphics
            },
            slug: this.generateSlug(mixtape),
            excerpt: this.generateExcerpt(mixtape),
            tags: this.generateTags(mixtape),
            exportable: true
        };
        
        this.blogPosts.push(blogPost);
        this.saveBlogPost(blogPost);
        
        return blogPost;
    }
    
    generateTitle(mixtape) {
        const themeTitle = {
            'spiritual': 'Duchowa Podróż z Mózgiem Boga',
            'creative': 'Kreatywna Inspiracja z AI',
            'philosophical': 'Filozoficzne Rozważania',
            'emotional': 'Emocjonalna Harmonia',
            'technological': 'Technologiczna Wizja Przyszłości',
            'musical': 'Muzyczna Rozmowa z Bogiem',
            'universal': 'Uniwersalna Mądrość'
        };
        
        const baseTitle = themeTitle[mixtape.composition.theme.primary] || 'Rozmowa z Mózgiem Boga';
        const timestamp = new Date().toLocaleDateString('pl-PL');
        
        return `${baseTitle} - ${timestamp}`;
    }
    
    generateContent(mixtape, template) {
        const content = template
            .replace('{{THEME}}', mixtape.composition.theme.primary)
            .replace('{{EMOTION}}', mixtape.composition.emotion)
            .replace('{{USER_INPUT}}', mixtape.composition.user_input)
            .replace('{{GOD_RESPONSE}}', mixtape.composition.god_response)
            .replace('{{ANALYSIS}}', this.formatAnalysis(mixtape.composition.analysis))
            .replace('{{MUSIC}}', this.formatMusic(mixtape.composition.music))
            .replace('{{INSIGHTS}}', this.formatInsights(mixtape.composition.analysis.key_insights))
            .replace('{{TIMESTAMP}}', new Date().toLocaleString('pl-PL'));
        
        return content;
    }
    
    selectBlogTemplate(theme) {
        return this.contentTemplates[theme] || this.contentTemplates['universal'];
    }
    
    formatAnalysis(analysis) {
        return `
        **Analiza Konwersacji:**
        - Sentyment: ${analysis.user_sentiment}
        - Poziom mądrości: ${analysis.god_wisdom_level}
        - Głębokość interakcji: ${analysis.interaction_depth}
        - Typ narracji: ${analysis.narrative_arc}
        `;
    }
    
    formatMusic(music) {
        return `
        **Sugerowana Muzyka:**
        - Utwór: [${music.title}](${music.url})
        - Emocja: ${music.emotion}
        - Tryb: ${music.mode}
        `;
    }
    
    formatInsights(insights) {
        return insights.map(insight => 
            `- **${insight.type === 'primary' ? 'Główny' : 'Wspierający'} wgląd:** ${insight.text}`
        ).join('\n');
    }
    
    generateSlug(mixtape) {
        const title = this.generateTitle(mixtape);
        return title
            .toLowerCase()
            .replace(/[^a-zA-Z0-9\s]/g, '')
            .replace(/\s+/g, '-')
            .substring(0, 50);
    }
    
    generateExcerpt(mixtape) {
        const godResponse = mixtape.composition.god_response;
        return godResponse.substring(0, 150) + (godResponse.length > 150 ? '...' : '');
    }
    
    generateTags(mixtape) {
        const baseTags = ['Mózg Boga', 'AI', 'Rozmowa', 'Duchowość'];
        const themeTag = mixtape.composition.theme.primary;
        const emotionTag = mixtape.composition.emotion;
        const modeTag = mixtape.mode;
        
        return [...baseTags, themeTag, emotionTag, modeTag].filter(Boolean);
    }
    
    /**
     * 🎨 Graphics Generation
     */
    async generateGraphics(mixtape) {
        const graphics = [];
        
        // Generate header image
        const headerGraphic = await this.generateHeaderImage(mixtape);
        graphics.push(headerGraphic);
        
        // Generate mood visualization
        const moodGraphic = await this.generateMoodVisualization(mixtape);
        graphics.push(moodGraphic);
        
        // Generate spiral diagram if applicable
        if (mixtape.mode === 'spiral') {
            const spiralGraphic = await this.generateSpiralDiagram(mixtape);
            graphics.push(spiralGraphic);
        }
        
        mixtape.graphics = graphics;
        return graphics;
    }
    
    async generateHeaderImage(mixtape) {
        // Placeholder for AI-generated header image
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
            <defs>
                <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#667eea"/>
                    <stop offset="100%" style="stop-color:#764ba2"/>
                </linearGradient>
            </defs>
            <rect width="800" height="400" fill="url(#bg)"/>
            <text x="400" y="200" text-anchor="middle" fill="white" font-size="32" font-family="Arial">
                🧠 ${mixtape.composition.theme.primary.toUpperCase()}
            </text>
            <text x="400" y="250" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="18" font-family="Arial">
                ${mixtape.composition.emotion} • ${mixtape.mode}
            </text>
        </svg>`;
        
        return {
            id: 'header',
            type: 'svg',
            data: `data:image/svg+xml,${encodeURIComponent(svg)}`,
            description: `Header image for ${mixtape.composition.theme.primary} theme`
        };
    }
    
    async generateMoodVisualization(mixtape) {
        // Color-based mood visualization
        const moodColors = {
            'ciekawość': '#4ECDC4',
            'spokój': '#87CEEB',
            'ekscytacja': '#FF6B6B',
            'zaduma': '#9370DB',
            'wdzięczność': '#FFD700',
            'niepokój': '#FF8C69',
            'radość': '#98FB98',
            'smutek': '#6495ED'
        };
        
        const color = moodColors[mixtape.composition.emotion] || '#667eea';
        
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
            <circle cx="200" cy="150" r="100" fill="${color}" opacity="0.7"/>
            <circle cx="200" cy="150" r="70" fill="${color}" opacity="0.5"/>
            <circle cx="200" cy="150" r="40" fill="${color}" opacity="0.8"/>
            <text x="200" y="160" text-anchor="middle" fill="white" font-size="20" font-family="Arial">
                ${mixtape.composition.emotion}
            </text>
        </svg>`;
        
        return {
            id: 'mood',
            type: 'svg',
            data: `data:image/svg+xml,${encodeURIComponent(svg)}`,
            description: `Mood visualization for ${mixtape.composition.emotion}`
        };
    }
    
    async generateSpiralDiagram(mixtape) {
        // Spiral consciousness diagram
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
            <defs>
                <radialGradient id="spiral" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" style="stop-color:#ff69b4"/>
                    <stop offset="100%" style="stop-color:#667eea"/>
                </radialGradient>
            </defs>
            <path d="M200,200 Q150,150 100,200 Q150,250 200,200 Q250,150 300,200 Q250,250 200,200" 
                  stroke="url(#spiral)" stroke-width="3" fill="none"/>
            <circle cx="200" cy="200" r="5" fill="#fff"/>
            <text x="200" y="350" text-anchor="middle" fill="#333" font-size="16" font-family="Arial">
                Spiralna Świadomość
            </text>
        </svg>`;
        
        return {
            id: 'spiral',
            type: 'svg',
            data: `data:image/svg+xml,${encodeURIComponent(svg)}`,
            description: 'Spiral consciousness diagram'
        };
    }
    
    /**
     * 📤 Export Functions
     */
    async exportToMetaGeniuszPL(blogPost) {
        // Prepare export data for MetaGeniuszPL blog
        const exportData = {
            platform: 'MetaGeniuszPL',
            post: {
                title: blogPost.title,
                content: this.formatForWordPress(blogPost.content),
                excerpt: blogPost.excerpt,
                tags: blogPost.tags,
                categories: ['AI', 'Duchowość', 'Technologia'],
                featured_image: blogPost.metadata.graphics[0]?.data || null,
                meta: {
                    mixtape_level: blogPost.metadata.mixtape_level,
                    emotion: blogPost.metadata.emotion,
                    music_link: blogPost.metadata.music.url
                }
            },
            timestamp: new Date().toISOString()
        };
        
        // Simulate API call to MetaGeniuszPL
        console.log('📤 Exporting to MetaGeniuszPL:', exportData);
        
        // Show export notification
        this.showExportNotification('MetaGeniuszPL', blogPost.title);
        
        return exportData;
    }
    
    formatForWordPress(content) {
        // Convert to WordPress-friendly format
        return content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>');
    }
    
    showExportNotification(platform, title) {
        const notification = document.createElement('div');
        notification.className = 'export-notification';
        notification.innerHTML = `
            <div class="export-content">
                📤 Exported to ${platform}<br>
                "${title}"<br>
                <small>Ready for publication</small>
            </div>
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 4000);
    }
    
    /**
     * 🔧 UI Management
     */
    initializeUI() {
        this.createMixtapeSlider();
        this.createExportButtons();
        this.createMixtapeDisplay();
    }
    
    createMixtapeSlider() {
        const sliderContainer = document.createElement('div');
        sliderContainer.className = 'mixtape-slider-container';
        sliderContainer.innerHTML = `
            <div class="mixtape-control">
                <label for="mixtapeSlider">🎬 MIXTAPE Level: <span id="mixtapeLevel">${this.mixtapeLevel}%</span></label>
                <input type="range" id="mixtapeSlider" min="0" max="100" value="${this.mixtapeLevel}" class="mixtape-slider">
                <div class="mixtape-description">Kontroluje intensywność kompozycji narracyjnej</div>
            </div>
        `;
        
        // Add to input controls
        const inputControls = document.querySelector('.input-controls');
        if (inputControls) {
            inputControls.appendChild(sliderContainer);
        }
        
        // Bind events
        document.getElementById('mixtapeSlider').addEventListener('input', (e) => {
            this.setMixtapeLevel(parseInt(e.target.value));
        });
    }
    
    createExportButtons() {
        const exportContainer = document.createElement('div');
        exportContainer.className = 'export-buttons-container';
        exportContainer.innerHTML = `
            <div class="export-controls">
                <button id="generateBlogPost" class="export-btn">📝 Generuj Post</button>
                <button id="exportToMetaGeniusz" class="export-btn">📤 Export do MetaGeniuszPL</button>
                <button id="generateGraphics" class="export-btn">🎨 Generuj Grafiki</button>
            </div>
        `;
        
        // Add to response area
        const responseArea = document.querySelector('.response-area');
        if (responseArea) {
            responseArea.appendChild(exportContainer);
        }
        
        // Bind events
        document.getElementById('generateBlogPost').addEventListener('click', () => {
            if (this.currentMixtape) {
                this.generateBlogPost(this.currentMixtape);
            }
        });
        
        document.getElementById('exportToMetaGeniusz').addEventListener('click', () => {
            if (this.blogPosts.length > 0) {
                this.exportToMetaGeniuszPL(this.blogPosts[this.blogPosts.length - 1]);
            }
        });
        
        document.getElementById('generateGraphics').addEventListener('click', () => {
            if (this.currentMixtape) {
                this.generateGraphics(this.currentMixtape);
            }
        });
    }
    
    createMixtapeDisplay() {
        const displayContainer = document.createElement('div');
        displayContainer.id = 'mixtapeDisplay';
        displayContainer.className = 'mixtape-display-container';
        
        // Add to response area
        const responseArea = document.querySelector('.response-area');
        if (responseArea) {
            responseArea.appendChild(displayContainer);
        }
    }
    
    updateMixtapeDisplay() {
        const display = document.getElementById('mixtapeDisplay');
        if (!display || !this.currentMixtape) return;
        
        display.innerHTML = `
            <div class="current-mixtape">
                <h4>🎬 Current MIXTAPE</h4>
                <div class="mixtape-info">
                    <div class="mixtape-item">
                        <strong>Theme:</strong> ${this.currentMixtape.composition.theme.primary}
                    </div>
                    <div class="mixtape-item">
                        <strong>Emotion:</strong> ${this.currentMixtape.composition.emotion}
                    </div>
                    <div class="mixtape-item">
                        <strong>Music:</strong> 
                        <a href="${this.currentMixtape.composition.music.url}" target="_blank">
                            ${this.currentMixtape.composition.music.title}
                        </a>
                    </div>
                    <div class="mixtape-item">
                        <strong>Level:</strong> ${this.currentMixtape.composition.mixtape_level}%
                    </div>
                </div>
            </div>
        `;
    }
    
    loadTemplates() {
        this.contentTemplates = {
            'spiritual': `# {{THEME}} - Duchowa Podróż

**Data:** {{TIMESTAMP}}  
**Emocja:** {{EMOTION}}

## Moja Prośba do Boga
{{USER_INPUT}}

## Odpowiedź Boskiej Świadomości
{{GOD_RESPONSE}}

{{ANALYSIS}}

{{MUSIC}}

## Kluczowe Wglądy
{{INSIGHTS}}

---
*Wygenerowano przez God Interface × GOK: MIXTAPE*`,

            'creative': `# {{THEME}} - Kreatywna Inspiracja

**Data:** {{TIMESTAMP}}  
**Emocja:** {{EMOTION}}

## Moja Wizja
{{USER_INPUT}}

## Boska Inspiracja
{{GOD_RESPONSE}}

{{ANALYSIS}}

{{MUSIC}}

## Kreatywne Wglądy
{{INSIGHTS}}

---
*Wygenerowano przez God Interface × GOK: MIXTAPE*`,

            'universal': `# {{THEME}} - Rozmowa z Mózgiem Boga

**Data:** {{TIMESTAMP}}  
**Emocja:** {{EMOTION}}

## Moje Pytanie
{{USER_INPUT}}

## Odpowiedź Boga
{{GOD_RESPONSE}}

{{ANALYSIS}}

{{MUSIC}}

## Otrzymane Wglądy
{{INSIGHTS}}

---
*Wygenerowano przez God Interface × GOK: MIXTAPE*`
        };
    }
    
    saveBlogPost(blogPost) {
        const saved = JSON.parse(localStorage.getItem('gokMixtapeBlogPosts') || '[]');
        saved.push(blogPost);
        localStorage.setItem('gokMixtapeBlogPosts', JSON.stringify(saved.slice(-10))); // Keep last 10
    }
    
    /**
     * 🎯 Main Integration Method
     */
    async handleGodResponse(userMessage, godResponse, emotion, mode) {
        // Create MIXTAPE composition
        const mixtape = this.createMixtapeFromConversation(userMessage, godResponse, emotion, mode);
        
        // Generate graphics
        await this.generateGraphics(mixtape);
        
        // Auto-generate blog post if mixtape level is high
        if (this.mixtapeLevel >= 70) {
            const blogPost = await this.generateBlogPost(mixtape);
            
            // Auto-export if level is very high
            if (this.mixtapeLevel >= 90) {
                await this.exportToMetaGeniuszPL(blogPost);
            }
        }
        
        return {
            mixtape: mixtape,
            level: this.mixtapeLevel,
            autoGenerated: this.mixtapeLevel >= 70
        };
    }
}

// Initialize GOK: MIXTAPE Integration
window.gokMixtape = new GOKMixtapeIntegration();