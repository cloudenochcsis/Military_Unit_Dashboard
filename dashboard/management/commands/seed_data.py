from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import Soldier, Equipment, UserProfile
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Create users with different roles if they don't exist
        roles = ['Admin', 'Officer', 'Soldier']
        
        # Create superuser/admin if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser('admin', 'admin@military.gov', 'adminpassword')
            # Update the role since UserProfile is created automatically by signal
            admin_user.profile.role = 'Admin'
            admin_user.profile.save()
            self.stdout.write(self.style.SUCCESS('Admin user created'))
        
        # Create officer users
        if not User.objects.filter(username='officer1').exists():
            officer1 = User.objects.create_user('officer1', 'officer1@military.gov', 'officerpass')
            # Update the role since UserProfile is created automatically by signal
            officer1.profile.role = 'Officer'
            officer1.profile.save()
            self.stdout.write(self.style.SUCCESS('Officer1 user created'))
            
        if not User.objects.filter(username='officer2').exists():
            officer2 = User.objects.create_user('officer2', 'officer2@military.gov', 'officerpass')
            # Update the role since UserProfile is created automatically by signal
            officer2.profile.role = 'Officer'
            officer2.profile.save()
            self.stdout.write(self.style.SUCCESS('Officer2 user created'))
        
        # Create soldier users
        for i in range(1, 4):  # Create 3 soldier users
            username = f'soldier{i}'
            if not User.objects.filter(username=username).exists():
                soldier_user = User.objects.create_user(
                    username, 
                    f'{username}@military.gov', 
                    'soldierpass'
                )
                # No need to update role since 'Soldier' is the default
                self.stdout.write(self.style.SUCCESS(f'{username.capitalize()} user created'))
        
        # Create soldiers if none exist
        if Soldier.objects.count() == 0:
            ranks = ['Private', 'Corporal', 'Sergeant', 'Lieutenant', 'Captain', 'Major', 'Colonel']
            statuses = ['Active', 'On Leave', 'Deployed']
            
            soldiers = []
            for i in range(1, 21):  # Create 20 soldiers
                rank = random.choice(ranks)
                name = f"Soldier {i}"
                email = f"soldier{i}@military.gov"
                phone = f"555-{random.randint(1000, 9999)}"
                status = random.choice(statuses)
                
                soldier = Soldier(
                    rank=rank,
                    name=name,
                    email=email,
                    phone=phone,
                    status=status
                )
                soldiers.append(soldier)
            
            Soldier.objects.bulk_create(soldiers)
            self.stdout.write(self.style.SUCCESS(f'Created {len(soldiers)} soldiers'))
        
        # Create equipment if none exists
        if Equipment.objects.count() == 0:
            equipment_types = ['Rifle', 'Pistol', 'Helmet', 'Body Armor', 'Radio', 'Night Vision', 'Medical Kit']
            statuses = ['Operational', 'Maintenance', 'Retired']
            
            soldiers = list(Soldier.objects.all())
            equipment = []
            
            for i in range(1, 51):  # Create 50 equipment items
                name = f"{random.choice(equipment_types)} {i}"
                equipment_type = name.split()[0]
                serial_number = f"SN-{random.randint(10000, 99999)}"
                status = random.choice(statuses)
                
                # 80% chance of being assigned to a soldier if operational
                assigned_to = None
                if status == 'Operational' and random.random() < 0.8:
                    assigned_to = random.choice(soldiers)
                
                equipment_item = Equipment(
                    name=name,
                    type=equipment_type,
                    serial_number=serial_number,
                    status=status,
                    assigned_to=assigned_to
                )
                equipment.append(equipment_item)
            
            Equipment.objects.bulk_create(equipment)
            self.stdout.write(self.style.SUCCESS(f'Created {len(equipment)} equipment items'))
        
        # Summary of created data
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully'))
        self.stdout.write(self.style.SUCCESS(f'Users created: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Soldiers created: {Soldier.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Equipment items created: {Equipment.objects.count()}'))
        
        # Print login credentials for testing
        self.stdout.write(self.style.SUCCESS('\nTest login credentials:'))
        self.stdout.write('Admin user: username=admin, password=adminpassword')
        self.stdout.write('Officer users: username=officer1/officer2, password=officerpass')
        self.stdout.write('Soldier users: username=soldier1/soldier2/soldier3, password=soldierpass')
