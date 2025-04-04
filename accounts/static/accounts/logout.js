document.addEventListener("DOMContentLoaded", function() {
    const token = localStorage.getItem("auth_token");
    if (!token) {
        window.location.href = "/auth/login/";
        return;
    }

    const logoutButton = document.getElementById("logout-button");
    if (!logoutButton) {
        console.error("Logout button not found");
        return;
    }

    logoutButton.addEventListener("click", function() {
        fetch("/auth/api/logout/", {
            method: "POST",
            headers: {
                "Authorization": `Token ${token}`,
            },
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Logout failed");
            }
            localStorage.removeItem("auth_token");
            window.location.href = "/auth/login/";
        })
        .catch(error => {
            console.error("Error during logout:", error);
        });
    });
});
