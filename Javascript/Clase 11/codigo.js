document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const usernameInput = document.querySelector('input[type="text"]');
    const passwordInput = document.querySelector('input[type="password"]');
    
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();
        
        if (username === "") {
            alert("Please enter your username.");
            return;
        }
        
        if (password === "") {
            alert("Please enter your password.");
            return;
        }
        
        // Agregar autenticacion de usuario
        console.log("Username:", username);
        console.log("Password:", password);
        
        // Redirige al usuario o muestra un mensaje de éxito
        alert("Login successful!");
    });
});
