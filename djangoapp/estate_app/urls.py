from django.urls import re_path, path
from rest_framework import routers
from .views import QueryView, PingView, ResultView, CadastralHistoryView

router = routers.DefaultRouter()

urlpatterns = [
    re_path(r"^query/", QueryView.as_view()),
    re_path(r"^ping/", PingView.as_view()),
    path("result/<int:pk>/", ResultView.as_view(), name="result"),
    path("history/<cadastral_number>/", CadastralHistoryView.as_view(), name="history"),
]

urlpatterns += router.urls
