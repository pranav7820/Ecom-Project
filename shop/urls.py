from django.urls import path ,include
from shop import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="About"),
    path('contact',views.contact,name="Contact"),
    path('tracker',views.tracker,name="TrackingStatus"),
    path('search',views.search,name="Search"),
    path('productView',views.productView,name="productView"),
    path('checkout',views.checkout,name="CheckOut"),

]
