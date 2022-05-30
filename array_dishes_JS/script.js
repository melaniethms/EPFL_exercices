var dishes = ["pasta", "pizza", "risotto"];
console.log(dishes[0]);
console.log(dishes[1]);
console.log(dishes[2]);
console.log("this array has " + dishes.length + " values");
dishes.push("fondue");

console.log("this array has " + dishes.length + " values");
dishes.splice(1,1);
dishes.sort();
console.log(dishes);
console.log("this array has " + dishes.length + " values");