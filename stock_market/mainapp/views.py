from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from yahoo_fin.stock_info import get_day_gainers,tickers_nifty50
# Create your views here.
@csrf_exempt
def getNifty50List(request):
    # topgainer100 = get_day_gainers()
    # print(topgainer100)
    nifty50 = tickers_nifty50()
    return JsonResponse({"nifty50": nifty50})
@csrf_exempt
def getStockdetails(request):
    if(request.method == 'POST'):
        name = request.POST.get("name")
        print(name)
        return HttpResponse("Le bhai tune ye bheja tha ",name)
    return HttpResponse("Bhai tune get request bhejdi hai,Post bhejni hai yar")