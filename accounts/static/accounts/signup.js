document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('signup-button').addEventListener('click', () => {
        const signupFormElement = document.getElementById('signup-form');
        if (!signupFormElement) return;

        const formData = new FormData(signupFormElement);
        const formObject = Object.fromEntries(formData);
        
        fetch('/auth/api/signup/', {
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
            console.log(data);
        })
        .catch(error => {
            console.error(error.message);
        });
    });
});
