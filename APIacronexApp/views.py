#Vistas que se pueden solicitar por url

from rest_framework import viewsets
from .serializador import maquinasSerializer
from .models import maquinas

class maquinasView(viewsets.ModelViewSet):
    serializer_class = maquinasSerializer
    queryset = maquinas.objects.all()



# class maquinasViewLista(View):
#     def get(self,request):
#         if ('name' in request.GET):
#             listaMaq = maquinas.objects.filter(nombre__contains=request.GET['name'])                    
#         else:
#             listaMaq = maquinas.objects.all()      
#         return JsonResponse(list(listaMaq.values()), safe=False)

# class maquinasViewEntidad(View):    
#         def get(self,request,pk):
#             maqDetalle = maquinas.objects.get(pk=pk)
#             return JsonResponse(model_to_dict(maqDetalle), safe=False)

# class maquinasViewPrueba(View):
#     def post(request):
#           if request.method == 'POST':
#                 serializer= serializers.serialize("json", request.data)
#                 #serializer = SnippetSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()  #da de alta un registro con este comando
#                     return JsonResponse(serializer.data, safe=False)
#                     #return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'POST'])
        # def snippet_list(request):   
        #     if request.method == 'GET':
        #         maquinas = maquinas.objects.all()
        #         serializer = model_to_dict(maquinas, many=True)
        #         return JsonResponse(serializer.data)

        #     elif request.method == 'POST':
        #         serializer = SnippetSerializer(data=request.data)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#class modificarMaquina(View):
#    def post(self,request):
#      if request.method == 'POST':
#        print(request.POST)

