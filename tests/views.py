from django.http import JsonResponse, HttpResponse
from django.views import View
import json
from .models import Question, Category , Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Question, Category, Answer
from .serializers import QuestionSerializer, CategorySerializer, AnswerSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated


class QuestionCategoryAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, pk=None):
        if pk is not None:  
            try:
                question = Question.objects.get(pk=pk)
                serializer = QuestionSerializer(question)
                return Response(serializer.data)
            except Question.DoesNotExist:
                return Response({"error": "Question does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
       
        questions = Question.objects.all()
        categories = Category.objects.all()
        question_serializer = QuestionSerializer(questions, many=True)
        category_serializer = CategorySerializer(categories, many=True)
        return Response({
            'questions': question_serializer.data,
            'categories': category_serializer.data
        })

    def post(self, request):
        data = request.data
        if 'category' in data and 'question' in data and 'answers' in data:
            category_name = data.get('category')
            question_text = data.get('question')
            marks = data.get('marks', None)
            answers = data.get('answers', [])

            category, created = Category.objects.get_or_create(cetagory_name=category_name)
            if created:
                print("Category added successfully")

            if Question.objects.filter(question=question_text, category=category).exists():
                return Response({"error": "Question already exists"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                question = Question.objects.create(
                    category=category,
                    question=question_text,
                    marks=marks
                )
                for key, value in answers.items():
                    ans_text = value.get('ans')
                    is_correct = value.get('is_correct')
                    answer = Answer.objects.create(
                        question=question,
                        answer=ans_text,
                        is_correct=is_correct
                    )
                return Response({"message": "Question and Answers added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        data = request.data
        current_category_name = data.get('currentcategory')
        category_name = data.get('updatedcategory')
        question_text = data.get('question')
        marks = data.get('marks', None)
        answers = data.get('answers', {})

        try:
            category = Category.objects.get(cetagory_name=current_category_name)
            # print("updation stage 1 clear...................")
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            question = Question.objects.get(pk=pk)
            # print("updation stage 2 clear...................")
        except Question.DoesNotExist:
            return Response({"error": "Question does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
        category.cetagory_name = category_name
        category.save()
        question.question = question_text
        question.marks = marks
        question.save()

        # print("updation stage 3 clear...................")

        for answer_id, answer_data in answers.items():
            try:
                answer = Answer.objects.get(pk=answer_id)
            except Answer.DoesNotExist:
                answer = Answer()

            answer.question = question
            answer.answer = answer_data.get('answer')
            answer.is_correct = answer_data.get('is_correct', False)
            answer.save()
        # print("updation stage 4 clear...................")
        return Response({"message": "Category, question, and answers updated successfully"}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        data  = request.data
        sectiontype = data.get('section')
        if sectiontype == 'question': 
            try:
                question = Question.objects.get(pk=pk)
            except Question.DoesNotExist:
                return Response({"error": "Question does not exist"}, status=status.HTTP_404_NOT_FOUND)
        elif sectiontype == 'category':
            try:
                question = Category.objects.get(pk=pk)
            except Question.DoesNotExist:
                return Response({"error": "category does not exist"}, status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response({"message": "delection successfully"},status=status.HTTP_200_OK)

