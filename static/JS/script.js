// Show alert after login
function showLoginSuccess() {
    alert("Login Successful!");
}

// Confirm logout
function confirmLogout() {
    return confirm("Are you sure you want to logout?");
}

// Simple search filter (for dashboard)
function searchStudent() {
    let input = document.getElementById("search").value.toLowerCase();
    let cards = document.getElementsByClassName("card");

    for (let i = 0; i < cards.length; i++) {
        let text = cards[i].innerText.toLowerCase();

        if (text.includes(input)) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    }
}