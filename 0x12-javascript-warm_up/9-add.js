#!/usr/bin/node
function adds (a, b) {
  const c = a + b;
  console.log(c);
}

adds(Number(process.argv[2]), Number(process.argv[3]));
