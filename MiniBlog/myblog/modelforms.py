from django.forms import ModelForm
from myblog.models import User

class UserForm(ModelForm):
    class Meta:
        model = User