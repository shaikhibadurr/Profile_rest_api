from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profile_app import views

router=DefaultRouter()
router.register('hello-viewsets',views.HelloViewSets, basename='hello-viewset')
urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
]
