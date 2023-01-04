function verify() {
    var data = new Date()
    var year = data.getFullYear()
    var fyear = document.querySelector('input#txtano')
    var res = document.querySelector('div#res')



    if (fyear.value.length == 0 || fyear.value > year) {  // If the box is empty OR the year is above the year system, give error message.
        alert('[ERROR]] Invalid year')
    } else {
        var fsex = document.getElementsByName('radsex')
        var age = year - Number(fyear.value)
        var gender = ''
        var img = document.createElement('img')  // Create the image section  || In html is <img id='img' src=''>
        img.setAttribute('id' , 'img') // Set the img as id attribute
        if (fsex[0].checked) {
            gender = 'Male'
            if (age >= 0 && age < 12 ) {
                // boy young
                img.setAttribute('src', 'image/boyyoung.png')  // Will get the img by source attributed
            } else if (age < 18) {
                // boy adolescente 
                img.setAttribute('src', 'image/boyadolesc.jpeg')
            } else if (age < 50) {
                // boy adult
                img.setAttribute('src', 'image/boyadult.jpeg')
            } else {
                // Boy older
                img.setAttribute('src', 'image/boyolder.jpeg')
            }
        } else if (fsex[1].checked) {
            gender = 'Female'
            if (age >= 0 && age < 12 ) {
                // girl young
                img.setAttribute('src', 'image/girlyoung.png') // Will get the img by source attributed
            } else if (age < 18) {
                // girl adolescente 
                img.setAttribute('src', 'image/girladolescente.jpeg')
            } else if (age < 50) {
                // girl adult
                img.setAttribute('src', 'image/girladult.jpeg')
            } else {
                // girl older
                img.setAttribute('src', 'image/girlolder.jpeg')
            }
        }
    }
    res.style.textAlign = 'center'
    res.innerHTML = `Your are ${gender} with ${age} years old`
    res.appendChild(img)
    img.style.width = '40%'
}