import csv
import json
from common.aws import ec2

def create_file(file):
    writer = csv.writer(file)
    writer.writerow(["InstanceName", "InstanceClass", "MachineImage", "Tags"])
    return writer
    
def write_to_file(writer, instance):
    writer.writerow([ec2.get_tag(instance, 'Name'), instance['InstanceType'], instance['ImageId'], json.dumps(ec2.get_tags(instance))])
    