from fabric.api import run, require, env, local, put
from fabric.contrib.files import exists
from fabric.context_managers import cd
import time

from app import app

env.branch = 'master'
env.app_name = app.logger.name

env.key_filename = '' # Full path to pem
env.hosts = [] # Hosts

env.user = 'ec2-user'
env.app_dir = '/home/ec2-user/apps/%s' % (env.app_name)
env.timestamp = time.strftime('%Y%m%d%H%M')
env.warn_only = True
env.version = '%s-%s' % (env.app_name, env.timestamp)
    
def setup():
    """Set up the initial structure on the remote hosts."""
    require('hosts')
    require('app_dir')
    
    with cd(env.app_dir):
        run("mkdir versions")
        run("mkdir archives")

def switch_to(version):
    """Switch the current (ie live) version"""
    require('hosts')
    require('app_dir')
    with cd(env.app_dir):
        if exists('versions/previous'):
            run('rm versions/previous')
    
        if exists('versions/current'):
            run('mv versions/current versions/previous')
        
        run('ln -s ../versions/%s versions/current' % version)
        with cd('versions/current'):
            run("mkdir logs")
            run("mkdir etc")

def switch_to_version(version):
    switch_to(version)
    # restart nginx/apache

def make_tar():
    require('version')
    #local('tar -cf %s.tar.gz .' % (env.version), capture=False)
    local("git archive --format=tar --prefix=%(release)s/ %(branch)s | gzip -c > %(release)s.tar.gz" % {
        'release': env.version,
        'branch': env.branch,
        }
    )
    local('rm -fr %s' % env.version)

def upload_tar():
    require('version', provided_by=[deploy])

    put('%s.tar.gz' % env.version, '%s/archives/' % env.app_dir)
    with cd(env.app_dir):
        with cd('versions'):
            run('tar -zxvf ../archives/%s.tar.gz ' % (env.version))
            
    local('rm %s.tar.gz' % env.version)
    

def deploy():
    make_tar()
    upload_tar()
    switch_to(env.version)

def start():
    with cd('%s/versions/current' % env.app_dir):
        run('supervisord')

def stop():
    with cd('%s/versions/current' % env.app_dir):
        run('supervisorctl shutdown')

def restart():
    with cd('%s/versions/current' % env.app_dir):
        run('supervisorctl restart ')