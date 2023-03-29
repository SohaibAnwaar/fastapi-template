# Fast API Boilerplate
This is a boilerplate for a Fast API project. It includes a basic setup for a Fast API project with a PostgreSQL database, a Dockerfile, a docker-compose file, and a Makefile.

## Getting Started
### Prerequisites
- Python 3.9.13

### Installing
1. Clone the repository
2. conda create -n fastapi-boilerplate python=3.8
3. conda activate fastapi-boilerplate
4. pip install -r requirements.txt

### Running the project
1. Run `uvicorn app.main:app --reload` to start the server
2. Go to `http://localhost:8000/docs` to see the API documentation
