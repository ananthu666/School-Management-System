from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, SubjectViewSet, MarkViewSet,LoginViewSet,SingupViewSet
# from .auth import CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'signup', SingupViewSet,basename='signup')
router.register(r'login',LoginViewSet,basename='login')
router.register(r'users', UserViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]