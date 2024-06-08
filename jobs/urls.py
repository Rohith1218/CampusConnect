
from django.urls import path
from .views import index, freelancerlistview, freelancerdetailview, freelancercreateview, businesscreateview, handle_login

urlpatterns = [
    path('',freelancerlistview.as_view(), name='freelancer-list'),
    path('account-setup/', handle_login, name='handle-login'),
    path('developer/<int:pk>/',freelancerdetailview.as_view(), name='freelancer-detail'),
    path('freelancer/create/',freelancercreateview.as_view(), name='freelancer-create'),
    path('business/create/',businesscreateview.as_view(), name='business-create'),

]