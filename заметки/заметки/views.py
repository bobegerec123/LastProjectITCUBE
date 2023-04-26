from django.http import HttpResponse
from django.shortcuts import render

from .forms import TipsName


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    return render(request, 'index.html')


def User_new(request):
    if request.method == "POST":
        try:
            if request.method == "POST":
                form = UserName(request.POST)
                if form.is_valid():
                    name = form['user_name'].value()
                    user = user(name=name)
                    name.save()
                    return HttpResponse(f"<h3>id: {user.id} name: {user.name}</h3>")
        except Exception as e:
            return HttpResponse(f"<h1><b>Продукт с этим именем уже есть!</b>{e}</h1>")
    else:
        form = UserName()
        return render(request, "addProduct.html", {'form': form})

def add_tips(request):
    if request.method == "POST":
        try:
            form = TipsName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                tips = tips(name=name)
                tips.save()
                return redirect("/")
        except Exception as e:
            form = TipsName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = TipsName()
        return render(request, "addProduct.html", {'form': form})