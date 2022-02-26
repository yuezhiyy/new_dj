from django.urls import path
# from mgr.customer import dispatcher
from mgr import customer
from mgr import sign_in_out

# 子路由表
urlpatterns = [

    path('customers', customer.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),

]
