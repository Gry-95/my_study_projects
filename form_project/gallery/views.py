from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import GalleryUploadForm
from .models import Gallery


# Create your views here.

class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'


# def storage_file(file): #Если нет модели юзаем это, иначе galleryview post заменяет эту функцию
#   with open(f'gallery_tmp/{file.name}', 'wb+') as new_file:
#      for chunk in file.chunks():
#         new_file.write(chunk)


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    # fields = '__all__'
    template_name = 'gallery/load_file.html'
    success_url = 'load_image'
