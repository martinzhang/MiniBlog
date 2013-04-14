from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('myblog.views',
    url(r'^$', 'index'),
    url(r'^add', 'blog_add'),
    )

urlpatterns += patterns('myblog.views',
    url(r'^user/add', 'user_add'),
    url(r'^user/login', 'user_login'),                   
    )