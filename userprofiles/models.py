from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

MyUser = settings.AUTH_USER_MODEL



def upload_profile(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)



class Profile(models.Model):
	user = models.OneToOneField(MyUser)
	industry = models.CharField(max_length=50, null=True, blank=True)
	overview = models.TextField(max_length=1000, null=True, blank=True)
	picture = models.ImageField(upload_to=upload_profile, null=True, blank=True)


	def __unicode__(self):
		return self.user.username


	def get_absolute_url(self):
		return reverse("profile_view", kwargs={"username": self.user.username})
		