var now = new Date()
var day = now.getDay()  // When ask the day , the console will show the date in number format (if the day is Sundey , will show 0)

/* 
    0 = Sunday, 
    1 = Monday, 
    2 = Tuesday, 
    3 = Wednesday
    4 = Thursday
    5 = Friday
    6 = Saturday
    
*/

switch(day) {
    case 0: 
    console.log("In your system , today is Sunday")
    break
    case 1: 
    console.log("In your system , today is Monday")
    break
    case 2: 
    console.log("In your system , today is Tuesday")
    break
    case 3:
    console.log("In your system , today is Wednesday")
    break
    case 4:
    console.log("In your system , today is Thursday")
    break
    case 5:
    console.log("In your system , today is Friday")
    break
    case 6:
    console.log("In your system , today is Saturday")
    break
}