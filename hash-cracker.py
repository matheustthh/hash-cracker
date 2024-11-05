import hashlib
import time
from typing import Optional

def hash_password(password: str, algorithm: str = 'md5') -> str:
    encoded = password.encode('utf-8')
    if algorithm == 'md5':
        return hashlib.md5(encoded).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(encoded).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(encoded).hexdigest()
    else:
        raise ValueError("Algoritmo inválido")

def dictionary_attack(target_hash: str, wordlist_file: str, algorithm: str = 'md5') -> Optional[str]:
    start_time = time.time()
    attempts = 0
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                attempts += 1
                
                if attempts % 1000 == 0:  
                    elapsed_time = time.time() - start_time
                    print(f"Tentou {attempts} senhas em {elapsed_time:.2f} segundos")
                
                if hash_password(password, algorithm) == target_hash:
                    elapsed_time = time.time() - start_time
                    print(f"\nHash quebrado em {elapsed_time:.2f} segundos após {attempts} tentativas!")
                    return password
    except FileNotFoundError:
        print(f"Erro: Arquivo wordlist '{wordlist_file}' não encontrado")
        return None
    
    print(f"\nSenha não encontrada após tentar {attempts} combinações")
    return None

def main():
    print("Algoritmos de hash disponíveis: md5, sha1, sha256")
    
    algorithm = input("\nDigite o algoritmo de hash (padrão: md5): ").lower() or 'md5'
    if algorithm not in ['md5', 'sha1', 'sha256']:
        print("Algoritmo inválido selecionado. Usando md5.")
        algorithm = 'md5'
    
    target_hash = input("Digite o hash para quebrar: ").lower()
    wordlist_file = input("Digite o caminho do arquivo wordlist: ")
    
    expected_lengths = {'md5': 32, 'sha1': 40, 'sha256': 64}
    if len(target_hash) != expected_lengths[algorithm]:
        print(f"Aviso: O comprimento do hash não corresponde ao formato {algorithm}")
        if not input("Continuar mesmo assim? (s/n): ").lower().startswith('s'):
            return
    
    print("\nIniciando ataque de dicionário...")
    result = dictionary_attack(target_hash, wordlist_file, algorithm)
    
    if result:
        print(f"Senha encontrada: {result}")
    else:
        print("Senha não encontrada na wordlist")

if __name__ == "__main__":
    main()