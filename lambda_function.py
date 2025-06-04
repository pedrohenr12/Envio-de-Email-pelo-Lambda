import json
import boto3

def lambda_handler(event, context):
    try:
        to_email = None
        subject = None
        body = None

        if 'queryStringParameters' in event and event['queryStringParameters']:
            to_email = event['queryStringParameters'].get('to')
            subject = event['queryStringParameters'].get('subject')
            body = event['queryStringParameters'].get('body')

        elif 'body' in event and event['body']:
            try:
                data = json.loads(event['body'])
                to_email = data.get('to')
                subject = data.get('subject')
                body = data.get('body')
            except json.JSONDecodeError:
                return {
                    'statusCode': 400,
                    'body': 'Erro: corpo da requisição não é um JSON válido.'
                }

        if not to_email or not subject or not body:
            return {
                'statusCode': 400,
                'body': 'Erro: Parâmetros "to", "subject" e "body" são obrigatórios.'
            }

        ses = boto3.client('ses', region_name='us-east-1')

        response = ses.send_email(
            Source='testeumfg@gmail.com', 
            Destination={
                'ToAddresses': [to_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'body': f"E-mail enviado com sucesso para {to_email}. MessageId: {response['MessageId']}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Erro ao enviar e-mail: {str(e)}"
        }
