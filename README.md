# Demonstração Segurança da Informação

Um programa educacional em Python para demonstrar como funciona um quebrador de hashes usando ataques de dicionário.

## 🎯 Objetivo
Este projeto foi criado apenas para fins educacionais, demonstrando:
- Como funcionam diferentes algoritmos de hash (MD5, SHA1, SHA256)
- Como funciona um ataque de dicionário básico
- A importância de senhas fortes

## 🔧 Tecnologias Utilizadas
- Python 3
- Bibliotecas padrão do Python:
  - `hashlib` (para funções de hash)
  - `time` (para medição de tempo)
  - `typing` (para type hints)

## 📋 Pré-requisitos
- Python 3 instalado
- Arquivo wordlist (lista de palavras)
  - Na sua maquina, você pode usar o arquivo "senhas-mais-usadas.txt" como um exemplo.
  - Exemplo de caminho:
    ```bash
    C:\Users\Usuario\Downloads\senhas-mais-usadas.txt
    ```

## 🚀 Como Executar
1. Clone o repositório ou baixe o arquivo Python
2. Abra o terminal na pasta do projeto
3. Execute o script:
   ```bash
   python3 hash_cracker.py
   ```
4. Siga as instruções no terminal:
   - Escolha o algoritmo (md5, sha1, sha256)
   - Digite o hash que deseja quebrar
   - Forneça o caminho para o arquivo wordlist

## 📝 Exemplo de Uso
```bash
Algoritmos de hash disponíveis: md5, sha1, sha256

Digite o algoritmo de hash (padrão: md5): md5
Digite o hash para quebrar: 5f4dcc3b5aa765d61d8327deb882cf99
Digite o caminho do arquivo de lista: /caminho/para/sua/lista.txt
```

## ⚠️ Aviso 
Este programa foi desenvolvido apenas para fins educacionais e de aprendizado.

## 📌 Possíveis Melhorias
- Implementar ataque de força bruta
- Adicionar mais algoritmos de hash
