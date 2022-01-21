from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        #if you want to add all the fields from model use '__all__'
        fields = "__all__"
        #if you want add partcular field from model use below lines
        # fields =['id','name','active']
        # if you want to exclue some fields can define those fields in list in exclude
        # exclude = ['description']

    # def get_len_name(self, object):
    #     return len(object.name)
    #
    # def validate_name(self, value):
    #     print("value is "+value)
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name is too short!!")
    #     else:
    #         return value
    #
    # def validate_active(self, value):
    #
    #     if value == False:
    #         raise serializers.ValidationError("Acceptiong only active movies!!")
    #     else:
    #         return value



"""def name_length(value):
    if len(value) <=2:
         raise serializers.ValidationError("Name is too short - found in validators!!")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance"""

    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description should be different!!")
    #     else:
    #         return data


    # def validate_name(self, value):
    #     print("value is "+value)
    #     if len(value) <= 2:
    #         raise serializers.ValidationError("Name is too short!!")
    #     else:
    #         return value
    #
    # def validate_active(self, value):
    #
    #     if value == False:
    #         raise serializers.ValidationError("Acceptiong only active movies!!")
    #     else:
    #         return value

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)

    # if you used StringRelatedField then it will display only related model __str__ method
    # watchlist = serializers.StringRelatedField(many=True)

    # if you used PrimaryKeyRelatedField then it will display only primery key of the model
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # if you used HyperlinkedRelatedField then it will display url of the model
    # watchlist = serializers.HyperlinkedRelatedField(
    #                         many=True, read_only=True,
    #                         view_name='movie-detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"
