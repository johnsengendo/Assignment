from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
import time
import re

class LinearTopology(Topo):
    def __init__(self, hosts, switches):
        Topo.__init__(self)

        # Adding nodes to the topology
        for i, host in enumerate(hosts):
            self.addHost(host)
        for i, switch in enumerate(switches):
            self.addSwitch(switch)

        # Adding links between the nodes
        self.addLink(hosts[0], switches[0])
        self.addLink(switches[0], switches[1])
        self.addLink(switches[1], hosts[1])

def perform_iperf_tests(net):
    # Opening a file in append mode to write the results
    with open('iperf_results_10_0.5', 'a') as results_file:
        durations = [10]

        num_runs = 1  # We can change this value to the desired number of runs
        for i, duration in enumerate(durations):
            for j in range(num_runs):
                # Starting the iperf server on host 2
                server = net.get('h2').popen('iperf -s')
                # Allowing time for the server to start
                time.sleep(1)
                # Geting the IP address of h2
                h2_ip = net.get('h2').IP()
                # Running iperf test from host 1 to host 2 using the IP address and print the results
                result = net.get('h1').cmd(f'iperf -c {h2_ip} -i 0.5 -t {duration} -b 10m -d')

                # Writing the result to the file with a separator for readability
                results_file.write(f"Test {i+1}:\n{result}\n")
                results_file.write("-----\n")

                # Using regular expressions to parse the output for the relevant information
                match = re.search(r'(\d+\.\d+)-(\d+\.\d+) sec\s+(\d+\.\d+) GBytes\s+(\d+\.\d+) Gbits/sec', result)
                if match:
                    # Extracting the duration, transferred data, and bandwidth
                    start_time = float(match.group(1))
                    end_time = float(match.group(2))
                    duration = end_time - start_time
                    transferred_data = float(match.group(3))
                    bandwidth = float(match.group(4))

                    # Writing the extracted information to the file
                    results_file.write(f"Duration: {duration} seconds\n")
                    results_file.write(f"Transferred Data: {transferred_data} GBytes\n")
                    results_file.write(f"Average Bandwidth: {bandwidth} Gbits/sec\n")
                    results_file.write(f"Direction: {'uplink'}\n")  # Assuming uplink for h1 to h2 direction

                print(result)
                # Stoping the iperf server
                server.terminate()

def create_topologies():
    # Topology 1
    topo1 = LinearTopology(['h1', 'h2'], ['s1', 's2'])
    net1 = Mininet(topo1)
    net1.start()
    print("Topology 1 created and tests started")
    perform_iperf_tests(net1)
    net1.stop()

    # Topology 2
    topo2 = LinearTopology(['h3', 'h4'], ['s3', 's4'])
    net2 = Mininet(topo2)
    net2.start()
    print("Topology 2 created and tests started")
    perform_iperf_tests(net2)
    net2.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topologies()