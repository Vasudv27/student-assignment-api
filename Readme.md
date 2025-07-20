📘 Student Assignment Management API
A simple RESTful API built using Django and Django REST Framework (DRF) to manage student assignments. This system supports authentication, soft deletion, update tracking via middleware, and webhook integration.

-----
🚀 Features
- Create, read, update, and soft-delete student assignments
- JWT-based authentication (only required for create, update, delete)
- Middleware to track created by and updated by
- Webhook support on assignment create/update
- Admin panel access for superusers
- Only non-deleted assignments are listed via API
-----
📚 API Endpoints

|Method|        Endpoint|                       Description|                            Auth Required|
| :-            | :-                            | :-                                    | :- 
|GET|     /api/assignments/                     |List all assignments                   |No|
|POST|    /api/assignments/                     |Create new assignment                  |Yes|
|GET|     /api/assignments/<id>/                |Retrieve a single assignment           |No|
|PUT|     /api/assignments/<id>/                |Update assignment completely           |Yes|
|PATCH|   /api/assignments/<id>/                |Partially update assignment            |Yes|
|DELETE|  /api/assignments/<id>/                |Soft delete assignment                 |Yes|
|POST|    /api/token/                           |Obtain JWT token                       |No|

-----
🔐 Authentication
- Token-based using SimpleJWT
- Obtain token by sending:

**POST** **/api/token/**
{
  "username": "yourusername",
  "password": "yourpassword"
}

- Use the received access token in headers:

Authorization: Bearer <your-access-token>

-----
🧠 Sample Assignment JSON
{
`  `"student_name": "Alice Johnson",
`  `"assignment_title": "Algebra Homework",
`  `"description": "Chapter 2 exercises",
`  `"due_date": "2025-08-01",
`  `"status": "Pending"
}

-----
⚙️ How to Run the API
*# Clone the repo*\
git clone https://github.com/yourusername/student-assignment-api.git\
cd student-assignment-api\
\
*# Create a virtual environment and activate*\
python -m venv env\
source env/bin/activate  *# or env\Scripts\activate on Windows*\
\
*# Install dependencies*\
pip install -r requirements.txt\
\
*# Run migrations*\
python manage.py migrate\
\
*# Create superuser*\
python manage.py createsuperuser\
\
*# Start the server*\
python manage.py runserver

Then visit:\
💎 http://127.0.0.1:8000/api/assignments/\
🔐 Admin: http://127.0.0.1:8000/admin/

-----
 Webhook Support
- Webhook is triggered on **create** and **update** of assignments.
- Payload includes the full assignment data.
-----
🧠 Tech Stack
- Python 3
- Django
- Django REST Framework
- SimpleJWT
- SQLite (default)
-----
👤 Author

GitHub: Vasudv27

-----
Screenshots for testing on Postman

Retrieving all data (GET)

![](Aspose.Words.d6fe543b-82cb-4cf6-be8a-f82761e3105d.001.png) 

Inserting new data (POST)

![](Aspose.Words.d6fe543b-82cb-4cf6-be8a-f82761e3105d.002.png)

Updating the data (PATCH)

![](Aspose.Words.d6fe543b-82cb-4cf6-be8a-f82761e3105d.003.png)

Deleting Data(DELETE)

![](Aspose.Words.d6fe543b-82cb-4cf6-be8a-f82761e3105d.004.png)

Admin Page 

![](Aspose.Words.d6fe543b-82cb-4cf6-be8a-f82761e3105d.005.png)
