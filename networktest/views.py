from django.shortcuts import render
import speedtest
# Create your views here.
def first(request):
    return render(request, 'button.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    speed = speedtest.Speedtest()
    speed.get_best_server()

    up = (speed.upload())//1000000
    down = speed.download()//1000000
    ping = int(speed.results.ping)

    results_dict = speed.results.dict()
    name = results_dict['server']['name']
    country = results_dict['server']['country']

    isp = results_dict['client']['isp']
    isprating = results_dict['client']['isprating']
    '''

    down=0
    up=0
    ping=0
    name=0
    country=0
    isp=0
    isprating=0'''

    return render(request, 'index.html', {'download':down, 'upload':up, 'ping':ping  ,'name' : name,'country':country,'isp':isp,'isprating':isprating})

