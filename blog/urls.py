from django.urls import path
from . import views
from .views import notify_user_about_post

app_name = 'blog'

urlpatterns = [
# представления поста
    path('', views.post_list, name='post_list'),    
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('notify/<int:user_id>/<int:post_id>/', notify_user_about_post, name='notify_user_about_post')
]

