# Cloudformation
# Web Stack/Infrastructure as Code
Description: You are responsible for provisioning a new environment for a multi-tiered web application
in AWS. Design a VPC with subnets for each application tier, including all supporting resources.

1. Multitier_appl.yaml file inside the WebStack_IaaC folder contains details about the stack .
The yaml file is written in the form of a pseudo-Cloudfomration template.

2. Servicerole.yaml file inside the WebStack_IaaC folder contains the details about IAM role and policy that is required to run
a cloudformation stack.
  CfnServiceRole service role is created and it is assigned with the required policy to execute the cloudformation Stack(create,update,delete stack etc.)
  
3. IAM roles for each application component, assigned with appropriate AssumeRole/Trust
Relationship principles for the component.


    Webapplication(EC2):
    Role description: Allows EC2 instances to call AWS services on your behalf.
    Trusted Entity: AWS service: ec2.amazonaws.com
    Policy:
    AmazonElastiCacheFullAccess
    AmazonRDSDataFullAccess

    AutoScalingGroup:
    Role description: Allows EC2 Auto Scaling to use or manage AWS services and resources on your behalf. 
    Trusted Entity:
    AWS service: autoscaling.amazonaws.com
    Policy:
    AutoScalingServiceRolePolicy

    AWSServiceRoleForElasticLoadBalancing(Load Balancer):
    Role description: Allows ELB to call AWS services on your behalf.
    Trusted Entity:
    AWS service: elasticloadbalancing.amazonaws.com
    Policy:
    AWSElasticLoadBalancingServiceRolePolicy 
    
    AWSServiceRoleforRDS:
    Role description: Allows RDS to perform operationsusing AWS resources on your behalf.
    Trusted Entity:
    AWS service: rds.amazonaws.com
    Policy:
    AmazonRDSServiceRolePolicy

    AWSServiceRoleForElastiCache(Redis)
    Role description: Allows ElastiCache to manage AWS resources for your cache on your behalf.
    Trusted Entity:
    AWS service: elasticache.amazonaws.com
    Policy:
    ElastiCacheServiceRolePolicy




