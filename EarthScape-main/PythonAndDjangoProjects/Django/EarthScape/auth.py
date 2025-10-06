from earthscapemodel.models import Signup
from django.contrib import messages
from django.shortcuts import render, redirect
import uuid
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.templatetags.static import static


def index(request):
    return render(request, 'splashscreen.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def graph(request):
    return render(request, 'map.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signupinsert(request) : 
  if request.method =="POST" :
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]
    signupdata = Signup.objects.filter(email=email).exists()
  if signupdata : 
      messages.error(request, 'email already exists')
      return render(request, 'signup.html')
  else :          
    userdata = Signup.objects.create(name=name,email =email,password=password)
    userdata.save()
    messages.success(request, 'account created')
    return render(request, 'login.html')





# Token store for demonstration
VALID_TOKENS = {}


def loginview(request):
    if request.method == 'POST':
        email = request.POST.get("email")  # GET method for safety
        password = request.POST.get("password")

        # Check if user exists
        logindata = Signup.objects.filter(email=email, password=password).first()

        if logindata:
            # Get name from the database
            name = logindata.name  # Assuming 'name' is a field in your Signup model

            # Redirect to the Python dashboard with email and name in the query parameter
            dashboard_url = f"http://localhost:8501/?email={email}&name={name}"
            # messages.success(request, 'Login Successfully')
            return redirect(dashboard_url)
        else:
            messages.error(request, 'Invalid email or Password')
            return render(request, 'login.html')

    return render(request, 'login.html')



def logout_view(request):
    # Clear the session completely
    request.session.flush()
    # Call the Django logout function to invalidate authentication
    logout(request)
    # Add a logout success message (optional)
    messages.success(request, 'Logout Successfully')
    # Redirect the user to the login page or homepage
    return redirect("/")  # Replace "/login/" with your login page URL


def check_login(request):
    """
    API endpoint to verify if a user is logged in using custom Signup model.
    """
    email = request.GET.get("email")  # Extract the email from the query parameters

    if email:
        # Check if the email exists in your Signup model
        user = Signup.objects.filter(email=email).first()
        if user:
            return JsonResponse({"logged_in": True, "email": user.email, "name": user.name})
    
    return JsonResponse({"logged_in": False, "error": "Invalid email or user not logged in."})
def navbar(request):
    return render(request, 'navbar.html')

def debug_view(request):
    logo_url = static('images/logo.jpg')
    print(f"Generated Static URL: {logo_url}")
    return HttpResponse(f"<img src='{logo_url}' alt='Logo'>")
#     if request.method == 'POST':
#         email = request.POST["email"]
#         password = request.POST["password"]

#         # Check if the user exists
#         logindata = Signup.objects.filter(email=email, password=password).first()

#         if logindata:
#             messages.success(request, 'Login Successfully')

#             # Generate a token for the session
#             token = str(uuid.uuid4())  # Generate a unique token
#             VALID_TOKENS[token] = email  # Map the token to the email

#             # Redirect to the dashboard with the token
#             dashboard_url = f"http://localhost:8501/?token={token}"
#             return redirect(dashboard_url)
#         else:
#             messages.error(request, 'Invalid email or Password')
#             return render(request, 'login.html')

#     return render(request, 'login.html')


