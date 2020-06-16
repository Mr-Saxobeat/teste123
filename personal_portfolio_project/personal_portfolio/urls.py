"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views as portfolio_views

urlpatterns = [
    path('', portfolio_views.home, name='portfolio'),
    # path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
<<<<<<< HEAD
    path('fraude/', portfolio_views.fraude, name='fraude'),
    path('agathinha/', portfolio_views.agathinha, name='agathinha'),
=======
    path('fraude/', portfolio_views.fraude, name='fraude')
>>>>>>> 171912b1ad87cf44a656baf5b6edbfb307bc7c67
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
