from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Student
from django.contrib.auth.models import User 


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})


def logout_page(request):
    logout(request)
    return redirect('login')


# ➕ ADD
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            age=request.POST['age']
        )
        return redirect('dashboard')

    return render(request, 'add_student.html')


# ✏ EDIT
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()
        return redirect('dashboard')

    return render(request, 'edit_student.html', {'student': student})


# ❌ DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('dashboard')


    from django.shortcuts import render, redirect
from .models import Student


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    query = request.GET.get('q')   # get search input

    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            course__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, 'dashboard.html', {
        'students': students
    })

    from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def signup_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Username exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        # Create user
        User.objects.create_user(username=username, password=password)

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')