// Hamburger Menu Functionality
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.book-sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    const body = document.body;
    
    if (!sidebarToggle || !sidebar) {
        console.warn('Sidebar toggle or sidebar element not found');
        return;
    }
    
    // Toggle sidebar function
    function toggleSidebar() {
        const isActive = sidebar.classList.contains('active');
        
        if (isActive) {
            closeSidebar();
        } else {
            openSidebar();
        }
    }
    
    // Open sidebar
    function openSidebar() {
        sidebar.classList.add('active');
        if (overlay) {
            overlay.classList.add('active');
        }
        sidebarToggle.setAttribute('aria-expanded', 'true');
        body.style.overflow = 'hidden'; // Prevent scrolling when sidebar is open
    }
    
    // Close sidebar
    function closeSidebar() {
        sidebar.classList.remove('active');
        if (overlay) {
            overlay.classList.remove('active');
        }
        sidebarToggle.setAttribute('aria-expanded', 'false');
        body.style.overflow = ''; // Restore scrolling
    }
    
    // Event listeners
    sidebarToggle.addEventListener('click', toggleSidebar);
    
    // Close sidebar when clicking overlay
    if (overlay) {
        overlay.addEventListener('click', closeSidebar);
    }
    
    // Close sidebar when clicking a link (mobile only)
    const navLinks = sidebar.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                closeSidebar();
            }
        });
    });
    
    // Handle escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && sidebar.classList.contains('active')) {
            closeSidebar();
        }
    });
    
    // Handle window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (window.innerWidth > 768) {
                // Remove mobile-specific classes on desktop
                sidebar.classList.remove('active');
                if (overlay) {
                    overlay.classList.remove('active');
                }
                body.style.overflow = '';
            }
        }, 250);
    });
    
    // Add active class to current page in navigation
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-link');
    
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href && currentPath.includes(href)) {
            item.classList.add('active');
        }
    });
});

// Theme toggle functionality (if not already implemented)
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.querySelector('.theme-toggle');
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }
});