from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts.views import home_view
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),  # custom views
    path('accounts/', include('django.contrib.auth.urls')),  # built-in auth views
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # homepage
    path('about/', views.about, name='about'), #about page
    path('products/', views.products, name='products'),
    path('market-research/', views.market_research, name='market_research'),
    path('contact/', views.contact, name='contact'),  
]
