import os
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_dynamodb,
    aws_apigateway as apigw,
    CfnOutput
)
from constructs import Construct

class LambdaUrlStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
      super().__init__(scope, construct_id, **kwargs)

      hello = lambda_.Function(self, "Hello",
         function_name="Hello2",
         runtime=lambda_.Runtime.PYTHON_3_12,
         handler="hello.handler",
         code=lambda_.Code.from_asset(
               os.path.join(os.path.dirname(__file__), "../lambdas"))
      )
      fn_url = hello.add_function_url(
          auth_type=lambda_.FunctionUrlAuthType.NONE
      )
      CfnOutput(self, "LambdaUrlOutput", value=fn_url.url)
