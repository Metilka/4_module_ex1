from django.urls import path
from .views import index, les

urlpatterns = [
    path('', index),
    path('start', index),
    path('lesson_4', les)

]