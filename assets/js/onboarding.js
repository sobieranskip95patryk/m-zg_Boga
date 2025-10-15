// Onboarding JavaScript
let currentStep = 1;
const totalSteps = 4;
let selectedUserType = null;
let selectedSkills = [];
let walletConnected = false;

document.addEventListener('DOMContentLoaded', function() {
    initializeOnboarding();
    setupFormInteractions();
    updateProgress();
});

// Initialize onboarding
function initializeOnboarding() {
    console.log('🚀 Hip-Hop Universe Onboarding - Starting...');
    
    // Show first step
    showStep(1);
    
    // Add entrance animation
    setTimeout(() => {
        const activeStep = document.querySelector('.onboarding-step.active');
        if (activeStep) {
            activeStep.style.animation = 'fadeInUp 0.8s ease-out';
        }
    }, 100);
}

// Setup form interactions
function setupFormInteractions() {
    // Skill tag selection
    const skillTags = document.querySelectorAll('.skill-tag');
    skillTags.forEach(tag => {
        tag.addEventListener('click', function(e) {
            e.preventDefault();
            toggleSkill(this);
        });
    });
    
    // Form validation
    const usernameInput = document.getElementById('username');
    if (usernameInput) {
        usernameInput.addEventListener('input', validateUsername);
    }
    
    // Social media inputs
    const socialInputs = document.querySelectorAll('.social-inputs input');
    socialInputs.forEach(input => {
        input.addEventListener('input', validateSocialUrl);
    });
}

// Navigation functions
function nextStep() {
    if (validateCurrentStep()) {
        if (currentStep < totalSteps) {
            currentStep++;
            showStep(currentStep);
            updateProgress();
            updateNavigation();
        } else {
            // Complete onboarding
            completeOnboarding();
        }
    }
}

function previousStep() {
    if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
        updateProgress();
        updateNavigation();
    }
}

function showStep(stepNumber) {
    // Hide all steps
    const allSteps = document.querySelectorAll('.onboarding-step');
    allSteps.forEach(step => {
        step.classList.remove('active');
    });
    
    // Show current step
    const currentStepElement = document.getElementById(`step${stepNumber}`);
    if (currentStepElement) {
        currentStepElement.classList.add('active');
        
        // Add animation
        setTimeout(() => {
            currentStepElement.style.animation = 'fadeInUp 0.6s ease-out';
        }, 50);
    }
    
    // Special handling for success step
    if (stepNumber === 'Success') {
        const successStep = document.getElementById('stepSuccess');
        if (successStep) {
            successStep.classList.add('active');
            // Hide progress bar and navigation for success step
            document.querySelector('.progress-container').style.display = 'none';
            document.querySelector('.onboarding-navigation').style.display = 'none';
        }
    }
}

function updateProgress() {
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    
    if (progressFill && progressText) {
        const progressPercentage = (currentStep / totalSteps) * 100;
        progressFill.style.width = `${progressPercentage}%`;
        progressText.textContent = `Krok ${currentStep} z ${totalSteps}`;
    }
}

function updateNavigation() {
    const backButton = document.getElementById('backButton');
    
    if (backButton) {
        backButton.disabled = currentStep <= 1;
    }
}

// Step validation
function validateCurrentStep() {
    switch(currentStep) {
        case 1:
            return true; // Welcome step - no validation needed
        case 2:
            return validateUserTypeStep();
        case 3:
            return validateProfileStep();
        case 4:
            return true; // Wallet step - optional
        default:
            return true;
    }
}

function validateUserTypeStep() {
    if (!selectedUserType) {
        showNotification('Wybierz swoją rolę w Hip-Hop Universe', 'warning');
        return false;
    }
    return true;
}

function validateProfileStep() {
    const username = document.getElementById('username').value.trim();
    
    if (!username) {
        showNotification('Nazwa użytkownika jest wymagana', 'warning');
        document.getElementById('username').focus();
        return false;
    }
    
    if (username.length < 3) {
        showNotification('Nazwa użytkownika musi mieć co najmniej 3 znaki', 'warning');
        document.getElementById('username').focus();
        return false;
    }
    
    return true;
}

// User type selection
function selectUserType(type) {
    // Remove previous selection
    const userTypeCards = document.querySelectorAll('.user-type-card');
    userTypeCards.forEach(card => {
        card.classList.remove('selected');
    });
    
    // Select new type
    const selectedCard = document.querySelector(`[data-type="${type}"]`);
    if (selectedCard) {
        selectedCard.classList.add('selected');
        selectedUserType = type;
        
        // Enable continue button
        const step2Button = document.getElementById('step2Button');
        if (step2Button) {
            step2Button.disabled = false;
        }
        
        // Add selection feedback
        const icon = selectedCard.querySelector('.user-type-icon');
        icon.style.transform = 'scale(1.2)';
        setTimeout(() => {
            icon.style.transform = 'scale(1)';
        }, 200);
        
        showNotification(`Wybrano: ${getTypeName(type)}`, 'success');
    }
}

function getTypeName(type) {
    const names = {
        'artist': 'Artysta / Twórca',
        'fan': 'Fan / Kolekcjoner',
        'investor': 'Inwestor / Mentor'
    };
    return names[type] || type;
}

// Skill selection
function toggleSkill(skillElement) {
    const skill = skillElement.dataset.skill;
    
    if (skillElement.classList.contains('selected')) {
        // Deselect skill
        skillElement.classList.remove('selected');
        selectedSkills = selectedSkills.filter(s => s !== skill);
    } else {
        // Select skill
        skillElement.classList.add('selected');
        selectedSkills.push(skill);
    }
    
    // Add animation feedback
    skillElement.style.transform = 'scale(1.1)';
    setTimeout(() => {
        skillElement.style.transform = 'scale(1)';
    }, 150);
}

// Form validation functions
function validateUsername(e) {
    const username = e.target.value.trim();
    const usernameInput = e.target;
    
    // Remove previous validation classes
    usernameInput.classList.remove('valid', 'invalid');
    
    if (username.length >= 3) {
        usernameInput.classList.add('valid');
        // Check availability (simulated)
        setTimeout(() => {
            checkUsernameAvailability(username, usernameInput);
        }, 500);
    } else if (username.length > 0) {
        usernameInput.classList.add('invalid');
    }
}

function checkUsernameAvailability(username, inputElement) {
    // Simulate API call
    const isAvailable = !['admin', 'test', 'user', 'mc_test'].includes(username.toLowerCase());
    
    if (!isAvailable) {
        inputElement.classList.remove('valid');
        inputElement.classList.add('invalid');
        showNotification('Ta nazwa użytkownika jest już zajęta', 'warning');
    }
}

function validateSocialUrl(e) {
    const url = e.target.value.trim();
    const input = e.target;
    
    if (url && !isValidUrl(url)) {
        input.style.borderColor = '#EF4444';
    } else {
        input.style.borderColor = '';
    }
}

function isValidUrl(string) {
    try {
        new URL(string);
        return true;
    } catch (_) {
        return false;
    }
}

// Wallet connection
function connectWallet(walletType) {
    showNotification(`Łączenie z ${getWalletName(walletType)}...`, 'info');
    
    // Simulate wallet connection
    setTimeout(() => {
        simulateWalletConnection(walletType);
    }, 2000);
}

function getWalletName(type) {
    const names = {
        'metamask': 'MetaMask',
        'walletconnect': 'WalletConnect',
        'coinbase': 'Coinbase Wallet'
    };
    return names[type] || type;
}

function simulateWalletConnection(walletType) {
    // Simulate successful connection
    const success = Math.random() > 0.1; // 90% success rate
    
    if (success) {
        walletConnected = true;
        showNotification(`Portfel ${getWalletName(walletType)} został połączony!`, 'success');
        
        // Update wallet option UI
        const walletOption = document.querySelector(`[onclick="connectWallet('${walletType}')"]`);
        if (walletOption) {
            const status = walletOption.querySelector('.wallet-status');
            status.textContent = 'Połączono ✓';
            status.style.color = '#10B981';
            walletOption.style.borderColor = '#10B981';
        }
        
        // Enable complete button
        const completeButton = document.getElementById('completeButton');
        if (completeButton) {
            completeButton.disabled = false;
        }
    } else {
        showNotification('Nie udało się połączyć portfela. Spróbuj ponownie.', 'error');
    }
}

function skipWallet() {
    showNotification('Możesz połączyć portfel później w ustawieniach', 'info');
    
    // Enable complete button
    const completeButton = document.getElementById('completeButton');
    if (completeButton) {
        completeButton.disabled = false;
    }
}

// Onboarding completion
function completeOnboarding() {
    // Gather all user data
    const userData = gatherUserData();
    
    // Save user data (simulated)
    saveUserData(userData);
    
    // Show success step
    showStep('Success');
    
    showNotification('Konto zostało utworzone pomyślnie!', 'success');
}

function gatherUserData() {
    const formData = new FormData(document.getElementById('profileForm'));
    
    return {
        userType: selectedUserType,
        username: formData.get('username'),
        displayName: formData.get('displayName'),
        bio: formData.get('bio'),
        location: formData.get('location'),
        skills: selectedSkills,
        socials: {
            instagram: formData.get('instagram'),
            twitter: formData.get('twitter'),
            youtube: formData.get('youtube'),
            spotify: formData.get('spotify')
        },
        walletConnected: walletConnected,
        onboardingCompletedAt: new Date().toISOString()
    };
}

function saveUserData(userData) {
    // Simulate API call to save user data
    console.log('💾 Saving user data:', userData);
    
    // Store in localStorage for demo purposes
    localStorage.setItem('hhUniverse_userData', JSON.stringify(userData));
    localStorage.setItem('hhUniverse_onboarded', 'true');
}

// Navigation to other parts of the platform
function goToDashboard() {
    showNotification('Przekierowywanie do Dashboard...', 'info');
    setTimeout(() => {
        window.location.href = 'modules/04_ui_ux_platforma/creator-dashboard.html';
    }, 1000);
}

function explorePlatform() {
    showNotification('Rozpoczynam tour po platformie...', 'info');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

function skipOnboarding() {
    if (confirm('Czy na pewno chcesz pominąć onboarding? Będziesz mógł go ukończyć później.')) {
        localStorage.setItem('hhUniverse_onboardingSkipped', 'true');
        window.location.href = 'index.html';
    }
}

// Notification system (reuse from main app)
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    Object.assign(notification.style, {
        position: 'fixed',
        top: '5rem',
        right: '2rem',
        padding: '1rem 1.5rem',
        borderRadius: '12px',
        color: 'white',
        fontWeight: '500',
        zIndex: '1001',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease',
        maxWidth: '300px',
        wordWrap: 'break-word'
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

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && e.ctrlKey) {
        nextStep();
    } else if (e.key === 'Escape') {
        if (currentStep > 1) {
            previousStep();
        }
    }
});

// Export functions for global access
window.nextStep = nextStep;
window.previousStep = previousStep;
window.selectUserType = selectUserType;
window.connectWallet = connectWallet;
window.skipWallet = skipWallet;
window.completeOnboarding = completeOnboarding;
window.goToDashboard = goToDashboard;
window.explorePlatform = explorePlatform;
window.skipOnboarding = skipOnboarding;

console.log('🎵 Hip-Hop Universe Onboarding loaded successfully!');