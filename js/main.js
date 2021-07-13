
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

function showSpinner() {
    spinner.style ="display:block;"
  
}

function hideSpinner() {
    spinner.style ="display:none;"
   
}

var JWT_Token ;




function begin() {
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


function signup() {
    showSpinner();

    var data = {};
    data.email = $('#email').val();
    data.password = $('#password').val()

    $.ajax({
        type: "POST",
        datatype:"application/json",
        url: "https://vbudget-apis.herokuapp.com/login",
       
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        
        success: (data) => { 
            // console.log(`JWT TOken : ${data}`)
            hideSpinner();
            JWT_Token =`${data.access_token}`;

            localStorage.setItem("SavedToken",JWT_Token);
            axios.defaults.headers.common['Authorization'] = JWT_Token;
          


            window.location.href = 'home.html';
           
            console.log(data.message)
            
          
        },
        error: function(xhr, status, error) {
            hideSpinner();
            console.log(`ERROR`)
            document.getElementById('error-output').style ="display:block;margin:auto!important;margin: 15px 0!important;";
            document.getElementById('error-output').textContent = `Error : Username or Password not correct!`;
        }
    });
    
  

}