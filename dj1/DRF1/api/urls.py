from app1.views import index,person
from django.urls import path,include
from app1.views import PersonApi, PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("personsx", PersonViewSet)
urlpatterns = [
    path('index/', index),
    path('person/',person),
    path('persons/',PersonApi.as_view()),
    path('router/', include(router.urls)),
]

