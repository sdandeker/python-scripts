import boto3
tagname = "AutoOff"
tagvalue = "True"
ec2 = boto3.resource('ec2')
ec2.instances.filter(Filters=[
    {'Name': 'tag:AutoOff', 'Values': True},
    {'Name': 'instance-state-name', 'Values': ['running']}
]).start()

ec2.instances.filter(Filters=[
    {'Name': 'tag:AutoOff', 'Values': True},
    {'Name': 'instance-state-name', 'Values': ['stopped']}
]).stop()
