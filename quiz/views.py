from quiz.models import QnaCategory, Question
from rest_framework import viewsets
from .serializers import CreateQueSerializer
from rest_framework.response import Response


class QuizViewSet(viewsets.ModelViewSet):
    model_class = Question

    serializer_action_classes = {
        'create': CreateQueSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, CreateQueSerializer)

    def list(self, request):
        queryset = self.model_class.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'ALL Ques',
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = CreateQueSerializer(data=request.data)
        serializer = self.get_serializer(data={
            **{
                "question": request.data["question"],
                "category_type": QnaCategory.objects.get_or_create(category_name=request.data["category_type"])[0].uid,
                "marks": request.data["marks"],
                "answer": request.data["answer"],
            }
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': True,
            'message': 'Que created Successfully',
            'data': serializer.data
        })
