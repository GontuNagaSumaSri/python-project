"""EventBookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name="index"),
    path('Login', views.Login ,name="Login"),
    path('about', views.about ,name="about"),
    path('add_Agriculture', views.add_Agriculture ,name="add_Agriculture"),
    path('add_Business', views.add_Business ,name="add_Business"),
    path('add_Education', views.add_Education ,name="add_Education"),
    path('add_Banking', views.add_Banking ,name="add_Banking"),
    path('add_RealEstate', views.add_RealEstate ,name="add_RealEstate"),
    path('add_Resume', views.add_Resume ,name="add_Resume"),
    path('full_time', views.full_time ,name="full_time"),
    path('student_project', views.student_project ,name="student_project"),
    path('resume_details', views.resume_details ,name="resume_details"),
    path('contact', views.contact ,name="contact"),
    path('innerhome', views.innerhome ,name="innerhome"),
    path('Logout', views.Logout ,name="Logout"),
    path('usersignup', views.usersignup ,name="usersignup"),
    path('Userlogin', views.Userlogin ,name="Userlogin"),
    path('userhome', views.userhome ,name="userhome"),
    path('add_event', views.add_event ,name="add_event"),
    path('view_event', views.view_event ,name="view_event"),
    path('delete_event(?p<int:pid>)', views.delete_event ,name="delete_event"),
    path('add_sponsor', views.add_sponsor,name="add_sponsor"),
    path('view_sponsor', views.view_sponsor ,name="view_sponsor"),
    path('delete_sponsor(?p<int:pid>)', views.delete_sponsor ,name="delete_sponsor"),
    path('add_category', views.add_category,name="add_category"),
    path('view_category', views.view_category ,name="view_category"),
    path('delete_category(?p<int:pid>)', views.delete_category ,name="delete_category"),
    path('view_user', views.view_user ,name="view_user"),
    path('delete_user(?p<int:pid>)', views.delete_user ,name="delete_user"),
    path('view_eventuser', views.view_eventuser ,name="view_eventuser"),
    path('view_details(?p<int:pid>)', views.view_details ,name="view_details"),
    path('book_now/<int:pid>', views.book_now ,name="book_now"),
    path('view_mybooking', views.view_mybooking ,name="view_mybooking"),
    path('delete_booking(?p<int:pid>)', views.delete_booking ,name="delete_booking"),
    path('change_passworduser', views.change_passworduser ,name="change_passworduser"),
    path('change_passwordadmin', views.change_passwordadmin ,name="change_passwordadmin"),
    path('booking_request', views.booking_request ,name="booking_request"),
    path('bookingdetail_user/<int:pid>',views.bookingdetail_user,name="bookingdetail_user"),
    path('bookingdetail_admin/<int:pid>',views.bookingdetail_admin,name="bookingdetail_admin"),
    path('accepted_booking',views.accepted_booking ,name="accepted_booking"),
    path('rejected_booking',views.rejected_booking ,name="rejected_booking"),
    path('all_booking',views.all_booking ,name="all_booking"),
    path('confirmed_booking',views.confirmed_booking ,name="confirmed_booking"),
    path('edit_event/<int:pid>',views.edit_event,name="edit_event"),
    path('edit_sponsor/<int:pid>',views.edit_sponsor,name="edit_sponsor"),
    path('edit_category/<int:pid>',views.edit_category,name="edit_category"),
    path('payment/<int:pid>',views.payment,name="payment"),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)