from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets


class PrimeraVista(APIView):
    '''API Vista de Prueba'''
    serializer_class = serializers.HelloSerializer

    def get(self,request, format=None):
        '''Retorno de lista de caracteristicas de APIView'''
        an_apiview = [
            'Usamos metodos HTTp',
            'Nos da Mayor control de la logica',
            'Esta mapeado a los url'
        ]

        return Response({'message': 'Hola', 'an_apiview': an_apiview})

    def post(self,request):
        '''Crea un mensaje con nuestro nombre'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Actualiza Objetos'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Maneja Actualizacion parcial'''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Borra un objeto'''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test Api ViewSet'''
    def list(self,request):
        '''Retornar Hola Mundo'''
        a_viewset = [
            'raaaaaaaaaaaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaaeeeeeeeeeeeeaaaaaaaaaaaa'
        ]
        return Response({'message': 'Hola', 'a_viewset':a_viewset})
