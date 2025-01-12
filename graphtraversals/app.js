
const canvas = document.getElementById('dfsCanvas');
const ctx = canvas.getContext('2d');

// Draw filled rectangle
ctx.fillStyle = 'blue'; // Set fill color
ctx.fillRect(50, 50, 100, 50);

// Draw rectangle border
ctx.strokeStyle = 'red'; // Set border color
ctx.strokeRect(200, 50, 100, 50);

// Clear part of the canvas
ctx.clearRect(60, 60, 30, 30); // Clears a section


console.log(ctx);










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

