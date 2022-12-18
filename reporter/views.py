from django.shortcuts import render, redirect 
from django.contrib import messages
from .models import Reporter, Article
import bcrypt
import re

# Create your views here.


def reporter(request):
    # GET request and response for reporter's page
    return render(request, "reporter/index.html")

def admin(request):
    # GET request and reponse for login and registration page
    return render(request, "reporter/login.html", {"users": Reporter.objects.all()})

def article_form(request):
        # GET request and response for article form page
        return render(request, "reporter/article_form.html", {"users": Reporter.objects.all()})
    

def article(request):
    # Article handling for POST request and response
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        date = request.POST["date"]
        article_image = request.FILES["image"]
        article_category = request.POST["category"]
        reporter = Reporter.objects.get(id=request.session["user_id"])

        Article.objects.create(title = title, body = body, created_on = date, article_category = article_category, article_image = article_image, reporter_details = reporter)
        messages.success(request, "Your article is successfully posted")
        return redirect(article_form)       
        
    else:
        return redirect(article_form)

def register(request):
    # Registration handling for POST request and response
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.%-]+@[a-zA-Z.-]+\.[a-z|A-Z]{2,}$")
        email_exist = Reporter.objects.filter(email = request.POST["email"])
        error_massages = {}
        if len(first_name) < 2 and len(first_name) >= 0:
            error_massages = "First name must be at least two characters"
        elif len(last_name) < 2 and len(last_name) >= 0:
            error_massages = "Last name must be at least two characters"
        elif not EMAIL_REGEX.match(email):
            error_massages = "Please enter a valid e-mail address"
        elif email_exist:
            error_massages = "That e-mail address is already registered"
        elif len(password) < 8:
            error_massages = "Password must at least 8 characters" 
        elif confirm_password != password:
            error_massages = "Passwords do not match"
        
        else:
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            reporter = Reporter.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = password_hash)
            request.session["user_id"] = reporter.id
            return redirect(article_form)
        return render(request, "reporter/login.html", {"messages": error_massages })
    else:
         return redirect(admin)
        
def login(request):
    # Login handling for POST request and response
    if request.method == "POST":
        error_messages = {}
        user = Reporter.objects.filter(email=request.POST["email"])
          
        if not user:
            error_messages = "Email not found, please register"
        elif not bcrypt.checkpw(request.POST["password"].encode(), user[0].password.encode()):
            error_messages = "Password is incorrect, try again"
        else:
            reporter = user[0]
            request.session["user_id"] = reporter.id
            return redirect(article_form)
        return render(request, "reporter/login.html", {"messages": error_messages })
    else:
        return redirect(admin)


def logout(request):
    # logout handling
    request.session.flush()
    return redirect("/")

