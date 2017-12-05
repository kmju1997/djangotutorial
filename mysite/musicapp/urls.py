from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'musicapp'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album_add'),
]

# r'' -> 정규식 / views.index -> 이 url을 요청하면 불러올 view  함수 / name -> url 별 이름 나중에 템플릿에서 사용