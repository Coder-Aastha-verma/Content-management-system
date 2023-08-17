from django.urls import path
from cmwapp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
    path('signin',views.signin,name="signin"),
    path('contactreg/',views.contactreg,name="contactreg"),
    path('foo/',views.foo,name="foo"),
    path('log/',views.log,name='log'),
    path('sign/',views.sign,name="sign"),
    path('blogblog/',views.blogblog,name="blogblog")

]