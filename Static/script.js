// ===============================
// AI Medical Assistant
// script.js
// ===============================

console.log("AI Medical Assistant Loaded");

// -------------------------------
// Form Validation
// -------------------------------

function validateForm() {

    const name = document.querySelector("input[name='name']");
    const age = document.querySelector("input[name='age']");
    const symptom = document.querySelector("input[name='symptom1']");

    if (name && name.value.trim() === "") {
        alert("Please enter your name.");
        return false;
    }

    if (age && (age.value < 1 || age.value > 120)) {
        alert("Please enter a valid age.");
        return false;
    }

    if (symptom && symptom.value.trim() === "") {
        alert("Please enter at least one symptom.");
        return false;
    }

    return true;
}

// -------------------------------
// Loading Effect
// -------------------------------

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (e) {

            if (!validateForm()) {
                e.preventDefault();
                return;
            }

            const button = form.querySelector("button");

            if (button) {
                button.innerHTML = "Predicting...";
                button.disabled = true;
            }

        });

    }

});

// -------------------------------
// Enter Key Support
// -------------------------------

const messageInput = document.getElementById("message");

if (messageInput) {

    messageInput.addEventListener("keypress", function (event) {

        if (event.key === "Enter") {
            event.preventDefault();

            if (typeof sendMessage === "function") {
                sendMessage();
            }

        }

    });

}

// -------------------------------
// Voice Input
// -------------------------------

function startVoiceInput() {

    if (!("webkitSpeechRecognition" in window)) {

        alert("Speech Recognition is not supported in this browser.");

        return;
    }

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";
    recognition.interimResults = false;

    recognition.onresult = function (event) {

        const text = event.results[0][0].transcript;

        const input = document.getElementById("message");

        if (input) {
            input.value = text;
        }

    };

    recognition.start();

}

// -------------------------------
// Auto Scroll Chat
// -------------------------------

function scrollChatToBottom() {

    const chatBox = document.getElementById("chat-box");

    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

}

// -------------------------------
// Welcome Message
// -------------------------------

window.onload = function () {

    console.log("Welcome to AI Medical Assistant");

};
