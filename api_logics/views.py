from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import pickUpSerializer, contactSerializer, testimonialSerializer
from .models import testimonialClass
from rest_framework import serializers, status
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.


@api_view(['POST'])
def pickUp(request):
    
    query_params = request.query_params.copy() or request.data.copy()
    query_params['phone_number'] = '+' + query_params['phone_number']
    serializer = pickUpSerializer(data=request.data or query_params)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        serializer.save(validated_data)

        return Response({
            'status' : status.HTTP_202_ACCEPTED,
            'request' : 'Your Pick up request has been accepted'
        })
    else:
        raise serializers.ValidationError(
            serializer.errors
        )
@api_view(['POST']) 
def contact(request):
    serializer = contactSerializer(data = request.data or request.query_params)

    if serializer.is_valid():
        data = serializer.validated_data
        serializer.save(data)
        return Response({
            'status': status.HTTP_202_ACCEPTED,
            'request': 'Your Contact has been recieved Thanks for reaching out'
        })
    else:
        raise serializers.ValidationError(
            serializer.errors
        )


@api_view(['GET'])
def testimonials(request):
    try:
        testimonial_list = testimonialClass.objects.all()
    except testimonialClass.DoesNotExist:
        return HttpResponse(status=404)
    serializer = testimonialSerializer(testimonial_list, many=True)

    return Response({
        'status': status.HTTP_200_OK,
        'responce' : serializer.data
    })

@api_view(['GET'])
def testimonial(request, pk):
    try:
        testimonial_list = testimonialClass.objects.get(pk=pk)
    except testimonialClass.DoesNotExist:
        return HttpResponse(status=404)
    serializer = testimonialSerializer(testimonial_list)

    return Response(
        serializer.data
    )
