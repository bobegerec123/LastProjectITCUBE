from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TipsName, UserName
from .models import *


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    return render(request, 'index.html')


def new_User(request):
    if request.method == "POST":
        try:
            if request.method == "POST":
                form = UserName(request.POST)
                if form.is_valid():
                    name = form['user_name'].value()
                    user = User(name=name)
                    name.save()
                    return HttpResponse(f"<h3>id: {user.id} name: {user.name}</h3>")
        except Exception as e:
            return HttpResponse(f"<h1><b>Это уже есть !!</b>{e}</h1>")
    else:
        form = UserName()
        return render(request, "addTips.html", {'form': form})


def add_tips(request):
    if request.method == "POST":
        try:
            form = TipsName(request.POST)
            if form.is_valid():
                name = form['tips_name'].value()
                tips = Tips(name=name)
                tips.save()
                return redirect("/")
        except Exception as e:
            form = TipsName(request.POST)
            return render(request, "addTips.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = TipsName()
        return render(request, "addTips.html", {'form': form})


def tips_list(request):
    out = Tips.objects.all()
    tips_ = []

    for tips in out:
        tips_.append((
            tips.id,
            tips.name
        ))

    return render(request, "tipsList.html", {'tips': tips_})


def delete_tips(request, id):
    product = Tips.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect("/")
    else:
        return render(request)


def edit_tips(request, id):
    tips = Tips.object.get(id=id)
    if request.method == "POST":
        form = TipsName(request.POST)
        if form.is_valid():
            name = form['tips_name'].value()
            tips.name = name
            try:
                tips.save()
                return redirect("/")
            except Exception as e:
                form = TipsName(request.POST)
            return render(request, "addTips.html", {
                'form': form,
                'error_massage': "занято"
            })
        else:
            form = TipsName(initial={
                "Tips_name": tips.name
            })

            return render(request, "addTips.html", {'form': form})
