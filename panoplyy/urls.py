"""panoplyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from people import views
from people.views import StudentLandingView, CompanyLandingView
from projects.views import ProjectListView
from portfolio.views import CompanyPortfolioCreateView, CompanyPortfolioDetailView, CompanyPortfolioUpdateView, StudentPortfolioDetailView

#from likes.views import like_user

#CompanyPortfolioListView
#from userprofiles.views import StudentListView 
#from userprofiles.views import 



urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
	#(r'', include('profiles.urls')),

    # Main pages
    url(r'^$', StudentLandingView.as_view()),
    url(r'company/$', CompanyLandingView.as_view(), name='company'),




    # Student Register & Login & Logout
    url(r'^student_register/$', 'people.views.student_register', name='student_register'),
    url(r'^student_login/$', 'people.views.student_login', name='student_login'),
    url(r'^student_logout/$', 'people.views.student_logout', name='student_logout'),


    # Company Reigster & Login & Logout
    url(r'^company_register/$', 'people.views.company_register', name='company_register'),
    url(r'^company_login/$', 'people.views.company_login', name='company_login'),
    url(r'^company_logout/$', 'people.views.company_logout', name='company_logout'),


    # Student & Company's profile
    #url(r'^profile/(?P<username>[\w.@+-]+)/$', StudentListView.as_view()),
    url(r'^profile/edit/$', 'userprofiles.views.profile_edit', name='profile_edit'),
    #url(r'^profile/(?P<username>[\w.@+-]+)/$', 'userprofiles.views.profile_view', name='profile_view'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'userprofiles.views.profile_view', name='profile_view'),
    url(r'^profile/$', 'userprofiles.views.profile_user', name='profile_user'),


    # Like
    url(r'^like/(?P<slug>[\w-]+)/$', 'trys.views.like_user', name='like_user'),
    



    # Projects page
    url(r'projects/$', ProjectListView.as_view(), name='project_list'),
    #url(r'^projects/(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^projects/(?P<slug>[\w-]+)/$', 'projects.views.detail', name='detail'),



    # Company's Post a Project
    url(r'^profile/(?P<username>[\w.@+-]+)/post/$', CompanyPortfolioCreateView.as_view(), name='post_project'),
    url(r'^profile/(?P<username>[\w.@+-]+)/(?P<slug>[\w-]+)/$', CompanyPortfolioDetailView.as_view(), name='portfolio_detail'),
    url(r'^profile/(?P<username>[\w.@+-]+)/(?P<slug>[-\w]+)/update/$', CompanyPortfolioUpdateView.as_view(), name='portfolio_update'),


    # Student's Projects on their Profile Page
    url(r'^(?P<username>[\w.@+-]+)/(?P<slug>[\w-]+)/$', StudentPortfolioDetailView.as_view(), name='student_detail'),
    








]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







