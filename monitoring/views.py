from django.views import generic
from django.contrib.auth import mixins

# Create your views here.


class Home(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'monitoring/home.html'

    def test_func(self):
        return self.request.user is not None
