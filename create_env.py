import os
import secrets
import sys

# Generate a secure secret key
secret_key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))

# Create .env file with secure configuration
with open('.env', 'w') as f:
    f.write(f"DEBUG={os.getenv('DEBUG', '1')}\n")
    f.write(f"SECRET_KEY={secret_key}\n")
    f.write("DATABASE_URL=postgres://postgres:postgres@db:5432/military_dashboard\n")
    f.write("ALLOWED_HOSTS=localhost,127.0.0.1\n")

print(".env file created with secure configuration!")
