from django.urls import path
from .views import *

urlpatterns = [
    path('user_list/',UserList.as_view(),name="user_list"),
    # path('testdata/',TestDataView.as_view()),

]


