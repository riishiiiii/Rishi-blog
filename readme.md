# Blog Application

### Introduction
This README provides a step-by-step guide to set up and run Application Name locally on your machine.


### Prerequisites
Before you begin, ensure you have the following installed on your local machine:
- Docker: Install Docker
- Docker Compose (usually comes with Docker Desktop): Install Docker Compose

### Getting Started
Follow these steps to set up and run the Django project locally using Docker:
1. Follow these steps to set up and run the Django project locally using Docker:
```bash
git clone https://github.com/riishiiiii/Rishi-blog.git
```

3. Navigate to the project directory:
```bash
cd Rishi-blog/blog
```

4. Build the Docker image:
```bash
docker-compose build
```

6. Run the Docker container:
```bash
docker-compose up
```

8. Access the Django application in your web browser at http://localhost:8000

### Additional Information
The Django application is configured to run with SQLite by default. The database file will be stored within the Docker container.
You can stop the Docker container by pressing Ctrl + C in the terminal where it is running.
