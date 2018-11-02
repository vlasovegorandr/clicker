from django.shortcuts import render, redirect

def homepage(request):
    return redirect('main_menu')

def main_menu(request):
    template = 'main_menu.html'

    return render(request, template)

def about(request):
    template = 'about.html'

    return render(request, template)