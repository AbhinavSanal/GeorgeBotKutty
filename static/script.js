// Display the initial message when the page loads
window.onload = function() {
    const chatBody = document.getElementById("chatBody");

    const botDiv = document.createElement("div");
    botDiv.classList.add("chat-message", "bot-message");
    botDiv.textContent = initialMessage;  // Use the initial message
    chatBody.appendChild(botDiv);  // Append to chat body
    chatBody.scrollTop = chatBody.scrollHeight;  // Scroll to bottom
};

function sendMessage() {
    const userInput = document.getElementById("userInput");
    const chatBody = document.getElementById("chatBody");

    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    const userDiv = document.createElement("div");
    userDiv.classList.add("chat-message", "user-message");
    userDiv.textContent = userMessage;
    chatBody.appendChild(userDiv);
    chatBody.scrollTop = chatBody.scrollHeight;

    fetch("http://localhost:5000/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        const botDiv = document.createElement("div");
        botDiv.classList.add("chat-message", "bot-message");
        botDiv.textContent = data.response;
        chatBody.appendChild(botDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    userInput.value = "";
}
