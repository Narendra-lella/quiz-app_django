from rest_framework import serializers
from .models import Category, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', 'is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.cetagory_name')

    class Meta:
        model = Question
        fields = ('category', 'question', 'marks', 'answers')

    def get_answers(self, obj):
        answers_queryset = Answer.objects.filter(question=obj)
        answers_data = {}
        for answer in answers_queryset:
            answer_data = AnswerSerializer(answer).data
            answers_data[str(answer.id)] = answer_data
        return answers_data
