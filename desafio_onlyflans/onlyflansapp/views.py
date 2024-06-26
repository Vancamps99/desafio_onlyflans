from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #flanes = Flan.objects.all()    
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html", {})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    
    return render(request, "welcome.html", context)

def login2(request):
    #get ->
    if request.method == "GET":
        return render(request, "login2.html", {})
    #post ->
    if request.method == "POST":
        #podemos guardar los datos enviados en variables
        email = request.POST["email"]
        request.session["email"] = email
        
        return redirect("/welcome", {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        #print(form)
        if form.is_valid():
            #aplicar logica
            form2 = ContactForm.objects.create(**form.cleaned_data)
            return redirect("/exito", {})
    else:
        form = ContactFormForm()
        context ={
            "form": form
        }
    return render(request,"contact.html",context)

def registro(request):
    if request.method == "POST":
        # Obtener los datos del formulario POST
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        user = User.objects.create_user(username=username, email=email, password=password)
        # Asignar nombres al usuario si se proporcionan
        user.first_name = first_name
        user.last_name = last_name
        user.save() 
        return redirect("welcome")
    
    # Renderizar la plantilla de registro con un formulario vacío
    return render(request, "registro.html")