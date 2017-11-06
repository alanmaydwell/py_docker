#!/usr/bin/env python

"""
Docker SDK simple example
- Accesses already running container
- Executes command within the container and captures response
"""
import docker

# Container to access 
# Can specifiy either ID or Name (interchangeably)
container_id = "e50d653402"
container_id = "silly_kilby"

# Docker client
dc = docker.from_env()

#Accesss already running container
try:
    container = dc.containers.get(container_id)
except docker.errors.NotFound as e:
    print "Container error:", e
else:
    #Run command within the container
    response = container.exec_run("ls -al")
    print response
