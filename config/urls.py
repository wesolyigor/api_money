from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include("todos.urls")),
    path('api/', include("transactions.urls"))
]

urlpatterns += [
    path('login/', views.obtain_auth_token)
]