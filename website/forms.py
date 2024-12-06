from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Song


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



# Create Add Song Form
class AddSongForm(forms.ModelForm):
	song_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Song Title", "class=":"form control"}), label="")
	release_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Release Type", "class=":"form control"}), label="")
	album_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Album Name", "class=":"form control"}), label="")
	album_format = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Album Format", "class=":"form control"}), label="")
	release_date = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Release Date", "class=":"form control"}), label="")
	artist_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Artist Name", "class=":"form control"}), label="")

	class Meta:
		model = Song
		exclude = ("user",) 
