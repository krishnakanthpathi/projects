
const canvas = document.getElementById('dfsCanvas');
const ctx = canvas.getContext('2d');

const width = canvas.width;
const height = canvas.height;

const gridSize = 100;

// Calculate the number of vertical and horizontal lines based on canvas dimensions
const numVerticalLines = Math.ceil(width / gridSize);
const numHorizontalLines = Math.ceil(height / gridSize);
 
// Draw vertical lines
for (let x = 0; x <= width; x += gridSize) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 3;
    ctx.stroke();
}

// Draw horizontal lines
for (let y = 0; y <= height; y += gridSize) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 3;
    ctx.stroke();
}

// draw a lines 
// ctx.beginPath(); // Start new path
// ctx.moveTo(0, 100); // Move to starting point
// ctx.lineTo(200, 100); // Draw a line to (200, 50)
// ctx.lineTo(0, 200); // Draw another line
// ctx.strokeStyle = 'red'; // Set line color
// ctx.lineWidth = 3; // Set line width
// ctx.stroke(); // Draw the path




// // Draw filled rectangle with border
// ctx.fillStyle = 'blue'; // Set fill color
// ctx.fillRect(50, 50, 100, 50);

// // Draw rectangle border
// ctx.strokeStyle = 'red'; // Set border color
// ctx.strokeRect(200, 50, 100, 50);

// // Clear part of the canvas
// ctx.clearRect(60, 60, 30, 30); // Clears a section


// console.log(ctx);



//  Set canvas dimensions and background color , width and height of canvas

// const width = canvas.width;
// const height = canvas.height;
// console.log(width, height);
// canvas.addEventListener('mousemove', function (event) {
//     // Get canvas bounds
//     const rect = canvas.getBoundingClientRect();

//     // Calculate x, y relative to the canvas
//     const x = event.clientX - rect.left;
//     const y = event.clientY - rect.top;

//     // Display coordinates in the console
//     console.log(`Coordinates: (${x.toFixed(0)}, ${y.toFixed(0)})`);

//     // Clear canvas and show coordinates as text
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     ctx.font = "16px Arial";
//     ctx.fillText(`(${x.toFixed(0)}, ${y.toFixed(0)})`, x, y);
//     });
// ctx.fillStyle = "blue";
// ctx.fillRect(0, 300, 150, 100); // x, y, width, height

