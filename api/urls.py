from django.urls import path
from .views import *

urlpatterns = [
    path('info/', InfoView.as_view()),
    path('counter-area/', CounterAreaView.as_view()),
    path('about-us-img/', AboutUsImgView.as_view()),
    path('about-us/', AboutUsView.as_view()),
    path('why-choose/', WhyChooseUsView.as_view()),
    path('products/', ProductView.as_view()),
    path('partner/', PartnerView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('faq/', FaqView.as_view()),
    path('faq-img/', FaqImgView.as_view()),
    path('pricing-table/', PricingTableView.as_view()),
    path('contact-us/', ContactUsView.as_view()),
    path('blog/<int:pk>/', BlogView.as_view()),
    path('blogs/', BlogsView.as_view()),
    path('comment-create/', CommentCreateView.as_view()),
    path('like-add/<int:pk>/', LikeAddView.as_view()),
    path('like-remove/<int:pk>/', LikeRemoveView.as_view()),
    path('subscriber/', SubscriberView.as_view()),
    path('slid-products/', SledProducts.as_view()),
    path('recent-products/', RecentProducts.as_view()),
    path('login/', login),
    path('cart-add/<int:pk>/', cart_add),
    path('cart-remove/<int:pk>/', cart_remove),
    path('carts/', carts),
    path('add-wishlist/<int:pk>/', add_wishlist),
    path('remove-wishlist/', remove_wishlist),
    path('search/', search)
]