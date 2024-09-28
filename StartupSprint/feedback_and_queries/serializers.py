from rest_framework import serializers
from feedback_and_queries .models import FeedBack


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields='__all__'