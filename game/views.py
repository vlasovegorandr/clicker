from django.shortcuts import render
from django.db.models import F
from accounts.models import PlayerInventory

def playscreen(request):

    template = 'game/playscreen.html'

    if request.POST.get('user-id'):
        current_player = PlayerInventory.objects.get(name=request.POST.get('user-id'))
        var = None
        if request.POST.get('add-click'):
            current_player.total_clicks=F('total_clicks') + 1
            current_player.save()
            current_player = PlayerInventory.objects.get(name=request.POST.get('user-id'))
        context = {
            'player': current_player,
            'var': var,
        }

    else:
        context = {

        }
    return render(request, template, context)
