from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Soldier, Equipment, UserProfile

class SoldierForm(forms.ModelForm):
    class Meta:
        model = Soldier
        fields = ['name', 'branch', 'rank', 'email', 'phone', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'rank': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].choices = Soldier.BRANCH_CHOICES
        # Set default rank choices to Army ranks
        self.fields['rank'].choices = Soldier.ARMY_RANKS

    def clean(self):
        cleaned_data = super().clean()
        branch = cleaned_data.get('branch')
        rank = cleaned_data.get('rank')
        
        # Validate that the rank is valid for the selected branch
        if branch and rank:
            valid_ranks = {}
            valid_ranks['Army'] = Soldier.ARMY_RANKS
            valid_ranks['Navy'] = Soldier.NAVY_RANKS
            valid_ranks['Air Force'] = Soldier.AIR_FORCE_RANKS
            valid_ranks['Marine Corps'] = Soldier.MARINE_RANKS
            valid_ranks['Coast Guard'] = Soldier.COAST_GUARD_RANKS
            
            if rank not in dict(valid_ranks[branch]):
                self.add_error('rank', f"Invalid rank for {branch}")

    def save(self, commit=True):
        soldier = super().save(commit=False)
        if commit:
            soldier.save()
        return soldier

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type', 'serial_number', 'status', 'assigned_to']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
        }

class SoldierSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'})
    )

class UserRegistrationForm(UserCreationForm):
    ROLE_CHOICES = UserProfile.ROLE_CHOICES
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create or get the user profile
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.role = self.cleaned_data['role']
            profile.save()
        
        return user
