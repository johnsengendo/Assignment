from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.log import setLogLevel, info
import time

def setup_topology1():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    net.addController('c1')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.start()

    info('*** Running iPerf3 between h1 and h2\n')
    h1.cmd('iperf3 -s -D &')
    time.sleep(1)  # wait for the server to start
    result = h2.cmd('iperf3 -c h1 -t 10')  # client connects to the server for 10 seconds
    info('*** iPerf3 results:\n' + result + '\n')

    net.stop()

def setup_topology2():
    net = Mininet(controller=Controller, switch=OVSSwitch)
    net.addController('c2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    s2 = net.addSwitch('s2')
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.start()

    info('*** Running iPerf3 between h3 and h4\n')
    h3.cmd('iperf3 -s -D &')
    time.sleep(1)  # wait for the server to start
    result = h4.cmd('iperf3 -c h3 -t 10')  # client connects to the server for 10 seconds
    info('*** iPerf3 results:\n' + result + '\n')

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology1()
    setup_topology2()