
const signInButton = document.getElementById('signIn');

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});




function begin() {
   
    var data = {};
    data.username = $('#username').val();
    data.password = $('#password').val()

    $.ajax({
        type: "POST",
        datatype:"application/json",
        url: "/login",
       
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        
        success: (data) => { 
            // console.log(`JWT TOken : ${data}`)
            hideSpinner();
            JWT_Token =`${data}`;

            localStorage.setItem("SavedToken",JWT_Token);
            axios.defaults.headers.common['Authorization'] = JWT_Token;
          


            window.location.href = 'test.html';
           
            console.log(JWT_Token)
            
          
        },
        error: function(xhr, status, error) {
            hideSpinner();
            console.log(`ERROR`)
            document.getElementById('error-output').style ="display:block;margin:auto!important;margin: 15px 0!important;";
            document.getElementById('error-output').textContent = `Error : Username or Password not correct!`;
        }
    });
    
  

}
