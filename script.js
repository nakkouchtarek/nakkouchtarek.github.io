
	function scaleTo1700pxWidth() {
    const desiredWidth = 1700; // The desired width you want to achieve (1700px in this case)
    const screenWidth = window.innerWidth; // Get the current screen width

    const zoomFactor = screenWidth / desiredWidth;

    // Limit the zoom factor to avoid zooming out beyond the original size of the content
    const maxZoomFactor = 1;
    const minZoomFactor = Math.min(zoomFactor, maxZoomFactor);

    // Apply the zoom level to the zoomed element
    const zoomedElement = document.getElementById("zoomedContent");
    zoomedElement.style.transform = `scale(${minZoomFactor})`;
}

// Call the function when the page loads and when the window is resized
window.onload = scaleTo1700pxWidth;
window.onresize = scaleTo1700pxWidth;