from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.enableCli()

# Network definition
net.addP4Switch('s1', cli_input='cmd.txt')
# net.setP4CliInput('s1', cli_input='cmd.txt')
# net.addP4Switch('s2')
# net.setP4CliInput('s2', 's2-commands.txt')
# net.addP4Switch('s3')
# net.setP4CliInput('s3', 's3-commands.txt')
net.setP4SourceAll('forwarding.p4')

net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
# net.addHost('h4')

# net.addLink('h1', 's1', weight=5)
net.addLink('s1', 'h1')
# net.setIntfIp('h1','s1','10.0.1.1/24')
# net.setIntfMac('h1','s1','00:00:00:00:01:01')
# net.setBw('h1', 's1', 20)
# net.setBw('h1', 's1', 20)
# net.setDelay('h1', 's1', 20)
# net.setMaxQueueSize('h1', 's1', 100)
# net.setLoss('h1', 's1', 0.01)
net.addLink('s1', 'h2')
# net.setIntfIp('h2','s1','10.0.2.2/24')
# net.setIntfMac('h2','s1','00:00:00:00:02:02')
# net.addLink('s1', 's1')
net.addLink('s1', 'h3')
# net.setIntfIp('h3','s1','10.0.3.3/24')
# net.setIntfMac('h3','s1','00:00:00:00:03:03')
# net.addLink('s1', 'h4')
# net.addLink('s1', 's1')

# Assignment strategy
net.mixed()

# Nodes general options
# net.addTaskFile('task.txt')
# net.addTask('h1', 'arp -s 10.0.1.254 00:00:00:00:01:01')
# net.addTask('h2', 'arp -s 10.0.2.254 00:00:00:00:02:02')
net.enablePcapDumpAll()
net.enableLogAll()

# Start the network
net.startNetwork()
