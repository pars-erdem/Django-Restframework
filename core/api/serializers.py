from rest_framework import serializers

from core.models import Article


class ArticleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    creation_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    publish_date = serializers.DateTimeField()
    active = serializers.BooleanField()
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    def update(self, instance, validated_data):
        ##instance::data to be updated
        instance.author=validated_data.get("author",instance.author)
        ########
        ##if "author" in validated_data:
        ##    instance.author = validated_data["author"]
        ##########
        instance.title=validated_data.get("title",instance.title)
        instance.text=validated_data.get("text",instance.text)
        instance.city=validated_data.get("city",instance.city)
        instance.publish_date =validated_data.get("publish_date",instance.publish_date)
        instance.active=validated_data.get("active",instance.active)
        instance.save()
        return instance
