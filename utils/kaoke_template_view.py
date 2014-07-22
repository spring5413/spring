import random
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin


class Kaoke_TemplateView(TemplateView):
    """
    A view that renders a template.
    """

    def get_context_data(self, **kwargs):
        is_debug = settings.DEBUG
        version = ""

        if is_debug:
            version = random.randint(1, 100000)
        version_rm = random.randint(1, 100000)
        print 'version = %s' % version
        return {
            'SHOP_CART_ID': settings.SHOP_CART_ID,
            'params': kwargs,
            'VERSION': version,
            'VERSIONRM': version_rm,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)