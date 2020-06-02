from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")

    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.first_name
        user.last_name = self.last_name        
	user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user