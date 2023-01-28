from django.urls import path
import poll.views as poll_views

urlpatterns = [
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('', poll_views.home, name='home'),
]