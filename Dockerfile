# Use multi-stage build for production
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Final stage
FROM python:3.11-slim

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd -r app && useradd -r -g app app

# Create appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# Install dependencies
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy project
COPY . $APP_HOME

# Collect static files
RUN python manage.py collectstatic --noinput

# Change ownership to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app

# Run gunicorn
CMD gunicorn military_dashboard.wsgi:application --bind 0.0.0.0:8000
