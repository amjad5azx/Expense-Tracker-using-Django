"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path('add/', views.add_expense, name='add_expense'),
    path('expense-chart/',views.expense_chart,name='expense_chart'),
    path('delete_expense/<str:source>/', views.delete_expense, name='delete_expense'),

    #testig only
    path('fullname/', views.fullname, name='fullname'),
    path('username/', views.username, name='username'),
    path('email/', views.email, name='email'),
    
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

