"""suorganizer URL Configuration

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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include, url

# from organizer import urls as organizer_urls
# from blog import urls as blog_urls

# urlpatterns = [

# 	# ADMIN
#     path('admin/', admin.site.urls),

#     # ORGANIZER
#     url(r'^', include(organizer_urls)),

#     # BLOG
#     url(r'^blog/', include(blog_urls)),
# ]


# USING CLASS-BASED VIEW
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from organizer import urls as organizer_urls
from blog import urls as blog_urls
from blog.views import PostList
from suorganizer.views import redirect_root

urlpatterns = [

    # BLOG
    # '''This url redirect to: http://127.0.0.1:8000/blog/'''
    url(r'^$', redirect_root),
    # '''This url returns: http://127.0.0.1:8000/blog/'''
    url(r'^$', PostList.as_view()), # replace by url above (line 50)
    url(r'^blog/', include(blog_urls)), 

    # ORGANIZER
    url(r'^', include(organizer_urls)),

	# ADMIN
    path('admin/', admin.site.urls),

]