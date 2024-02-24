# this is a test of the docker sdk
# it is a simple test to see if the docker sdk is working
# it will pull the hello-world image and run it
# it will then print the output of the container
# it will then remove the container
# it will then remove the image

import docker
import os

# create a client
client = docker.from_env()

# pull the hello-world image
client.images.pull('hello-world')

# run the hello-world image
container = client.containers.run('hello-world')

# print the output of the container
print(container)

# remove the container
container.remove()

# remove the image
client.images.remove('hello-world')

# close the client
client.close()

print("Test complete")