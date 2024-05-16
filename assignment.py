from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
import time

def setup_topology1():
    """Create the first isolated topology with two hosts and one switch."""
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    info('*** Adding controller\n')
    net.addController('c1')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.1.0.1/24')
    h2 = net.addHost('h2', ip='10.1.0.2/24')

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(h1, s1, bw=10, delay='0ms')
    net.addLink(h2, s1, bw=10, delay='0ms')

    info('*** Starting network\n')
    net.start()

    info('*** Running ping between h1 and h2\n')
    net.ping([h1, h2], timeout='10')

    net.stop()

def setup_topology2():
    """Create the second isolated topology with two hosts and one switch."""
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    info('*** Adding controller\n')
    net.addController('c2')

    info('*** Adding hosts\n')
    h3 = net.addHost('h3', ip='10.2.0.1/24')
    h4 = net.addHost('h4', ip='10.2.0.2/24')

    info('*** Adding switch\n')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    net.addLink(h3, s2, bw=10, delay='0ms')
    net.addLink(h4, s2, bw=10, delay='0ms')

    info('*** Starting network\n')
    net.start()

    info('*** Running ping between h3 and h4\n')
    net.ping([h3, h4], timeout='10')
    time.sleep(2)  # Adding a delay to clearly separate the ping attempts

    info('*** Running another ping between h3 and h4\n')
    net.ping([h3, h4], timeout='10')

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology1()  # Initialize and run the first topology
    setup_topology2()  # Initialize and run the second topology
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
import time

def setup_topology1():
    """Create the first isolated topology with two hosts and one switch."""
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    info('*** Adding controller\n')
    net.addController('c1')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.1.0.1/24')
    h2 = net.addHost('h2', ip='10.1.0.2/24')

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(h1, s1, bw=10, delay='0ms')
    net.addLink(h2, s1, bw=10, delay='0ms')

    info('*** Starting network\n')
    net.start()

    info('*** Running ping between h1 and h2\n')
    net.ping([h1, h2], timeout='10')

    net.stop()

def setup_topology2():
    """Create the second isolated topology with two hosts and one switch."""
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)
    info('*** Adding controller\n')
    net.addController('c2')

    info('*** Adding hosts\n')
    h3 = net.addHost('h3', ip='10.2.0.1/24')
    h4 = net.addHost('h4', ip='10.2.0.2/24')

    info('*** Adding switch\n')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    net.addLink(h3, s2, bw=10, delay='0ms')
    net.addLink(h4, s2, bw=10, delay='0ms')

    info('*** Starting network\n')
    net.start()

    info('*** Running ping between h3 and h4\n')
    net.ping([h3, h4], timeout='10')
    time.sleep(2)  # Adding a delay to clearly separate the ping attempts

    info('*** Running another ping between h3 and h4\n')
    net.ping([h3, h4], timeout='10')

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_topology1()  # Initialize and run the first topology
    setup_topology2()  # Initialize and run the second topology
