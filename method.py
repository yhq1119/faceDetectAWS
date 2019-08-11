import boto3


s3 = boto3.resource('s3')

data = open('test.jpg','rb')
s3.Bucket('photos1119').put_object(Key='test.jpg', Body=data)
