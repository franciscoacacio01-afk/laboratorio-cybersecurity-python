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

## 5. Resultados e validação do experimento

O experimento foi realizado com dois scripts Python desenvolvidos para o laboratório:

- **Etapa de criptografia:** o primeiro script gerou uma chave Fernet e a utilizou para criptografar os arquivos fictícios encontrados em `Teste_Files`.
- **Etapa de recuperação:** o segundo script carregou a chave gerada e realizou a descriptografia dos arquivos do mesmo ambiente.

**Resultado informado após a execução prática:** a etapa de descriptografia foi concluída e todos os arquivos fictícios originais foram recuperados corretamente.

Esse resultado confirma a recuperação funcional observada no laboratório. Não foi relatada uma comparação criptográfica por hash antes e depois do experimento; portanto, a validação documentada aqui corresponde à conferência prática dos arquivos recuperados.

## 6. Análise técnica e limitações observadas

O exercício também permitiu identificar cuidados importantes:

- Os scripts modificam o conteúdo dos arquivos de teste diretamente, em vez de trabalhar com cópias.
- A geração de uma nova chave a cada execução pode sobrescrever a chave anterior. Se isso ocorrer, arquivos criptografados com a chave antiga podem deixar de ser recuperáveis.
- A recuperação depende da preservação e da disponibilidade da chave correta.
- O script de descriptografia pressupõe que os arquivos encontrados no diretório sejam compatíveis com a chave utilizada; arquivos não criptografados ou criptografados com outra chave podem provocar erros.
- O experimento não incluiu validação automatizada de integridade por hash.

Esses pontos reforçam a importância de preservar chaves, trabalhar com cópias em laboratórios e validar a integridade dos dados por procedimentos próprios.

## 7. Aprendizados

- Conceitos de criptografia simétrica.
- Utilização da biblioteca Cryptography.
- Funcionamento do mecanismo Fernet.
- Importância do gerenciamento seguro de chaves.
- Riscos associados à indisponibilidade de arquivos.
- Diferença entre uma mensagem de execução e a comprovação de recuperação.
- Necessidade de backups e procedimentos de recuperação.

## 8. Medidas de segurança

Para reduzir os riscos relacionados a ransomware, destacam-se:

- Manter backups periódicos e isolados.
- Utilizar antivírus ou soluções EDR.
- Manter sistemas e aplicações atualizados.
- Aplicar o princípio do menor privilégio.
- Monitorar alterações anormais em arquivos.
- Testar regularmente os procedimentos de recuperação.

## 9. Considerações finais

Este experimento teve finalidade exclusivamente educacional e foi executado em ambiente controlado, utilizando apenas arquivos fictícios na pasta `Teste_Files`. A prática contemplou tanto a criptografia quanto a recuperação dos arquivos, que, segundo a validação realizada, foram restaurados corretamente.

O estudo contribuiu para compreender conceitos de criptografia, gerenciamento de chaves e impactos de ataques de ransomware, além de destacar a importância de prevenção, detecção, backups e recuperação.

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
