// Global variables
let size = 0;
let world = [];
let worldStr = '';
let tilesQueue = [];
let largestContinents = {};
let averageRunningTime = 0.0;

/**
 * Main entry point for our continent counter challenge
 */
function main() {

  document.getElementById('sizeInput').disabled = true;
  document.getElementById('submitButton').disabled = true;

  let worldStr = '';
  let largestContinentsStr = '';
  let benchmarkStr = '';

  let result = function () {
      // TODO: use promises to solve the continent counter challenge
  };

  // generate world of size input by the user
  world = generateRandomWorld(size);

  // get a string representation of the previously (randomly) generated world
  worldStr = getWorldAsString();

  // compute the two largest continents from the world
  largestContinents = getTwoLargestContinents();

  // benchmark: measure average time taken by program to run over a thousand iterations
  averageRunningTime = getAverageRunningTime(size);

  // unhide computation results components
  document.getElementById('continentCounter').hidden = false;
  document.getElementById('generatedWorld').innerText = "Generated World is:\n" + worldStr;
  document.getElementById('largestContinents').innerText = "The two largest continents are: ";
  document.getElementById('benchmark').innerText = "Average running time is: ";
}

/**
 * Check user input for world size
 */
/* jslint node:true, unused:false */
// noinspection JSUnusedGlobalSymbols
function checkUserInput() {
    // retrieve the size of world to generate
    let world_size = document.getElementById('sizeInput').value;
    size = parseInt(world_size);

    if (isNaN(size) || (size < 1)) {
        // should the user input be "illegal":
        document.getElementById('errorLabel').innerText = "Please, enter valid positive number!";
        document.getElementById('submitButton').disabled = true;
        size = 0;
        return;
    }

    // when the user's input is correct
    document.getElementById('errorLabel').innerText = "";
    document.getElementById('submitButton').disabled = false;
}

/**
 * Randomly generate a world of size n
 * @param n size of the world to generate
 * @return any[] randomly generated world
 */
function generateRandomWorld(n) {
    let grid = [];
    for (let i = 0; i < n; i++) {
        let line = [];
        for (let j = 0; j < n; j++) {
            // generate a random integer value between 0 and 1
            line[j] = Math.floor(Math.random() * 2);
        }
        grid[i] = line;
    }
    return grid;
}

/**
 * Return a string representation of the generated world (grid)
 */
function getWorldAsString() {
    let griddStr = '\t[';
    let n = world.length;
    for (let i = 0; i < n; i++) {
        if (i !== 0) {
          griddStr += '\t ' + world[i];
        } else {
          griddStr += world[i];
        }
        if (i !== n - 1) {
          griddStr += '\n';
        }
    }
    griddStr += ']';
    return griddStr;
}

/**
 * Return the two largest continents of a generated world
 * @return a map of the two largest continents of the world
 */
function getTwoLargestContinents() {
    let continents = getAllContinentsSizes();
    let sortedContinents = new Map([...continents.entries()].sort(
        (a, b) => b[1] - a[1]
    ));

    let counter = 0;
    let result = {};

    // choose the two largest continents
    if (sortedContinents.size > 2) {
        sortedContinents.forEach((key, value) => {
            if (counter < 1) {
                result.set(key, value);
                counter++;
            }
        });
    } else {
        // or return all continents when their count is less or equal to 2
        result = sortedContinents;
    }
    return result;
}

/**
 * Return the average running time of the continent counter program
 * @param n size of the world input by the user
 * @return number running time of program over a thousand iterations
 */
function getAverageRunningTime(n) {
    let total_time = 0;
    let iterations = 1000;
    for (let i = 0; i < iterations; i++) {
        let start = performance.now();
        world = generateRandomWorld(n);
        getAllContinentsSizes();
        total_time = performance.now() - start;
    }
    return total_time/iterations;
}

/**
 * (Re)Initialize global variables
 */
function initialize() {
    // (re)initialize global variables
    size = 0;
    world = [];
    worldStr = '';
    tilesQueue = [];
    largestContinents = {};
    averageRunningTime = 0.0;

    // (re)initialize HTML components to dispaly results
    document.getElementById('sizeInput').disabled = false;
    document.getElementById('sizeInput').innerHTML = '';
    document.getElementById('submitButton').disabled = false;

    document.getElementById('generatedWorld').innerText = "";
    document.getElementById('largestContinents').innerText = "";
    document.getElementById('benchmark').innerText = "";
    document.getElementById('continentCounter').hidden = true;
}

// noinspection JSClosureCompilerSyntax
/**
 * Given the generated world, compute all of its continents sizes
 * @return Map<any, any> continents sizes
 */
function getAllContinentsSizes() {
    let counter = 0;
    let result = new Map();
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (world[i][j] === 1) {
                counter++;
                let contSize = getContinentSize([i, j]);
                result.set(counter.toString(), contSize);
            }
        }
    }
    return result;
}

/**
 * Return the size of the continent which the start position is part of
 * @param startPosition starting position is an array of indices
 * @return number continent size around the input starting position
 */
function getContinentSize(startPosition) {
    let continent_size = 0;
    let n = world.length;

    // startPosition is an array of indices on the grid
    let row = startPosition[0];
    let col = startPosition[1];

    // make sure the starting position is inside the world bounds
    if ((row >= 0) && (row < n) && (col >= 0) && (col < n)) {
        // start exploring from the input starting position
        tilesQueue.push(startPosition);

        while (tilesQueue.length > 0) {
            let tile = tilesQueue.pop();
            let i = tile[0]; let j = tile[1];
            if (world[i][j] === 1) {
                continent_size += 1;
                // mark this element as "already treated"
                world[i][j] = 0;
                // explore this "element/tile" neighbours
                checkNeighbours(tile);
            }
        }
    }
    return continent_size;
}

/**
 * Check if the neighbouring tiles have a desired value (1 in this case)
 * and add them to our global variable tilesQueue so they can be explored later
 * @param tile input tile as an array of indices
 */
function checkNeighbours(tile) {
    let row = tile[0]; let col = tile[1]; let n = world.length;

    /* The exploration zone is a 3x3 square centered at the input tile.
     * Therefore, row-wise, we start exploring from (row - 1) to (row + 1) included.
     * And, column-wise, we'll also explore from (col - 1) to (col + 1) included.
     */
    for (let i = (row - 1); i <= (row + 1); i++) {
        // make sure we're still inside the world/grid's bounds
        if ((i >= 0) && (i < n)) {
            for (let j = (col - 1); j <= (col + 1); i++) {
                // make sure we're still inside the world/grid's bounds
                if ((j >= 0) && (j < n)) {
                    // check the tile's value
                    if (world[i][j] === 1) {
                        // push the current tile (grid position) onto the queue
                        tilesQueue.push([i, j]);
                    }
                }
            }
        }
    }
}



