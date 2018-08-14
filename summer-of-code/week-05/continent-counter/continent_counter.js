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
 * @return a list of the two largest continents of the world
 */
function getTwoLargestContinents() {
  // TODO: implement function
}

/**
 * Return the average running time of the continent counter program
 * @param n size of the world input by the user
 * @return average running time of program over a thousand iterations
 */
function getAverageRunningTime(n) {
    // TODO: implement function
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



