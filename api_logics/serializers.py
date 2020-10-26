from rest_framework import serializers
from .models import pickUpClass, contactClass, testimonialClass


class pickUpSerializer(serializers.ModelSerializer):

    def save(self, validated_data):
        
        pickUp = pickUpClass.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            bus_stop=validated_data['bus_stop'],
            address=validated_data['address'],
            number_of_item=validated_data['number_of_item'],
            message = validated_data['message'] 
        )
        pickUp.save()

    class Meta:
        model = pickUpClass
        fields = ['full_name', 'email', 'phone_number',
                 'bus_stop', 'address', 'number_of_item', 'message']
        

class contactSerializer(serializers.ModelSerializer):

    def save(self, validated_data):
        contact = contactClass.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            subject=validated_data['subject'],
            message=validated_data['message']
        )

        contact.save()

    class Meta:
        model = contactClass
        fields = '__all__'

class testimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = testimonialClass
        fields = '__all__'
