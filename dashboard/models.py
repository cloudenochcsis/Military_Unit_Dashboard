from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Officer', 'Officer'),
        ('Soldier', 'Soldier'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Soldier')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        if hasattr(instance, 'profile'):
            instance.profile.save()
    except Exception as e:
        # Log the error for debugging
        print(f"Error saving user profile: {str(e)}")

class Soldier(models.Model):
    # Military Branches
    BRANCH_CHOICES = [
        ('Army', 'Army'),
        ('Navy', 'Navy'),
        ('Air Force', 'Air Force'),
        ('Marine Corps', 'Marine Corps'),
        ('Coast Guard', 'Coast Guard'),
    ]

    # Army Ranks
    ARMY_RANKS = [
        # Non-Commissioned Officers
        ('Private', 'Private'),
        ('Private First Class', 'Private First Class'),
        ('Specialist', 'Specialist'),
        ('Corporal', 'Corporal'),
        ('Sergeant', 'Sergeant'),
        ('Staff Sergeant', 'Staff Sergeant'),
        ('Sergeant First Class', 'Sergeant First Class'),
        ('Master Sergeant', 'Master Sergeant'),
        ('First Sergeant', 'First Sergeant'),
        ('Sergeant Major', 'Sergeant Major'),
        ('Command Sergeant Major', 'Command Sergeant Major'),
        ('Sergeant Major of the Army', 'Sergeant Major of the Army'),
        # Warrant Officers
        ('Warrant Officer 1', 'Warrant Officer 1'),
        ('Chief Warrant Officer 2', 'Chief Warrant Officer 2'),
        ('Chief Warrant Officer 3', 'Chief Warrant Officer 3'),
        ('Chief Warrant Officer 4', 'Chief Warrant Officer 4'),
        ('Chief Warrant Officer 5', 'Chief Warrant Officer 5'),
        # Commissioned Officers
        ('Second Lieutenant', 'Second Lieutenant'),
        ('First Lieutenant', 'First Lieutenant'),
        ('Captain', 'Captain'),
        ('Major', 'Major'),
        ('Lieutenant Colonel', 'Lieutenant Colonel'),
        ('Colonel', 'Colonel'),
        ('Brigadier General', 'Brigadier General'),
        ('Major General', 'Major General'),
        ('Lieutenant General', 'Lieutenant General'),
        ('General', 'General'),
        ('General of the Army', 'General of the Army'),
    ]

    # Navy Ranks
    NAVY_RANKS = [
        # Enlisted
        ('Seaman Recruit', 'Seaman Recruit'),
        ('Seaman Apprentice', 'Seaman Apprentice'),
        ('Seaman', 'Seaman'),
        ('Petty Officer Third Class', 'Petty Officer Third Class'),
        ('Petty Officer Second Class', 'Petty Officer Second Class'),
        ('Petty Officer First Class', 'Petty Officer First Class'),
        ('Chief Petty Officer', 'Chief Petty Officer'),
        ('Senior Chief Petty Officer', 'Senior Chief Petty Officer'),
        ('Master Chief Petty Officer', 'Master Chief Petty Officer'),
        ('Command Master Chief Petty Officer', 'Command Master Chief Petty Officer'),
        ('Fleet/Force Master Chief Petty Officer', 'Fleet/Force Master Chief Petty Officer'),
        ('Master Chief Petty Officer of the Navy', 'Master Chief Petty Officer of the Navy'),
        # Commissioned Officers
        ('Ensign', 'Ensign'),
        ('Lieutenant Junior Grade', 'Lieutenant Junior Grade'),
        ('Lieutenant', 'Lieutenant'),
        ('Lieutenant Commander', 'Lieutenant Commander'),
        ('Commander', 'Commander'),
        ('Captain', 'Captain'),
        ('Rear Admiral Lower Half', 'Rear Admiral Lower Half'),
        ('Rear Admiral Upper Half', 'Rear Admiral Upper Half'),
        ('Vice Admiral', 'Vice Admiral'),
        ('Admiral', 'Admiral'),
        ('Fleet Admiral', 'Fleet Admiral'),
    ]

    # Air Force Ranks
    AIR_FORCE_RANKS = [
        # Enlisted
        ('Airman Basic', 'Airman Basic'),
        ('Airman', 'Airman'),
        ('Airman First Class', 'Airman First Class'),
        ('Senior Airman', 'Senior Airman'),
        ('Staff Sergeant', 'Staff Sergeant'),
        ('Technical Sergeant', 'Technical Sergeant'),
        ('Master Sergeant', 'Master Sergeant'),
        ('Senior Master Sergeant', 'Senior Master Sergeant'),
        ('Chief Master Sergeant', 'Chief Master Sergeant'),
        ('Command Chief Master Sergeant', 'Command Chief Master Sergeant'),
        ('Chief Master Sergeant of the Air Force', 'Chief Master Sergeant of the Air Force'),
        # Commissioned Officers
        ('Second Lieutenant', 'Second Lieutenant'),
        ('First Lieutenant', 'First Lieutenant'),
        ('Captain', 'Captain'),
        ('Major', 'Major'),
        ('Lieutenant Colonel', 'Lieutenant Colonel'),
        ('Colonel', 'Colonel'),
        ('Brigadier General', 'Brigadier General'),
        ('Major General', 'Major General'),
        ('Lieutenant General', 'Lieutenant General'),
        ('General', 'General'),
        ('General of the Air Force', 'General of the Air Force'),
    ]

    # Marine Corps Ranks
    MARINE_RANKS = [
        # Enlisted
        ('Private', 'Private'),
        ('Private First Class', 'Private First Class'),
        ('Lance Corporal', 'Lance Corporal'),
        ('Corporal', 'Corporal'),
        ('Sergeant', 'Sergeant'),
        ('Staff Sergeant', 'Staff Sergeant'),
        ('Gunnery Sergeant', 'Gunnery Sergeant'),
        ('Master Sergeant', 'Master Sergeant'),
        ('First Sergeant', 'First Sergeant'),
        ('Master Gunnery Sergeant', 'Master Gunnery Sergeant'),
        ('Sergeant Major', 'Sergeant Major'),
        ('Sergeant Major of the Marine Corps', 'Sergeant Major of the Marine Corps'),
        # Commissioned Officers
        ('Second Lieutenant', 'Second Lieutenant'),
        ('First Lieutenant', 'First Lieutenant'),
        ('Captain', 'Captain'),
        ('Major', 'Major'),
        ('Lieutenant Colonel', 'Lieutenant Colonel'),
        ('Colonel', 'Colonel'),
        ('Brigadier General', 'Brigadier General'),
        ('Major General', 'Major General'),
        ('Lieutenant General', 'Lieutenant General'),
        ('General', 'General'),
        ('Commandant of the Marine Corps', 'Commandant of the Marine Corps'),
    ]

    # Coast Guard Ranks
    COAST_GUARD_RANKS = [
        # Enlisted
        ('Seaman Recruit', 'Seaman Recruit'),
        ('Seaman Apprentice', 'Seaman Apprentice'),
        ('Seaman', 'Seaman'),
        ('Petty Officer Third Class', 'Petty Officer Third Class'),
        ('Petty Officer Second Class', 'Petty Officer Second Class'),
        ('Petty Officer First Class', 'Petty Officer First Class'),
        ('Chief Petty Officer', 'Chief Petty Officer'),
        ('Senior Chief Petty Officer', 'Senior Chief Petty Officer'),
        ('Master Chief Petty Officer', 'Master Chief Petty Officer'),
        ('Command Master Chief Petty Officer', 'Command Master Chief Petty Officer'),
        ('District Master Chief Petty Officer', 'District Master Chief Petty Officer'),
        ('Area Master Chief Petty Officer', 'Area Master Chief Petty Officer'),
        ('Master Chief Petty Officer of the Coast Guard', 'Master Chief Petty Officer of the Coast Guard'),
        # Commissioned Officers
        ('Ensign', 'Ensign'),
        ('Lieutenant Junior Grade', 'Lieutenant Junior Grade'),
        ('Lieutenant', 'Lieutenant'),
        ('Lieutenant Commander', 'Lieutenant Commander'),
        ('Commander', 'Commander'),
        ('Captain', 'Captain'),
        ('Rear Admiral Lower Half', 'Rear Admiral Lower Half'),
        ('Rear Admiral Upper Half', 'Rear Admiral Upper Half'),
        ('Vice Admiral', 'Vice Admiral'),
        ('Admiral', 'Admiral'),
    ]

    # Status Choices
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Deployed', 'Deployed'),
    ]

    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES, default='Army')
    rank = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    service_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.rank} {self.name}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Operational', 'Operational'),
        ('Maintenance', 'Maintenance'),
        ('Retired', 'Retired'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Operational')
    assigned_to = models.ForeignKey(Soldier, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.serial_number})"
