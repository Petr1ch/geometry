# Geometry Service

## Requirements
- Python 3.10
- FastAPI
- Poetry
- Docker (optional)

## Getting Started

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Petr1ch/geometry.git

2. Install dependencies with Poetry
   ```bash
   poetry install

3. Create database and make database migrations
   ```bash
   alembic upgrade head

4. Run FastAPI application
   ```bash
   python app.py
   
### Docker Compose Setup
1. Copy to ```json_dump```  folder your GeoJSON file
2. Build and run the Docker containers. Database, migrations and data migration will be done by itself
   ```bash
   docker-compose up --build

#### Note: Current docker-compose configuration for Mac M1. Check if you need to change POSTGRES_HOST env.

## Endpoints

### 1. Get Nearby Fields

- **Endpoint:** `GET /fields/nearby/`
- **Description:** Get fields within a specified radius from a given point.

### 2. Get Fields in Parallelogram

- **Endpoint:** `POST /get_fields_in_parallelogram`
- **Description:** Get fields that intersect with a specified parallelogram.

### 3. Get Fields Intersecting Geometry

- **Endpoint:** `POST /get_fields_intersect_geometry`
- **Description:** Get fields that intersect with a specified geometry figure.

### 4. Calculate Agricultural Metrics

- **Endpoint:** `GET /calculate__metrics`
- **Description:** Calculate agricultural metrics for fields in a specified region.


## API Documentation

The API documentation (Swagger UI) can be accessed at `http://127.0.0.1:8000/docs`.