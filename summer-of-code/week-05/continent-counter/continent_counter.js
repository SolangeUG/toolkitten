// Global variables
let world = [];
let tilesQueue = [];
let largestContinents = {};
let averageRunningTime = 0.0;

/**
 * Main entry point for our continent counter challenge
 */
function main() {

  // make sure to (re)initialize global variables
  initialize();

  // retrieve the size of world to generate
  let world_size = document.getElementById('sizeInput').innerText;
  let size = parseInt(world_size);
  if (isNaN(size)) {
    document.getElementById('errorLabel').innerText = "Please, enter valid positive number!";
  }

  // generate world of size input by the user
  world = generateRandomWorld(size);

  // display the previously (randomly) generated world
  displayWorld();

  // compute the two largest continents from the world
  largestContinents = getTwoLargestContinents();
  console.log("Two largest continents:", largestContinents);

  // benchmark: measure average time taken by program to run over a thousand iterations
  averageRunningTime = getAverageRunningTime(size);
  console.log("Average running time:", averageRunningTime);

}

/**
 * Randomly generate a world of size n
 * @param n size of the world to generate
 * @return a randomly generated world
 */
function generateRandomWorld(n) {
  // TODO: implement function
  console.log("Tiles queue:", tilesQueue)
}

/**
 * Display the generated world (grid)
 */
function displayWorld() {
  // TODO: implement function
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
  world = [];
  tilesQueue = [];
  largestContinents = {};
  averageRunningTime = 0.0;
}



