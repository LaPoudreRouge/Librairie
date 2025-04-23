from rest_framework import serializers




class BookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    like = serializers.BooleanField()
    authors = serializers.ListField(child=serializers.CharField())
    tags = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        from . import book_management as bm
        pass