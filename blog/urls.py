# # blog/urls.py
# from django.conf.urls import url


# from .views import post_list, post_detail

# urlpatterns = [

#     url(r'^$',
# 	        post_list,
# 	        name='blog_post_list'),

#     url(r'^(?P<year>\d{4})/'
# 	        r'(?P<month>\d{1,2})/'
# 	        r'(?P<slug>[\w\-]+)/$',
# 	        post_detail,
# 	        name='blog_post_detail'),
# ]


# USING CLASS-BASED VIEW
# blog/urls.py
from django.conf.urls import url


from .views import PostList, post_detail

urlpatterns = [

    url(r'^$',
	        # post_list,
	        PostList.as_view(),
	        name='blog_post_list'),

    url(r'^(?P<year>\d{4})/'
	        r'(?P<month>\d{1,2})/'
	        r'(?P<slug>[\w\-]+)/$',
	        post_detail,
	        name='blog_post_detail'),
]