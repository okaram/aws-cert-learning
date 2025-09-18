#!/usr/bin/env python3
import os

import aws_cdk as cdk

from examples.code_stack import CodeStack
from examples.lambda_url_stack import LambdaUrlStack

app = cdk.App()
LambdaUrlStack(app, "LambdaUrlStack")

app.synth()
