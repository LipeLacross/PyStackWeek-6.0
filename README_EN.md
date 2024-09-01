# Certificate Generation System

A project developed with Django and SQLite for event management and certificate generation. This system is ideal for events where issuing certificates to participants is necessary.

## 🔨 Project Features

- **Event Management**: Manage events with detailed information.
- **Certificate Generation**: Create and store customized certificates in PNG format.
- **Certificate Search**: Functionality to search for certificates by email.
- **Certificate Viewing**: Display generated certificates for participants and administrators.

### Visual Example of the Project

![image](https://github.com/user-attachments/assets/d5aa7568-f98d-45a3-959f-ffc44087cadd)
![image](https://github.com/user-attachments/assets/3e143541-ac6e-4567-b73e-bceec462256f)
![image](https://github.com/user-attachments/assets/7e08598f-3e47-4c42-b1d0-8775449cea66)
![image](https://github.com/user-attachments/assets/1aaa8d21-9200-4888-84e4-074deb938832)

## ✔️ Techniques and Technologies Used

- **Django**: Web framework for rapid and secure development.
- **SQLite**: Lightweight database for data storage.
- **Python**: Programming language used for the backend.
- **Pillow**: Library for image manipulation and certificate generation.

### Features and Descriptions

- **Certificate Creation**: Model and view to generate certificates with event and participant information.
- **Certificate Display**: Interface for viewing and downloading generated certificates.
- **Certificate Search**: Form to search for certificates by participant's email.
- **Event Management**: Pages to manage events and view participants.

## 📂 File Structure

- **cliente/**: Code related to the client module.
- **eventos/**: Code related to the events module.
- **media/**: Media files, such as images and certificates.
- **templates/**: HTML templates used by the project.
- **type_event/**: Code related to event types.
- **usuarios/**: Code related to the users module.
- **.gitignore**: File to ignore files and directories in Git.
- **LICENSE**: Project license file.
- **README.md**: This file with project documentation.
- **db.sqlite3**: SQLite database.
- **manage.py**: Django management script.
- **requirements.txt**: List of project dependencies.

## 🛠️ Running the Project

### Prerequisites

- Python 3.x installed on your machine
- Django installed (see `requirements.txt` for dependencies)

### Basic Commands

- `pip install -r requirements.txt` -> Install the project dependencies.
- `venv\Scripts\Activate` -> Activate the virtual environment.
- `python manage.py makemigrations` -> Create migration files based on changes to Django models.
- `python manage.py migrate` -> Apply pending migrations to the database.
- `python manage.py runserver` -> Start the Django development server at http://localhost:8000/.

## PSW 6.0
[PSW 6.0](https://grizzly-amaranthus-f6a.notion.site/PSW-6-0-4926964e82e843e4b95a00f5107c40b8)

## Notion All Classes
[Notion All Classes](https://grizzly-amaranthus-f6a.notion.site/PSW-e33ff4be6f624a87bc1e8574ba435e8d)
