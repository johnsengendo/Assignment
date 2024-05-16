from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
import time

def calculate_data_transmitted(ping_results):
    """Calculate the data transmitted based on ping results."""
    transmitted, received = 0, 0
    for result in ping_results:
        if 'packets transmitted' in result:
            transmitted += int(result.split()[0])
            received += int(result.split()[3])
    # Assuming each packet (request and reply) is 64 bytes
    data_transmitted = transmitted * 64  # in bytes
    data_received = received * 64  # in bytes
    return data_transmitted, data_received

def setup_topology1():
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    net.addController('c1')
    h1 = net.addHost('h1', ip='10.1.0.1/24')
    h2 = net.addHost('h2', ip='10.1.0.2/24')
    s1 = net.addSwitch('s1')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.start()

    results = net.pingFull([h1, h2], timeout='10')
    data_transmitted, data_received = calculate_data_transmitted(results)
    info(f'*** Data transmitted: {data_transmitted} bytes, Data received: {data_received} bytes\n')

    net.stop()

def setup_topology2():
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    net.addController('c2')
    h3 = net.addHost('h3', ip='10.2.0.1/24')
    h4 = net.addHost('h4', ip='10.2.0.2/24')
    s2 = net.addSwitch('s2')
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.start()

    results = net.pingFull([h3, h4], timeout='10')
    data_transmitted, data_received = calculate_data_transmitted(results)
    info(f'*** Data transmitted: {data_transmitted} bytes, Data received: {data_received} bytes\n')

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology1()
    setup_topology2()
