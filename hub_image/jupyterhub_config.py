# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
<<<<<<< HEAD
c.JupyterHub.hub_connect_ip = 'book2_jupyterhub_1'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image_whitelist = {'e350':'phaustin/user_notebook:sep07',
#                                    'a301':'phaustin/user_notebook:sep07'}
c.DockerSpawner.image= "phaustin/user_notebook:sep17"
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'book2_jupyterhub'
#c.DockerSpawner.default_url = '/lab'
c.DockerSpawner.notebook_dir = '~/notebooks'
#c.DockerSpawner.args = ['--NotebookApp.default_url=/notebooks/index.ipynb']
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image_whitelist = {'e350':'phaustin/notebook:0.1',
                                   'a301':'phaustin/notebook:0.1'}
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'
#c.DockerSpawner.default_url = '/lab'
c.DockerSpawner.notebook_dir = '~/notebooks'


# explicitly set cmd, so we start jupyterhub-singleuser rather than jupyter notebook
# This is useful when running docker images that aren't built specifically for JupyterHub
c.DockerSpawner.cmd = 'jupyterhub-singleuser'


# delete containers when the stop
c.DockerSpawner.remove = True
