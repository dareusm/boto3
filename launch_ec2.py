import boto3

aws_management_console = boto3.session.Session(profile_name="default")
ec2_console = aws_management_console.client("ec2")

response = ec2_console.run_instances(
    ImageId='ami-02ca28e7c7b8f8be1',
    InstanceType = 't2.micro',
    MaxCount=3,
    MinCount=1
)
