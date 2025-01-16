# Chat Application

Welcome to the Chat Application repository! This project is a real-time chat platform built using Django and WebSockets. The application allows users to sign up, log in, and exchange messages in real-time.

## Features
- User authentication (signup, login, logout)
- Real-time messaging using WebSockets
- User-friendly interface
- Responsive design

---

## Installation

### 1. Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/Akshaj2506/Django_Chat_App.git
cd Django_Chat_App
```
OR 
Download the .zip file of this git repository and and extract the contents of the repository on your machine at a safe location.

### 2. Set Up a Virtual Environment
Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Navigate to The Project Folder
```bash
pip install -r requirements.txt
```
### 4. Install Python Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
Apply migrations to set up the database:
```bash
python manage.py migrate
```


### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/` in your browser.

---

## Testing WebSocket Connections

1. Open the application in two browsers or two tabs(One of them should be incognito).
2. Create two different users using Signup functionality.
3. Once being authenticated, click on the respective users to open the chat.

---

## Common Issues
1. **User Responsiveness:** The appearance of mobile layout can be better
2. **WebSocket Errors:** Make sure your browser supports WebSockets and you’re using the correct URL format (`ws://` for local environments, `wss://` for production with HTTPS).

