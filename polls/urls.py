from django.urls import path

from . import views
from . views import Colorlistview
urlpatterns = [
    path('', views.index, name='index'),
    path('color/', Colorlistview.as_view(), name='Colorlistview'),

]