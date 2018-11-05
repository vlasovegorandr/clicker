from shop.models import ClickButton, Background
from accounts.models import PlayerInventory
from django.shortcuts import  render

def shop_items_list(request):
    template = 'shop/itemlist.html'
    button_list = []
    background_list = []
    player = PlayerInventory.objects.get(name=request.user.id)
    all_buttons = ClickButton.objects.all().order_by('btn_price')
    for item in all_buttons:
        if player.total_clicks >= item.btn_price:
            button_list.append(item)
    all_backgrounds = Background.objects.all().order_by('bkg_price')
    for item in all_backgrounds:
        if player.total_clicks >= item.bkg_price:
            background_list.append(item)
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
        'button_list': button_list,
        'background_list': background_list
    }
    return render(request, template, context)