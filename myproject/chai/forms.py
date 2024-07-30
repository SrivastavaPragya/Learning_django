from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
    #ModelChoiceField yai form exsisting model  kai andr query krta hai and yai by default choice field bna kr dega
  chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select Chai Variety")