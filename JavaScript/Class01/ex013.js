var now = new Date()
var hour = now.getHours()

console.log(`It's ${hour} o'clock`)
if (hour >= 6 && hour < 12) {
    console.log("Good Morning!")
} else if (hour >= 12 && hour < 19) {
    console.log("Good Evening!")
} else {
    console.log("Good Night!")
}