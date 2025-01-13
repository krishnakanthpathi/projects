

// drawing canvas
function generateGraph( ) {
    const graph = {} ; // graph

    // Clear canvas
    const rowsInput = document.getElementById('rows').value;
    const colsInput = document.getElementById('cols').value;
    const algorithm = document.getElementById('algorithm').value;

    const dfsDiv = document.getElementsByClassName("dfsCanvas")[0]; 
    const bfsDiv = document.getElementsByClassName("bfsCanvas")[0]; 
    const canvas = document.getElementById(algorithm);
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    if (algorithm == "dfsCanvas") {
        dfsDiv.classList.remove("d-none")
        bfsDiv.classList.add("d-none")
    }else{
        dfsDiv.classList.add("d-none")
        bfsDiv.classList.remove("d-none")        
    }

    const rows = parseInt(rowsInput, 10) || 6; // Default to 3 if input is invalid
    const cols = parseInt(colsInput, 10) || 6; // Default to 3 if input is invalid

    const gridSizeX = width / cols;
    const gridSizeY = height / rows;

    for (let i = 0; i < rows; i++) {
        for(let j = 0 ; j < cols ; j++){
            let node = i*cols + j ;
            graph[node] = [] ;
            if (i > 0) graph[node].push((i - 1) * cols + j); // up
            if (i < rows - 1) graph[node].push((i + 1) * cols + j); // down
            if (j > 0) graph[node].push(i * cols + (j - 1)); // left
            if (j < cols - 1) graph[node].push(i * cols + (j + 1)); // right
        }
    }
    // Draw vertical lines
    for (let x = 0; x <= width; x += gridSizeX) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    // Draw horizontal lines
    for (let y = 0; y <= height; y += gridSizeY) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    const bfstraversal = bfs(graph , 0);
    const dfstraversal = dfs(graph , 0);
    const traversal = algorithm == "dfsCanvas" ? dfstraversal : bfstraversal ;

    traversal.forEach((element , idx) => {
        setTimeout(() => {
                const r = Math.floor(element / cols);
                const c = element % cols;
                console.log(r , c )
                ctx.moveTo(r , c);
                ctx.fillRect( r * gridSizeX , c * gridSizeY   , gridSizeX , gridSizeY);
        } , 100*idx);
    });


}



function dfs(graph , start) {
    const stack = [start];
    const visited = new Set();
    const order = [];

    while (stack.length > 0) {
        const node = stack.pop();
        if (!visited.has(node)) {
            visited.add(node);
            order.push(node);
            graph[node].forEach(neighbor => {
                if (!visited.has(neighbor)) {
                    stack.push(neighbor);
                }
            });
        }
    }
    return order;
}

function bfs(graph , start) {
    const queue = [start];
    const visited = new Set();
    const order = [];

    while (queue.length > 0) {
        const node = queue.shift();
        if (!visited.has(node)) {
            visited.add(node);
            order.push(node);
            graph[node].forEach(neighbor => {
                if (!visited.has(neighbor)) {
                    queue.push(neighbor);
                }
            });
        }
    }
    return order;
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

