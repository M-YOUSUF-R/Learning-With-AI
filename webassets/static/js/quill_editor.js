// Initialize Quill editor
const quill = new Quill("#editor", {
  theme: "snow",
  modules: {
    toolbar: "#toolbar",
  },
  // placeholder: 'Type your message here...'
});

// DOM elements
const chatMessages = document.getElementById("chat-messages");

// Message state tracking
let currentAIMessageDiv = null;
let currentAIMessageContent = null;

// Function to add a user message
function addMessage(content, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${sender}-message`;

  if (sender === "user") {
    messageDiv.innerHTML = `
            <div class="message-content">👤 ${content}</div>
            <div class="message-meta">${new Date().toLocaleTimeString()}</div>
        `;
    chatMessages.appendChild(messageDiv);
  }

  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to handle AI streaming response
function startAIStream() {
  // Create message container
  currentAIMessageDiv = document.createElement("div");
  currentAIMessageDiv.className = "message ai-message";

  // Create content element with loading indicator
  currentAIMessageContent = document.createElement("div");
  currentAIMessageContent.className = "message-content";
  currentAIMessageContent.innerHTML =
    '🤖 <span class="typing-indicator"></span>';

  // Create meta element for timestamp
  const messageMeta = document.createElement("div");
  messageMeta.className = "message-meta";
  messageMeta.textContent = new Date().toLocaleTimeString();

  // Assemble the message
  currentAIMessageDiv.appendChild(currentAIMessageContent);
  currentAIMessageDiv.appendChild(messageMeta);
  chatMessages.appendChild(currentAIMessageDiv);

  return {
    appendChunk: (chunk) => {
      if (currentAIMessageContent.querySelector(".typing-indicator")) {
        currentAIMessageContent.innerHTML = "🤖 ";
      }
      currentAIMessageContent.innerHTML += chunk;
      chatMessages.scrollTop = chatMessages.scrollHeight;
    },
    complete: () => {
      // Remove any remaining typing indicator
      const typingIndicator =
        currentAIMessageContent.querySelector(".typing-indicator");
      if (typingIndicator) {
        typingIndicator.remove();
      }

      // Reset for next message
      currentAIMessageDiv = null;
      currentAIMessageContent = null;
    },
  };
}
// Export the necessary functions and objects
export { quill, startAIStream, addMessage };
