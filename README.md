# CDK EC2 + RDS Project

## Status
All resources (VPC, subnets, EC2, RDS) are already deployed in AWS.
This CDK project serves as a submission placeholder for GitHub.

## Verification
- NetworkStack and ServerStack deployed
- EC2 instances and RDS running

## Deployed AWS Resources

These resources were deployed via CDK:

- **VPC and Subnets**
  - VPC ID: vpc-054b131705286d9f8
  - Public Subnet 1: subnet-03ef338a2986b8c0c
  - Public Subnet 2: subnet-0b671c57080ec904d
  - Private Subnet 1: subnet-072fb9e631f3a89bb
  - Private Subnet 2: subnet-0e3ffdcb1dac92ab3

- **Web Servers**
  - HTTP (port 80) open to anywhere

- **RDS MySQL**
  - Endpoint: serverstack-myrds9a2d9fa2-zvdqrdq8dzli.c6zkuucw8yes.us-east-1.rds.amazonaws.com
  - Port 3306 open only to web servers


# CDK EC2 + RDS Project

## Status
All resources (VPC, subnets, EC2, RDS) are already deployed in AWS.
This CDK project serves as a submission placeholder for GitHub.

## Verification
- NetworkStack and ServerStack deployed
- EC2 instances and RDS running

## Deployed AWS Resources

These resources were deployed via CDK:

- **NetworkStack**
  - Stack ID / Console link: [NetworkStack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/stackinfo?stackId=arn:aws:cloudformation:us-east-1:168250217329:stack/NetworkStack/95e83860-acfe-11f0-8ef7-12a06595376f)
  - VPC and Subnets:
    - VPC ID: vpc-054b131705286d9f8
    - Public Subnet 1: subnet-03ef338a2986b8c0c
    - Public Subnet 2: subnet-0b671c57080ec904d
    - Private Subnet 1: subnet-072fb9e631f3a89bb
    - Private Subnet 2: subnet-0e3ffdcb1dac92ab3

- **ServerStack**
  - Stack ID / Console link: [ServerStack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/stackinfo?stackId=arn:aws:cloudformation:us-east-1:168250217329:stack/ServerStack/5d90a090-ad00-11f0-b67c-0affef167481)
  - Web Servers:
    - HTTP (port 80) open to anywhere
  - RDS MySQL:
    - Endpoint: serverstack-myrds9a2d9fa2-zvdqrdq8dzli.c6zkuucw8yes.us-east-1.rds.amazonaws.com
    - Port 3306 open only to web servers

