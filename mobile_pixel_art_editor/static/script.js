const canvas = document.getElementById('pixelCanvas');
const ctx = canvas.getContext('2d');
const gridSize = 16;
const cellSize = 25;
canvas.width = gridSize * cellSize;
canvas.height = gridSize * cellSize;

let currentColor = '#000000';
let currentTool = 'pencil';
let pixels = Array(gridSize).fill().map(() => Array(gridSize).fill('#ffffff'));
let isDrawing = false;

function drawGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let y = 0; y < gridSize; y++) {
        for (let x = 0; x < gridSize; x++) {
            ctx.fillStyle = pixels[y][x];
            ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);
            ctx.strokeStyle = '#ddd';
            ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);
        }
    }
}

function drawPixel(x, y) {
    if (x < 0 || x >= gridSize || y < 0 || y >= gridSize) return;
    pixels[y][x] = currentTool === 'pencil' ? currentColor : '#ffffff';
    drawGrid();
}

function getCoords(e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    
    let clientX, clientY;
    
    if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
    } else {
        clientX = e.clientX;
        clientY = e.clientY;
    }
    
    const x = Math.floor(((clientX - rect.left) * scaleX) / cellSize);
    const y = Math.floor(((clientY - rect.top) * scaleY) / cellSize);
    return { x, y };
}

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    const { x, y } = getCoords(e);
    drawPixel(x, y);
});

canvas.addEventListener('mousemove', (e) => {
    if (!isDrawing) return;
    const { x, y } = getCoords(e);
    drawPixel(x, y);
});

canvas.addEventListener('mouseup', () => {
    isDrawing = false;
});

canvas.addEventListener('mouseleave', () => {
    isDrawing = false;
});

canvas.addEventListener('touchstart', (e) => {
    e.preventDefault();
    e.stopPropagation();
    isDrawing = true;
    const { x, y } = getCoords(e);
    drawPixel(x, y);
}, { passive: false });

canvas.addEventListener('touchmove', (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (!isDrawing) return;
    const { x, y } = getCoords(e);
    drawPixel(x, y);
}, { passive: false });

canvas.addEventListener('touchend', (e) => {
    e.preventDefault();
    e.stopPropagation();
    isDrawing = false;
}, { passive: false });

canvas.addEventListener('touchcancel', (e) => {
    e.preventDefault();
    isDrawing = false;
}, { passive: false });

document.querySelectorAll('.color-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        currentColor = btn.dataset.color;
        document.querySelectorAll('.color-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    });
    
    btn.addEventListener('touchend', (e) => {
        e.preventDefault();
        e.stopPropagation();
        currentColor = btn.dataset.color;
        document.querySelectorAll('.color-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }, { passive: false });
});

document.querySelectorAll('.tool-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        currentTool = btn.dataset.tool;
        document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    });
    
    btn.addEventListener('touchend', (e) => {
        e.preventDefault();
        e.stopPropagation();
        currentTool = btn.dataset.tool;
        document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }, { passive: false });
});

const clearBtn = document.getElementById('clearBtn');
clearBtn.addEventListener('click', (e) => {
    e.preventDefault();
    if (confirm('Очистить холст?')) {
        pixels = Array(gridSize).fill().map(() => Array(gridSize).fill('#ffffff'));
        drawGrid();
    }
});

clearBtn.addEventListener('touchend', (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (confirm('Очистить холст?')) {
        pixels = Array(gridSize).fill().map(() => Array(gridSize).fill('#ffffff'));
        drawGrid();
    }
}, { passive: false });

const downloadBtn = document.getElementById('downloadBtn');
downloadBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const link = document.createElement('a');
    link.download = 'pixel_art_' + Date.now() + '.png';
    link.href = canvas.toDataURL();
    link.click();
});

downloadBtn.addEventListener('touchend', (e) => {
    e.preventDefault();
    e.stopPropagation();
    const link = document.createElement('a');
    link.download = 'pixel_art_' + Date.now() + '.png';
    link.href = canvas.toDataURL();
    link.click();
}, { passive: false });

drawGrid();
