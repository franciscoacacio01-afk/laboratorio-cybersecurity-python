# Keylogger — Estudo e Análise em Python

## 1. Sobre o projeto

Este módulo apresenta um estudo educacional sobre Keyloggers, utilizando Python para compreender seus conceitos, funcionamento e riscos à segurança da informação.

A atividade foi desenvolvida em dois experimentos independentes, abordando o registro de entradas do teclado e o conceito de transmissão de informações por e-mail.

## 2. Objetivos

- Compreender o funcionamento conceitual de um Keylogger.
- Conhecer a biblioteca Python `pynput`.
- Estudar o registro de eventos do teclado.
- Compreender o funcionamento de comunicação SMTP.
- Analisar riscos de captura e transmissão não autorizada de informações.
- Identificar mecanismos de prevenção e detecção.

## 3. Experimentos realizados

### Experimento 1 — Registro local

Desenvolvimento de um programa utilizando `pynput` para demonstrar o registro de eventos do teclado em arquivo de texto.

Também foi estudada a extensão `.pyw`, utilizada no Windows para executar aplicações Python sem abrir uma janela de console.

### Experimento 2 — Comunicação por e-mail

Desenvolvimento de um segundo programa utilizando:

- `smtplib`
- `email.mime.text`
- `threading.Timer`
- Comunicação SMTP

O experimento abordou o conceito de transmissão periódica de informações por e-mail.

Os dois experimentos foram demonstrados separadamente em vídeo. O envio por e-mail não foi validado localmente, pois não houve configuração de uma conta de e-mail para o teste.

## 4. Ambiente de desenvolvimento

- Sistema operacional: Windows 10 Pro
- Linguagem: Python 3.15.2
- Editor: Visual Studio Code
- Biblioteca estudada: pynput

## 5. Segurança e responsabilidade

Os experimentos possuem finalidade exclusivamente educacional.

A documentação não disponibiliza mecanismos operacionais de captura furtiva, coleta de credenciais ou transmissão não autorizada de informações.

## 6. Organização dos arquivos

- `README.md`: apresentação do módulo.
- `relatorio_analise.md`: análise técnica dos experimentos.
- `simulacao_keylogger.py`: simulação controlada de eventos fictícios.

## 7. Conclusão

O estudo permitiu compreender conceitos relacionados ao funcionamento de Keyloggers, comunicação SMTP e riscos associados à exposição de informações.

A atividade reforça a importância da segurança de endpoints, monitoramento de processos, controle de permissões e proteção de dados.
