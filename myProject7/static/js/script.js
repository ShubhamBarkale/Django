// ============================================
// BlogHub - JavaScript Interactivity
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    initializeAnimations();
    initializeFormValidation();
    initializeInteractivity();
});

// ============================================
// ANIMATIONS & EFFECTS
// ============================================

function initializeAnimations() {
    // Stagger animations for post cards
    const postCards = document.querySelectorAll('.post-card');
    postCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.addEventListener('mouseenter', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = '';
            }, 10);
        });
    });

    // Scroll animations
    observeElements();

    // Button ripple effect
    addRippleEffect();

    // Auto-hide alerts
    autoHideAlerts();
}

// Intersection Observer for scroll animations
function observeElements() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.post-card, .filter-section, .form-wrapper').forEach(el => {
        observer.observe(el);
    });
}

// Ripple click effect for buttons
function addRippleEffect() {
    const buttons = document.querySelectorAll('.btn, .filter-btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                background: rgba(255, 255, 255, 0.5);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
                left: ${x}px;
                top: ${y}px;
            `;

            // Add ripple animation to stylesheet if not exists
            if (!document.querySelector('style[data-ripple]')) {
                const style = document.createElement('style');
                style.setAttribute('data-ripple', 'true');
                style.textContent = `
                    @keyframes ripple {
                        to {
                            transform: scale(4);
                            opacity: 0;
                        }
                    }
                    .btn, .filter-btn {
                        position: relative;
                        overflow: hidden;
                    }
                `;
                document.head.appendChild(style);
            }

            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });
}

// Auto-hide alert messages after 5 seconds
function autoHideAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideInDown 0.3s ease-out reverse';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
}

// ============================================
// FORM VALIDATION
// ============================================

function initializeFormValidation() {
    const forms = document.querySelectorAll('.post-form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showFormError('Please fill in all required fields correctly.');
            }
        });

        // Real-time validation for text inputs
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            input.addEventListener('input', function() {
                if (this.value.trim() !== '') {
                    this.style.borderColor = '#10b981';
                }
            });
        });
    });
}

function validateForm(form) {
    const requiredFields = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });

    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    
    if (value === '') {
        field.style.borderColor = '#ef4444';
        field.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.1)';
        return false;
    } else {
        field.style.borderColor = '#10b981';
        return true;
    }
}

function showFormError(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-error';
    alertDiv.innerHTML = `
        <span>${message}</span>
        <button class="close-btn" onclick="this.parentElement.style.display='none';">&times;</button>
    `;
    
    const form = document.querySelector('.post-form');
    form.parentElement.insertBefore(alertDiv, form);
    
    setTimeout(() => {
        alertDiv.style.animation = 'slideInDown 0.3s ease-out reverse';
        setTimeout(() => alertDiv.remove(), 300);
    }, 4000);
}

// ============================================
// INTERACTIVITY
// ============================================

function initializeInteractivity() {
    // Smooth scroll for navigation
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') {
                e.preventDefault();
            }
        });
    });

    // Confirm before delete
    const deleteLinks = document.querySelectorAll('a[href*="/delete/"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Let the link go through since we have a delete confirmation page
        });
    });

    // Enhance textarea with auto-expand
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 400) + 'px';
        });
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + E to edit (when on detail page)
        if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
            e.preventDefault();
            const editBtn = document.querySelector('a[href*="/edit/"]');
            if (editBtn) {
                editBtn.click();
            }
        }

        // Ctrl/Cmd + N to create new post
        if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
            e.preventDefault();
            const createBtn = document.querySelector('a[href*="/create/"]');
            if (createBtn) {
                createBtn.click();
            }
        }

        // Esc to go back
        if (e.key === 'Escape') {
            const backLink = document.querySelector('.back-link');
            if (backLink) {
                backLink.click();
            }
        }
    });
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Scroll to top button
function createScrollToTopButton() {
    if (document.querySelector('.scroll-to-top')) return;

    const scrollBtn = document.createElement('button');
    scrollBtn.className = 'scroll-to-top';
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #6366f1, #4f46e5);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        z-index: 99;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    `;

    document.body.appendChild(scrollBtn);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    scrollBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    scrollBtn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
    });

    scrollBtn.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
}

// Initialize scroll to top button
createScrollToTopButton();

// ============================================
// LAZY LOADING FOR IMAGES (if any)
// ============================================

function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }
}

// ============================================
// PERFORMANCE OPTIMIZATION
// ============================================

// Debounce function for resize and scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

console.log('BlogHub initialized successfully! 🚀');
