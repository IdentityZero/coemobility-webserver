let fields = [
    {"field" : "username", "errorMsgDiv" : "username-errorMsg", "inputField": "id_username"},
    {"field" : "contact number", "errorMsgDiv" : "contact_number-errorMsg", "inputField": "id_contact_number"},
    {"field" : "password", "errorMsgDiv" : "password-errorMsg", "inputField": "id_password"},
    {"field" : "password repeat", "errorMsgDiv" : "repeat_password-errorMsg", "inputField": "id_repeat_password"},
    {"field" : "first name", "errorMsgDiv" : "first_name-errorMsg", "inputField": "id_first_name"},
    {"field" : "last name", "errorMsgDiv" : "last_name-errorMsg", "inputField": "id_last_name"},
    {"field" : "email", "errorMsgDiv" : "email-errorMsg", "inputField": "id_email"},
    {"field" : "profile picture", "errorMsgDiv" : "profile_picture-errorMsg", "inputField": "id_profile_picture"},
    {"field" : "role", "errorMsgDiv" : "role-errorMsg", "inputField": "id_role"},
    {"field" : "university number", "errorMsgDiv" : "university_number-errorMsg", "inputField": "id_university_number"},
    {"field" : "department", "errorMsgDiv" : "department-errorMsg", "inputField": "id_department"},
]

fields.forEach(function(item){
    errorDiv = document.getElementById(item.errorMsgDiv)
    inputField = document.getElementById(item.inputField)

    if (errorDiv.querySelector('ul') !== null){
        inputField.style.borderColor = 'red';
    }
})


// FOR RESIZING
// let imageInput = document.getElementById("id_profile_picture")

// imageInput.addEventListener('change', (event)=>{

//     let image_file = event.target.files[0]
//     let image_file_name = image_file.name.split(".")[0]
    
//     let reader = new FileReader()
//     reader.readAsDataURL(image_file)

//     reader.onload = (event) =>{

//         let image_url = event.target.result

//         let image = document.createElement("img")
//         image.src = image_url

//         image.onload = (e) =>{

//             let canvas = document.createElement("canvas")
//             let ratio = 300 / e.target.width
//             canvas.width = 300
//             canvas.height = e.target.height* ratio

//             const context = canvas.getContext("2d")
//             context.drawImage(image, 0,0,canvas.width, canvas.height)

//             let new_image_url = context.canvas.toDataURL("image/jpeg", 100)

//             let final_file = urlToFile(new_image_url, image_file_name)

//         }
//     }
// } )

// let urlToFile = (url, image_file_name) =>{
//     let arr = url.split(",")

//     let mime = arr[0].match(/:(.*?);/)[1]
//     let data = arr[1]

//     let dataStr = atob(data)
//     let n = dataStr.length

//     let dataArr = new Uint8Array(n)

//     while(n--){
//         dataArr[n] = dataStr.charCodeAt(n)
//     }

//     let file = new File([dataArr], `${image_file_name}.jpg`, {type:mime})

//     return file
// }
