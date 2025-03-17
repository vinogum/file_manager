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
            if (!response.ok)
            {
                return response.json().then(data => {
                    throw new Error(data.message);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log(data.message);
        })
        .catch(error => {
            console.error(error.message);
        });
    });
});
