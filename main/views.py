from django.shortcuts import render
import json # json data to load JSON to python dictionary
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # source is the json data received from weather api
        murl = 'http://api.openweathermap.org/data/2.5/weather?q='+city+',&APPID=*****************************'
        source = urllib.request.urlopen(murl).read()
        list_of_data = json.loads(source)
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request,'main/index.html',data)



