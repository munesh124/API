from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]