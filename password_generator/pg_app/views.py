from django.shortcuts import render
import random
# Create your views here.

def home(request):
  return render(request,'pg_app/home.html')

def about(request):
  return render(request,'pg_app/about.html')

def password(request):
  characters = list('abcdefghijklmnopqrstuvwxyz')

  if request.GET.get('numbers'):
    characters.extend(list('1234567890'))

  if request.GET.get('special'):
      characters.extend(list('!@#$%^&*()'))

  if request.GET.get('uppercase'):
      characters.extend(list('ABDEFGHIJKLMNOPQRSTUVWXYZ'))   

  length = int(request.GET.get('length',12))

  generatedPass = ''

  for x in range(length):
    generatedPass += random.choice(characters)

  return render(request,'pg_app/Generated_password.html',{'password':generatedPass})
  