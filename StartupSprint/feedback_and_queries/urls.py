from django.urls import path
from feedback_and_queries import views


urlpatterns =[
    path('feedback/',views.FeedbackView.as_view(),name='feedback'),
    path('feedback_list/',views.FeedbackView.as_view(),name='feedback_list')
    

]
