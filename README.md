# 📧 Documentação: AWS Lambda para Envio de E-mails com Amazon SES

Este projeto consiste em uma função AWS Lambda que realiza o envio de e-mails utilizando o Amazon SES (Simple Email Service). A função pode ser chamada via uma URL pública (Function URL) e recebe parâmetros no formato JSON.

---

## 📌 Requisitos

- Conta ativa na AWS
- E-mails verificados no Amazon SES
- Função Lambda criada e configurada
- API pública ativada com Function URL
- Permissões configuradas no IAM
- Postman (ou outro cliente HTTP) para testes

---

## 🛠️ Etapas de Criação e Configuração

### 1. Criar Conta na AWS

1. Acesse [aws.amazon.com](https://aws.amazon.com/)
2. Crie uma conta gratuita (Free Tier)
3. Confirme o e-mail e adicione um método de pagamento

---

### 2. Criar a Função Lambda

1. Acesse o serviço **Lambda** no console da AWS
2. Clique em **Criar função**
3. Defina:
   - Nome: por exemplo, `EnviarEmailLambda`
   - Runtime: `Python 3.12`
   - Permissões: `Criar uma nova role com permissões básicas do Lambda`
4. Clique em **Criar função**

---

### 3. Verificar Endereço de E-mail no SES

1. Acesse o serviço **Amazon SES**
2. Vá até **Verified Identities**
3. Clique em **Create Identity**
4. Escolha a opção **Email address**
5. Insira o e-mail que será usado como remetente
6. Verifique clicando no link enviado para o e-mail

> ⚠️ Enquanto sua conta estiver no sandbox do SES, apenas e-mails verificados poderão ser usados como destinatários.

---

### 4. Adicionar Permissão SES à Lambda

1. Acesse o serviço **IAM** > **Roles**
2. Selecione a role atribuída à função Lambda
3. Clique em **Anexar políticas**
4. Pesquise por `AmazonSESFullAccess`
5. Marque a opção e clique em **Anexar políticas**

---

## 🔁 Entrada e Saída Esperadas

## Construindo a Lambda

1. Coloque o código fonte .py no console da Lambda
2. Faça o Deploy
3. Depois vá para a parte de Testes
4. Clique em criar novo teste
5. Coloque o seguinte Json

```json
{
  "queryStringParameters": {
    "to": "testeumfg2@gmail.com",
    "subject": "Teste Lambda",
    "body": "Mensagem enviada com sucesso!"
  }
}
```
6. Clique em Testar
7. Deve retornar uma mensagem de Sucesso, com status 200

### 📤 Requisição (via POST):

No POSTMAN, cole a URL 

https://biwefmqh3tcea6dtlzpz4axvkq0vjdhd.lambda-url.us-east-1.on.aws/

E coloque o seguinte Json, com o seu email verificado no SES no lugar do testeumfg2@gmail.com

```json
{
    "to": "testeumfg2@gmail.com",
    "subject": "Teste Lambda",
    "body": "Mensagem enviada com sucesso!"
}
```

Verifique na caixa de entrada do E-mail utilizado no Json via POSTMAN, pode ser que esteja na área de Spam no E-mail.
