from django import forms

from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
def some_view(request):
    user = User.objects.get(username='example')  
    user_role = user.role 



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'role')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return confirm_password
    
    from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
    model_choices = (
        ('team', 'TeamLeaderData'),
        ('sample', 'Sample'),
        ('sales_ex', 'salesEx'),
    )
    model_selection = forms.ChoiceField(choices=model_choices)



    



   



    
    
    

