import time
import digitalio

from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = '6e26656af98c4249844260ebb4f6bd36'
ADAFRUIT_IO_USERNAME = 'ladovi'

aio = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def connected(client):
	print('Conectado. ')
	client.subscribe('msj')
	client.subscribe('locationX')
	client.subscribe('locationY')

def disconnected(client):
	print('Desconectado')
	sys.exit(1)

def message(client, feed_id, payload):
	print('Fedd {0} received new value: {1}'.format(feed_id, payload))

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()

client.loop_background()

def publicarMsj(m):
	print('publicando {0} a msj'.format(m))
	client.publish('msj', m)

def publicarLocationX(x):
	print('publicando {0} a locationX'.format(x))
	client.publish('locationX', x)

def publicarLocationY(y):
	print('publicando {0} a location'.format(y))
	client.publish('locationY', y)
