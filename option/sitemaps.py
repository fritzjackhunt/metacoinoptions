from typing import Protocol
from django.contrib import sitemaps
from django.urls import reverse
from django.conf import settings

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    protocol = 'https'
    SITE_ID = 1

    def items(self):
        return ['homepage', 'ourteam', 'awards', 'segregated', 'disclosure', 'terms', 'policy', 'laundering', 'audit', 'trade_risk', 'bonus', 'forex_essentials', 'exchange_rates', 'analysis', 'technical_analysis', 'forex', 'precious_metals', 'cfd_shares', 'cfd_indices', 'cfd_crypto', 'leverage']

    def location(self, item):
        return reverse(item)