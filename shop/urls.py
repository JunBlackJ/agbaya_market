from django.urls import path
from . import views

app_name ='shop'

urlpatterns = [

    #
    path('partenaire', views.PartenaireList.as_view(), name='partenaire_list'),
    path('partenaire/create', views.PartenaireCreate.as_view(), name='partenaire_create'),
    path('partenaire/<str:slug>', views.PartenaireDetail, name='partenaire_detail'),
    path('partenaire/update/<str:slug>', views.PartenaireUpdate.as_view(), name='partenaire_update'),
    path('partenaire/delete/<str:slug>', views.PartenaireDelet.as_view(), name='partenaire_delet'),
    # CATEGORY URLS
    path('category', views.CategoryList.as_view(), name='category_list'),
    path('category/create', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<str:slug>', views.CategoryDetail, name='category_detail'),
    path('category/update/<str:slug>', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<str:slug>', views.CategoryDelet.as_view(), name='category_delet'),
    
    # PRODUCTS URLS
    path('search', views.Search, name='search'),
    path('products', views.ProductList.as_view(), name='product_list'),
    path('products/create', views.ProductCreate.as_view(), name='product_create'),
    path('products/<str:slug>', views.ProductDetail, name='product_detail'),
    path('products/update/<str:slug>', views.ProductUpdate.as_view(), name='product_update'),
    path('products/delete/<str:slug>', views.ProductDelete.as_view(), name='product_delete'),
    # WISHLIST URLS
    path('wishlist/<str:slug>', views.wishlist, name='product_wishlist'),
    path('wishlistview', views.WishListView, name='wishlist_view')
]
