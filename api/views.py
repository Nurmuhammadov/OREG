from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import *
from .serializers import *
from rest_framework.decorators import *
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import *


@api_view(['POST'])
def login(request):
    username = request.data['username']
    passwd = request.data['password']
    User.objects.get(username=username)
    user = authenticate(username=username, password=passwd)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
        }
        return Response(data)
    else:
        return Response({'message': 'No such user!'})


class InfoView(ListAPIView):
    queryset = Information.objects.last()
    serializer_class = InfoSerializer

    def list(self, request):
        return Response(InfoSerializer(self.queryset).data)


class CounterAreaView(ListAPIView):
    queryset = CounterArea.objects.last()
    serializer_class = CounterAreaSerializer

    def list(self, request):
        ser = CounterAreaSerializer(self.queryset).data
        return Response(ser)


class AboutUsImgView(ListAPIView):
    queryset = AboutUsImg.objects.last()
    serializer_class = AboutUsImgSerializer

    def list(self, request):
        ser = AboutUsImgSerializer(self.queryset).data
        return Response(ser)


class AboutUsView(ListAPIView):
    queryset = AboutUs.objects.last()
    serializer_class = AboutUsSerializer

    def list(self, request):
        ser = AboutUsSerializer(self.queryset).data
        return Response(ser)


class WhyChooseUsView(ListAPIView):
    queryset = WhyChooseUs.objects.last()
    serializer_class = WhyChooseUsSerializer

    def list(self, request):
        ser = WhyChooseUsSerializer(self.queryset).data
        return Response(ser)


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class GalleryView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class FaqView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def list(self, request):
        obj = self.queryset.all().order_by('-id')[:5]
        return Response(self.serializer_class(obj, many=True).data)


class FaqImgView(ListAPIView):
    queryset = FaqImg.objects.last()
    serializer_class = FaqImgSerializer

    def list(self, request):
        ser = FaqImgSerializer(self.queryset).data
        return Response(ser)


class PricingTableView(ListAPIView):
    queryset = PricingTable.objects.all()
    serializer_class = PricingTableSerializer


class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def create(self, request):
        new = ContactUsSerializer(data=request.data)
        if new.is_valid():
            new.save()
            return Response({"success": True})
        else:
            return Response({"success": False})


class BlogView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        obj = self.queryset.get(id=pk)
        comment = Comment.objects.filter(which_blog=obj)
        comments = []
        for i in comment:
            comments.append(i.comment_text)
            data = {'obj': BlogSerializer(obj).data,
                    'comment_count': len(comments),
                    'comments': CommentSerializer(comment, many=True).data
                    }
        return Response(data)


class BlogsView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        obj = self.queryset.all().order_by('-id')[:3]
        return Response(self.serializer_class(obj, many=True).data)


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        comment = request.POST.get('comment_text')
        which_blog = request.POST.get('which_blog')
        fil = Blog.objects.get(id=which_blog)
        a = Comment.objects.create(comment_text=comment, which_blog=fil)
        return Response(CommentSerializer(a).data)
        # return Response(CommentSerializer(Comment.objects.last()).data)


class LikeAddView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        q = self.queryset.get(id=pk)
        q.likes += 1
        q.save()
        return Response(BlogSerializer(q).data)


class LikeRemoveView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, pk):
        q = self.queryset.get(id=pk)
        q.likes -= 1
        q.save()
        return Response(BlogSerializer(q).data)


class SubscriberView(CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request):
        new = SubscriberSerializer(data=request.data)
        if new.is_valid():
            new.save()
            return Response({'success': True})
        else:
            return Response({'success': False})


class SledProducts(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        sled_products = self.queryset.filter(is_slid=True)
        return Response(ProductSerializer(sled_products, many=True).data)


class RecentProducts(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        recent_products = self.queryset.all().order_by('-id')[:3]
        ser = self.serializer_class(recent_products, many=True).data
        return Response(ser)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_add(request, pk):
    # noinspection PyBroadException
    try:
        product = Product.objects.get(id=pk)
        Cart.objects.create(product=product, user=request.user)
        return Response({'success': True}, status=HTTP_201_CREATED)
    except:
        return Response(0)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_remove(request, pk):
    cart = Cart.objects.get(id=pk, user=request.user)
    cart.delete()
    return Response({'success': True})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def carts(request):
    cart = Cart.objects.filter(user=request.user)
    return Response(CartSerializer(cart, many=True).data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_wishlist(request, pk):
    product = Product.objects.get(id=pk)
    Wishlist.objects.create(product=product, user=request.user)
    return Response({'success': True}, status=HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_wishlist(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response({'success': True})


@api_view(['GET'])
def search(request):
    search = request.GET.get('search')
    products = Product.objects.filter(name__icontains=search)
    return Response(ProductSerializer(products, many=True).data, status=HTTP_200_OK)