html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MessageX Chat</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }

        body{
            background:#f4f6f9;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }

        .chat-container{
            width:450px;
            max-width:95%;
            height:90vh;
            background:#fff;
            border-radius:12px;
            box-shadow:0 10px 30px rgba(0,0,0,.15);
            display:flex;
            flex-direction:column;
            overflow:hidden;
        }

        .header{
            background:#2563eb;
            color:#fff;
            padding:18px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .messages{
            flex:1;
            padding:15px;
            overflow-y:auto;
            background:#eef2f7;
        }

        .message{
            padding:10px 14px;
            border-radius:16px;
            margin-bottom:10px;
            max-width:75%;
            word-wrap:break-word;
        }

        .self{
            background:#2563eb;
            color:#fff;
            margin-left:auto;
        }

        .other{
            background:#fff;
            border:1px solid #ddd;
        }

        .footer{
            display:flex;
            gap:10px;
            padding:15px;
            border-top:1px solid #ddd;
        }

        input{
            flex:1;
            padding:12px;
            border-radius:8px;
            border:1px solid #ccc;
            outline:none;
        }

        button{
            background:#2563eb;
            color:white;
            border:none;
            border-radius:8px;
            padding:12px 18px;
            cursor:pointer;
        }

        button:hover{
            background:#1d4ed8;
        }
    </style>
</head>

<body>

<div class="chat-container">

    <div class="header">
        <h2>MessageX</h2>
        <span id="status">Connecting...</span>
    </div>

    <div id="messages" class="messages"></div>

    <div class="footer">
        <input
            id="messageInput"
            type="text"
            placeholder="Type your message..."
        />

        <button onclick="sendMessage()">Send</button>
    </div>

</div>

<script>

const socket = new WebSocket(`ws://${window.location.host}/ws`);

const status = document.getElementById("status");
const messages = document.getElementById("messages");
const input = document.getElementById("messageInput");

socket.onopen = () => {
    status.textContent = "🟢 Connected";
};

socket.onclose = () => {
    status.textContent = "🔴 Disconnected";
};

socket.onerror = () => {
    status.textContent = "⚠ Connection Error";
};

socket.onmessage = (event) => {
    addMessage(event.data, "other");
};

function addMessage(message, type) {
    const div = document.createElement("div");
    div.className = `message ${type}`;
    div.textContent = message;

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}

function sendMessage() {
    const text = input.value.trim();

    if (text === "") return;

    socket.send(text);

    addMessage(text, "self");

    input.value = "";
    input.focus();
}

input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

</script>

</body>
</html>"""