from django.urls import path
from .views import FollowsView, UnfollowView, FollowersListView, FollowingListView

urlpatterns = [
    path('follow/<int:user_id>/', FollowsView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='following'),
]
