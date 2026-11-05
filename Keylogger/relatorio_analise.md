# Relatório de Análise Técnica — Keylogger

## 1. Introdução

Este relatório apresenta a análise de dois experimentos educacionais desenvolvidos em Python para estudar o funcionamento de Keyloggers e os riscos associados à captura e transmissão de informações.

Os experimentos foram realizados separadamente, utilizando bibliotecas específicas para monitoramento de eventos de teclado e comunicação por e-mail.

## 2. Experimento 1 — Registro local de eventos

### Tecnologias utilizadas

- Python
- Biblioteca `pynput`
- Manipulação de arquivos com `open()`

### Análise técnica

O primeiro programa utiliza a biblioteca `pynput.keyboard` para trabalhar com eventos do teclado.

A função `on_press()` representa o tratamento de eventos de pressionamento de teclas.

O programa diferencia caracteres comuns de teclas especiais e utiliza um arquivo chamado `log.txt` como destino do registro local.

### Execução em segundo plano no Windows

Durante o estudo, foi utilizada a extensão `.pyw`.

No Windows, arquivos `.pyw` podem ser executados pelo interpretador `pythonw.exe`, permitindo a execução sem abertura de uma janela de console.

Essa característica merece atenção em segurança, pois programas maliciosos podem utilizar processos sem console para dificultar a percepção de sua execução pelo usuário.

## 3. Experimento 2 — Comunicação SMTP

### Tecnologias utilizadas

- `smtplib`
- `email.mime.text`
- `threading.Timer`

### Análise técnica

O segundo programa foi desenvolvido para estudar a comunicação com um servidor SMTP e a preparação de mensagens de e-mail.

A biblioteca `smtplib` permite estabelecer comunicação com servidores de e-mail.

O componente `MIMEText` prepara o conteúdo da mensagem, enquanto `Timer` permite estudar o agendamento de tarefas periódicas.

O experimento apresentou o conceito de transmissão periódica de informações para um destino externo.

### Limitação do teste local

O código foi desenvolvido e apresentado em demonstração de vídeo.

Entretanto, o envio por e-mail não foi validado localmente, pois não houve configuração de uma conta de e-mail para realização do teste.

## 4. Integração conceitual dos experimentos

Os dois experimentos representam componentes que podem estar presentes em uma ameaça do tipo Keylogger:

1. Registro de eventos de teclado.
2. Armazenamento das informações.
3. Preparação de mensagens.
4. Comunicação com servidor externo.

O primeiro código aborda o registro local, enquanto o segundo estuda a comunicação SMTP e o agendamento de envios.

A proposta conjunta permite compreender como a captura de informações e sua transmissão podem representar riscos à privacidade e à segurança dos usuários.

## 5. Principais riscos identificados

- Exposição de senhas e credenciais.
- Roubo de informações pessoais.
- Comprometimento de contas.
- Transmissão não autorizada de dados.
- Execução de programas suspeitos em segundo plano.
- Dificuldade de identificação de processos maliciosos.

## 6. Estratégias de detecção e prevenção

### Proteção de endpoints

Utilizar antivírus e soluções EDR atualizadas para identificar comportamentos suspeitos.

### Monitoramento de processos

Verificar processos desconhecidos e programas configurados para inicialização automática.

### Monitoramento de rede

Investigar conexões externas inesperadas e comunicações suspeitas.

### Controle de acesso

Aplicar o princípio do menor privilégio e restringir a execução de programas não autorizados.

### Autenticação

Utilizar autenticação multifator (MFA) para reduzir os impactos do comprometimento de credenciais.

## 7. Resultados dos experimentos

| Atividade | Resultado |
|---|---|
| Desenvolvimento do primeiro código | Realizado |
| Demonstração do registro local em vídeo | Apresentada |
| Estudo da extensão `.pyw` | Realizado |
| Desenvolvimento do segundo código | Realizado |
| Demonstração do segundo experimento em vídeo | Apresentada |
| Configuração de conta de e-mail | Não realizada |
| Validação local do envio SMTP | Não realizada |

## 8. Conclusão

Os experimentos permitiram estudar diferentes componentes associados ao funcionamento de Keyloggers, incluindo registro de eventos do teclado, execução sem console no Windows e comunicação SMTP.

A atividade contribuiu para a compreensão dos riscos de captura e transmissão indevida de informações, além de destacar a importância do monitoramento de processos, proteção de endpoints e conscientização dos usuários.

O conhecimento desses mecanismos é importante para profissionais de segurança da informação, especialmente nas atividades de prevenção, análise e resposta a incidentes.
