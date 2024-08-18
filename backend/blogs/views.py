from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, permissions
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit


@method_decorator(ratelimit(key='ip', rate='2/m', block=True), name='dispatch')
class CategoryList(generics.ListCreateAPIView):
    """
    List all categories, or create a new category.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]



# class CategoryDetail(APIView):
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category instance.
    """
    # def get_object(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class BlogList(generics.ListCreateAPIView):
    """
    List all blogs, or create a new blog.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Delete Blog instance
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]