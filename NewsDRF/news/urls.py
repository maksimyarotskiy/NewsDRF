from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsView


# router = DefaultRouter()
# router.register(r'news', NewsViewSet)

urlpatterns = [
    # path('', include(router.urls)),
        path('news/', NewsView.as_view(), name='news-list'),
]
