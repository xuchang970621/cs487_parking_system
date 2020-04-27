'''chang: ->'''
from django.urls import path

from . import views

app_name = 'parking'
urlpatterns = [
            path('', views.index, name='index'),
            path('<int:lot_id>/', views.detail, name='detail'),
            path('myspots/', views.MySpots.as_view(), name='myspots'),
            path('book/<int:spot_id>', views.book, name='book'),

]
'''<- chang'''
