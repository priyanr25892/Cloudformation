from . import resource_client

def get_running_instances():
    ec2client = resource_client.get('ec2')
    filters = [
        {  
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
    response = ec2client.describe_instances(Filters=filters)
    return response

def get_tags(instance):
    tags = dict()
    if 'Tags' in instance:
        for tag in instance['Tags']:
            tags[tag['Key']] = tag['Value']
    return tags

def get_tag(instance, tagname):
    tags = get_tags(instance)
    if tagname in tags:
        return tags[tagname]
    else:
        return ''

def is_exceptional_instance(instance):
    if 'Tags' not in instance:
        return True
    else:
        tags = get_tags(instance);
        if 'Service' not in tags:
            return True
        elif tags['Service'] not in ['Data', 'Processing', 'Web']:
            return True
    return False