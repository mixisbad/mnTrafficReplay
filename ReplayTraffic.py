#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.link import TCIntf
from mininet.node import CPULimitedHost
from multiprocessing import Process, Queue
from time import sleep
from sys import argv,stdin
import socket
import sys
import os
import random

class ReplayTopo(Topo):
	# This class creates a network topology where each server (simply a host running nweb) is connected 
	#			to a unique switch and each switch is then connected to a "central switch" that is also 
	#			connected to multiple other hosts that will act as normal clients (randomly connect to 
	#			the Controller) and malicious clients (attempt to queue up a single server to be overloaded)

	def __init__(self, servers, linkBWSS, linkBWCS, hosts):
		Topo.__init__(self)
        self.clients = []
		
		# Define the middle switch
		centralSwitch = self.addSwitch('s%s' %str(servers + 1))

		# Make the "server side" of the network
		for n in range (1, servers + 1):
			host = self.addHost('h%s' %n)
			switch = self.addSwitch('s%s' %n)
			self.addLink(host, switch, bw=linkBWSS)
			self.addLink(switch, centralSwitch, bw=linkBWSS)
		
		# Make the "client side" of the network
        for h in hosts:
            clients.append(line)
			host = self.addHost('h%s' % (h,))
			self.addLink(host, centralSwitch, bw=linkBWCS) 
		

def ReplayTraffic(servers, controllerIP, linkBWSS, linkBWCS, traffic):

    # Read in the log file and prepare the requests dictionary
    requests = {}
    for line in traffic:
        request = line.split(';')
        if request[0] not in requests:
            requets[request[0]] = []
        requests[request[0]].append((request[1],request[2]))

	# Initialize and start the network
	topo = ReplayTopo(servers, total, linkBWSS, linkBWCS, requests.keys())
	net = Mininet(topo=topo, link=TCLink, controller=lambda name:RemoteController(name, defaultIP='127.0.0.1'), listenPort=6633)
	net.start()

	# Do a ping sweep to identify all hosts with controller
    for i in range(len(topo.clients)):
		host1 = net.get('h%s' % (topo.clients[i],))
		host2 = net.get('h%s' % (i % servers + 1,))
		host1.cmd('ping -c1', host2.IP())

	# Set up nweb server on hosts
	for i in range (1, len(topo.clients)):
		host = net.get('h%s' % (i,))
		host.cmd('sudo /home/mininet/Desktop/Server/nweb 80 /home/mininet/Desktop/Server')

	#net.interact()

    # Replay the traffic
	
	net.stop()

if __name__ == '__main__':
	# Main method of the script
	# Arguments: Servers, Number of Malicious, Number of Normal, IAT of normal hosts, controller IP, 
	#		 the link speed on the server side, the link speed on the client side 
	setLogLevel('info')
	servers = int(argv[1])
	controllerIP = argv[2]
	linkBWSS = int(argv[3])
	linkBWCS = int(argv[4])
	RunTest(servers, controllerIP, linkBWSS, linkBWCS, sys.stdin)
