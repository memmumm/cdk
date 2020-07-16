import json
import pytest

from aws_cdk import core
from cdk_cloud_formation.cdk_cloud_formation_stack import CdkCloudFormationStack


def get_template():
    app = core.App()
    CdkCloudFormationStack(app, "cdk-cloud-formation")
    return json.dumps(app.synth().get_stack("cdk-cloud-formation").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
