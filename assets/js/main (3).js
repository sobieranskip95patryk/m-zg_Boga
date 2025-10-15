// Hip-Hop Universe - Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    initializeUniverse();
    setupNavigation();
    setupModuleInteractions();
    setupAnimations();
});

// Initialize the Hip-Hop Universe platform
function initializeUniverse() {
    console.log('🧠 Hip-Hop Universe - Initializing...');
    
    // Add fade-in animation to main sections
    const sections = document.querySelectorAll('.universe-overview, .modules-section, .roadmap-section');
    sections.forEach((section, index) => {
        setTimeout(() => {
            section.classList.add('fade-in');
        }, index * 200);
    });
    
    // Initialize module cards with staggered animation
    const moduleCards = document.querySelectorAll('.module-card');
    moduleCards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 150);
    });
}

// Setup smooth navigation
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
            
            // Update active nav link
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Update active nav link on scroll
    window.addEventListener('scroll', function() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}

// Setup module interactions
function setupModuleInteractions() {
    const moduleCards = document.querySelectorAll('.module-card');
    
    // Add hover effects and click handlers
    moduleCards.forEach(card => {
        const moduleNumber = card.dataset.module;
        
        // Enhanced hover effect
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-12px) scale(1.02)';
            this.style.boxShadow = '0 20px 60px rgba(139, 92, 246, 0.3)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 8px 32px rgba(139, 92, 246, 0.1)';
        });
        
        // Add click handler for entire card
        card.addEventListener('click', function() {
            exploreModule(moduleNumber);
        });
    });
}

// Explore module functionality
function exploreModule(moduleNumber) {
    const moduleData = getModuleData(moduleNumber);
    showModuleModal(moduleData);
}

// Get detailed module data
function getModuleData(moduleNumber) {
    const modules = {
        1: {
            title: "Infrastruktura Kulturowa",
            description: "Zjednoczenie wszystkich elementów kultury hip-hopowej w jednej cyfrowej przestrzeni",
            detailedFeatures: [
                {
                    name: "Profile Artystów",
                    description: "Kompletne portfolio dla raperów, DJ-ów, producentów, tancerzy i grafficiarzy",
                    tech: "React Native, GraphQL, AI recommendation engine"
                },
                {
                    name: "Kreatywne Pokoje",
                    description: "Prywatne strefy współpracy z narzędziami do freestyle'u i produkcji beatów",
                    tech: "WebRTC, real-time collaboration, cloud recording"
                },
                {
                    name: "Centrum Edukacyjne",
                    description: "Warsztaty, mentoring i kursy prowadzone przez legendy hip-hopu",
                    tech: "Video streaming, interactive courses, progress tracking"
                },
                {
                    name: "AI Matchmaking",
                    description: "Inteligentne łączenie twórców według stylu, celów i lokalizacji",
                    tech: "Machine learning, geolocation, style analysis"
                }
            ],
            timeline: "Q1 2025 - Q2 2025",
            priority: "Wysoki",
            dependencies: ["Podstawowa infrastruktura", "System użytkowników"]
        },
        2: {
            title: "Tokenizacja i Marketplace",
            description: "Przekształcenie wartości artystycznej w realne dochody",
            detailedFeatures: [
                {
                    name: "Tokeny Artystów",
                    description: "Fani mogą inwestować w twórców jak w akcje spółek",
                    tech: "Ethereum, smart contracts, ERC-20 tokens"
                },
                {
                    name: "NFT Marketplace",
                    description: "Handel unikalnymi beatami, grafikami i merchandisem",
                    tech: "IPFS, OpenSea integration, custom marketplace"
                },
                {
                    name: "Smart Kontrakty",
                    description: "Automatyczne, przejrzyste rozliczenia między twórcami",
                    tech: "Solidity, automated royalties, escrow services"
                },
                {
                    name: "Platforma Inwestycyjna",
                    description: "Crowdfunding albumów, eventów i teledysków",
                    tech: "DeFi protocols, yield farming, governance tokens"
                }
            ],
            timeline: "Q2 2025 - Q3 2025",
            priority: "Wysoki",
            dependencies: ["Infrastruktura kulturowa", "System KYC"]
        },
        3: {
            title: "Integracja z Drift Money",
            description: "Zapewnienie stabilnego finansowania i niezależności",
            detailedFeatures: [
                {
                    name: "1% Revenue Share",
                    description: "Stały strumień dochodów z Drift Global na rozwój platformy",
                    tech: "Automated revenue distribution, smart contracts"
                },
                {
                    name: "Fundusz Edukacyjny",
                    description: "Finansowanie warsztatów, eventów i produkcji artystycznej",
                    tech: "Grant management system, milestone tracking"
                },
                {
                    name: "AI Analytics",
                    description: "Analiza trendów rynkowych i optymalizacja inwestycji",
                    tech: "Machine learning, market data analysis, predictive models"
                },
                {
                    name: "Blockchain Infrastructure",
                    description: "Transparentne i bezpieczne zarządzanie funduszami",
                    tech: "Multi-sig wallets, DAO governance, audit trails"
                }
            ],
            timeline: "Q1 2025 - ongoing",
            priority: "Krytyczny",
            dependencies: ["Drift Money API", "Legal framework"]
        },
        4: {
            title: "UI/UX i Projekt Platformy",
            description: "Intuicyjny, inkluzywny interfejs dla twórców i fanów",
            detailedFeatures: [
                {
                    name: "Dual Zone Architecture",
                    description: "Strefa twórcza (prywatna) i publiczna (dla fanów)",
                    tech: "Role-based access control, dynamic UI components"
                },
                {
                    name: "Cross-Platform Apps",
                    description: "Aplikacje mobilne i desktopowe z synchronizacją",
                    tech: "React Native, Electron, real-time sync"
                },
                {
                    name: "Community Voting",
                    description: "Społeczność decyduje które projekty trafiają do publikacji",
                    tech: "Voting smart contracts, reputation system"
                },
                {
                    name: "Live Streaming",
                    description: "Koncerty, bitwy freestyle i backstage content",
                    tech: "WebRTC, CDN distribution, interactive features"
                }
            ],
            timeline: "Q1 2025 - Q4 2025",
            priority: "Wysoki",
            dependencies: ["User research", "Design system"]
        },
        5: {
            title: "Ekspansja Globalna",
            description: "Polska jako centrum technologiczne i kulturowe",
            detailedFeatures: [
                {
                    name: "Apex Infinity HQ",
                    description: "Zarządzanie AI, blockchainem i obliczeniami kwantowymi",
                    tech: "Distributed computing, quantum-ready architecture"
                },
                {
                    name: "Lokalne Huby",
                    description: "Regionalne centra połączone z polskim HQ",
                    tech: "Microservices architecture, edge computing"
                },
                {
                    name: "Cultural Curators",
                    description: "Polscy twórcy jako mentorzy i strategicy globalni",
                    tech: "Mentorship platform, cultural exchange tools"
                },
                {
                    name: "Cultural Diplomacy",
                    description: "Polska jako serce cyfrowej kultury hip-hop",
                    tech: "International partnerships, cultural data exchange"
                }
            ],
            timeline: "Q3 2025 - Q1 2026",
            priority: "Średni",
            dependencies: ["Local infrastructure", "International partnerships"]
        },
        6: {
            title: "Governance i Społeczność",
            description: "Zaprojektowanie skalowalnej, odpornej struktury społecznej",
            detailedFeatures: [
                {
                    name: "Interaction Models",
                    description: "Testowanie zamkniętych, otwartych i hybrydowych modeli",
                    tech: "A/B testing platform, social network analysis"
                },
                {
                    name: "Membership Hierarchy",
                    description: "System zatwierdzania nowych członków przez starszych",
                    tech: "Reputation-based access, verification protocols"
                },
                {
                    name: "Feedback Loops",
                    description: "Ankiety, głosowania i adaptacyjne reguły społeczności",
                    tech: "Governance smart contracts, sentiment analysis"
                },
                {
                    name: "Creator Autonomy",
                    description: "Artyści decydują o zasadach własnych przestrzeni",
                    tech: "Modular governance, custom rule engines"
                }
            ],
            timeline: "Q2 2025 - ongoing",
            priority: "Średni",
            dependencies: ["Community research", "Governance framework"]
        }
    };
    
    return modules[moduleNumber];
}

// Show module modal with detailed information
function showModuleModal(moduleData) {
    const modal = document.getElementById('moduleModal');
    const modalContent = document.getElementById('modalContent');
    
    modalContent.innerHTML = `
        <div class="modal-header">
            <h2 style="color: #8B5CF6; margin-bottom: 1rem;">${moduleData.title}</h2>
            <p style="color: #A3A3A3; font-style: italic; margin-bottom: 2rem;">${moduleData.description}</p>
        </div>
        
        <div class="module-details">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                <div style="background: #1A1A1A; padding: 1rem; border-radius: 12px; border: 1px solid #333;">
                    <strong style="color: #EC4899;">Timeline:</strong>
                    <p style="color: #A3A3A3; margin-top: 0.5rem;">${moduleData.timeline}</p>
                </div>
                <div style="background: #1A1A1A; padding: 1rem; border-radius: 12px; border: 1px solid #333;">
                    <strong style="color: #3B82F6;">Priorytet:</strong>
                    <p style="color: #A3A3A3; margin-top: 0.5rem;">${moduleData.priority}</p>
                </div>
            </div>
            
            <h3 style="color: #FFFFFF; margin-bottom: 1rem;">Szczegółowe Funkcjonalności:</h3>
            <div style="display: grid; gap: 1rem;">
                ${moduleData.detailedFeatures.map(feature => `
                    <div style="background: linear-gradient(135deg, #1A1A1A, #2D2D2D); padding: 1.5rem; border-radius: 16px; border: 1px solid #333;">
                        <h4 style="color: #8B5CF6; margin-bottom: 0.5rem;">${feature.name}</h4>
                        <p style="color: #A3A3A3; margin-bottom: 1rem;">${feature.description}</p>
                        <div style="background: rgba(139, 92, 246, 0.1); padding: 0.75rem; border-radius: 8px; border-left: 3px solid #8B5CF6;">
                            <small style="color: #E5E7EB;"><strong>Tech Stack:</strong> ${feature.tech}</small>
                        </div>
                    </div>
                `).join('')}
            </div>
            
            <div style="margin-top: 2rem; padding: 1rem; background: rgba(139, 92, 246, 0.1); border-radius: 12px; border: 1px solid #8B5CF6;">
                <strong style="color: #8B5CF6;">Zależności:</strong>
                <p style="color: #A3A3A3; margin-top: 0.5rem;">${moduleData.dependencies.join(', ')}</p>
            </div>
        </div>
    `;
    
    modal.style.display = 'block';
    modalContent.style.animation = 'fadeIn 0.3s ease-out';
}

// Close modal
function closeModal() {
    const modal = document.getElementById('moduleModal');
    modal.style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('moduleModal');
    if (event.target == modal) {
        closeModal();
    }
}

// Setup scroll animations
function setupAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach(item => observer.observe(item));
}

// Utility functions
function animateNumber(element, finalNumber, duration = 2000) {
    const startNumber = 0;
    const startTime = Date.now();
    
    function updateNumber() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentNumber = Math.floor(progress * finalNumber);
        
        element.textContent = currentNumber;
        
        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        }
    }
    
    updateNumber();
}

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Export functions for global access
window.exploreModule = exploreModule;
window.closeModal = closeModal;
window.scrollToTop = scrollToTop;

console.log('🎵 Hip-Hop Universe loaded successfully!');