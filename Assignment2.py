import time
from subprocess import Popen, PIPE
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.log import setLogLevel, info

def start_iperf3_server(host):
    server_process = host.popen('iperf3 -s -D', shell=True, stdout=PIPE, stderr=PIPE)
    time.sleep(1)
    return server_process

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
    server_process = start_iperf3_server(h1)
    result = h2.cmd('iperf3 -c h1 -t 10')  # client connects to the server for 10 seconds
    info('*** iPerf3 results:\n' + result + '\n')

    server_process.terminate()
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
    server_process = start_iperf3_server(h3)
    result = h4.cmd('iperf3 -c h3 -t 10')  # client connects to the server for 10 seconds
    info('*** iPerf3 results:\n' + result + '\n')

    server_process.terminate()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology1()
    setup_topology2()
