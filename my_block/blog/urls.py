from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    path("", post_list, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail')
]
