// Initialize Quill editor
const quill = new Quill('#editor', {
    theme: 'snow',
    modules: {
        toolbar: '#toolbar'
    },
    // placeholder: 'Type your message here...'
});

// DOM elements
const chatMessages = document.getElementById('chat-messages');

// Message state tracking
let currentAIMessageDiv = null;
let currentAIMessageContent = null;

// Function to add a user message
function addMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    if (sender === 'user') {
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
    currentAIMessageDiv = document.createElement('div');
    currentAIMessageDiv.className = 'message ai-message';
    
    // Create content element with loading indicator
    currentAIMessageContent = document.createElement('div');
    currentAIMessageContent.className = 'message-content';
    currentAIMessageContent.innerHTML = '🤖 <span class="typing-indicator"></span>';
    
    // Create meta element for timestamp
    const messageMeta = document.createElement('div');
    messageMeta.className = 'message-meta';
    messageMeta.textContent = new Date().toLocaleTimeString();
    
    // Assemble the message
    currentAIMessageDiv.appendChild(currentAIMessageContent);
    currentAIMessageDiv.appendChild(messageMeta);
    chatMessages.appendChild(currentAIMessageDiv);
    
    // Buffer to hold incomplete lines
    let buffer = '';
    
    return {
        appendChunk: (chunk) => {
            // Remove typing indicator if it's the first chunk
            if (currentAIMessageContent.querySelector('.typing-indicator')) {
                currentAIMessageContent.innerHTML = '🤖 ';
            }
            
            // Add new chunk to buffer
            buffer += chunk;
            
            // Process complete lines
            const lines = buffer.split('\n');
            buffer = lines.pop() || ''; // Keep last incomplete line in buffer
            
            // Process each complete line
            lines.forEach(line => {
                // Convert markdown to simple HTML
                line = line.replace(/\*\*\*(.*?)\*\*\*/g, '<hr><strong>$1</strong><hr>')
                          .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                          .replace(/\*(.*?)\*/g, '<em>$1</em>');
                
                // Create paragraph for each line
                const p = document.createElement('p');
                p.innerHTML = line || '&nbsp;'; // Use &nbsp; for empty lines
                currentAIMessageContent.appendChild(p);
            });
            
            // If we have remaining content in buffer, add it
            if (buffer) {
                const lastSpan = currentAIMessageContent.lastElementChild;
                if (lastSpan && lastSpan.tagName !== 'P') {
                    lastSpan.textContent += buffer;
                } else {
                    const span = document.createElement('span');
                    span.textContent = buffer;
                    currentAIMessageContent.appendChild(span);
                }
            }
            
            // Scroll to bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        },
        complete: () => {
            // Process any remaining buffer content
            if (buffer.trim()) {
                const p = document.createElement('p');
                p.innerHTML = buffer.replace(/\*\*\*(.*?)\*\*\*/g, '<hr><strong>$1</strong><hr>')
                                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                                    .replace(/\*(.*?)\*/g, '<em>$1</em>');
                currentAIMessageContent.appendChild(p);
            }
            
            // Remove any remaining typing indicator
            const typingIndicator = currentAIMessageContent.querySelector('.typing-indicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
            
            // Reset for next message
            currentAIMessageDiv = null;
            currentAIMessageContent = null;
            buffer = '';
        }
    };
}
// Export the necessary functions and objects
export { quill, startAIStream, addMessage };