import aws_cdk as cdk

from network_stack import NetworkStack
from server_stack import ServerStack

app = cdk.App()

network = NetworkStack(app, "NetworkStack")
ServerStack(app, "ServerStack", vpc=network.vpc)

app.synth()

