import paho.mqtt.client as paho
import time
import random
import math
import json
import areas
#Points


broker="localhost"
port=1883
TOPIC="owntracks/david/Ranger"; 			#TOPIC
print "Target is moving\n";
time.sleep(1);
print ("Speed.... \n")

def on_publish(client,userdata,result):             #create function for callback	
	pass

def  Area(a,b,c):
	S=math.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4;  		#Tinh dien tich
	return S

client1= paho.Client("cuong")                           #create client object
#client1.on_publish = on_publish                          #assign function to callback
#client1.username_pw_set("cuong","dat")
client1.connect(broker,port);                                 #establish connection

lat = 20.981020
lon = 105.787303
a= 111.044736
#LOOP
loop =1
while 1:

	

	t=time.localtime();		#get time then convert to Time Unix
	T=time.asctime(t);
	ticks=time.mktime(t);
	MSG={'_type':'location','tid':'dat','conn':'w','lat':lat,'lon':lon,'tst':ticks,'acc':25,'batt':96}
	P=json.dumps(MSG);
	ret= client1.publish(TOPIC,P);                  #publish
	time.sleep(3)
	#print areas.Pt(lon,lat)

	point=areas.Pt(lon,lat);
	ptit=areas.ptit						#Khai bao khu vuc quy dinh
	aosen=areas.aosen
	home=areas.home

	isptit= areas.ispointinside(point,ptit)			#Kiem tra doi tuong trong khu vuc
	isaosen=areas.ispointinside(point,aosen)
	ishome=areas.ispointinside(point,home)

	# Chon mot so ngau nhien tu 0.001 <= number < ...
	
	choice = random.randrange(123, 798, 100 )
	delta=float(choice)/1000000

	d = a*math. sqrt(2*delta*delta);
	speed = round(d/5*3600,2);
	
	h=t.tm_hour
	m=t.tm_min
	tg=h*60+m
	
	if tg>420 and tg<1050:	#7h-17h30
		if isptit:
			print speed,"\tkm/h","\t",T
		else:	
			print speed,"\tkm/h","\t",T,"\tCaution! Cuong is outside the shool";
	elif tg>1050 and tg<1110:	#17h30-18h30
		if isaosen:
			print speed,"\tkm/h","\t",T
		else:	
			print speed,"\tkm/h","\t",T,"\tCaution! Cuong is outside the aosen";
	elif (tg>1110 and tg<1439) or (tg>0 and tg<420): #else
		if ishome:
			print speed,"\tkm/h","\t",T
		else:	
			print speed,"\tkm/h","\t",T,"\tCaution! Cuong is outside his home";
	else: print speed,"\tkm/h","\t",T
	

