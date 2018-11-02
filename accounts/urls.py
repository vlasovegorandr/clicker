from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.LeaderboardsListView.as_view(), name='leaderboards'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^player_creation$', views.player_creation, name='player_creation')
]