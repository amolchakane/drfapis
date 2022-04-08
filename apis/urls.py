from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from apis import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
