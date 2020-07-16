#!/usr/bin/env python3

from aws_cdk import core

from cdk_cloud_formation.cdk_cloud_formation_stack import CdkCloudFormationStack


app = core.App()
CdkCloudFormationStack(app, "cdk-cloud-formation", env={'region': 'us-west-2'})

app.synth()
