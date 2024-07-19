from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Item

def get_data(request):
    items = Item.objects.all().values('id', 'name')
    return JsonResponse(list(items), safe=False)

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        item = Item.objects.create(name=name)
        return JsonResponse({'id': item.id, 'name': item.name})
    else:
        return HttpResponseNotAllowed(['POST'])
