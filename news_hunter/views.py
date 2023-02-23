from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


def get_hour():
    # Get current UTC time
    utc_time = datetime.utcnow()

    # Convert UTC time to GMT+6 time
    gmt_plus_6_time = utc_time + timedelta(hours=6)

    # Extract hour component of GMT+6 time
    hour = gmt_plus_6_time.hour

    # Return hour as integer
    return hour


def news(request):
	
	print("current bd time ",get_hour())

	

	req_url = "https://ec.forexprostools.com/?columns=exc_currency%2Cexc_importance&importance=3&calType=day&timeZone=25&lang=1"

	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
	req = requests.get(req_url,headers = headers,timeout = 50)

	soup = BeautifulSoup(req.content,'lxml')

	all_times = soup.find_all('td', class_='first left time')

	
	final_times = []


	for time in all_times:
		t=time.get_text()
		
		just_hour = t.split(":")[0]
		final_times.append(int(just_hour))


	print(final_times)

	
	if int(get_hour())+1 in final_times or int(get_hour()) in final_times:
		return HttpResponse("no")

	else:
		return HttpResponse("yes")

	return HttpResponse("none")