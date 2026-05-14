# S3 Simple Example & Person CRUD

This project is a Python-based REST API that demonstrates how to interact with AWS S3 and perform CRUD operations on a PostgreSQL database using SQLAlchemy. It follows the principles of Clean Architecture to ensure maintainability and scalability.

## Technologies Used

- **Python 3**: Core programming language.
- **Flask**: Lightweight web framework for building the API.
- **SQLAlchemy & Flask-SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Relational database for persistent storage.
- **Boto3**: AWS SDK for Python to interact with S3.
- **Docker & Docker Compose**: For containerizing the database and AWS Local services (LocalStack/Floci).

## Project Structure

The project follows a simplified Clean Architecture pattern:

```text
.
├── app/
│   ├── controllers/      # Interface Adapters: Flask Blueprints and Request Handling
│   ├── services/         # Use Cases: Business logic layer
│   ├── infrastructure/   # Frameworks & Drivers: Repository implementations and S3 client
│   ├── models/           # Domain Entities: SQLAlchemy models
│   ├── config.py         # Configuration settings
│   └── database.py       # Database initialization
├── main.py               # Entry point of the application
├── requirements.txt      # Project dependencies
├── docker-compose.yml    # Infrastructure services (PostgreSQL, LocalStack)
├── boostrap.sh           # Script to setup the environment and database
└── teardown.sh           # Script to clean up the environment
```

## API Endpoints

### Person CRUD (`/api/v1/person`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/v1/person` | Create a new person record. |
| GET    | `/api/v1/person` | Retrieve all person records. |
| GET    | `/api/v1/person/<id>` | Retrieve a specific person by ID. |
| PUT    | `/api/v1/person/<id>` | Update an existing person record. |
| DELETE | `/api/v1/person/<id>` | Delete a person record. |

### S3 Operations (`/s3`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/s3/all` | List all files in the S3 bucket. |
| POST   | `/s3` | Upload a file to the S3 bucket. |
| GET    | `/s3/<filename>` | Download a specific file from S3. |
| DELETE | `/s3/<filename>` | Delete a file from the S3 bucket. |

### Health Checks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/health` | Check application health status. |
| GET    | `/ready` | Check if the application is ready to handle requests. |

## Getting Started

### Prerequisites

- **Docker & Docker Compose**: Installed and running.
- **AWS CLI**: Installed and configured.

### Setup Instructions

1. **Setup Infrastructure**:
   Primero se debe ejecutar el script de bootstrap para levantar los servicios base:
   ```bash
   chmod +x boostrap.sh
   ./boostrap.sh
   ```

2. **Create AWS Resources**:
   Utiliza la AWS CLI para crear el bucket de S3 y la instancia de RDS (PostgreSQL).

   **RDS (Postgresql):**
   ```bash
   aws rds create-db-instance \
     --db-instance-identifier mypostgres \
     --db-instance-class db.t3.micro \
     --engine postgres \
     --master-username admin \
     --master-user-password secret123 \
     --allocated-storage 20
   ```

   **Bucket S3:**
   ```bash
   aws s3 mb s3://my-bucket
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
