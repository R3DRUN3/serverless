import json


def show_data(event, context):
    try:
        source_ip_address = event['requestContext']['identity']['sourceIp']
        source_user_agent = event['requestContext']['identity']['userAgent']
        response = {"ip": source_ip_address,
                     "user_agent": source_user_agent}
        return dict(
            statusCode=200,
            body=json.dumps(response)
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )