function cube(n) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let z = 0; z < n; z++) {
        console.log(i, j, z);
      }
    }
  }
}

cube(4);

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
