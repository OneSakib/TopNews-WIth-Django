from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("", views.index, name="index Page"),
                  path("product/<str:slug>", views.product, name="Product Page"),
                  path("productcategory", views.productcategory, name="Product Page"),
                  path("search", views.search, name="Product Page"),
                  path("productview/<str:slug>", views.productview, name="product view"),
                  path("contact", views.contact, name="Contact Page"),
                  path("about", views.about, name="About Page"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
