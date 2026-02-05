function cube(n) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let z = 0; z < n; z++) {
        console.log(i, j, z);
      }
    }
  }
}

// cube(4);

function logFuncRecursive(n) {
  if (n === 0) return "Done";
  n = Math.floor(n / 2);
  return logFunc(n);
}

function logFunc(n) {
  while (n > 1) {
    n = Math.floor(n / 2);
  }
  return "Done";
}

let arr = [];
let start = 0;
let target = 120;

for (let i = 1; i <= 1024; i++) {
  arr.push(i);
}

let end = arr.length - 1;

function binarySearch(arr, start, end, target) {
  console.log(arr.slice(start, end));
  if (start > end) return false;

  let midIndex = Math.floor((start + end) / 2);

  if (arr[midIndex === target]) {
    return true;
  }

  if (arr[midIndex] > target) {
    return binarySearch(arr, start, midIndex - 1, target);
  } else {
    return binarySearch(arr, midIndex + 1, end, target);
  }
}

binarySearch(arr, start, end, target);
