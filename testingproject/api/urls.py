from django.urls import path,include
from itemapp.views import RegisterApi,LoginApi,ListCategory,DetailCategory,ProductList,ProductDetail,ListUser,DetailUser,ListCart,DetailCart,helloview
# ,ProductViewset
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'product',ProductViewset,basename='Product')
# urlpatterns = router.urls


urlpatterns = [
    path('hello/', helloview,name='Hello'),
    path('register/',RegisterApi.as_view(),name='Register'),
    path('login/',LoginApi.as_view(),name='Login'),
    path('categorylist/',ListCategory.as_view(),name='CategoryList'),
    path('categorydetail/',DetailCategory.as_view(),name='CategoryDetail'),
    path('productlist/',ProductList.as_view(),name='ProductList'),
    path('productdetail/<int:id>',ProductDetail.as_view(),name='ProductDetail'),
    path('users/',ListUser.as_view(),name='Users'),
    path('users/<int:id>',DetailUser.as_view(),name='UserDetail'),
    path('cart/',ListCart.as_view(),name='Cart'),
    path('cart/<int:id>',DetailCart.as_view(),name='DetailCart'),
    # path('',include(router.urls)),
]