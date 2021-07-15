function otp(e) {
    const id = e.target.id.split("_")[1];
    const next = parseInt(id)+1;
    const prev = parseInt(id)-1;
    const otps = document.querySelectorAll("input");
    
    for(let i = 0; i < otps.length; i++){
      
    }
    if(e.code !== "Backspace"){
      if(next <=6){
        document.querySelector(`#otp_${next}`).focus();
      }
      else{
        e.target.blur();
      }
      e.target.classList.add("active");
    }
    else{
      if(prev > 0){
        document.querySelector(`#otp_${prev}`).focus();
        document.querySelector(`#otp_${prev}`).classList.remove("active");
      }
      e.target.classList.remove("active");
    }
  }
  
  document.querySelectorAll('input').forEach(ele =>                                     
    {
      ele.addEventListener("keyup", otp)
  });
  
  document.querySelector("button").addEventListener("click", (e) => {
    e.target.classList.add("animate");
  })

  function openloginpage() {
    alert("Registration Successful!");
    window.location.href = 'sign_in_up.html'; 
  }