from django.urls import path
from .views import MsgCreate, MsgDelete, logoutfunc, signupfunc,loginfunc,sredfunc,boardfunc,BoardCreate,BoardDelete,MsgDetailfunc

urlpatterns = [
    path('', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('sred/', sredfunc, name='sred'),
    path('board/', boardfunc, name='board'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete'),
    path('logout/', logoutfunc,name='logout'),
    path('detail/<int:pk>',MsgDetailfunc.as_view(),name='detail'),
    path('msg_create/<int:pk>',MsgCreate.as_view(),name='msg_create'),
    path('msg_delete/<int:pk>',MsgDelete.as_view(),name='msg_delete')
]