
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Sagar shop admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

]
