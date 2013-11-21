from path import path as ppath
from fabric.api import env

env.hosts = ['edw@pigeon.eea.europa.eu']

env.app['repo'] = ppath('/var/local/naaya/live_catalogue')

__all__ = ()
