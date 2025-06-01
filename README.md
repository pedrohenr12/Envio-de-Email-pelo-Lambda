# Envio-de-Email-pelo-Lambda

Código da Função de envio de Email Lambda

```python
import boto3

def lambda_handler(event, context):
    try:
        to_email = event.get('to')
        subject = event.get('subject')
        body = event.get('body')

        if not to_email or not subject or not body:
            return {
                'statusCode': 400,
                'body': 'Erro: Parâmetros "to", "subject" e "body" são obrigatórios.'
            }

        ses = boto3.client('ses', region_name='us-east-1')

        response = ses.send_email(
            Source='testeumfg@gmail.com',  # <- DEVE estar verificado no SES
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
```

Teste

```json
{
  "to": "testeumfg2@gmail.com",
  "subject": "Teste da função Lambda",
  "body": "Este é um e-mail enviado automaticamente pela função Lambda usando o Amazon SES."
}
```
