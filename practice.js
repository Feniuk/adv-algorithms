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

function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  const middleIndex = Math.floor(arr.length / 2);
  const leftArr = arr.slice(0, middleIndex);
  const rightArr = arr.slice(middleIndex);
  return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(leftArr, rightArr) {
  let mergedArr = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
    if (leftArr[leftIndex] < rightArr[rightIndex]) {
      mergedArr.push(leftArr[leftIndex]);
      leftIndex += 1;
    } else {
      mergedArr.push(rightArr[rightIndex]);
      rightIndex += 1;
    }
  }

  return mergedArr
    .concat(leftArr.slice(leftIndex))
    .concat(rightArr.slice(rightIndex));
}

let array = [12, 3, 16, 6, 5, 1];

console.log(mergeSort(array));
