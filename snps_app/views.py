from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'snps_app/index.html'

class AboutUsView(TemplateView):
    template_name = 'snps_app/aboutus.html'

class FindUsView(TemplateView):
    template_name = 'snps_app/findus.html'

class GalleryView(TemplateView):
    template_name = 'snps_app/gallery.html'

class StaffView(TemplateView):
    template_name = 'snps_app/staff.html'
