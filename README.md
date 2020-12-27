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

# PythonLambda
Description: An inventory of all EC2 instances running in a particular AWS account needs to be taken
twice per day using serverless function (Lambda) in Python 3.

1. lambda_function.py file inside the folder pythonlambda contains the lambda function that is triggered on an event in cloudwatch which is scheduled twice per day. And packages related to are inside common folder.
      ![alt text](https://github.com/priyanr25892/Cloudformation/blob/main/pythonlambda/package_layout.png?raw=true)
2. lambdaCFT.yaml inside the folder pythonlambda contains Infrastructure-as-pseudo-Code for the solution.

3. IAM Permission required for the lambda function are the following.

                Cloudwatch logs:
                Access: write
                Permissions:
                logs:CreateLogStream    
                logs:PutLogEvents
                logs:CreateLogGroup

                EC2:
                Access: List
                Permissions:
                ec2:DescribeInstances

                S3:
                Access: Read,Write
                Permissions:
                s3:PutObject
                s3:GetObject

                SNS:
                Access: Write(sns-topic created in lambda function)
                Permissions:
                Publish

4. Trigger for the lambda function and its configuration:
    CLoudwatch events is the trigger.
    It is done from the configuration setting of lambda function.
    From the designer we need to click on Add trigger
    configure the trigger which is Event Bridge(Cloud Watch Events)

    Create a new rule,provide name and description for the rule
    Rule type should be Schedule Expression
    and value is rate(12 hours)--> means twice a day.
    And click on Enable trigger.

    Go to Cloudwatch Events-->Rules. Edit the created rule and provide the target as lambda function .
    Enter the name of the function and configure input as Constant with key test and value as true.

