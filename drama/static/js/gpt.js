const messageInput = document.getElementById("message-input");
const messageBox = document.getElementById("messages");
const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
const csrfToken = csrfTokenMeta ? csrfTokenMeta.content : '';
let conversation = [];

const handleAsk = async () => {
    let message = messageInput.value;

    if (message.length > 0) {
        messageInput.value = "";
        await askGpt(message);
    }
};

const askGpt = async (message) => {
    try {
        let jailbreak = document.getElementById("jailbreak");
        let model = document.getElementById("model");
        let systemMessage = document.querySelector(".system-text").value;
        let jailbreakMessage = jailbreak.options[jailbreak.selectedIndex].value;

        if (jailbreakMessage) {
            systemMessage = jailbreakMessage;
        }

        if (conversation.length === 0) {
            conversation.push({ role: "system", content: systemMessage });
        }

        conversation.push({ role: "user", content: message });

        const response = await fetch(`/chat-completion/`, {
            method: `POST`,
            headers: {
                "content-type": `application/json`,
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                model: model.options[model.selectedIndex].value,
                conversation: conversation
            }),
        });

        const data = await response.json();
        const assistantResponse = data.text;
        conversation.push({ role: "assistant", content: assistantResponse });

        localStorage.setItem("conversation", JSON.stringify(conversation));

        messageBox.innerHTML += `
            <div class="message">
                <div class="user">
                    ${user_image}
                    <i class="fa-regular fa-phone-arrow-up-right"></i>
                </div>
                <div class="content">
                    ${message.replace(/(?:\r\n|\r|\n)/g, "<br>")}
                </div>
            </div>
            <div class="message">
                <div class="user">
                    ${gpt_image}
                    <i class="fa-regular fa-phone-arrow-down-left"></i>
                </div>
                <div class="content">
                    ${assistantResponse.replace(/(?:\r\n|\r|\n)/g, "<br>")}
                </div>
            </div>
        `;

        messageBox.scrollTop = messageBox.scrollHeight;
        window.scrollTo(0, 0);

    } catch (e) {
        console.log(e);
    }
};

messageInput.addEventListener("keydown", async (evt) => {
    if (evt.keyCode === 13 && !evt.shiftKey) {
        evt.preventDefault();
        await handleAsk();
    }
})
