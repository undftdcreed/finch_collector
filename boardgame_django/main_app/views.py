from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
#auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"
    
class About(TemplateView):
  template_name = "about.html"

class Games:
  def __init__(self, name, image, bio):
    self.name = name
    self.image = image
    self.bio = bio

class GameCreate(CreateView):
   model = Game
   fields = ['name', 'img', 'bio']
   template_name = "game_create.html"

   def form_valid(self, form): 
      form.instance.user = self.request.user
      return super(GameCreate, self).form_valid(form)

   def get_success_url(self):
      print(self.kwargs)
      return reverse('game_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class GameList(TemplateView):
  template_name = "game_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
        context["games"] = Game.objects.filter(
           name__icontains=name, user=self.request.user)
        context["header"] = f"searching for {name}"
    else:
        context["games"] = Game.objects.filter(user=self.request.user)
        context["header"] = "Top Shelf Games"
    return context
  

class GameUpdate(UpdateView):
   model = Game
   fields = ['name', 'img', 'bio']
   template_name = "game_update.html"

   def get_success_url(self):
      return reverse('game_detail', kwargs={'pk': self.object.pk})

class GameDetail(DetailView):
   model = Game
   template_name = "game_detail.html"


class GameDelete(DeleteView):
   model = Game
   template_name = "game_delete_confirmation.html"
   success_url = "/games/"


class Signup(TemplateView):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("game_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


