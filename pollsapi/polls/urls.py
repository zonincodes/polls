from .views import polls_list, polls_detail
from django.urls import path

from .apiviews import PollList, PollDetail

# urlpatterns = [
#     path("polls/", polls_list, name='polls_list'),
#     path("polls/<int:pk>", polls_detail, name="polls_detail"),
# ]

urlpatterns = [
    path("polls/", PollList.as_view(), name='polls_list'),
    path("polls/<int:pk>", PollDetail.as_view(), name="polls_detail"),
]

