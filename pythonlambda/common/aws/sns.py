from . import resource_client



def send_notification(topicarn, subject, message):
    s3client = resource_client.get('sns')
    snsresponse = s3client.publish(
        TopicArn= topicarn,
        Message= message,
        Subject= subject
    )
    