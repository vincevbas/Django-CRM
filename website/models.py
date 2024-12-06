from django.db import models


class Song(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	song_title = models.CharField(max_length=100)
	release_type = models.CharField(max_length=100)
	album_name = models.CharField(max_length=100)
	album_format = models.CharField(max_length=100)
	release_date = models.CharField(max_length=100)
	artist_name = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.song_title}")