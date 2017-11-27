"""
Deployment scripts
"""
from __future__ import unicode_literals, print_function

from fabric.decorators import task
from fabric.operations import local


@task
def deploy(stage='dev', initial=False):
    command = 'wrench deploy zappa --stage {}'.format(stage)
    if initial:
        command += ' --initial'

    local(command)


@task
def undeploy(stage='dev'):
    # You must destroy the CloudFormation stack which manages some API endpoints
    # before calling this command.
    local('wrench deploy undeploy_zappa --stage {}'.format(stage))
