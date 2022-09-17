"""crs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from adm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('user.urls')),
    path('admin/', admin.site.urls),
    path('ahome/',views.ahome),
    path('deletel/<int:id>',views.deletel ),
    path('editl/<int:id>',views.editl),
    path('updatel/<int:id>',views.updatel),
    path('admlogin',views.alogin),
    path('addloc/',views.addlocation),
    path('viewl/',views.viewl),
    path('addveh/',views.addvehicle),
    path('viewv/',views.viewv),
    path('editv/<int:id>',views.editv),
    path('updatev/<int:id>',views.updatev),
    path('deletev/<int:id>',views.deletev ),
    path('viewuser/',views.viewuser),
    path('viewuserdetails/<str:email_id>',views.viewuserdetails),
    path('completebooking/<str:booking_id>',views.completebooking),
    path('acc_s',views.accountingselect),
    path('acc',views.accounting),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
