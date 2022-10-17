from .models import Category,Product,Cart
from .serializers import RegisterSerializer,LoginSerializer,CategorySerializer,ProductSerializer,UserSerializer,CartSerializer,CartUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

# # class CustomPaginator(PageNumberPagination):
# #     page_size = 3
# #     page_query_param = "page"
# #     page_size_query_param = "page_size"

from django.http import HttpResponse
def helloview(request):
    return HttpResponse('<h1>Hello World</h1>') 


class RegisterApi(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'User Created',
            },status=status.HTTP_201_CREATED)

        else:
            return Response({
                'status': False,
                'message': serializer.errors,
            },status=status.HTTP_400_BAD_REQUEST)

class LoginApi(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username = serializer.data['username'],password=serializer.data['password'])
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'status': True,
                'message': 'User Logged In',
                'token':str(token)
            },status=status.HTTP_201_CREATED)

        else:
            return Response({
                'status': False,
                'message': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

class ListCategory(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes=[IsAuthenticated]

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes=[IsAuthenticated]

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    # pagination_class = CustomPaginator

    def get(self,request): 
        #obj = Person.objects.filter(color__isnull=False)
        try:
            obj = Product.objects.all()
            page = request.GET.get('page',1)
            page_size=2
            paginator = Paginator(obj,page_size)
            serializer=ProductSerializer(paginator.page(page),many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status':False,
                'message':'Invalid Page. This Page doesnot have any results'
            })

    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = ProductSerializer(queryset,many=True)
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request): 
             
        try:
            obj = Product.objects.all()
            page = request.GET.get('page',1)
            page_size=2
            paginator = Paginator(obj,page_size)
            serializer=ProductSerializer(paginator.page(page),many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status':False,
                'message':'Invalid Page. This Page doesnot have any results'
            })   

    
    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = ProductSerializer(queryset,many=True)
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK)

# #usage-->http://127.0.0.1:8000/api/product/?search=tv

class ListUser(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    
