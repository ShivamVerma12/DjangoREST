from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=200, required=True)
    # last_name = serializers.CharField(max_length=200, required=True)
    # class_name = serializers.CharField(max_length=200, required=True)
    # age = serializers.IntegerField()

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Students` instance, given the validated data.
        """
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Students` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.age = validated_data.get('age', instance.age)

        instance.save()
        return instance
