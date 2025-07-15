# 💬 ChatLOG

**ChatLOG** is a GUI-based real-time chat application built with **FastAPI**. It enables users to communicate seamlessly through a user-friendly interface, leveraging the power of asynchronous WebSocket connections.

---

## 🚀 Features

- 🧠 Real-time messaging via WebSockets  
- 🖥️ Intuitive graphical user interface (GUI)  
- ⚡ FastAPI backend with async support  
- 🔄 Hot-reloading during development with `uvicorn`  
- 🧪 Ideal for learning and experimentation  

---

## 📦 Installation

### ✅ Prerequisites

- Python 3.7 or higher
- `pip` package manager

---

### 🛠️ Setup

1. **Clone the repository**
git clone https://github.com/ShaunakG18/fastapi-chat.git
cd fastapi-chat
Clone the FastAPI backend

bash
Copy
Edit
git clone https://github.com/ShaunakG18/fastapi-chat.git
cd fastapi-chat
(Optional) Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI backend

bash
Copy
Edit
uvicorn main:app --reload
Run the ChatLOG GUI app (if separate Python file exists)

bash
Copy
Edit
python app.py
Access the chat (GUI or browser)

Open the GUI app if using CustomTkinter

Or open: http://localhost:8000

📁 Project Structure
bash
Copy
Edit
ChatLOG/
├── app.py             # GUI chat client
├── requirements.txt   # GUI dependencies
├── README.md          # This file

fastapi-chat/
├── main.py            # FastAPI WebSocket backend
├── requirements.txt
📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it with proper attribution.

🙋‍♂️ Author
Made by Shaunak G

