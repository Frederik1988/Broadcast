BROADCAST_TO_PORT = 5687
from sense_hat import SenseHat
from time import sleep
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))   #(ip, port)
# no explicit bind : will bind to default IP + random port

s.setsocketopt(SOL_SOCKET, SO_BROADCAST, 1)

sense = SenseHat()
def get_sense_data():
  hum = sense.get_humidity()
  temp = sense.get_temperature()
  press = sense.get_pressure()

  sense_data = []
  sense_data.append(temp)
  sense_data.append(hum)
  sense_data.append(press)
  return sense_data


while True:
  data = "Current time: " + str(datetime.now()) + "And data: " +  str(get_sense_data())
  s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  print(data)
  sleep(5)
