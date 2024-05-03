from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='home'),
    path('form',views.form,name='form'),
    path('tab',views.tab,name='tab'),
    path('table',views.table,name='table'),
    path('blank/',views.blank,name='blank'),
    path('updateBook/<str:pk>',views.update,name='update'),
    path('deleteBook/<str:pk>',views.delete,name='delete'),
    path('<slug:slug>/',views.detal_Book,name='detail'),
    

]