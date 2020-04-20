import serial
import os,sys

class OxiHRMonitor():
	#driver code
	def serialContext(self, ttyFile):
		try:
			return serial.Serial(port=ttyFile, baudrate=9600)
		except Excpetion as e:
			print(e)
			return None

	def listen(self, ctx, debug=False):
		while True:
			if ctx.readable():
				data = ctx.readline()
				data = data.decode().split(' ')
				if debug == True:
					res = '[Rate] {} , [Concentration] {} '.format(data[0], data[1].split('\r\n')[0])
					yield res
				else:
					yield (data[0], data[1].split('\r\n'))

#Test
'''
if __name__=="__main__":
	clss = OxiHRMonitor()
	ctx = clss.serialContext('/dev/tty.KMU_MSPL-DevB')
	res = clss.listen(ctx, True)
	while True:
		print(next(res))
'''




	
