import json
import os
import logging
import boto3


# Initialize the logger
logger = logging.getLogger()
logger.setLevel("INFO")

def handler(event, context):
    try:
        print(event)        
        return {
            "statusCode": 200,
            "body" : json.dumps(event),
            "headers": {
                "Content-Type": "text/html"
            }
        }

    except Exception as e:
        logger.error(f"Error processing order: {str(e)}")
        raise