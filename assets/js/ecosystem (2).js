// Ecosystem Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    initializeEcosystem();
    setupAnimations();
    setupInteractions();
    startStatsCounter();
});

// Initialize ecosystem page
function initializeEcosystem() {
    console.log('🧠 Hip-Hop Universe Ecosystem - Initializing...');
    
    // Add entrance animations
    setTimeout(() => {
        addEntranceAnimations();
    }, 500);
    
    // Setup intersection observer for scroll animations
    setupScrollAnimations();
}

// Add entrance animations
function addEntranceAnimations() {
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.style.animation = 'fadeInUp 1s ease-out';
    }
    
    // Animate platform cards with stagger
    const platformCards = document.querySelectorAll('.platform-card');
    platformCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.animation = 'fadeIn 0.8s ease-out';
        }, index * 200);
    });
}

// Setup scroll animations
function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                
                // Special handling for stats
                if (entry.target.classList.contains('stat-number')) {
                    animateStatNumber(entry.target);
                }
            }
        });
    }, observerOptions);
    
    // Observe various elements
    const elementsToObserve = document.querySelectorAll(`
        .flow-step,
        .stat-card,
        .user-type-card,
        .roadmap-quarter,
        .milestone
    `);
    
    elementsToObserve.forEach(el => observer.observe(el));
}

// Setup interactions
function setupInteractions() {
    // Platform card interactions
    setupPlatformCards();
    
    // User type card interactions
    setupUserTypeCards();
    
    // Flow step interactions
    setupFlowSteps();
    
    // Button interactions
    setupButtons();
}

function setupPlatformCards() {
    const platformCards = document.querySelectorAll('.platform-card');
    
    platformCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // Enhanced hover effect
            this.style.transform = 'translateY(-12px) scale(1.02)';
            
            // Add glow effect based on platform type
            const platform = this.dataset.platform;
            switch(platform) {
                case 'hhu':
                    this.style.boxShadow = '0 20px 60px rgba(139, 92, 246, 0.3)';
                    break;
                case 'drift':
                    this.style.boxShadow = '0 20px 60px rgba(16, 185, 129, 0.3)';
                    break;
                case 'portfolio':
                    this.style.boxShadow = '0 20px 60px rgba(59, 130, 246, 0.3)';
                    break;
                case 'rocket':
                    this.style.boxShadow = '0 20px 60px rgba(236, 72, 153, 0.3)';
                    break;
            }
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '';
        });
        
        // Click handling
        card.addEventListener('click', function() {
            const platform = this.dataset.platform;
            if (platform) {
                explorePlatform(platform);
            }
        });
    });
}

function setupUserTypeCards() {
    const userTypeCards = document.querySelectorAll('.user-type-card');
    
    userTypeCards.forEach(card => {
        card.addEventListener('click', function() {
            // Remove active class from all cards
            userTypeCards.forEach(c => c.classList.remove('active'));
            
            // Add active class to clicked card
            this.classList.add('active');
            
            // Add selection animation
            const icon = this.querySelector('.user-type-icon');
            if (icon) {
                icon.style.transform = 'scale(1.2)';
                setTimeout(() => {
                    icon.style.transform = 'scale(1)';
                }, 300);
            }
            
            // Show selection feedback
            const userType = this.classList.contains('creator') ? 'Creator' :
                           this.classList.contains('muse') ? 'Muse' :
                           this.classList.contains('fan') ? 'Fan' : 'Investor';
            
            showNotification(`Wybrano ścieżkę: ${userType}`, 'success');
        });
    });
}

function setupFlowSteps() {
    const flowSteps = document.querySelectorAll('.flow-step');
    
    flowSteps.forEach((step, index) => {
        step.addEventListener('mouseenter', function() {
            // Highlight the step and its connectors
            this.style.transform = 'translateY(-5px)';
            
            // Animate step number
            const stepNumber = this.querySelector('.step-number');
            if (stepNumber) {
                stepNumber.style.transform = 'scale(1.1)';
                stepNumber.style.background = 'var(--gradient-main)';
            }
        });
        
        step.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            
            const stepNumber = this.querySelector('.step-number');
            if (stepNumber) {
                stepNumber.style.transform = 'scale(1)';
                stepNumber.style.background = 'var(--primary-purple)';
            }
        });
    });
}

function setupButtons() {
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('button[class*="btn-"]');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            createRippleEffect(e, this);
        });
    });
}

// Stats counter animation
function startStatsCounter() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                animateStatNumber(entry.target);
                entry.target.dataset.animated = 'true';
            }
        });
    }, observerOptions);
    
    statNumbers.forEach(stat => observer.observe(stat));
}

function animateStatNumber(element) {
    const target = parseInt(element.dataset.target);
    const duration = 2000;
    const startTime = Date.now();
    
    function updateNumber() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const currentNumber = Math.floor(easeOutQuart * target);
        
        // Format number with appropriate suffix
        element.textContent = formatStatNumber(currentNumber);
        
        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        } else {
            element.textContent = formatStatNumber(target);
        }
    }
    
    updateNumber();
}

function formatStatNumber(number) {
    if (number >= 1000000) {
        return (number / 1000000).toFixed(1) + 'M';
    } else if (number >= 1000) {
        return (number / 1000).toFixed(0) + 'K';
    }
    return number.toLocaleString();
}

// Navigation functions
function startJourney() {
    showNotification('🚀 Rozpoczynamy podróż po ekosystemie...', 'info');
    
    // Smooth scroll to platform integration
    const targetSection = document.querySelector('.platform-integration');
    if (targetSection) {
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function exploreEcosystem() {
    showNotification('🌐 Eksploracja ekosystemu...', 'info');
    
    // Scroll to user types section
    const targetSection = document.querySelector('.user-types');
    if (targetSection) {
        targetSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function explorePlatform(platform) {
    const platformNames = {
        'hhu': 'Hip-Hop Universe',
        'drift': 'Drift Money',
        'portfolio': 'Portfolio+',
        'rocket': 'Rocket Fuell Girls'
    };
    
    const platformName = platformNames[platform] || platform;
    showNotification(`🎵 Eksploracja ${platformName}...`, 'info');
    
    // Simulate navigation to platform
    setTimeout(() => {
        switch(platform) {
            case 'hhu':
                window.open('index.html', '_blank');
                break;
            case 'drift':
                showNotification('💰 Drift Money - Wkrótce!', 'info');
                break;
            case 'portfolio':
                showNotification('🎨 Portfolio+ - W rozwoju!', 'info');
                break;
            case 'rocket':
                showNotification('💎 Rocket Fuell Girls - Coming Soon!', 'info');
                break;
        }
    }, 1000);
}

function selectUserJourney(userType) {
    const userTypeNames = {
        'creator': 'Creator/Artist',
        'muse': 'Muse/Model',
        'fan': 'Fan/Collector',
        'investor': 'Investor/Mentor'
    };
    
    const typeName = userTypeNames[userType] || userType;
    showNotification(`✨ Wybrano ścieżkę: ${typeName}`, 'success');
    
    // Show relevant onboarding path
    setTimeout(() => {
        showUserJourneyModal(userType);
    }, 500);
}

function showUserJourneyModal(userType) {
    // Create modal with user journey details
    const modal = document.createElement('div');
    modal.className = 'user-journey-modal';
    modal.innerHTML = getUserJourneyContent(userType);
    
    document.body.appendChild(modal);
    
    // Show modal with animation
    setTimeout(() => {
        modal.classList.add('active');
    }, 100);
    
    // Close modal functionality
    modal.addEventListener('click', function(e) {
        if (e.target === modal || e.target.classList.contains('modal-close')) {
            modal.classList.remove('active');
            setTimeout(() => {
                document.body.removeChild(modal);
            }, 300);
        }
    });
}

function getUserJourneyContent(userType) {
    const journeys = {
        creator: {
            title: '🎤 Creator/Artist Journey',
            description: 'Twoja ścieżka w ekosystemie jako twórca',
            steps: [
                'Stwórz profil artysty w Hip-Hop Universe',
                'Uploaduj swoje utwory i otrzymaj tokeny',
                'Znajdź collaboratorów przez AI matchmaking',
                'Monetyzuj talent przez Drift Money',
                'Buduj portfolio w Portfolio+',
                'Rozwijaj fanbase i inwestorów'
            ],
            platforms: ['HHU', 'Drift', 'Portfolio+']
        },
        muse: {
            title: '💎 Muse/Model Journey',
            description: 'Redefiniuj kobiecą siłę w hip-hop',
            steps: [
                'Wybierz archetyp w Rocket Fuell Girls',
                'Stwórz Style Portfolio z NFT',
                'Współpracuj z artystami HHU',
                'Otrzymuj DRT za stylizacje',
                'Buduj community i influence',
                'Twórz unikalne kolekcje NFT'
            ],
            platforms: ['Rocket', 'HHU', 'Portfolio+', 'Drift']
        },
        fan: {
            title: '❤️ Fan/Collector Journey',
            description: 'Inwestuj w kulturę i twórców',
            steps: [
                'Dołącz do społeczności fanów',
                'Inwestuj w tokenizowanych artystów',
                'Kolekcjonuj unikalne NFT',
                'Głosuj nad projektami artystów',
                'Otrzymuj exclusive content',
                'Zarządzaj portfolio inwestycji'
            ],
            platforms: ['Drift', 'Portfolio+', 'HHU']
        },
        investor: {
            title: '💼 Investor/Mentor Journey',
            description: 'Wspieraj talenty i rozwijaj ecosystem',
            steps: [
                'Analizuj talenty w Portfolio+',
                'Inwestuj w perspektywicznych artystów',
                'Oferuj mentoring i wsparcie',
                'Zarządzaj portfolio talentów',
                'Otrzymuj ROI z sukcesów artystów',
                'Rozwijaj ecosystem przez partnerships'
            ],
            platforms: ['Portfolio+', 'Drift', 'HHU']
        }
    };
    
    const journey = journeys[userType];
    
    return `
        <div class="modal-content">
            <button class="modal-close">&times;</button>
            <div class="journey-header">
                <h2>${journey.title}</h2>
                <p>${journey.description}</p>
            </div>
            <div class="journey-steps">
                <h3>Twoja ścieżka w ekosystemie:</h3>
                <ol>
                    ${journey.steps.map(step => `<li>${step}</li>`).join('')}
                </ol>
            </div>
            <div class="journey-platforms">
                <h4>Używane platformy:</h4>
                <div class="platform-badges">
                    ${journey.platforms.map(platform => `<span class="platform-badge">${platform}</span>`).join('')}
                </div>
            </div>
            <div class="journey-actions">
                <button class="btn-primary" onclick="startOnboarding('${userType}')">
                    Rozpocznij Teraz
                </button>
                <button class="btn-secondary modal-close">
                    Później
                </button>
            </div>
        </div>
    `;
}

function startOnboarding(userType = null) {
    showNotification('🚀 Przekierowywanie do onboarding...', 'info');
    
    let onboardingUrl = 'onboarding.html';
    if (userType) {
        onboardingUrl += `?type=${userType}`;
    }
    
    setTimeout(() => {
        window.location.href = onboardingUrl;
    }, 1000);
}

function learnMore() {
    showNotification('📖 Otwieranie dokumentacji...', 'info');
    setTimeout(() => {
        window.open('ECOSYSTEM_MANIFEST.md', '_blank');
    }, 500);
}

// Utility functions
function createRippleEffect(event, element) {
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    const ripple = document.createElement('div');
    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        left: ${x}px;
        top: ${y}px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        transform: scale(0);
        animation: ripple 0.6s ease-out;
        pointer-events: none;
        z-index: 1;
    `;
    
    element.style.position = 'relative';
    element.style.overflow = 'hidden';
    element.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `ecosystem-notification notification-${type}`;
    notification.textContent = message;
    
    Object.assign(notification.style, {
        position: 'fixed',
        top: '2rem',
        right: '2rem',
        padding: '1rem 1.5rem',
        borderRadius: '12px',
        color: 'white',
        fontWeight: '500',
        zIndex: '10000',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease',
        maxWidth: '350px',
        wordWrap: 'break-word',
        boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)'
    });
    
    switch(type) {
        case 'success':
            notification.style.background = 'linear-gradient(135deg, #10B981, #059669)';
            break;
        case 'error':
            notification.style.background = 'linear-gradient(135deg, #EF4444, #DC2626)';
            break;
        case 'warning':
            notification.style.background = 'linear-gradient(135deg, #F59E0B, #D97706)';
            break;
        default:
            notification.style.background = 'linear-gradient(135deg, #8B5CF6, #7C3AED)';
    }
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 4000);
}

// CSS for modal and animations
const modalCSS = `
    .user-journey-modal {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(5px);
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
        padding: 2rem;
    }
    
    .user-journey-modal.active {
        opacity: 1;
    }
    
    .user-journey-modal .modal-content {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        padding: 2rem;
        max-width: 500px;
        width: 100%;
        position: relative;
        transform: translateY(20px);
        transition: transform 0.3s ease;
    }
    
    .user-journey-modal.active .modal-content {
        transform: translateY(0);
    }
    
    .modal-close {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: none;
        border: none;
        color: var(--text-secondary);
        font-size: 1.5rem;
        cursor: pointer;
        width: 2rem;
        height: 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: all 0.3s ease;
    }
    
    .modal-close:hover {
        background: rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
    }
    
    .journey-header h2 {
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .journey-header p {
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
    
    .journey-steps h3 {
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .journey-steps ol {
        color: var(--text-secondary);
        margin-bottom: 2rem;
        padding-left: 1.5rem;
    }
    
    .journey-steps li {
        margin-bottom: 0.5rem;
        line-height: 1.4;
    }
    
    .journey-platforms h4 {
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    .platform-badges {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    
    .platform-badges .platform-badge {
        background: rgba(139, 92, 246, 0.2);
        color: var(--primary-purple);
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .journey-actions {
        display: flex;
        gap: 1rem;
        justify-content: center;
    }
    
    @keyframes ripple {
        to {
            transform: scale(2);
            opacity: 0;
        }
    }
`;

// Add modal CSS to document
const styleSheet = document.createElement('style');
styleSheet.textContent = modalCSS;
document.head.appendChild(styleSheet);

// Export functions for global access
window.startJourney = startJourney;
window.exploreEcosystem = exploreEcosystem;
window.explorePlatform = explorePlatform;
window.selectUserJourney = selectUserJourney;
window.startOnboarding = startOnboarding;
window.learnMore = learnMore;

console.log('🌐 Hip-Hop Universe Ecosystem loaded successfully!');