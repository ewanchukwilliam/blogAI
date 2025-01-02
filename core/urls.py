from django.urls import path

from core import views

urlpatterns = [
    path("", views.homepage, name="home"),
]

# path("january", views.homepageview),
# path('<int:arguments>',views.dynamicNumber, name="dynamicNumber"),
# path('<str:arguments>',views.dynamicURL, name="dynamicURL"),
# path("<int:month>", views.month_number, name="month_number"),
# path("<str:month>", views.month, name="month"),
