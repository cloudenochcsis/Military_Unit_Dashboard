from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.db.models import Count, Q
from .models import Soldier, Equipment, UserProfile
from .forms import SoldierForm, EquipmentForm, SoldierSearchForm, UserRegistrationForm

# Helper functions for role-based access control
def is_admin(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == 'Admin'
    except:
        return False

def is_officer_or_admin(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role in ['Officer', 'Admin']
    except:
        return False

# Authentication views
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

# Health check endpoint for Kubernetes probes
def health_check(request):
    return JsonResponse({'status': 'ok'})

# Dashboard view
@login_required
def dashboard(request):
    # Get counts for dashboard
    soldier_count = Soldier.objects.count()
    equipment_count = Equipment.objects.count()
    operational_equipment_count = Equipment.objects.filter(status='Operational').count()
    
    # Get equipment status distribution for charts
    equipment_status = Equipment.objects.values('status').annotate(count=Count('status'))
    
    # Get recent additions
    recent_soldiers = Soldier.objects.order_by('-created_at')[:5]
    recent_equipment = Equipment.objects.order_by('-created_at')[:5]
    
    context = {
        'soldier_count': soldier_count,
        'equipment_count': equipment_count,
        'operational_equipment_count': operational_equipment_count,
        'equipment_status': equipment_status,
        'recent_soldiers': recent_soldiers,
        'recent_equipment': recent_equipment,
    }
    
    return render(request, 'dashboard.html', context)

# Soldier CRUD views
@login_required
@user_passes_test(is_officer_or_admin, login_url='dashboard')
def soldier_list(request):
    search_form = SoldierSearchForm(request.GET)
    soldiers = Soldier.objects.all().order_by('name')
    
    # Handle search
    if search_form.is_valid() and search_form.cleaned_data.get('search'):
        search_query = search_form.cleaned_data.get('search')
        soldiers = soldiers.filter(Q(name__icontains=search_query) | Q(rank__icontains=search_query))
    
    context = {
        'soldiers': soldiers,
        'search_form': search_form,
    }
    return render(request, 'soldier_list.html', context)

@login_required
@user_passes_test(is_officer_or_admin, login_url='dashboard')
def soldier_detail(request, pk):
    soldier = get_object_or_404(Soldier, pk=pk)
    assigned_equipment = soldier.equipment.all()
    
    context = {
        'soldier': soldier,
        'assigned_equipment': assigned_equipment,
    }
    return render(request, 'soldier_detail.html', context)

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def soldier_create(request):
    if request.method == 'POST':
        form = SoldierForm(request.POST)
        if form.is_valid():
            soldier = form.save()
            messages.success(request, f'Soldier {soldier.name} created successfully!')
            return redirect('soldier_list')
    else:
        form = SoldierForm()
    
    return render(request, 'soldier_form.html', {'form': form, 'title': 'Add Soldier'})

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def soldier_update(request, pk):
    soldier = get_object_or_404(Soldier, pk=pk)
    
    if request.method == 'POST':
        form = SoldierForm(request.POST, instance=soldier)
        if form.is_valid():
            form.save()
            messages.success(request, f'Soldier {soldier.name} updated successfully!')
            return redirect('soldier_detail', pk=soldier.pk)
    else:
        form = SoldierForm(instance=soldier)
    
    return render(request, 'soldier_form.html', {'form': form, 'title': 'Update Soldier'})

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def soldier_delete(request, pk):
    soldier = get_object_or_404(Soldier, pk=pk)
    
    if request.method == 'POST':
        name = soldier.name
        soldier.delete()
        messages.success(request, f'Soldier {name} deleted successfully!')
        return redirect('soldier_list')
    
    return render(request, 'soldier_confirm_delete.html', {'soldier': soldier})

# Equipment CRUD views
@login_required
@user_passes_test(is_officer_or_admin, login_url='dashboard')
def equipment_list(request):
    equipment = Equipment.objects.all().order_by('name')
    context = {
        'equipment': equipment,
    }
    return render(request, 'equipment_list.html', context)

@login_required
@user_passes_test(is_officer_or_admin, login_url='dashboard')
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    context = {
        'equipment': equipment,
    }
    return render(request, 'equipment_detail.html', context)

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, f'Equipment {equipment.name} created successfully!')
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    
    return render(request, 'equipment_form.html', {'form': form, 'title': 'Add Equipment'})

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, f'Equipment {equipment.name} updated successfully!')
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    
    return render(request, 'equipment_form.html', {'form': form, 'title': 'Update Equipment'})

@login_required
@user_passes_test(is_admin, login_url='dashboard')
def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    
    if request.method == 'POST':
        name = equipment.name
        equipment.delete()
        messages.success(request, f'Equipment {name} deleted successfully!')
        return redirect('equipment_list')
    
    return render(request, 'equipment_confirm_delete.html', {'equipment': equipment})

