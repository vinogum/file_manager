# File Manager API

This is a Django-based REST API for a file management system. It allows users to upload, manage, and version their files.

## Features

- **User Authentication**: Users can sign up and log in to the system. [cite: 37, 38]  
- **File Management**: Users can upload, view, and delete their files. [cite: 86]  
- **File Versioning**: Every upload of a file with the same name creates a new version. [cite: 297-303]  
- **Download Files**: Users can download any version of their files. [cite: 110-114]  
- **Organized Storage**: Files are stored in a structured way on the server. The path is based on the user's ID and the file's ID. [cite: 128]  
- **Docker Support**: The project includes a `Dockerfile` for easy setup and deployment. [cite: 7]

## Project Structure

The project has two main Django apps: `accounts` and `files`. [cite: 3, 4]

file_manager/
├── accounts/ # Handles user registration and authentication
├── files/ # Handles file and version management
├── file_manager/ # Main Django project settings
├── media/ # Stores uploaded files
├── Dockerfile # Docker configuration
└── Makefile # Helper commands


## API Endpoints

### Authentication

- `POST /accounts/signup/`: Register a new user  
  - **Body**: `username`, `password`, `confirm_password`

- `POST /accounts/login/`: Log in a user  
  - **Body**: `username`, `password`

- `POST /accounts/logout/`: Log out a user

### Files

- `GET /files/`: Get a list of all files for the logged-in user [cite: 193]  
- `POST /files/`: Create a new file. This also creates the first version of the file [cite: 196]  
  - **Body (form-data)**: `url` (the path where you want to save the file), `file_data` (the file itself) [cite: 197-200]  
- `GET /files/{id}/`: Get details of a specific file [cite: 205]  
- `DELETE /files/{id}/`: Delete a file and all its versions [cite: 209]

### File Versions

- `GET /files/{file_id}/versions/`: Get a list of all versions for a specific file [cite: 219]  
- `POST /files/{file_id}/versions/`: Upload a new version of an existing file  
- `GET /files/{file_id}/versions/{id}/`: Download a specific version of a file [cite: 223]  
- `DELETE /files/{file_id}/versions/{id}/`: Delete a specific version of a file

## Setup and Installation

### With Docker

1. **Build the image:**
    ```sh
    docker build -t file-manager .
    ```

2. **Run the container:**
    ```sh
    docker run -p 8000:8000 file-manager
    ```

### Local Setup

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd file-manager
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**  
   The `Makefile` has a command to create the `requirements.txt` file. [cite: 353, 354]
    ```sh
    make requirements
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    make db
    ```

5. **Run the server:**
    ```sh
    make run
    ```

The server will start at `http://127.0.0.1:8000`.

## How to Run Tests

To run the tests for the application, use this command:

```sh
make test
