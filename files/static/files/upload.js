document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem("auth_token");
    if (!token) {
        window.location.href = "/auth/login/";
        return;
    }

    document.getElementById('upload-button').addEventListener('click', () => {
        const uploadFormElement = document.getElementById('upload-form');
        if (!uploadFormElement) return;

        const formData = new FormData(uploadFormElement);
        formData.append("file_data", formData.get("file-data"));
        formData.append("url", formData.get("url"));

        fetch('/api/files/', {
            method: 'POST',
            headers: {
                'Authorization': `Token ${token}`,
            },
            body: formData,
        })
        .then(response => {
            if (!response.ok)
            {
                return response.json().then(error => {
                    throw new Error(error);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
    });
});
