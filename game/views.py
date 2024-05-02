from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import Game
import random

# Home view
def home(request):
    print("Home view called") 
    # Check if there is an existing Game object
    game = Game.objects.first()
    if not game:
        # If no existing Game object, create a new one
        game = Game.objects.create(min_range=1, max_range=100)
        game.secret_number = random.randint(game.min_range, game.max_range)   
    else:
        # If an existing Game object is found, update its secret_number
        game.secret_number = random.randint(game.min_range, game.max_range)

    # Save the changes to the Game object
    game.save()

    return render(request, 'game/home.html', {'game': game})
    
# Providing hint to the player
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

#  Restart the game 
def restart(request):
    print("Restart view called") 
    game = Game.objects.first()
    if game:
        game.secret_number = random.randint(game.min_range,game.max_range)
        game.save()
    return HttpResponseRedirect('/')
    
# For testing purposes
def game_list(request):
    games = Game.objects.all()
    data = [{'id': game.id, 'max_range': game.max_range,'min_range':game.min_range,'secret_number': game.secret_number} for game in games]
    return JsonResponse(data, safe=False)
