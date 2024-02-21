import boto3

aws_management_console = boto3.session.Session(profile_name="default")

ec2_console = aws_management_console.client("ec2")
#Get Name
response = ec2_console.describe_instances()['Reservations'][0]['Instances'][0]['Tags'][0]['Value']
print(response)