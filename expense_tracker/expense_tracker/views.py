from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from .models import Expense, ExpenseSource
from .forms import ExpenseForm



def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            # Authentication failed, handle accordingly (e.g., display an error message)
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Check if a user with the given username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Username or email already exists. Please choose a different one.')
            return redirect('/#SignUp')

        if password == cpassword:
            # Create a new user
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            messages.success(request, f"User {username} created successfully. You can now log in.")
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('/#SignUp')

    return redirect('/#SignUp')

@login_required
def profile(request):
    user_info = request.user
    return render(request, 'profile.html', {'user_info': user_info})

@login_required
def add_expense(request):
    expenses = Expense.objects.filter(user=request.user)
    e_source=ExpenseSource.objects.all()
    print(e_source.exists())
    if expenses.exists():
        for expense in expenses:
            print(f"User: {expense.user.username}, Source: {expense.source.source_name}, Total Amount: {expense.total_amount}, Spent Amount: {expense.spent_amount}")
    else:
        print("no expenses for the current user.")
    if request.method == 'POST':
        print('Check 1:',e_source.exists())

        form = ExpenseForm(request.POST)
        if form.is_valid():
            print('Check :',e_source.exists())

            source_name = form.cleaned_data['source_name']
            total_amount = form.cleaned_data['total_amount']
            user = request.user  

            #Souce check ho raha hay
            existing_source = ExpenseSource.objects.filter(user=user, source_name=source_name).first()
            print('Check 3 :',existing_source==None)

            if existing_source:
                message = f"Source '{source_name}' already exists for the user."
            else:
                source = ExpenseSource.objects.create(user=user, source_name=source_name)
                message = f"Source '{source_name}' has been created for the user."

                expense = Expense.objects.create(user=user, source=source, total_amount=total_amount)

                expenses = Expense.objects.all()


            return render(request, 'add_expense.html', {'form': form, 'expenses': expenses})
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form, 'expenses': expenses})


# for tesing only
@login_required
def fullname(request):
    user_info = User.objects.get(username=request.user.username)
    return render(request, 'fullname.html', {'user_info': user_info})

@login_required
def username(request):
    user_info = User.objects.get(username=request.user.username)
    return render(request, 'username.html', {'user_info': user_info})

@login_required
def email(request):
    user_info = User.objects.get(username=request.user.username)
    return render(request, 'email.html', {'user_info': user_info})


def logout_view(request):
    logout(request)
    return redirect('index')
