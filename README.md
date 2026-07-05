# Simple Realtime Chat App

A lightweight real-time chat application built using **FastAPI** and **WebSockets**. The project demonstrates persistent bidirectional communication between multiple connected clients using FastAPI's WebSocket support and a custom connection manager.

---

## Overview

This project showcases how to build a real-time messaging application using FastAPI without relying on external messaging services. Multiple clients can connect simultaneously, send messages, and receive broadcasts instantly.

The application serves as a practical example for understanding WebSockets, connection management, and asynchronous programming in FastAPI.

---

## Features

- Real-time messaging using WebSockets
- Multiple client support
- Automatic client connection management
- Broadcast messages to all connected clients
- Personal acknowledgment messages
- Automatic client ID generation
- Connection and disconnection notifications
- Responsive web-based chat interface
- Asynchronous communication using FastAPI

---

## Tech Stack

- Python 3.x
- FastAPI
- WebSockets
- Uvicorn
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
Simple_Realtime_ChatAPP/
│
├── app/
│   ├── features/
│   │   └── connectors.py
│   │
│   ├── utilities/
│   │   ├── helpers.py
│   │   └── websockets.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/AmoghShukla/Simple_Realtime_ChatAPP.git
```

```bash
cd Simple_Realtime_ChatAPP
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server using Uvicorn.

```bash
uvicorn app.main:app --reload
```

The application will be available at

```
http://127.0.0.1:8000
```

Open the application in multiple browser tabs to simulate multiple chat clients.

---

## How It Works

1. A client opens the web page.
2. A WebSocket connection is established with the FastAPI server.
3. The server generates a unique client ID.
4. Messages sent by any client are broadcast to all connected users.
5. Each sender also receives a personal confirmation message.
6. When a client disconnects, all connected users are notified.

---

## Example

**Client A**

```
Hello Everyone!
```

**Server**

```
You have sent: Hello Everyone!
```

**Other Clients**

```
Client #4837291041: Hello Everyone!
```

---

## Learning Objectives

This project demonstrates:

- FastAPI WebSocket endpoints
- Asynchronous programming with async/await
- Managing multiple active WebSocket connections
- Broadcasting messages
- Connection lifecycle management
- Building a simple real-time communication system

---

## Future Improvements

- User authentication
- Usernames instead of random IDs
- Private messaging
- Chat rooms
- Message persistence using PostgreSQL
- Redis Pub/Sub support
- Typing indicators
- Online users list
- Message timestamps
- File sharing
- Docker support

---

## Author

**Amogh Shukla**

- GitHub: https://github.com/AmoghShukla
