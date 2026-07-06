function copyPassword() {
    const password = document.getElementById("password");

    // FIX: Check if empty OR if it contains an error message
    if (password.value === "" || password.value.includes("!")) {
        alert("Generate a valid password first!");
        return;
    }

    navigator.clipboard.writeText(password.value)
        .then(() => {
            const copyButton = document.querySelector(".copy-btn");
            copyButton.innerHTML = "✅ Copied!";

            setTimeout(() => {
                copyButton.innerHTML = "📋 Copy Password";
            }, 2000);
        })
        .catch(() => {
            alert("Failed to copy password.");
        });
}

function togglePassword() {
    const password = document.getElementById("password");
    const button = document.getElementById("togglePassword");

    if (password.type === "password") {
        password.type = "text";
        button.innerHTML = "🙈";
    } else {
        password.type = "password";
        button.innerHTML = "👁";
    }
}