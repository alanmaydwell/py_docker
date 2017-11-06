#!/usr/bin/env python

"""
Docker SDK simple example
- Starts a container from existing image
- Runs command within the container and captures response
- Stops the container
"""

import docker

# Docker client
dc = docker.from_env()
# Run image
# stdin_open=True, same effect as docker run -i (keeps container running)
container = dc.containers.run(image='ubuntu-alan:latest',
                              detach=True,
                              stdin_open=True,
                              name='py_ubuntu')
# Run command within the container
response = container.exec_run("ls -al")
#Stop the container
container.stop()
#Show result
print response
