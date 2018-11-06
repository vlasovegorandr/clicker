from shop.models import ClickButtonSkin, Background, ClickMultiplier
from accounts.models import PlayerInventory
from django.shortcuts import  render

def shop_items_list(request):
    template = 'shop/itemlist.html'
    player = PlayerInventory.objects.get(name=request.user.id)
    button_list = ClickButtonSkin.objects.filter(btn_price__lte=player.total_clicks).order_by('btn_price')
    background_list = Background.objects.filter(bkg_price__lte=player.total_clicks).order_by('bkg_price')
    mltplr_list = ClickMultiplier.objects.filter(mltplr_price__lte=player.total_clicks).order_by('mltplr_value')
    if request.POST.get('apply-button'):
        player.equipped_button = ClickButtonSkin.objects.get(id=request.POST.get('apply-button'))
        player.save()
        player = PlayerInventory.objects.get(name=request.user.id)
    if request.POST.get('apply-background'):
        player.equipped_background = Background.objects.get(id=request.POST.get('apply-background'))
        player.save()
        player = PlayerInventory.objects.get(name=request.user.id)
    if request.POST.get('apply-multiplier'):
        player.equipped_mltplr = ClickMultiplier.objects.get(id=request.POST.get('apply-multiplier'))
        player.save()
        player = PlayerInventory.objects.get(name=request.user.id)
    context = {
        'player': player,
        'button_list': button_list,
        'background_list': background_list,
        'multiplier_list': mltplr_list
    }
    return render(request, template, context)