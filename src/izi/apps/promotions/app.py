from django.conf.urls import url

from izi.core.application import Application
from izi.core.loading import get_class, get_model


KeywordPromotion = get_model('promotions', 'KeywordPromotion')
PagePromotion = get_model('promotions', 'PagePromotion')


class PromotionsApplication(Application):
    name = 'promotions'

    home_view = get_class('promotions.views', 'HomeView')
    record_click_view = get_class('promotions.views', 'RecordClickView')

    def get_urls(self):
        urls = [
            url(r'page-redirect/(?P<page_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=PagePromotion),
                name='page-click'),
            url(r'keyword-redirect/(?P<keyword_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click'),
            url(r'^$', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)


application = PromotionsApplication()
