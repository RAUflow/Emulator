#!/usr/bin/python
from flask import Flask
import commands


app = Flask(__name__)

@app.route('/topo/calc/')
def calcularTopo():
	print 'HI : '
	commandResult = commands.getstatusoutput('/home/mina/work/telnetRouters.py')
	print 'SENDING TOPOLOGY : '
	print commandResult
	return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=5001)


