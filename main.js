const closed = []

function selectIcon(element) {
    // Remove selection from all icons
    document.querySelectorAll('.desktop-icon').forEach(icon => {
        icon.classList.remove('selected');
    });
    
    // Add selection to clicked icon
    element.classList.add('selected');
}

document.addEventListener('DOMContentLoaded', function () {

// Make both terminal windows draggable
const terminals = document.querySelectorAll('.mac-terminal-window');
const closeButtons = document.querySelectorAll('.mac-terminal-close');



closeButtons.forEach((closeButton, index) => {
    closeButton.addEventListener('click', () => {
        const terminal = document.querySelectorAll('.mac-terminal-window')[index];
        
        terminal.style.transition = 'transform 0.5s ease-in-out'; // Apply transition
        
        // Check if terminal id is terminal3, then use translateY for movement
        if (terminal.id === 'terminal3') {
            terminal.style.transform = 'translateY(150%)'; // Move terminal off-screen vertically
            closed.push(index)
        } else {
            terminal.style.transform = 'translateX(-150%)'; // Move terminal off-screen horizontally
            closed.push(index)
        }
    });
});


});

function showTerminals() {
const terminals = document.querySelectorAll('.mac-terminal-window');

let check = false;

terminals.forEach((terminal, index) => {

    if ( closed.includes(index) )
    {
        terminal.style.transition = 'transform 0.5s ease-in-out';

        if (terminal.id === 'terminal3') {

            terminal.style.transform = 'translateY(150%)';
            
            setTimeout(() => {
                terminal.style.transform = 'translateY(0)'; 
            }, index * 100); 

        } else {
            terminal.style.transform = 'translateX(150%)';

            setTimeout(() => {
                terminal.style.transform = 'translateX(0)'; 
            }, index * 200); 
        }


        const idx = closed.indexOf(index);
        if (idx !== -1) {
            closed.splice(idx, 1);
        }

        check = true;
    }
});

if ( !check )
{
    terminals.forEach((terminal, index) => {
        terminal.style.transition = 'transform 0.5s ease-in-out'; // Apply transition
        
        // Check if terminal id is terminal3, then use translateY for movement
        if (terminal.id === 'terminal3') {
            terminal.style.transform = 'translateY(150%)'; // Move terminal off-screen vertically
            closed.push(index)
        } else {
            terminal.style.transform = 'translateX(-150%)'; // Move terminal off-screen horizontally
            closed.push(index)
        }
    });
}
}

function updateTime() {
    const now = new Date();
    document.getElementById('current-time').textContent = now.toLocaleTimeString();
}
setInterval(updateTime, 1000);
updateTime();

// Blog functionality
const browserWindow = document.querySelector('.browser-window');
const browserFrame = document.getElementById('browser-frame');
const addressBar = document.getElementById('address-bar');
const backButton = document.getElementById('back-button');
const forwardButton = document.getElementById('forward-button');
const refreshButton = document.getElementById('refresh-button');

document.querySelector('#blog').parentElement.addEventListener('click', () => {
browserWindow.style.display = 'flex';
loadPage('blog.html');
});

document.querySelector('#projects').parentElement.addEventListener('click', () => {
browserWindow.style.display = 'flex';
loadPage('projects.html');
});

document.querySelector('.browser-close').addEventListener('click', () => {
browserWindow.style.display = 'none';
});

function loadPage(url) {
browserFrame.src = url;
addressBar.textContent = url;
}

browserFrame.addEventListener('load', () => {
// Update address bar when iframe navigation occurs
try {
    addressBar.textContent = browserFrame.contentWindow.location.href;
} catch(e) {
    console.error('Cannot access iframe location:', e);
}
});

backButton.addEventListener('click', () => browserFrame.contentWindow.history.back());
forwardButton.addEventListener('click', () => browserFrame.contentWindow.history.forward());
refreshButton.addEventListener('click', () => browserFrame.contentWindow.location.reload());

function adjustZoom() {
const baseWidth = 1920; 
const baseHeight = 955;
const screenWidth = window.innerWidth;
const screenHeight = window.innerHeight;

// Calculate scale factor
const scaleX = screenWidth / baseWidth;
const scaleY = screenHeight / baseHeight;
const scale = Math.min(scaleX, scaleY); // Keep aspect ratio

// Apply zoom
document.body.style.transform = `scale(${scale})`;
document.body.style.transformOrigin = "top left"; // Adjust origin to avoid cutoff
document.body.style.width = `${baseWidth}px`; // Prevent content from shrinking
document.body.style.height = `${baseHeight}px`;
}

// Function to detect mobile devices
function redirectToMobile() {
if (window.innerWidth <= 800) { // You can adjust this threshold based on your needs
    window.location.href = "mobile.html";
}
}
// Redirect when the page loads
window.onload = redirectToMobile;

adjustZoom();
window.addEventListener("resize", adjustZoom);

