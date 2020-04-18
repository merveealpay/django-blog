from django.urls import path

app_name = 'post'
# post uygulamasının url'leri bunlar , o diğer uygulama url leri ile karısmasın diye app name verildi.
from .views import *

urlpatterns = [
    path('index/', post_index, name='index'),
    path('<int:id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('<int:id>/update/', post_update, name='update'),
    path('<int:id>/delete/', post_delete, name='delete'),
]
