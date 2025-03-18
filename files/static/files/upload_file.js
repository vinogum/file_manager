document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('upload-button').addEventListener('click', () => {
        const uploadFormElement = document.getElementById('upload-form');
        if (!uploadFormElement) return;

        const token = localStorage.getItem('auth_token');
        const formData = new FormData(uploadFormElement);
        fetch('/api/files/', {
            method: 'POST',
            body: formData,
            headers: {
                'Authorization': `Token ${token}`,
            },
        })
        .then(response => {
            if (!response.ok)
            {
                return response.json().then(error => {
                    throw new Error(error.message);
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
