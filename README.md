# 📚 Book Manager - FastAPI + Pydantic + UI

A **minimal and modern web application** for managing books using **FastAPI** and **Pydantic**.  
You can add new books, search existing ones, and paginate results.  

All API endpoints are accessible via **Swagger**, and a **dark-themed UI** built with HTML/CSS/JS provides a smooth browser-based experience without needing Postman.

---

## 🚀 Features

- Book management using `Book` model in **Pydantic**  
- Add new books via **POST /create**  
- Search books via **GET /search** with query validation (min 3, max 100 characters)  
- Pagination support for search results  
- Persistent storage in `books.json`  
- Clean **dark mode UI** using HTML, CSS, and JS  
- Click on book images to open the cover in a new tab  
- Forms support submission via **Enter key**  
- User-friendly and responsive interface  

---

## 🛠 Installation & Running

1. **Clone the repository**

```bash
git clone https://github.com/BackendCourseDocs/assignment5-erfanRmoghadam
cd path 
```

2. **Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt 
```
4. **Run the FastAPI server**
```bash
uvicorn main:app --reload
```
The server will run at http://127.0.0.1:8000  

## 🔹 Usage
1️⃣ **Open the UI**

Open index.html in your browser (ensure the backend server is running).

Add new books using the Add Book form.

Search books using the Search form with pagination controls.

2️⃣ **API via Swagger**

Open http://127.0.0.1:8000/docs

Test POST /create to add a book

Test GET /search to search with query, page, and size

## Project Structure
```bash
.
├── main.py            # FastAPI backend
├── books.json         # Local book storage
├── requirements.txt   # All libraries and modules you need
├── index.html         # Frontend HTML
├── style.css          # Dark theme CSS
├── app.js             # JavaScript logic
└── .gitignore         # Ignored files (venv, books.json, etc.)
```
## 🔹 Technologies Used

Python 3.x

FastAPI - Modern, fast (high-performance) web framework

Pydantic - Data validation and settings management using Python type hints

JavaScript / HTML / CSS - Frontend for interactive UI

## 🔹 Notes

Any books added via the frontend or Swagger are saved in books.json for persistence.

Pagination is fully functional, and the image of each book is clickable to view the cover in a new tab.

The UI is responsive and works well on both desktop and mobile screens.