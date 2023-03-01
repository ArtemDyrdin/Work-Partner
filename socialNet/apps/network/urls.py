from django.contrib.auth import logout
from socialNet.settings import LOGOUT_REDIRECT_URL
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.main, name='main'),
    path('account', views.account, name='account'),
    path('find', views.find, name='find'),
    path('account_edit', views.account_edit, name='account_edit'),
    path('friends', views.friends, name='friends'),
    path('addpartner/<int:pk>', views.add_partner, name='add_partner'),
    path('person/<int:pk>', views.person, name='person'),
    path('dialogs/create/<int:user_id>',
         views.CreateDialogView.as_view(), name='create_dialog'),
    path('dialogs/<int:chat_id>',
         views.MessagesView.as_view(), name='messages'),
    path('dialogs', views.DialogsView.as_view(), name='dialogs'),
    path('signup', views.register, name='signup'),
    path('signin', views.LogInView.as_view(), name='signin'),
    path('logout', authViews.LogoutView.as_view(), name='logout'),
]
