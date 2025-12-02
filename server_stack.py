from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct

class ServerStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc=None, **kwargs):
        super().__init__(scope, id, **kwargs)

        if not vpc:
            raise ValueError("vpc must be provided")

        # Security group for web server
        web_sg = ec2.SecurityGroup(
            self, "WebSG",
            vpc=vpc,
            description="Allow HTTP and SSH",
            allow_all_outbound=True
        )
        web_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Allow HTTP")
        web_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH")

        # Single free-tier EC2 instance
        ec2.Instance(
            self, "WebServer",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            instance_type=ec2.InstanceType("t3.micro"),  # Free-tier eligible
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            security_group=web_sg
        )


