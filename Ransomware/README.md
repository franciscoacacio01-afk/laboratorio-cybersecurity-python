# Experimento Educacional — Ransomware

## 1. Objetivo

Estudar os conceitos de ransomware e compreender como a criptografia simétrica pode ser utilizada indevidamente para comprometer a disponibilidade de arquivos.

## 2. Ambiente utilizado

- Sistema operacional: Windows 10 Pro
- Linguagem: Python 3.15.2
- Editor: Visual Studio Code
- Biblioteca: Cryptography
- Mecanismo estudado: Fernet

## 3. Ambiente de testes

Foi utilizada uma pasta denominada `Teste_Files`, contendo arquivos fictícios, criada exclusivamente para fins educacionais.

O experimento foi realizado em ambiente controlado, sem utilização de arquivos pessoais ou dados de terceiros.

## 4. Execução

O script Python foi executado pelo PowerShell.

Saída apresentada no terminal:

```text
>>> PROGRAMA INICIADO <<<
>>> ENTRANDO NA FUNCAO MAIN <<<
Todos os arquivos foram criptografados com sucesso!
>>> PROGRAMA FINALIZADO <<<
```

**Observação:** essa saída registra a mensagem apresentada pelo programa, mas, isoladamente, não comprova a integridade dos arquivos nem a possibilidade de recuperação.

## 5. Aprendizados

- Conceitos de criptografia simétrica.
- Utilização da biblioteca Cryptography.
- Funcionamento do mecanismo Fernet.
- Importância do gerenciamento seguro de chaves.
- Riscos associados à indisponibilidade de arquivos.
- Necessidade de backups e procedimentos de recuperação.

## 6. Medidas de segurança

Para reduzir os riscos relacionados a ransomware, destacam-se:

- Manter backups periódicos e isolados.
- Utilizar antivírus ou soluções EDR.
- Manter sistemas e aplicações atualizados.
- Aplicar o princípio do menor privilégio.
- Monitorar alterações anormais em arquivos.
- Testar regularmente os procedimentos de recuperação.

## 7. Considerações finais

Este experimento teve finalidade exclusivamente educacional e contribuiu para compreender conceitos de criptografia e os impactos de ataques de ransomware.

O objetivo do estudo é fortalecer conhecimentos de segurança cibernética e compreender mecanismos de prevenção, detecção e recuperação.
