# Exusiai Spaces

## What is Digital Ocean Spaces

Spaces is a simple, standalone object storage service that enables developers to store and serve any amount of data with automatic scalability, performance, and reliability.

DigitalOcean Spaces provide S3-compatible object storage which lets you store and serve large amounts of data. You can create them in a few seconds and use them immediately with no configuration. Data transfer is automatically secured with HTTPS, and the available storage capacity scales seamlessly.

Spaces are ideal for storing static, unstructured data like audio, video, and images as well as large amounts of text. Because Spaces are an object storage implementation, use cases like databases, applications written in server-side languages, and mission-critical applications will work best with local storage or block storage.

## What is Exusiai Spaces

Exusiai is a micro API that helps you with the upload of files to DO Spaces, it is also compatible with AWS S3, Exusiai is made for simple tests like using the service of Spaces or S3 for the first time.

### How to start

First of all, you need to have three essential things.
1. A key that gives you DO Spaces.
2. A secret key that gives you DO Spaces.
3. Your 'Space' in Digital Ocean. (Also, called 'Bucket' in AWS S3).

Después de obtener esos datos, vamos a python y declaramos unas variables.

- `key = 'CVSUDYBV27NZQV2JWKDH'`
- `secret_key = '0BuzYwSJ4v4zxz1+NkVImxTcCU70'`
- `space = 'name_of_your_space'`

Declared the variables we proceed to make the connection using the class Exusiai, which we must import first.

- `ex_space = Exusiai(key, secret_key, space)`

From here you can do what you like with Exusiai.
In [example.py](https://github.com/raviancad7/exusiai-spaces/blob/master/example.py) you can find an example of how to use Exusiai.

## TODO List
- [ ] Add documentation.


# Changelog 

## [06-10-2020]

### New

- Added README.md file to repository.

### Removed

- `import os` removed from line 1 in [exusiai.py](https://github.com/raviancad7/exusiai-spaces/blob/master/exusiai.py).

## [10-10-2020]

### New

- Added information to README.md file.
- Added example.py to repository.