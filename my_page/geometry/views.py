from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def redirect(request, **kwargs):
    figure = request.path.split('/')[2]
    match figure:
        case 'get_rectangle_area':
            redirect_url_rectangle = reverse('redirect-rectangle', args=(kwargs["width"], kwargs["height"], ))
            return HttpResponseRedirect(redirect_url_rectangle)
        case 'get_square_area':
            redirect_url_square = reverse('redirect-square', args=(kwargs["width"], ))
            return HttpResponseRedirect(redirect_url_square)
        case 'get_circle_area':
            redirect_url_circle = reverse('redirect-circle', args=(kwargs["radius"], ))
            return HttpResponseRedirect(redirect_url_circle)


def get_rectangle_area(request, width, height):
    return render(request, 'geometry/rectangle.html')
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width):
    return render(request, 'geometry/square.html')
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius):
    return render(request, 'geometry/circle.html')
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius ** 2}')
