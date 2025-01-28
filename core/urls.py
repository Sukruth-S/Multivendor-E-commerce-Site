from django.urls import path
from . import views
from .views import landing_page, frontpage
app_name = 'core'


urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('home/', frontpage, name='home'),
    # path('', views.frontpage, name="home"),
    path('contact-us/', views.contactpage, name="contact"),
]
