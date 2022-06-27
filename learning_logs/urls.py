'''Define URL patterns for learning_logs'''
from django.urls import path

from .import views

app_name = 'learning_logs'
urlpatterns = [
    # homepage (learning/)
    path('', views.index, name='index'),
    # page that shows all topics (learning/topics/)
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic (learning/topics/topic_id/)
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic (learning/new_topic/)
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
