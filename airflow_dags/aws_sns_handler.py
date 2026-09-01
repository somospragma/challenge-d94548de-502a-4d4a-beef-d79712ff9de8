import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class AWSSNSHandler(BaseOperator):
    @apply_defaults
    def __init__(self, topic_arn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topic_arn = topic_arn

    def execute(self, context):
        sns = boto3.client('sns')
        sns.publish(TopicArn=self.topic_arn, Message='New data available')