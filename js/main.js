
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

const spinner = document.getElementById("spinner");
const spinner2 = document.getElementById("spinner2");

function showSpinner() {
    spinner.style ="display:block;"
  
}

function hideSpinner() {
    spinner.style ="display:none;"
   
}
function showSpinner2() {
    spinner2.style ="display:block;"
  
}

function hideSpinner2() {
    spinner2.style ="display:none;"
   
}
var JWT_Token ;




function login() {
    showSpinner();

    var data = {};
    data.email = $('#email').val();
    data.password = $('#password').val()

    $.ajax({
        type: "POST",
        datatype:"application/json",
        url: "http://127.0.0.1:5000/login",
       
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        
        success: (data) => { 
            // console.log(`JWT TOken : ${data}`)
            hideSpinner();
            JWT_Token =`${data.access_token}`;

            localStorage.setItem("SavedToken",JWT_Token);
            axios.defaults.headers.common['Authorization'] = JWT_Token;
          


            //window.location.href = 'home.html';
           
            console.log(data.message)
            console.log(data.access_token)
            
          
        },
        error: function(xhr, status, error) {
            hideSpinner();
            console.log(`ERROR`)
            document.getElementById('error-output').style ="display:block;margin:auto!important;margin: 15px 0!important;";
            document.getElementById('error-output').textContent = `Error : Username or Password not correct!`;
        }
    });
    
  

}
id_count = 104;

function register() {
    
    showSpinner2();

    var data = {};
    data.name = $('#name_').val()
    data.email = $('#email_').val()
    data.password = $('#password_').val()
    data.user_id = id_count
    id_count = id_count + 1
    data.budget = $('#budget_').val()
    data.address = $('#address_').val()

    $.ajax({
        type: "POST",
        datatype:"application/json",
        url: "http://127.0.0.1:5000/register",
       
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        
        success: (data) => { 
            // console.log(`JWT TOken : ${data}`)
            hideSpinner2();
            window.location.href = 'otp.html';
            console.log(data.message)
            
          
        },
        error: function(xhr, status, error) {
            hideSpinner2();
            console.log(`ERROR`)
            document.getElementById('error-output2').style ="display:block;margin:auto!important;margin: 15px 0!important;";
            document.getElementById('error-output2').textContent = `Error!`;
        }
    });
    
  

}

function register2() {
    window.location.href = 'otp.html';
}