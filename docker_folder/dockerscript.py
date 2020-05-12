import docker
objdocker = docker.Client(base_url="unix://var/run/docker.sock")
objdocker.info()