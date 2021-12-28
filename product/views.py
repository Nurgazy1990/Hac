import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from product.filters import ProductFilter
from product.models import Product, Category, Comment, Like
from product.permissions import IsAdmin, IsAuthor
from product.serializers import ProductSerializer, ProductsListSerializer, CategorySerializer, CommentSerializer, \
    LikeSerializer, LikeItemSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    # pagination_class = rest_framework.pagination.PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    # api/v1/products/id/comments/
    @action(['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]




class CommentViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]


class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # user = request.user
        # like_item = Like.objects.filter(user=user)
        data = request.data
        serializer = LikeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            message = f'Вы поставили лайк'
            return Response(message, status=201)

class LikeItemView(CreateAPIView):
    serializer_class = LikeItemSerializer
    permission_classes = [IsAuthenticated]