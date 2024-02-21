import boto3
import instance_ids

aws_management_console = boto3.session.Session(profile_name="default")

instanceids = instance_ids.instance_ids

ec2_console = aws_management_console.client('ec2')

stop = ec2_console.stop_instances(
    InstanceIds=[
        instanceids[0], instanceids[1], instanceids[2]
    ]
)
