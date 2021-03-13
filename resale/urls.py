from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ResaleHome"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="RTrackingStatus"),
    path("search/", views.search, name="RSearch"),
    path("products/<int:myid>", views.productView, name="RProductView"),
    path("checkout/", views.checkout, name="RCheckout"),
    path("form/", views.form, name="RForm")

]
