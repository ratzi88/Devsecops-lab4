// register/app.js
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://localhost:5001/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();

    if (response.ok) {
        alert('User registered successfully!');
        window.location.href = '../login/index.html'; // Redirect to login page
    } else {
        alert(result.error || 'Registration failed');
    }
});
