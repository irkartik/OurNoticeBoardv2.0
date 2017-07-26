from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Note(models.Model):
	created_by = models.ForeignKey(User, default=1)
	note_title = models.CharField(max_length=250)
	brief = models.CharField(max_length=100)
	body = models.TextField(max_length=100000000000)
	date = models.DateTimeField(default=datetime.now)
	note_logo = models.FileField(default="default.jpg", blank= True, null=True)
	private = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('notes:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.note_title

	






