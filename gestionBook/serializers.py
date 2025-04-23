from rest_framework import serializers




class BookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    like = serializers.BooleanField(required=False)
    authors = serializers.ListField(child=serializers.CharField())
    tags = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        from . import book_management as bm

        book_id = validated_data.pop('book_id')
        list_authors = validated_data.pop('authors')
        list_tags = validated_data.pop('tags')
        liked = validated_data.pop('like')

        result = bm.book.add(book_id,list_authors,list_tags,liked)
        return result