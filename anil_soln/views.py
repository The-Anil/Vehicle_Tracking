from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd


config = {
    'apiKey': "AIzaSyDmyDz3GpxEkIZnrauTbSkSGthZk2LHNX4",
    'authDomain': "anil-soln.firebaseapp.com",
    'databaseURL': "https://anil-soln.firebaseio.com",
    'projectId': "anil-soln",
    'storageBucket': "anil-soln.appspot.com",
    'messagingSenderId': "1005850294597"
  }

firebase = pyrebase.initialize_app(config)





# Create your views here.
def index(request):
    # Get a reference to the database service
    db = firebase.database()
    all = {}
    a = db.child('/').get()
    for user in a.each():
        c = user.key()
        d = user.val()
        all.update({c: d})
    return render(request, 'anil_soln/index.html', {'dic2': all})
