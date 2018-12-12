from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name='feed'),
    path("<image_id>/like/", view=views.LikeImage.as_view(), name='like_image'),
    path("<image_id>/unlike/", view=views.UnLikeImage.as_view(), name='unlike_image'),
    path("<image_id>/comment/", view=views.CommentOnImage.as_view(), name='comment_image'),
    path("comments/<comment_id>/", view=views.Comment.as_view(), name='comment'),
    path("search/", view=views.Search.as_view(), name='search'),
]




# images/3/Like/

# 0 creeate the url and the view
# 1 take the id from the url
# 2 we went to find an image with this id
# 3 we want to create a like for that image