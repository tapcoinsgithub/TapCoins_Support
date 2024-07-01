from django.urls import path
from .views import support_page

app_name = "support_urls"
urlpatterns = [
    path('', support_page, name="supportPage"),
]