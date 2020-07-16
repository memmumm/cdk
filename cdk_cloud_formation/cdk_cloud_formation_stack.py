from aws_cdk import (
    core
)

import aws_cdk.aws_ec2 as ec2


class CdkCloudFormationStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "VPC", cidr="10.0.0.0/16",
                      max_azs=2,
                      subnet_configuration=[ec2.SubnetConfiguration(
                          subnet_type=ec2.SubnetType.PUBLIC,
                          name="MerviPub",
                          cidr_mask=24

                      ), ec2.SubnetConfiguration(
                          name="MerviPri",
                          cidr_mask=24,
                          subnet_type=ec2.SubnetType.PRIVATE

                      )
                      ]
        )

















