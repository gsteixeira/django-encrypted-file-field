from app.views import FoobarView
from django.urls import path

urlpatterns = [
    path("foobar/<int:pk>/", FoobarView.as_view(), name="foobar_view"),
]
