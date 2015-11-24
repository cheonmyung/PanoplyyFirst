from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from datetime import datetime, timedelta

#import datetime, timedelta
from django.utils import timezone

MyUser = settings.AUTH_USER_MODEL



class ProjectQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def thirty_days(self):
		return self.filter(date_start__lte=timezone.now())\
			.filter(date_end__gt=timezone.now())

	#def same_user_project(self, user):
	#	return self.filter(user_company=user)


class ProjectManager(models.Manager):
	def get_queryset(self):
		return ProjectQuerySet(self.model, using=self._db)

	def only_active(self, *args, **kwargs):
		return self.get_queryset().active()

	def only_thirty_days(self):
		return self.get_queryset().active().thirty_days()

	#def only_same_user_project(self):
	#	return self.get_queryset().same_user_project().active()





CATEGORY_CHOICES = (
    ('Internship', 'Internship'),
    #('Internship Part-time', 'Internship Part-time'),
    ('Entry-Level Job', 'Entry-Level Job'),
    #('Engineering', 'Engineering'),
    #('Health', 'Health'),
    #('NewsMedia', 'NewsMedia'),
    #('Psychology', 'Psychology'),
    #('Trade', 'Trade'),
    )




def after_thirty_days():
	return datetime.today() + timedelta(days=30)
	



	#project = Project.objects.all()
	#if 
	#start = project.date_start 
	#project.date_end = start + datetime.timedelta(days=30, hours=10)
	#print project.date_end
	#return project.date_end

#profile, created = Project.objects.get_or_create(user_company=request.user)



class Project(models.Model):
	user_student = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
	user_company = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='company_user')

	# Slug
	slug = models.SlugField(blank=True)

	# To fill out a form
	job_type = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
	project_title = models.CharField(max_length=200)
	company_overview = models.TextField(max_length=5000)
	position_name = models.CharField(max_length=200)

	position_summary = models.TextField(max_length=5000)
	salary_or_what_we_offer = models.TextField(max_length=5000)
	deliverables = models.TextField(max_length=5000)
	comments = models.TextField(max_length=5000, null=True, blank=True)
	how_to_submit = models.CharField(max_length=2000)
	#job_category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
	#image = models.ImageField(upload_to=upload_image, null=True, blank=True)

	# related to Time
	#created_at = models.DateTimeField(auto_now_add=True, auto_now=False) 
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	# project post date & deadline date
	date_start = models.DateTimeField(default=datetime.today, verbose_name='Start Date')
	# auto_now_add=True, auto_now=False,
	date_end = models.DateTimeField(default=after_thirty_days, verbose_name='End Date')

	
	class Meta:
		ordering = ["-date_start", "-updated"]



	def __unicode__(self):
		return self.project_title
		#[:10]


	objects = ProjectManager()


	#def get_absolute_url(self):
	#	return reverse("project_detail", kwargs={"slug": self.slug})

	def get_absolute_url(self):
		return reverse("detail", kwargs={"slug": self.slug})





	#def get_absolute_url(self):
	#	return reverse("portfolio_detail", kwargs={"slug": self.slug})


	#def get_absolute_url(self):
	#	return reverse("portfolio_update", kwargs={"slug": self.slug})


	def like_link(self):
		url = reverse("like_user", kwargs={"slug": self.slug})
		return url

	





	#def project_status(self):
	#	if self.date_end >= timezone.now():
	#		self.active = True
	#		self.save()
	#	elif self.date_end < timezone.now():
	#		self.active = False
	#		self.save()
	#	else:
	#		pass






# Slug to title for each project
def pre_save_project(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.project_title)


pre_save.connect(pre_save_project, sender=Project)






class ProjectLike(models.Model):
	user = models.OneToOneField(MyUser)
	liked_projects = models.ManyToManyField(Project, related_name='liked_projects', blank=True)


	def __unicode__(self):
		return self.user.username



#def post_save_user_trying(sender, instance, created, *args, **kwargs):
#	print sender
#	print instance
#	print created

#	if created:
		#slug = instance.liked_projects.first()

#		new_project, is_created = Project.objects.get_or_create(user_student=instance.user)
		#new_project.user_student = instance.user
		#new_project.save()


#post_save.connect(post_save_user_trying, sender=ProjectLike)


	#if instance.user == request.user:
	

	##instance.liked_projects.user_student = instance.user
	
	#m = instance.liked_projects.all()
	#m.save()
	#user = instance.user
	#projects = instance.liked_projects.all()




	#new_user = Project.objects.get_or_create(user_student=user)

	#if projects.count() > 0:
		#projects.user_student = user
		#new = Project()
		#new.user_student = user
		#new.save()




	#new = Project()
	#new_project, created = Project.objects.get_or_create(slug=title)
	#if new in projects:
	#	new.user_student = user
	#	new.save()		






#	job = instance.position.lower()
#	location = instance.location.lower()
#	employer_name = instance.employer_name.lower()
	#Job.objects.get(text__iexact=job)
#	new_job = Job.objects.get_or_create(text=job) #case insenstive Cashier or cashier
#	new_location, created = Location.objects.get_or_create(name=location)
#	new_employer = Employer.objects.get_or_create(location=new_location, name=employer_name)


#	product = instance
#		variations = product.variation_set.all()
#		if variations.count() == 0:
#			new_var = Variation()
#			new_var.product = product
#			new_var.title = "Default"
#			new_var.price = product.price
#			new_var.save()









#related_name='liker'
























#def post_saved_project(sender, instance, created, *args, **kwargs):
#	if created:
#		instance.date_start = timezone.now()
#		start = instance.date_start
#		instance.date_end = start + datetime.timedelta(days=30, hours=10)
#		instance.active = True
#		instance.save()
#	instance.project_status()

#post_save.connect(post_saved_project, sender=Project)










# post_save_project?
#def post_save_project(sender, instance, created, *args, **kwargs):
#	if created:
#		instance.start_date = datetime.today()
#		instance.active = True
#		instance.save()

#	if 	instance.end_date >= datetime.today():
#		instance.active = True
#		instance.save()

#	elif instance.end_date < datetime.today():
#		 instance.active = False
#		 instance.save()

#	else:
#		pass


#post_save.connect(post_save_project, sender=Project)







	

	#def save(self, *args, **kwargs):
	#	students = MyUser.objects.student_type()
	#	companies = MyUser.objects.company_type()
	#	self.user_student = students
	#	self.user_company = companies
	#	super(Project, self).save(*args, **kwargs)


	#def student_and_company(self):
	#	students = MyUser.objects.student_type()
	#	companies = MyUser.objects.company_type()
	#	self.user_student = students
	#	self.user_company = companies
	#	self.save()








