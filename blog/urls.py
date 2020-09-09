from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'blog'
'''
berguna pas manggil si url di hyperlink.
i.e. {% url 'blog:detail' blog.id %}
bisa aja app lain juga punya path namanya detail.
'''

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]