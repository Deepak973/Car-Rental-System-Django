from django import forms
from user.models import user

class registerform(forms.ModelForm):
    class Meta:
      model = user
      fields = "__all__"