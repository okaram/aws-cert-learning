import os
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_dynamodb,
    aws_apigateway as apigw
)
from constructs import Construct

class ApigwMoviesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        table=aws_dynamodb.Table(self,"MoviesTable",            
            table_name="MoviesTable", 
            partition_key=aws_dynamodb.Attribute(
                name="id", 
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        insert = lambda_.Function(self, "InsertMovie",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="insert_movie.handler",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "../lambdas"))
        )

        hello = lambda_.Function(self, "Hello",
            function_name="Hello",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="hello.handler",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "../lambdas"))
        )

        get_movie = lambda_.Function(self, "GetMovie",
            function_name="GetMovie",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="get_movie.handler",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "../lambdas"))
        )

        table.grant_read_data(get_movie)
        # Create an API Gateway REST API
        api = apigw.RestApi(
            self, "MyRestApi",
            rest_api_name="MyServiceApi",
            description="This is my API Gateway for MyService.",
            deploy_options=apigw.StageOptions(
                stage_name="dev", # Define a stage name
            )
        )

        # Add a resource to the API Gateway (e.g., /hello)
        hello_resource = api.root.add_resource("hello")

        # Add a GET method to the /hello resource and integrate it with the Lambda function
        hello_resource.add_method(
            "GET",
            apigw.LambdaIntegration(hello),
            api_key_required=False,
            request_parameters={
                "integration.request.header.get_form": True
            }
        )

        # form_resource = api.root.add_resource("movies_form")
        # # Add a GET method to the /hello resource and integrate it with the Lambda function
        # form_resource.add_method(
        #     "GET",
        #     apigw.LambdaIntegration(get_movie_form),
        #     api_key_required=False # Set to True if API key authentication is desired
        # )


        movies_resource = api.root.add_resource("movies")
        movies_with_id=movies_resource.add_resource("{id}")
        # Add a GET method to the /hello resource and integrate it with the Lambda function
        movies_with_id.add_method(
            "GET",
            apigw.LambdaIntegration(get_movie),
            api_key_required=False # Set to True if API key authentication is desired
        )

        movies_resource.add_method(
            "POST",
            apigw.LambdaIntegration(hello),
            api_key_required=False # Set to True if API key authentication is desired
        )


        # You can add more resources and methods as needed
        # For example, a POST method for /items
        # items_resource = api.root.add_resource("items")
        # items_resource.add_method("POST", apigw.LambdaIntegration(my_post_lambda))
