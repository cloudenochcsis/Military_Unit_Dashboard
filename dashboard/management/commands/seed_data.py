from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import Soldier, Equipment
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@military.gov', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        
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
        
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully'))
