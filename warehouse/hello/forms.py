from django.forms import ModelForm, TextInput
from.models import *


class AddStorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ["number", "name", "phone"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер склада'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название склада'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон склада'
            })
        }


class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "type"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название инвентаря'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип инвентаря'
            })
        }


class FindStorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ["number"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите номер склада'
            })
        }


class FindInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите название инвентаря'
            })
        }


class EditStorage(ModelForm):
    class Meta:
        model = Storage
        fields = ["number", "name", "phone"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите номер склада'
            }),
            "name": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите название склада'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите телефон склада'
            })
        }


class EditInventory(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "type"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите название инвентаряа'
            }),
            "type": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите тип инвентаря'
            })
        }


class SearchInventory(ModelForm):
    class Meta:
        model = Inventory
        fields = ["type"]
        widgets = {
            "type": TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Введите тип инвентаря'
            })
        }
