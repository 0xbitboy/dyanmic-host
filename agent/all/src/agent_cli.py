import argparse
import agent
parser = argparse.ArgumentParser()
parser.add_argument(
      "--eth",
      type=str,
      required=True,
      help="The network interface for monitor.")
parser.add_argument(
    "--hostname",
    type=str,
    help="Custom hostname.")
parser.add_argument(
    "--scheme",
    type=str,
    default="http",
    help="server protocal.")
parser.add_argument(
    "--server",
    type=str,
    required=True,
    help="The server domain or ip[:port].")
parser.add_argument(
    "--agent-key",
    type=str,
    required=True,
    help="The agent-key for this machine.")
parser.add_argument(
    'command',
    help="run  ->Start reporting host info to the cloud [server].     sync ->Start sync host file from cloud"
    )
argv = parser.parse_args()
ag = agent.Agent(argv.agent_key,argv.server,argv.scheme)
if 'run'==argv.command:
    ag.report(argv.hostname,ag.getLocalIp())    
elif 'sync'==argv.command:
    pass
else:
    print("Ivalid command [%s]: \nUsage: \nrun ->Start reporting host info to the cloud [server].\nsync ->Start sync host file from cloud"%(argv.command))
