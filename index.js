var IS = require("initial-state");
var bucket = IS.bucket("BBK3MJ765C8G", "ist_BQsWk-sOdzWzz1-aANne7TBz_GNISkfB");

// Push event to initial state
bucket.push("Demo State", "active");

setTimeout(function () {
  // Push another event
  bucket.push("Demo State", "inactive");
}, 1000);
console.log("hi");
