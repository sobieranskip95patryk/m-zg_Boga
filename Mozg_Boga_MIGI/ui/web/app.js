// This file contains the JavaScript logic for the web interface.

document.addEventListener("DOMContentLoaded", function() {
    const askButton = document.getElementById("ask-button");
    const inputField = document.getElementById("input-field");
    const outputArea = document.getElementById("output-area");

    askButton.addEventListener("click", function() {
        const userInput = inputField.value;
        if (userInput) {
            fetch("/v1/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ query: userInput })
            })
            .then(response => response.json())
            .then(data => {
                outputArea.innerText = data.response || "No response from server.";
            })
            .catch(error => {
                console.error("Error:", error);
                outputArea.innerText = "An error occurred. Please try again.";
            });
        } else {
            outputArea.innerText = "Please enter a query.";
        }
    });
});