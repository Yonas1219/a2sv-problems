'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(arr) {

    let swapCount = 0;
    
for (let i = 0; i < arr.length - 1; i+=1) {
    for (let k = 0; k < arr.length - 1; k+=1) {
        if (arr[k] > arr[k + 1]) {
           const temp = arr[k];
           arr[k] = arr[k + 1];
           arr[k + 1] = temp;
           swapCount +=1;
        }
    }
    
}
console.log(`Array is sorted in ${swapCount} swaps.`);
console.log(`First Element: ${arr[0]}`);
console.log(`Last Element: ${arr[arr.length - 1]}`); 
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
