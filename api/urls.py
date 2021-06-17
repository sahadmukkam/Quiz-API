from django.urls import path
from .views import Quiz,RandomQuestion,QuizQuestion,StartQuiz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    
    path('', Quiz.as_view(),name='quiz'),
    path('r/<str:topic>', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>', QuizQuestion.as_view(), name='questions'),
    path('single/<str:title>/',StartQuiz.as_view(),name='quiz')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)