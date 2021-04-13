"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from myapp.views import postregister, logout_view

admin.site.site_header="TheBoyes Administrator Dashboard"
# https://www.youtube.com/watch?v=PX6J6h_ihyE&list=PLVZgTVNoxdMksQAJI7J2IHpNW7rY7U3XI&index=2
urlpatterns = [

    path('admin/', admin.site.urls, name="admin"),
    path("external/",  v.external),
    path("normal_external/",  v.norm_scan, name="normal_scan"),
    path("fullscan/",  v.fullscan_arachni, name="full"),
    path("fullauthscan/",  v.fullscan_arachni_auth, name="full_auth"),
    path("fullscan_external/",  v.arachni),
    path("fullscan_external_auth/",  v.arachni_auth),
    path("normal/", v.normal),
    path('home/', v.home, name="home"),
    path('report/', v.report, name="report"),
    path('normal/', v.normal, name="normal"),
    path('attack', v.attack, name='attack'),
    path('administrator/', v.admin_custom, name='admin_custom'),
    path('new-user/', v.admin_reg, name='admin_reg'),
    path('full-normal/', v.index, name="welcome"),
    # path('', v.postsign, name="post_sign"),
    # path('login/', v.signIn, name="login"),
    path('welcome/', v.postsign, name="post_sign"),
    path('', v.signIn, name="login"),
    path('signup/', v.postregister),
    path('processing_user/',v.del_disble_user, name="del_disble_user"),
    path('post_adm_login/',v.admin_process_log),
    path('admin-login/', v.admin_login, name="admin_log_in"),
    path('logout/', v.logout_admin, name="logoutadmin"),
    path('accounts/logout/', logout_view, name="logout")
    
]

urlpatterns += staticfiles_urlpatterns()



