# 📝 Notes API

A robust RESTful API for managing notes built with Django REST Framework and PostgreSQL.

## ✨ Features

- 🎯 Complete CRUD operations for notes
- 🏷️ Note categorization (Personal, Work, Finances, Others)
- 🔒 UUID-based identifiers for security
- 📊 PostgreSQL database integration
- ✅ Field validations
- 🌐 RESTful architecture

## 🛠️ Tech Stack

- **Framework:** Django 5.2
- **API Framework:** Django REST Framework
- **Database:** PostgreSQL
- **Language:** Python 3.13
- **Dependencies:** psycopg2-binary

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- PostgreSQL
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Toussaint-Manzi/simple-django-notes-CRUD-app.git
cd simple-django-notes-CRUD-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL:
```bash
psql postgres
CREATE DATABASE notes_db;
\q
```

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create superuser (optional):
```bash
python manage.py createsuperuser
```

## 🔥 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/notes/` | List all notes |
| POST | `/api/v1/notes/` | Create a new note |
| GET | `/api/v1/notes/{id}/` | Retrieve a note |
| PATCH | `/api/v1/notes/{id}/` | Update a note |
| DELETE | `/api/v1/notes/{id}/` | Delete a note |

## 📝 Request/Response Examples

### Create Note
```bash
POST /api/v1/notes/
{
    "title": "Meeting Notes",
    "content": "Discuss project timeline",
    "type": "work"
}
```

### Response
```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Meeting Notes",
    "content": "Discuss project timeline",
    "type": "work",
    "created_at": "2024-04-22T12:00:00Z",
    "updated_at": "2024-04-22T12:00:00Z"
}
```

## ✅ Validation Rules

- **Title:** Minimum 3 characters
- **Content:** Minimum 10 characters
- **Type:** Must be one of: personal, work, finances, others

## 🏗️ Project Structure

```
notes_api/
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── core/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## 💻 Development

### Running the Server

```bash
python manage.py runserver
```
The API will be available at `http://localhost:8000/api/v1/`

### Running Tests

```bash
python manage.py test
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
