from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from user.views import CustomTokenObtainPairView, UserView

from . import views

urlpatterns = [

    #user profile
    path('<int:user_id>/', views.UserProfileView.as_view(), name = 'user_profile'),
    # path('<int:user_id>/update/', views.UserProfileView.as_view(), name = 'user_profile'),
    path('check/', views.UserViewSet.as_view({'get' : 'username_check'})),
    path('', UserView.as_view(), name='user_view'),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
]