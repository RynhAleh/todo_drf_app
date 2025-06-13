from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, PeopleViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'people', PeopleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
