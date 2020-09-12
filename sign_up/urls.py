from django.urls import path
from .  import views


app_name = 'sign_up'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('blog/', views.Post_blog.as_view(), name='blog'),
    # path('blog/', views.U.as_view(), name='blog'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    # path('blog/edit/<int:pk>', views.PostUpdateView.as_view(), name='update-detail'),
    path('blog/edit/<int:pk>', views.view_edit, name='update-detail'),
    path('blog/edit/now/<int:pk>', views.post_edit, name='edit-detail'),
    path('blog/delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('register/', views.register_page, name='register'),
     # path('home/', views.home_page, name='home'),
]