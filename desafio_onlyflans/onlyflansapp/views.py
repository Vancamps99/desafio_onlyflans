from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from .forms import ContactFormForm

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

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    
    return render(request, "welcome.html", context)

def registro(request):
    return render(request, "registro.html", {})

def login(request):
    #get ->
    if request.method == "GET":
        return render(request, "login.html", {})
    #post ->
    if request.method == "POST":
        #podemos guardar los datos enviados en variables
        email = request.POST["email"]
        request.session["email"] = email
        
        return redirect("/welcome", {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        print(form)
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