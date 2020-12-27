import json
from common import *

def lambda_handler(event, context):
    # TODO implement
    #print(resource_client.s3())
    #print(write.to_s3())
    try:
        exceptionalInstances = ''
        if 'Test' in event:
            disableNotification = event['Test'] == 'True'
        else:
            disableNotification = False
        reservationDetails = ec2.get_running_instances()
        with open('/tmp/list_of_ec2_instaces.csv', 'w', newline='') as file:
            writer = csv_operations.create_file(file)
            for reservation in reservationDetails['Reservations']:
                for instance in reservation['Instances']:
                    print('instance', instance)
                    csv_operations.write_to_file(writer, instance)
                    if (not disableNotification) and ec2.is_exceptional_instance(instance):
                        if(exceptionalInstances != ''):
                            exceptionalInstances += '\n' + instance['InstanceId']
                        else:
                            exceptionalInstances += instance['InstanceId']
        
        if (not disableNotification) and exceptionalInstances != '':
            sns.send_notification('arn:aws:sns:ap-south-1:825351774204:ec2-exception-list', 'Exception instances', 'Below are the exceptional instances' + '\n' + exceptionalInstances )
        s3.upload_to_bucket('/tmp/list_of_ec2_instaces.csv', 'my-ec2-list','list_of_ec2_instaces.csv')
        return {
            'statusCode': 200,
            'body': json.dumps('CSV uploaded')
        }
    except Exception as err:
        return {
            'statusCode': 500,
            'body': str(err)
        }
