from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.homee, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('test', views.test, name='testpage'),
    path('ourteam', views.ourteam, name='ourteam'),
    path('awards', views.awards, name='awards'),
    path('segregated', views.segregated, name='segregated'),
    path('disclosure', views.disclosure, name='disclosure'),
    path('terms', views.terms, name='terms'),
    path('policy', views.policy, name='policy'),
    path('laundering', views.laundering, name='laundering'),
    path('audit', views.audit, name='audit'),
    path('trade_risk', views.trade_risk, name='trade_risk'),
    path('bonus', views.bonus, name='bonus'),
    path('forex_essentials', views.forex_essentials, name='forex_essentials'),
    path('exchange_rates', views.exchange_rates, name='exchange_rates'),
    path('analysis', views.analysis, name='analysis'),
    path('technical_analysis', views.technical_analysis, name='technical_analysis'),
    path('forex', views.forex, name='forex'),
    path('precious_metals', views.precious_metals, name='precious_metals'),
    path('cfd_shares', views.cfd_shares, name='cfd_shares'),
    path('cfd_indices', views.cfd_indices, name='cfd_indices'),
    path('cfd_crypto', views.cfd_crypto, name='cfd_crypto'),
    path('leverage', views.leverage, name='leverage'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'), #sitemap
    path("robots.txt",TemplateView.as_view(template_name="zloggr/robots.txt", content_type="text/plain")),  #robots.txt file
]