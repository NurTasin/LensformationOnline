var form = document.querySelector('.pageclip-form')
var submission=document.getElementById('submission_text')
Pageclip.form(form, {
  onSubmit: function (event) {
    submission.innerHTML=`<span class='text-info text-center'> Sending... 🤖 </span>`
   },
  onResponse: function (error, response) {
        if(error){
            submission.innerHTML=`<span class='text-danger text-center'> Unable to send your message 😢</span>`
        }else{
            submission.innerHTML=`<span class='text-success text-center'> Message sent! We will contact with you ASAP 😊</span>`
        }
    },
  successTemplate: '<span>Sent!! 😃</span>'
})