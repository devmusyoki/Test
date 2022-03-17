from django.urls import path
from .views import SidebarDetail, SidebarList

app_name = "testing"

urlpatterns = [
    path('<int:pk>/', SidebarDetail.as_view(), name='detailcreate'),
    path('', SidebarList.as_view(), name='listcreate'),
]
