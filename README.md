# 🥘 Recipe App

A full-stack Recipe Sharing web application built using **Django**, **Bulma CSS**, and **Bootstrap**. Users can create, view, edit, delete, and rate recipes. Features include authentication, category filtering, and live UI integration without Postman!

---

## 🚀 Features

- 🔐 User Registration, Login, Logout
- 📄 Add, Edit & Delete Recipes (author-only access)
- 🍽️ Category filter (Breakfast, Lunch, Dinner, etc.)
- 🔍 Search by title or description
- ⭐ User rating system (1 to 5 stars)
- 📊 Average rating display per recipe
- 🎨 Responsive and clean UI using Bulma & Bootstrap
- 🧪 REST API with Django REST Framework

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Bulma CSS, Bootstrap
- **Database**: SQLite (default)
- **Auth**: Django's built-in auth system
- **WebSocket Ready**: Can integrate Channels for live features

---

## 🧪 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shashank-712/Recipe-App.git
   cd Recipe-App
   ```
2. **Create and activate virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```
   python manage.py migrate
   ```
5. **Create superuser (optional)**
   ```
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```
   python manage.py runserver
   ```
7. **Open in Browser**
   ```
   Visit: http://localhost:8000/api/ui/recipes/
   ```


📁 Project Structure
```
├── recipes/                 # App folder
│   ├── models.py            # Models (Recipe, Ingredient, Rating)
│   ├── views.py             # UI + API views
│   ├── templates/           # HTML Templates
│   ├── forms.py             # Django forms
├── Recipe App/             # Main project folder
├── static/                 # Optional for custom styling
├── db.sqlite3              # Default SQLite DB
├── .env                    # Environment variables (excluded by .gitignore)
├── .gitignore              # Git ignored files (including venv & .env)
├── README.md
└── requirements.txt
```

Author Made with 💻 by Shashank Rawat👹 👉 github.com/Shashank-712
   

