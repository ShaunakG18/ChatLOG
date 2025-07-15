**ChatLOG** is a GUI-based real-time chat application built with **FastAPI**.  
The backend is deployed live on **Render**, so users can instantly chat using the downloadable app.
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
## 🔗 Download App

You can download the ChatLOG GUI application (executable) from the link below:

📁 [Download from Google Drive](https://drive.google.com/drive/folders/1UP6do9Rxg3Y0HoBdKQKyjl8bkuekPXzt?usp=drive_link)

> ✅ This version is fully functional and connects directly to the live FastAPI backend deployed on Render — **no setup needed** to start chatting.

### 🛠️ Setup

1. **Clone the ChatLOG GUI repository**
   ```bash
   git clone https://github.com/ShaunakG18/ChatLOG.git
   cd ChatLOG
2. **Clone the FastAPI backend**
   ```bash
   git clone https://github.com/ShaunakG18/fastapi-chat.git
   cd fastapi-chat
3. (Optional) Create and activate a virtual environment  
   - On macOS/Linux: `python -m venv venv` and then `source venv/bin/activate`  
   - On Windows: `python -m venv venv` and then `venv\Scripts\activate`

4. Install the required dependencies using:  
   `pip install -r requirements.txt`

5. Run the FastAPI backend server with:  
   `uvicorn main:app --reload`
6. Run the ChatLOG GUI app  
   - Navigate to the `ChatLOG` directory  
   - Run the GUI using: `python app.py`

7. Access the chat  
   - Use the GUI window (built with CustomTkinter), or  
   - Open your browser and go to: `http://localhost:8000` to see the FastAPI backend

---

## 📁 Project Structure

**Main directories and important files:**

- `ChatLOG/` – GUI chat client  
  - `app.py` – Main GUI application  
  - `requirements.txt` – GUI dependencies  
  - `README.md` – Project documentation

- `fastapi-chat/` – FastAPI WebSocket backend  
  - `main.py` – FastAPI server logic  
  - `requirements.txt` – Backend dependencies
