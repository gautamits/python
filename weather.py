from datetime import date
import requests
import math 
forecast_io_key = '7bf4e5f81927d57e70077ccde6eb038c'
api_forecast_io = 'https://api.forecast.io/forecast/{}/{},{},{}'

def get_weather(lat, lng):
	dat = '{}T12:00:00-0400'.format(date.today()) 
	lookup_url = api_forecast_io.format(forecast_io_key, lat, lng, dat)
	json_response = requests.get(lookup_url).json()
	hourly_data = json_response[u'hourly'][u'data']
	hourly = []  
	for hour in hourly_data:
		#find the windchill
		T = hour[u'temperature']
		V = hour[u'windSpeed']
		windchill = math.ceil(35.74 + (0.6215*T) - (35.75*(V**0.16)) + (0.4275*T*(V**0.16)))

		hour_dict= {'time': hour[u'time'],'temperature': hour[u'temperature'],'windspeed': hour[u'windSpeed'],'windchill': windchill}
		hourly.append(hour_dict)
	return hourly
data=get_weather(25,81)
for i in data:
	print i
