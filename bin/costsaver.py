#!/usr/bin/python
# -*- coding: utf-8 -*-
import boto3
import logging
# setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# Connection
ec2 = boto3.resource('ec2')
def notif(message):
    logger.info('ERROR is %s' % message)

def costsaver_handler(event, context):
    state = event['action']
    isRunning = ''
    logger.info(event)

    if(state == 'start'):
        isRunning = 'stopped'
    elif (state == 'stop'):
        isRunning = 'running'
 # all running EC2 instances.
    filters = [{'Name': 'tag:dev', 'Values': ['true']},
               {'Name': 'instance-state-name', 'Values': [isRunning]}]
 # filter the instances
    instances = ec2.instances.filter(Filters=filters)
 # locate all running instances
    RunningInstances = [instance.id for instance in instances]
 # print the instances for logging purposes
    logger.info(RunningInstances)
 # make sure there are actually instances to shut down or startup
    if len(RunningInstances) > 0:
       if(state == 'start'):
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).start()
       elif (state == 'stop'):
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
