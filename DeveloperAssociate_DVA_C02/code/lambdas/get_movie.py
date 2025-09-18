import json
import os
import logging
import boto3

# Initialize the dynamo client outside of the handler
table = boto3.resource('dynamodb').Table('MoviesTable')

logger = logging.getLogger()
logger.setLevel("INFO")

def handler(event, context):
   try:
      print(json.dumps(event))
      id=event.get('pathParameters').get('id')
      item=table.get_item( Key={'id': id})['Item']
      return {
         "statusCode": 200,
         "body" : json.dumps(item),
         "headers": {
               "Content-Type": "text/json"
         }
      }
   except Exception as e:
      logger.error(f"Error getting movie: {str(e)}")
      raise