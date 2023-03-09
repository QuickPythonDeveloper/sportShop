from django.urls import path

from .views.category.crud import HandleProductCat
from .views.category.list import ProductCatList
from .views.category.parent import CatAddParent
from .views.category.choosePar import ChooseCatParLs

from .views.product.crud import HandleProduct
from .views.product.list import ProdList
from .views.product.addInstaPerm import ProdAddInstaPerm

from .views.product.attr.crud import HandleProdAttr
from .views.product.attr.list import ProdAttrList

from .views.product.gImage.crud import HandleProdGalImage
from .views.product.gImage.list import ProdGalImageList

from .views.product.prop.crud import HandleProdProp
from .views.product.prop.list import ProdPropList


urlpatterns = [

    path('cat/crud/', HandleProductCat.as_view()),
    path('cat/crud/<int:cat_id>/', HandleProductCat.as_view()),
    path('cat/all/', ProductCatList.as_view()),
    path('cat/par/<int:cat_id>/', CatAddParent.as_view()),
    path('cat/par/<int:cat_id>/<int:parent_id>/', CatAddParent.as_view()),
    path('cat/par/ls/<int:cat_id>/', ChooseCatParLs.as_view()),

    path('p/<int:cat_id>/', HandleProduct.as_view()),
    path('g_d/<int:prod_id>/', HandleProduct.as_view()),
    path('p/<int:cat_id>/<int:prod_id>/', HandleProduct.as_view()),
    path('ls/<int:cat_id>/', ProdList.as_view()),
    path('perm/<int:prod_id>/', ProdAddInstaPerm.as_view()),

    path('attr/cr/<int:attr_id>/', HandleProdAttr.as_view()),
    path('attr/p/<int:prod_id>/', HandleProdAttr.as_view()),
    path('attr/ls/<int:prod_id>/', ProdAttrList.as_view()),

    path('img/p/<int:prod_id>/', HandleProdGalImage.as_view()),
    path('img/cr/<int:img_id>/', HandleProdGalImage.as_view()),
    path('img/ls/<int:prod_id>/', ProdGalImageList.as_view()),

    path('prop/cr/<int:prop_id>/', HandleProdProp.as_view()),
    path('prop/p/<int:prod_id>/', HandleProdProp.as_view()),
    path('prop/ls/<int:prod_id>/', ProdPropList.as_view()),

]
