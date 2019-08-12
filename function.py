import boto3

file_paths = ['file.text']
bucket = 'bucket'
s3 = boto3.client('s3')
for file_path in file_paths:
    try:
        data = open(file_path, 'rb').read()
        s3.put_object(
            ACL='bucket-owner-full-control',
            Body=data,
            Bucket=bucket,
            Key=file_path,
            ServerSideEncryption='AES256',
            StorageClass='GLACIER'
        )
    except Exception as e:
        print e.message