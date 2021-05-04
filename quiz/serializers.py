from rest_framework import serializers
from .models import *

class CreateQueSerializer(serializers.ModelSerializer):
    category_type = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ["question", "category_type", "is_multiple_choice", "answer", "marks", "is_mandatory", "marks", ]
        
    def get_category_type(self, obj):
        return obj.category_type.category_name
