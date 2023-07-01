from django.shortcuts import render
from django.views.generic.base import TemplateView# <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from .models import Artist

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
       template_name = "home.html"
    


class About(TemplateView):
        template_name = "about.html"


 #adds artist class for mock database data
class Artist:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


artists = [
  Artist("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
          "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
  Artist("Panic! At The Disco",
          "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
  Artist("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
          "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
  Artist("Metallica",
          "https://i1.sndcdn.com/artworks-001099370752-qhj3j0-t500x500.jpg", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
  Artist("Bad Bunny",
          "https://m.media-amazon.com/images/I/91pz0YqKG9L._AC_SX466_.jpg", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
  Artist("Kaskade",
          "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
]


class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = Artist.objects.all()# this is where we add the key into our context object for the view to use
        return context
    

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs # this is where we add the key into our context object for the view to use
        return context
