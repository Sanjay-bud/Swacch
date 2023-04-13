from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import F
from . import models
from . import forms

def index(request):
    username = models.form.objects.first().name
    my_obj  = models.form.objects.first()
    phn_getin = request.POST.get('phn')
    if request.method == 'POST':
        phn_input = models.form.objects.filter(phn_num=phn_getin).first()
        if phn_input is not None:
            msg = "THANK YOU {}".format(phn_input.name)
            phn_input.count = F('count') + 1
            phn_input.save()
            messages.success(request, msg)
        else:
            mes = "CHECK YOUR MOBILE NUMBER"
            messages.error(request, mes)
    return render(request, 'index.html')


def user(request):
    form = forms.userdetailsform()
    if request.method == 'POST':
        print(request)
        form = forms.userdetailsform(request.POST)
        if form.is_valid:
            form = form.save(commit = False)
            form.save()
            message = "user id for {} has been updated successfully"
            for_message = message.format(form.name)
            messages.success(request, for_message)
            return redirect("/swachh/register/")
    context = {"form": form}
    return render(request,"register.html", context)

