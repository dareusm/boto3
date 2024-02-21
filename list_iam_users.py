#List all IAM users
import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_resource = aws_management_console.resource("iam")
iam_client = aws_management_console.client("iam")

for users in iam_resource.users.all():
    print(users.name)
    
for users in iam_client.list_users()['Users']:
    print(users['UserName'])
