from django.urls import path

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, ChoiceDetail


urlpatterns = [
    path("polls/", PollList.as_view(), name='polls_list'),
    path("polls/<int:pk>", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("choices/<int:pk>", ChoiceDetail.as_view(), name="choice_detail"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]
