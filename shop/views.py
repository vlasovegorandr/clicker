from shop.models import ClickButton, Background
from accounts.models import PlayerInventory
from django.shortcuts import  render

def shop_items_list(request):
    template = 'shop/itemlist.html'
    player = PlayerInventory.objects.get(name=request.user.id)
    buttons = ClickButton.objects.all().order_by('btn_price')
    backgrounds = Background.objects.all().order_by('bkg_price')
    if request.POST.get('apply-button'):
        player.equipped_button = ClickButton.objects.get(id=request.POST.get('apply-button'))
        player.save()
        player = PlayerInventory.objects.get(name=request.user.id)
    if request.POST.get('apply-background'):
        player.equipped_background = Background.objects.get(id=request.POST.get('apply-background'))
        player.save()
        player = PlayerInventory.objects.get(name=request.user.id)
    context = {
        'player': player,
        'button_list': buttons,
        'background_list': backgrounds
    }
    return render(request, template, context)