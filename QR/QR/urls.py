from django.contrib import admin
from django.urls import path
from app.views import ValidateApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('validation/', ValidateApiView.as_view()),

]


# API=http://127.0.0.1:8000/validation