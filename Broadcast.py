BROADCAST_TO_PORT = 5687
from sense_hat import SenseHat
from time import sleep
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))   #(ip, port)
# no explicit bind : will bind to default IP + random port

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sense = SenseHat()
def get_sense_data(index):
  hum = sense.get_humidity()
  temp = sense.get_temperature()
  press = sense.get_pressure()

  sense_data = []
  sense_data.append(temp)
  sense_data.append(hum)
  sense_data.append(press)
  return sense_data[index]


while True:
  data = "\n" + "Current time: " + str(datetime.now())+ "\n" + "Temperature: " +  str(get_sense_data(0)) + "\n" + "Humidity: " + str(get_sense_data(1)) + "\n" + "Pressure: " + str(get_sense_data(2))
  s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  print(data)
  sleep(5)
