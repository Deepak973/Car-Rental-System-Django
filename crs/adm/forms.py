from django import forms
from adm.models import login
from adm.models import location

class adminform(forms.ModelForm):
    class Meta:
      model = login
      fields = "__all__"
