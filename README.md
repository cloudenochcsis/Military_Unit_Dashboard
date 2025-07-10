# Military Unit Dashboard

A simple MVP Django web application for military unit management, focused on basic functionality for Kubernetes deployment practice. This project serves as a learning tool for DevOps engineers practicing Kubernetes deployment, scaling, and management.

## Features

- **User Authentication**: Login/logout functionality using Django's built-in authentication system
- **Soldier Management**: Add, edit, delete, and view soldiers with basic information
- **Equipment Tracking**: Add, edit, delete, and view equipment with assignment to soldiers
- **Dashboard**: View counts, recent additions, and equipment status distribution
- **Admin Panel**: Django admin interface for data management
- **Kubernetes Ready**: Includes Dockerfile, docker-compose.yml, and Kubernetes manifests

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
   git clone git@github.com:cloudenochcsis/Military_Unit_Dashboard.git
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

1. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Access the application at http://localhost:8000

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

## Project Structure

```
military_dashboard/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── db.sqlite3                # SQLite database file for development
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── military_dashboard/
│   ├── __init__.py
│   ├── settings.py           # Updated with LOGIN_URL settings
│   ├── urls.py
│   └── wsgi.py
├── dashboard/
│   ├── models.py             # Soldier and Equipment models
│   ├── views.py              # Views for dashboard, auth, and CRUD operations
│   ├── urls.py               # URL patterns for all views
│   ├── forms.py              # Forms for Soldier and Equipment
│   ├── admin.py              # Admin configuration
│   ├── migrations/           # Database migrations
│   │   └── 0001_initial.py
│   └── management/
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           └── seed_data.py  # Command to generate sample data
├── static/
│   ├── css/
│   │   └── style.css        # Custom CSS styles
│   └── js/
│       └── main.js          # JavaScript for UI interactions
└── templates/
    ├── base.html            # Base template with navigation
    ├── dashboard.html       # Dashboard with metrics and charts
    ├── login.html           # Login form
    ├── soldier_list.html    # List of soldiers with search
    ├── soldier_detail.html  # Soldier details and assigned equipment
    ├── soldier_form.html    # Form for creating/editing soldiers
    ├── soldier_confirm_delete.html
    ├── equipment_list.html  # List of equipment
    ├── equipment_detail.html # Equipment details
    ├── equipment_form.html  # Form for creating/editing equipment
    └── equipment_confirm_delete.html
```

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
