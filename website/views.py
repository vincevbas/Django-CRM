from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddSongForm
from .models import Song

def home(request):
	songs = Song.objects.all()

	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You are now logged in!")
			return redirect('home')
		else:
			messages.success(request, "There was an error logging in. Please try again.")
			return redirect('home')
	else:
		return render(request, 'home.html', {'songs':songs})  


def logout_user(request):
	logout(request)
	messages.success(request, "You have been removed from the mobius strip.")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have been successfully registered, Orbit!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form': form})

	return render(request, 'register.html', {'form': form})


def loona_song(request, pk):
	if request.user.is_authenticated:
		# Look up Songs
		loona_song = Song.objects.get(id=pk)
		return render(request, 'song.html', {'loona_song':loona_song})
	else:
		messages.success(request, "OOPS! You must be logged in to view this page.")
		return redirect('home')


def delete_song(request, pk):
	if request.user.is_authenticated:
		delete_it = Song.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Song deleted successfully!")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in to delete a song.")
		return redirect('home')

def add_song(request):
	form = AddSongForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Song added!")
				return redirect('home')
		return render(request, 'add_song.html', {'form':form})
	else:
		messages.success(request, "You must be logged in.")
		return redirect('home')

def update_song(request, pk):
	if request.user.is_authenticated:
		current_song = Song.objects.get(id=pk)
		form = AddSongForm(request.POST or None, instance=current_song)
		if form.is_valid():
			form.save()
			messages.success(request, "Song has been updated!")
			return redirect('home')
		return render(request, 'update_song.html', {'form':form})
	else:
		messages.success(request, "You must be logged in.")
		return redirect('home')
