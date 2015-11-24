from django.db import models
from projects.models import Project
from people.models import MyUser




class Portfolio(models.Model):
	user = models.ForeignKey(MyUser)
	project = models.OneToOneField(Project)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False) 
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	# slug?

	# After "MVP", 
	# files?

	class Meta:
		ordering = ["-updated"]


	def __unicode__(self):
		return self.project.title
