# Full Stack CRUD Backend (Flask + SQLAlchemy)

This is the backend part of a Full Stack CRUD (Create, Read, Update, Delete) application built using **Flask**, **SQLAlchemy**, and **SQLite**. It provides RESTful API endpoints to manage contact information.

## 🔗 Repository

Frontend Repo (if available): _[Add link here]_

---

## 🚀 Features

- Create new contacts
- Read all contacts
- Update contact by ID
- Delete contact by ID
- JSON-based API
- Easy integration with any frontend

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite (default) or any other RDBMS
- Postman (for testing)

---

## 📂 Project Structure

├── config.py # DB and app configuration
├── main.py # API routes
├── models.py # SQLAlchemy models
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

# ⚙️ Setup Instructions

# 1. Clone the Repository

git clone https://github.com/malinda6997/Full-Stack-CRUD-Backend.git
cd Full-Stack-CRUD-Backend

#2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

#3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

#4. Run the Application
bash
Copy
Edit
python main.py
The server will start on:

cpp
Copy
Edit
http://127.0.0.1:5000
📬 API Endpoints
Method	Endpoint	Description
GET	/contacts	Get all contacts
POST	/contacts	Create a new contact
PUT	/contacts/<id>	Update a contact by ID
DELETE	/contacts/<id>	Delete a contact by ID

📦 Sample JSON (for POST/PUT)
json
Copy
Edit
{
  "firstName": "John",
  "lastName": "Doe",
  "mobileNumber": "0771234567",
  "age": 25
}
🧪 Testing with Postman
You can test the API using Postman by sending HTTP requests to:

arduino
Copy
Edit
http://127.0.0.1:5000/contacts
🙌 Author
Malinda
GitHub Profile

📄 License
This project is open-source and available under the MIT License.

yaml
Copy
Edit


Would you like a `requirements.txt` file generated for this project too?
