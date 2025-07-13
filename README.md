# Military Unit Dashboard

A simple MVP Django web application for military unit management, focused on basic functionality for Kubernetes deployment practice. This project serves as a learning tool for DevOps engineers practicing Kubernetes deployment, scaling, and management.

## Dashboard Overview

![Unit Dashboard Overview](images/Unit_dashboard_overview.png)

## Soldiers Dashboard

![Soldiers Dashboard](images/Soldiers.png)

## Equipment Dashboard

![Equipment Dashboard](images/Equipments.png)

## Features

- **User Authentication**: Login/logout functionality using Django's built-in authentication system
- **Soldier Management**: Add, edit, delete, and view soldiers with basic information
- **Equipment Tracking**: Add, edit, delete, and view equipment with assignment to soldiers
- **Dashboard**: View counts, recent additions, and equipment status distribution
- **Admin Panel**: Django admin interface for data management
- **Kubernetes Ready**: Includes Dockerfile, docker-compose.yml, and Kubernetes manifests

## User Authentication

![Register](images/Register.png)

![Secure Login](images/secure_login.png)

## Technology Stack

- **Backend**: Python/Django 4.2+
- **Database**: PostgreSQL
- **Frontend**: Django Templates with Bootstrap CSS
- **Authentication**: Django's built-in authentication
- **Containerization**: Docker
- **Orchestration**: Kubernetes

## Local Development Setup

### Prerequisites

- Python 3.11+
- pip
- PostgreSQL (optional, SQLite is used by default for development)
- Docker and Docker Compose (optional)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/cloudenochcsis/Military_Unit_Dashboard.git
   cd Military_Unit_Dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables (optional for development):
   ```
   DEBUG=1
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/military_dashboard
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py makemigrations dashboard
   python manage.py migrate dashboard
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Load sample data (optional):
   ```bash
   python manage.py seed_data
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the application at http://127.0.0.1:8000

10. Login with the superuser credentials you created in step 6

## Docker Deployment

1. Create a `.env` file with the following required environment variables:
   ```bash
   cp .env.example .env
   # Edit .env to customize settings if needed
   ```

2. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the application at http://localhost:8000

4. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. Load sample data (optional):
   ```bash
   docker-compose exec web python manage.py seed_data
   ```

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster
- kubectl configured to connect to your cluster

### Deployment Steps

1. Build and push the Docker image to a registry:
   ```bash
   docker build -t your-registry/military-dashboard:latest .
   docker push your-registry/military-dashboard:latest
   ```

2. Update the image name in `kubernetes/deployment.yaml` to match your registry.

3. Apply the Kubernetes manifests:
   ```bash
   kubectl apply -f kubernetes/configmap.yaml
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

4. Access the application through the Ingress hostname (you may need to add the hostname to your /etc/hosts file):
   ```
   military-dashboard.local
   ```

## Health Check Endpoint

The application provides a health check endpoint at `/health/` that returns a JSON response with status "ok". This endpoint is used by Kubernetes for liveness and readiness probes.



## Notes for Production Deployment

- Change the `SECRET_KEY` to a secure value in production
- Set `DEBUG=0` in production
- Update `ALLOWED_HOSTS` with your production domain
- Consider using a managed PostgreSQL service
- Set up proper TLS/SSL for secure connections
- Implement proper backup strategies for the database
- Configure appropriate resource limits in Kubernetes manifests

## Version History

- **v1.0.0** - Initial MVP release with core features (Soldier and Equipment management, Dashboard, Docker and Kubernetes support)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
