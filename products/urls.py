from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, my_products, signup,
    block_user, unblock_user, chat_view, report_product, transfer_view
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('my/', my_products, name='my_products'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
    path('signup/', signup, name='signup'),
    path('block/<int:user_id>/', block_user, name='block_user'),
    path('unblock/<int:user_id>/', unblock_user, name='unblock_user'),
    
    path('chat/', chat_view, name='chat'),
    path('<int:pk>/report/', report_product, name='report_product'),
    path('transfer/', transfer_view, name='transfer'),
]