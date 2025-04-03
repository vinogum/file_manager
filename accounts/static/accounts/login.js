document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('login-button').addEventListener('click', () => {
        const loginFormElement = document.getElementById('login-form');
        if (!loginFormElement) return;

        const formData = new FormData(loginFormElement);
        const formObject = Object.fromEntries(formData);
        
        fetch('/auth/api/login/', {
            method: 'POST',
            body: JSON.stringify(formObject),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Invalid request!");
            }
            return response.json();
        })
        .then(data => {
            console.log(data.user);
            console.log(data.token);
            localStorage.setItem('auth_token', data.token);
        })
        .catch(error => {
            console.error(error.message);
        });
    });
});
