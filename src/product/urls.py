from django.urls import path
from . import views
from .views import ProductDetails, SingleProduct, SearchFilterPage, ApplyFilters

urlpatterns = [
    path('compare/', views.Compare, name='compare'),
    path('product_detail', ProductDetails.as_view(), name='product_detail'),
    path('search', views.Search, name='search'),
    path('search_by_category/<int:category_id>/', SearchFilterPage.as_view(), name='search_by_category'),
    path('search_by_category/', SearchFilterPage.as_view(), name='search_by_query'),
    path('search_by_category/apply_filters/', ApplyFilters.as_view(), name='search_by_filter'),
    path('product/<int:pk>', SingleProduct.as_view(), name='product_detail'),
    path('search_by_category/<int:category_id>/apply_filters/', ApplyFilters.as_view(), name='search_by_filter'),
]