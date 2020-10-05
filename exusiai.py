import os
import boto3

class Exusiai:
    def __init__(self, key, secret_key, space):
        self.key = key
        self.secret_key = secret_key
        self.space = space

        self.session = boto3.session.Session()
        self.client = self.session.client(
            's3',
            region_name = 'nyc3',
            endpoint_url = 'https://nyc3.digitaloceanspaces.com',
            aws_access_key_id = self.key,
            aws_secret_access_key = self.secret_key
        )

    # Create a new Space in DO Spaces.
    def create_space(self, name):
        self.client.create_bucket(Bucket = name)

    # List all spaces.
    def list_spaces(self):
        result = self.client.list_buckets()

        return result

    # Upload a file to Spaces.
    def upload_file(self, path, file, content_type):
        self.client.put_object(
            Bucket = self.space,
            Key = path,
            Body = file,
            ACL = 'public-read',
            ContentType = content_type
        )

        return True

    # List all the files in your Space.
    def list_files(self, space):
        result = self.client.list_objects(Bucket = space)

        return result

    # Download a file from Spaces.
    def download_file(self, file, path):
        self.client.download_file(self.space, file, path)

        return True

    # Create a temporary url for a file.
    def temporary_url(self, path, space, valid_for = '300'):
        url = self.client.generate_presigned_url(
            ClientMethod = 'get_object',
            Params = {'Bucket': space, 'Key': path},
            ExpiresIn = valid_for)

        return url

    # Delete a file from Spaces.
    def delete_file(self, path, space):
        self.client.delete_object(
            Bucket = space,
            Key = path)

        return True