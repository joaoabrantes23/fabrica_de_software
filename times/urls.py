from rest_framework import routers
from times.views import campeonatoViewSet, timeViewSet, jogadorViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'campeonato', campeonatoViewSet)
router.register(r'time', timeViewSet)
router.register(r'jogador', jogadorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]