from django.contrib import admin
from django.urls import path, include
# from api.views import *
# from rest_framework.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('clientes/', include('clientes.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/', include("rest_framework.urls")),
    path('api-auth/', include('rest_framework.urls')),
	path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
]
