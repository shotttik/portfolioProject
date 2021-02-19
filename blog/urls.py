from django.urls import path

from blog.views import allblogs, detail

urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>/', detail, name='detail')
]
