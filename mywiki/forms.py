from django import forms

class login_form(forms.Form):
	Email = forms.CharField(max_length = 50)
	Password = forms.CharField()

class signup_form(forms.Form):
	 UserName = forms.CharField()
	 Email = forms.CharField(max_length = 50)
	 Password = forms.CharField()

