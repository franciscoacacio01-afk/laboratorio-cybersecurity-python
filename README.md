# Laboratório de CyberSecurity com Python

Laboratório educacional desenvolvido durante meus estudos de CyberSecurity, com atividades de análise sobre ransomware, keyloggers, criptografia e estratégias de defesa.

## Sobre o projeto

Este repositório reúne documentação, relatórios e uma simulação segura desenvolvidos para compreender conceitos de segurança da informação. As atividades têm finalidade exclusivamente educacional e utilizam dados fictícios ou registros de testes.

## Objetivos

- Compreender conceitos relacionados ao funcionamento de ransomware.
- Estudar criptografia simétrica e o mecanismo Fernet.
- Analisar conceitos e riscos associados a keyloggers.
- Compreender riscos de captura e transmissão indevida de informações.
- Identificar medidas de prevenção, detecção, resposta e recuperação.

## Ambiente de desenvolvimento

| Componente | Configuração |
|---|---|
| Sistema operacional | Windows 10 Pro |
| Linguagem | Python 3.15.2 |
| Editor | Visual Studio Code |
| Criptografia estudada | Cryptography / Fernet |
| Terminal | PowerShell |

## Estrutura do repositório

```text
laboratorio-cybersecurity-python/
├── README.md
├── Ransomware/
│   └── README.md
├── Keylogger/
│   ├── README.md
│   ├── relatorio_analise.md
│   ├── simulacao_keylogger.py
│   └── registro_simulado.txt
└── Reflexao_Defesa/
    └── reflexao.md
```

## 1. Estudo sobre Ransomware

A pasta [Ransomware](Ransomware/README.md) contém a documentação do experimento educacional realizado em ambiente controlado, com arquivos fictícios.

O estudo aborda conceitos de criptografia simétrica com Fernet, gerenciamento de chaves, riscos de indisponibilidade de dados e a importância de backups e procedimentos de recuperação.

A documentação também registra a saída observada no terminal e ressalta que essa mensagem, isoladamente, não comprova a integridade dos arquivos nem sua recuperação.

## 2. Estudo sobre Keyloggers

A pasta [Keylogger](Keylogger/README.md) reúne o estudo conceitual e a simulação segura:

- **README.md:** apresentação dos experimentos e tecnologias estudadas.
- **relatorio_analise.md:** análise técnica, riscos, limitações e estratégias de defesa.
- **simulacao_keylogger.py:** simulação com eventos fictícios; não monitora o teclado real.
- **registro_simulado.txt:** resultado textual gerado pela simulação.

O estudo também aborda a biblioteca `pynput`, a execução de arquivos `.pyw` no Windows e conceitos de comunicação SMTP. O envio por e-mail não foi validado localmente, pois não foi configurada uma conta para o teste.

## 3. Reflexão sobre Defesa

A pasta [Reflexão sobre Defesa](Reflexao_Defesa/reflexao.md) apresenta medidas de prevenção, detecção, mitigação e resposta a incidentes envolvendo ransomware e keyloggers.

Entre os temas abordados estão backups, antivírus e EDR, firewall, atualizações, controle de privilégios, autenticação multifator, isolamento de ambientes e conscientização dos usuários.

## Aprendizados

As atividades contribuíram para ampliar a compreensão sobre ameaças digitais, criptografia, proteção de endpoints, privacidade e práticas de defesa em segurança da informação.

## Aviso educacional

Este repositório destina-se exclusivamente ao estudo e à formação em CyberSecurity. Não utilize técnicas ou ferramentas para monitorar pessoas, capturar informações, comprometer sistemas ou acessar dados sem autorização. Mantenha testes em ambientes controlados e utilize apenas dados fictícios ou próprios.

## Autor

**Francisco Acácio**  
Estudante de CyberSecurity | Tecnologia da Informação

GitHub: [@franciscoacacio01-afk](https://github.com/franciscoacacio01-afk)
