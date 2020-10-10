from exusiai import Exusiai
import mimetypes

'''
Example of how to use the Exusiai to handle files in DigitalOcean Spaces
This is just a practice and is a simple and easy to use API, but is not recommended for large production environments.
'''
# First we declare the variables: key, secretKey and space with their respective data
key = 'KEY' # Your key should look like this: CVSUDYBV27NZQV2JWKDH
secret_key = 'SECRET_KEY' # Your secret key should look like this: 0BuzYwSJ4v4zxz1+NkVImxTcCU70
space = 'Space' # Name of your Space

# We make an instance of Exusiai and pass the respective parameters.
ex_space = Exusiai(key, secret_key, space)

'''
The next thing will be to place the path where the file will be stored in Spaces, 
if the directories does not exist Spaces will create them automatically
'''
path = 'example/test-python/file.ext' # Destination path.
file = open('tree.jpg', 'rb') # We open the file in binary read.
content_type = mimetypes.guess_type('tree.jpg') # We get its ContentType.

result = ex_space.upload_file(path, file, content_type[0]) # Finally we use Exusiai's 'upload_file' method to make the upload-

if result:
    print('Success.')
    file.close()

else:
    print('Fail.')
    file.close()