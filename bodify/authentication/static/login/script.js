// Function to validate the login form
function validateLoginForm() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorElement = document.getElementById("error");
  
    if (username === "" || password === "") {
      errorElement.textContent = "Username and password are required.";
      return false;
    }
  
    // You can add more validation logic here if needed
  
    return true;
  }
  
  // Handle form submission
  const loginForm = document.getElementById("login-form");
  
  // loginForm.addEventListener("submit", function (e) {
  //   e.preventDefault(); // Prevent the form from submitting
  
  //   if (validateLoginForm()) {
  //     // Perform AJAX login request or other actions here
  //     alert("Form submitted successfully!");
  //     // You can redirect the user to another page or perform other actions
  //   }
  // });
  