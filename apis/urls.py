from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from apis import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
