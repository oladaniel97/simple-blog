from django.urls import path
from . import views


# namevarible in important in the path because it is used to reference the url in your a tag

urlpatterns = [
        path('',views.index,name='index'),
        path('<slug:slug>/',views.post_detail,name='post_detail')
]
