/**
 * Mobile Hamburger Menu JavaScript
 */

(function() {
    'use strict';
    
    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
        initMobileMenu();
    });
    
    function initMobileMenu() {
        // Create hamburger button
        createHamburgerButton();
        
        // Create sidebar overlay
        createSidebarOverlay();
        
        // Add event listeners
        addEventListeners();
        
        // Handle window resize
        handleWindowResize();
    }
    
    function createHamburgerButton() {
        // Check if button already exists
        if (document.querySelector('.hamburger-btn')) {
            return;
        }
        
        const hamburgerBtn = document.createElement('button');
        hamburgerBtn.className = 'hamburger-btn';
        hamburgerBtn.setAttribute('aria-label', 'メニューを開く');
        hamburgerBtn.setAttribute('aria-expanded', 'false');
        
        // Create hamburger lines
        for (let i = 0; i < 3; i++) {
            const span = document.createElement('span');
            hamburgerBtn.appendChild(span);
        }
        
        // Insert button into page
        document.body.insertBefore(hamburgerBtn, document.body.firstChild);
    }
    
    function createSidebarOverlay() {
        // Check if overlay already exists
        if (document.querySelector('.sidebar-overlay')) {
            return;
        }
        
        const overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        overlay.setAttribute('aria-hidden', 'true');
        
        document.body.appendChild(overlay);
    }
    
    function addEventListeners() {
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        const sidebar = document.querySelector('.sidebar');
        const overlay = document.querySelector('.sidebar-overlay');
        const body = document.body;
        
        if (!hamburgerBtn || !sidebar || !overlay) {
            console.warn('Mobile menu elements not found');
            return;
        }
        
        // Hamburger button click
        hamburgerBtn.addEventListener('click', function(e) {
            e.preventDefault();
            toggleSidebar();
        });
        
        // Overlay click to close
        overlay.addEventListener('click', function() {
            closeSidebar();
        });
        
        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeSidebar();
            }
        });
        
        // Close sidebar when clicking navigation links (mobile only)
        const navLinks = sidebar.querySelectorAll('.nav-link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 968) {
                    closeSidebar();
                }
            });
        });
        
        // Handle focus trap when sidebar is open
        sidebar.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                trapFocus(e, sidebar);
            }
        });
    }
    
    function toggleSidebar() {
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        const sidebar = document.querySelector('.sidebar');
        const overlay = document.querySelector('.sidebar-overlay');
        const body = document.body;
        
        const isActive = sidebar.classList.contains('active');
        
        if (isActive) {
            closeSidebar();
        } else {
            openSidebar();
        }
    }
    
    function openSidebar() {
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        const sidebar = document.querySelector('.sidebar');
        const overlay = document.querySelector('.sidebar-overlay');
        const body = document.body;
        
        // Add active classes
        hamburgerBtn.classList.add('active');
        sidebar.classList.add('active');
        overlay.classList.add('active');
        body.classList.add('sidebar-open');
        
        // Update ARIA attributes
        hamburgerBtn.setAttribute('aria-expanded', 'true');
        hamburgerBtn.setAttribute('aria-label', 'メニューを閉じる');
        sidebar.setAttribute('aria-hidden', 'false');
        overlay.setAttribute('aria-hidden', 'false');
        
        // Focus first navigation link
        const firstNavLink = sidebar.querySelector('.nav-link');
        if (firstNavLink) {
            setTimeout(function() {
                firstNavLink.focus();
            }, 100);
        }
    }
    
    function closeSidebar() {
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        const sidebar = document.querySelector('.sidebar');
        const overlay = document.querySelector('.sidebar-overlay');
        const body = document.body;
        
        // Remove active classes
        hamburgerBtn.classList.remove('active');
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        body.classList.remove('sidebar-open');
        
        // Update ARIA attributes
        hamburgerBtn.setAttribute('aria-expanded', 'false');
        hamburgerBtn.setAttribute('aria-label', 'メニューを開く');
        sidebar.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('aria-hidden', 'true');
        
        // Return focus to hamburger button
        hamburgerBtn.focus();
    }
    
    function handleWindowResize() {
        window.addEventListener('resize', function() {
            // Close sidebar if window is resized to desktop size
            if (window.innerWidth > 968) {
                closeSidebar();
            }
        });
    }
    
    function trapFocus(e, container) {
        const focusableElements = container.querySelectorAll(
            'a[href], button:not([disabled]), textarea:not([disabled]), input[type="text"]:not([disabled]), input[type="radio"]:not([disabled]), input[type="checkbox"]:not([disabled]), select:not([disabled])'
        );
        
        const firstFocusable = focusableElements[0];
        const lastFocusable = focusableElements[focusableElements.length - 1];
        
        if (e.shiftKey) {
            if (document.activeElement === firstFocusable) {
                e.preventDefault();
                lastFocusable.focus();
            }
        } else {
            if (document.activeElement === lastFocusable) {
                e.preventDefault();
                firstFocusable.focus();
            }
        }
    }
    
    // Public API (if needed)
    window.MobileMenu = {
        open: openSidebar,
        close: closeSidebar,
        toggle: toggleSidebar
    };
})();