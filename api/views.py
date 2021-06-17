from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Category, Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(
            quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class StartQuiz(APIView):
    def get(self,request,**kwargs):
        quiz = Quizzes.objects.filter(Category__name=kwargs['title'])
        Serializer=QuizSerializer(Quiz,many=True)
        return Response(Serializer.data)
