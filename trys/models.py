#from django.conf import settings
from django.db import models
from projects.models import Project, ProjectLike
# Create your models here.

#MyUser = settings.AUTH_USER_MODEL

# Moved to Project model

#class ProjectLike(models.Model):
#	user = models.OneToOneField(MyUser, related_name='liker')
#	liked_projects = models.ManyToManyField(Project, related_name='liked_projects', blank=True)

#project = models.OneToOneField(Project, related_name='liker')
#liked_users = models.ManyToManyField(MyUser, related_name='liked_users', blank=True)


#	def __unicode__(self):
#		return self.user.username



#request.user.liker.liked_users.all()


#so, request.project.liker.liked_users.all()


class BookMarks(models.Model):
	project_like_user = models.ForeignKey(ProjectLike)
	project = models.ForeignKey(Project)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.project_like_user.user.username 
