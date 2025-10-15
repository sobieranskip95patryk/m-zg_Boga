// Creator Dashboard JavaScript
document.addEventListener('DOMContentLoaded', function() {
    initializeCreatorDashboard();
    setupSidebarNavigation();
    setupDashboardInteractions();
    loadDashboardData();
});

// Initialize creator dashboard
function initializeCreatorDashboard() {
    console.log('🎤 Creator Dashboard - Initializing...');
    
    // Add animation to stats cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.animation = 'fadeIn 0.6s ease-out';
        }, index * 100);
    });
    
    // Initialize progress bars animation
    setTimeout(() => {
        animateProgressBars();
    }, 500);
}

// Setup sidebar navigation
function setupSidebarNavigation() {
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            sidebarLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get the target section
            const targetSection = this.getAttribute('href').substring(1);
            loadSection(targetSection);
        });
    });
}

// Load different sections of the dashboard
function loadSection(sectionName) {
    const mainContent = document.querySelector('.dashboard-content');
    
    switch(sectionName) {
        case 'dashboard':
            // Already loaded - just scroll to top
            mainContent.scrollTop = 0;
            break;
        case 'profile':
            loadProfileSection();
            break;
        case 'creative-rooms':
            loadCreativeRoomsSection();
            break;
        case 'marketplace':
            loadMarketplaceSection();
            break;
        case 'analytics':
            loadAnalyticsSection();
            break;
        case 'collaborations':
            loadCollaborationsSection();
            break;
        case 'tokens':
            loadTokensSection();
            break;
        case 'learning':
            loadLearningSection();
            break;
        default:
            console.log('Section not found:', sectionName);
    }
}

// Dashboard interaction functions
function setupDashboardInteractions() {
    // Quick action buttons
    setupQuickActions();
    
    // Project interactions
    setupProjectInteractions();
    
    // Stats animations
    setupStatsAnimations();
}

function setupQuickActions() {
    const quickActionBtns = document.querySelectorAll('.quick-action-btn');
    
    quickActionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const icon = this.querySelector('.action-icon');
            
            // Animation feedback
            icon.style.transform = 'scale(1.2)';
            setTimeout(() => {
                icon.style.transform = 'scale(1)';
            }, 200);
        });
    });
}

function setupProjectInteractions() {
    const projectItems = document.querySelectorAll('.project-item');
    
    projectItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.background = 'rgba(139, 92, 246, 0.05)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.background = 'transparent';
        });
    });
}

function setupStatsAnimations() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    // Animate numbers on load
    statNumbers.forEach(stat => {
        const finalValue = stat.textContent;
        if (!isNaN(parseInt(finalValue))) {
            animateStatNumber(stat, parseInt(finalValue.replace(/,/g, '')));
        }
    });
}

function animateStatNumber(element, finalNumber) {
    const duration = 2000;
    const startTime = Date.now();
    const originalText = element.textContent;
    
    function updateNumber() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentNumber = Math.floor(progress * finalNumber);
        
        // Format number with commas
        element.textContent = currentNumber.toLocaleString();
        
        if (progress < 1) {
            requestAnimationFrame(updateNumber);
        } else {
            element.textContent = originalText; // Restore original formatting
        }
    }
    
    updateNumber();
}

function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    
    progressBars.forEach(bar => {
        const targetWidth = bar.style.width;
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, 100);
    });
}

// Quick Action Functions
function openStudio() {
    showNotification('🎤 Otwieranie studia nagraniowego...', 'info');
    // Simulate loading
    setTimeout(() => {
        showNotification('Studio jest gotowe! Rozpocznij nagrywanie.', 'success');
    }, 2000);
}

function uploadTrack() {
    showNotification('⬆️ Rozpoczynam upload track...', 'info');
    // Create file input
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'audio/*';
    fileInput.onchange = function(e) {
        const file = e.target.files[0];
        if (file) {
            showNotification(`Uploading: ${file.name}`, 'info');
            simulateUpload();
        }
    };
    fileInput.click();
}

function createNFT() {
    showNotification('💎 Uruchamiam kreator NFT...', 'info');
    // Simulate NFT creation process
    setTimeout(() => {
        showNotification('NFT Creator jest gotowy!', 'success');
    }, 1500);
}

function findCollaborators() {
    showNotification('🤝 Szukam pasujących artystów...', 'info');
    setTimeout(() => {
        showNotification('Znaleziono 12 potencjalnych współpracowników!', 'success');
    }, 2000);
}

function scheduleEvent() {
    showNotification('📅 Otwieranie kalendarza eventów...', 'info');
    setTimeout(() => {
        showNotification('Kalendarz jest gotowy do planowania!', 'success');
    }, 1000);
}

function viewAnalytics() {
    showNotification('📊 Ładowanie szczegółowej analityki...', 'info');
    setTimeout(() => {
        showNotification('Analityka gotowa do przeglądania!', 'success');
    }, 1500);
}

function createNewProject() {
    showNotification('➕ Tworzenie nowego projektu...', 'info');
    
    // Simulate project creation
    setTimeout(() => {
        const newProject = {
            title: 'Nowy Projekt ' + Date.now(),
            status: 'Inicjalizacja',
            progress: 5
        };
        
        addNewProjectToList(newProject);
        showNotification('Nowy projekt został utworzony!', 'success');
    }, 1000);
}

function togglePublicView() {
    showNotification('👁️ Przełączam na widok publiczny...', 'info');
    setTimeout(() => {
        window.open('../index.html', '_blank');
    }, 500);
}

// Helper Functions
function simulateUpload() {
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 20;
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            showNotification('✅ Track został pomyślnie uploaded!', 'success');
        } else {
            showNotification(`Uploading... ${Math.floor(progress)}%`, 'info');
        }
    }, 300);
}

function addNewProjectToList(project) {
    const projectsList = document.querySelector('.projects-list');
    const newProjectHTML = `
        <div class="project-item" style="animation: fadeIn 0.5s ease-out;">
            <div class="project-info">
                <h3 class="project-title">${project.title}</h3>
                <p class="project-status">${project.status}</p>
                <div class="project-progress">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${project.progress}%"></div>
                    </div>
                    <span class="progress-text">${project.progress}% ukończenia</span>
                </div>
            </div>
            <div class="project-actions">
                <button class="btn-small">Otwórz</button>
            </div>
        </div>
    `;
    
    projectsList.insertAdjacentHTML('afterbegin', newProjectHTML);
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style the notification
    Object.assign(notification.style, {
        position: 'fixed',
        top: '2rem',
        right: '2rem',
        padding: '1rem 1.5rem',
        borderRadius: '12px',
        color: 'white',
        fontWeight: '500',
        zIndex: '1000',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease',
        maxWidth: '300px',
        wordWrap: 'break-word'
    });
    
    // Set background based on type
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
    
    // Add to page
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after delay
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

function loadDashboardData() {
    // Simulate loading real data
    console.log('📊 Loading dashboard data...');
    
    // Update stats with real-time data (simulated)
    setTimeout(() => {
        updateLiveStats();
    }, 2000);
}

function updateLiveStats() {
    // Simulate real-time updates
    const statsData = {
        followers: Math.floor(Math.random() * 100) + 2800,
        tokens: Math.floor(Math.random() * 20) + 150,
        income: Math.floor(Math.random() * 500) + 3000,
        tracks: Math.floor(Math.random() * 5) + 40
    };
    
    // Update without full page reload
    console.log('📈 Stats updated:', statsData);
}

// Section Loading Functions (placeholders for future implementation)
function loadProfileSection() {
    showNotification('👤 Ładowanie profilu artysty...', 'info');
}

function loadCreativeRoomsSection() {
    showNotification('🎵 Ładowanie kreatywnych pokoi...', 'info');
}

function loadMarketplaceSection() {
    showNotification('💎 Ładowanie marketplace...', 'info');
}

function loadAnalyticsSection() {
    showNotification('📈 Ładowanie analityki...', 'info');
}

function loadCollaborationsSection() {
    showNotification('🤝 Ładowanie współprac...', 'info');
}

function loadTokensSection() {
    showNotification('🪙 Ładowanie tokenów...', 'info');
}

function loadLearningSection() {
    showNotification('🎓 Ładowanie centrum nauki...', 'info');
}

// Mobile sidebar toggle
function toggleSidebar() {
    const sidebar = document.querySelector('.creator-sidebar');
    sidebar.classList.toggle('open');
}

// Export functions for global access
window.openStudio = openStudio;
window.uploadTrack = uploadTrack;
window.createNFT = createNFT;
window.findCollaborators = findCollaborators;
window.scheduleEvent = scheduleEvent;
window.viewAnalytics = viewAnalytics;
window.createNewProject = createNewProject;
window.togglePublicView = togglePublicView;
window.toggleSidebar = toggleSidebar;

console.log('🎤 Creator Dashboard loaded successfully!');