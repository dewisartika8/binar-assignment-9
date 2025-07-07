# Python Authentication App

This project implements authentication features for a web application, including user sign up and sign in functionalities. The application is structured into a backend and a frontend, with a focus on data validation and secure storage of user credentials.

## Features

- User registration with email and password
- User login with email and password
- Data validation for user inputs
- Secure password storage using hashing
- API documentation using Swagger

## Project Structure

```
binar-assignment-9
├── backend
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── database.py
│   └── requirements.txt
├── frontend
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   ├── login.html
│   │   └── register.html
│   └── app.py
├── docs
│   ├── swagger.yaml
│   └── implementation_flow.md
├── tests
│   ├── test_auth.py
│   └── test_validation.py
└── README.md
```

## Cara Menjalankan Aplikasi

1. **Clone repository & masuk ke folder backend**
   ```bash
   git clone <repo-url>
   cd binar-assignment-9/backend
   ```

2. **Buat virtual environment & install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Jalankan backend**
   ```bash
   python app.py
   ```
   Backend akan berjalan di `http://127.0.0.1:5000` (atau sesuai port di app.py)

4. **Akses dokumentasi API (Swagger)**
   Buka browser ke:  
   ```
   http://127.0.0.1:8000/docs
   ```

5. **Jalankan frontend**
   Buka terminal baru, lalu:
   ```bash
   cd ../frontend
   python app.py
   ```
   Frontend akan berjalan di `http://127.0.0.1:5000`

## API Endpoints

- **POST /api/register**: Register a new user.
  - Request Body: `{ "email": "user@example.com", "password": "yourpassword" }`
  - Response: `{ "message": "User registered successfully." }`

- **POST /api/login**: Log in an existing user.
  - Request Body: `{ "email": "user@example.com", "password": "yourpassword" }`
  - Response: `{ "message": "Login successful." }`

## Cara Testing

1. **Testing API Otomatis**
   Di folder backend:
   ```bash
   pytest
   ```

2. **Testing Manual**
   - Gunakan Swagger UI (`/docs`) untuk mencoba endpoint register & login.
   - Coba akses form login/register di frontend dan pastikan alur otentikasi berjalan.

## API Documentation

API endpoints are documented using Swagger. You can find the documentation in the `docs/swagger.yaml` file.

## Implementation Flow

For a detailed explanation of the implementation flow, refer to the `docs/implementation_flow.md` file.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.

## License

This project is licensed under the MIT License.

from fastapi import FastAPI
app = FastAPI()