from django.forms import ModelForm
from .models import PlayerInventory

class CreatePlayerInventoryInstanceForm(ModelForm): #name too long?
    class Meta():
        model = PlayerInventory
        fields = '__all__'