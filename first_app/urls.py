from . import views
from django.conf.urls import url


app_name='first_app'

urlpatterns=[
    url(r'^index/$',views.index,name="index"),
    url(r'^registration/$',views.registration,name="register"),
    url(r'^user_login/',views.user_login,name="user_login"),
    url(r'^special_page',views.specialpage,name="special_page")
]
