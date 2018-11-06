from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import ListView
from accounts.models import PlayerInventory
from shop.models import ClickButtonSkin, Background, ClickMultiplier
from .forms import CreatePlayerInventoryInstanceForm


class LeaderboardsListView(ListView):
    model = PlayerInventory
    template_name = 'accounts/leaderboards.html'
    context_object_name = 'list_of_players'

    def get_queryset(self):
        return PlayerInventory.objects.all().order_by('-total_clicks')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_length'] = len(self.get_queryset())
        return context

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:player_creation')
    else:
        form = UserCreationForm()

    template = 'accounts/signup.html'
    context = {
        'signup_form': form,
    }
    return render(request, template, context)

def player_creation(request):
    if request.method == 'GET':
        create_player_form = CreatePlayerInventoryInstanceForm()
        instance = create_player_form.save(commit=False)
        instance.name = request.user
        print(request.user, '\n\n\n\n')
        instance.total_clicks = 0
        instance.equipped_button_id = ClickButtonSkin.objects.get(btn_name='default').id
        instance.equipped_background_id = Background.objects.get(bkg_name='default_bkg').id
        instance.equipped_mltplr_id = ClickMultiplier.objects.get(mltplr_name='x1').id
        instance.save()

    return redirect('main_menu')


def user_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_menu')

    else:
        form = AuthenticationForm()
    template = 'accounts/login.html'
    context = {
        'login_form': form
    }
    return render(request, template, context)

def user_logout(request):

    if request.method == 'POST':
        logout(request)
        return redirect('main_menu')