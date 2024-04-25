from django.shortcuts import render, redirect
from .models import Game
import random

# Create your views here.

def home(request):
    game = Game.objects.first()
    if not game:
        game = Game.objects.create(secret_number=random.randint(game.min_range, game.max_range))
    else:
        game.secret_number = random.randint(game.min_range, game.max_range)
        game.save()
    print("Secret number:", game.secret_number)    
    return render(request, 'game/home.html', {'game': game})  

def guess(request):
    if request.method == 'POST':
        guessed_number = int(request.POST['guessed_number']) 
        game = Game.objects.first()
        if guessed_number == game.secret_number:
            message = 'Congratulations! You guessed the number.'
        elif guessed_number < game.secret_number:
            message = 'Try a higher number.'
        else:
            message = 'Try a lower number.'  
        return render(request,'game/home.html',{'game':game ,'message':message})     
    return redirect('home')