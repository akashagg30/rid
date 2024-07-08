from django.urls import path, include
from base.users.urls import urlpatterns as users_urls
from base.boards.urls import urlpatterns as boards_urls

urlpatterns = [
    path("", include(users_urls)),
    path("", include(boards_urls)),
]