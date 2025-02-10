from django.urls import path
from . import views

urlpatterns = [
    path("comments",views.comments,name="comments"),
    path("comments/<int:comment_id>",views.comment,name="comment")
]