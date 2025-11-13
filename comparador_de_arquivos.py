import os

def listar_dlls_disco(disco: str) -> list[str]:
    """Percorre todo o disco e retorna uma lista com caminhos completos de arquivos .dll encontrados."""
    dlls_encontradas = []
    for raiz, _, arquivos in os.walk(disco):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.dll'):
                caminho_completo = os.path.join(raiz, arquivo)
                dlls_encontradas.append(caminho_completo)
    return dlls_encontradas

def salvar_lista_em_txt(lista: list[str], caminho_arquivo: str) -> None:
    """Salva a lista de DLLs em um arquivo TXT."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        for item in lista:
            f.write(f"{item}\n")

def carregar_lista_de_txt(caminho_arquivo: str) -> list[str]:
    """Carrega uma lista de DLLs de um arquivo TXT."""
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for linha in f.readlines()]

def comparar_listas(lista_origem: list[str], lista_destino: list[str]) -> list[str]:
    """Retorna as DLLs que estão faltando na lista destino."""
    return [dll for dll in lista_origem if dll not in lista_destino]

def gerar_relatorio_faltantes(faltando: list[str], caminho_relatorio: str) -> None:
    """Gera um relatório com as DLLs faltantes."""
    with open(caminho_relatorio, 'w', encoding='utf-8') as f:
        f.write("=== RELATÓRIO DE DLLs FALTANTES ===\n\n")
        for dll in faltando:
            f.write(f"{dll}\n")
        f.write(f"\nTotal faltando: {len(faltando)}\n")

# Menu interativo
print("Escolha uma opção:")
print("1 - Varrer disco e salvar lista de DLLs")
print("2 - Comparar dois arquivos TXT e gerar relatório")

opcao = input("Digite a opção (1 ou 2): ")

if opcao == "1":
    disco = input("Informe o caminho do disco (ex.: C:\\): ")
    if os.path.exists(disco):
        print(f"Analisando disco {disco}... Isso pode levar alguns minutos.")
        dlls = listar_dlls_disco(disco)
        salvar_lista_em_txt(dlls, "dlls_maquina.txt")
        print(f"Total de DLLs encontradas: {len(dlls)}")
        print("Lista salva em dlls_maquina.txt")
    else:
        print(f"Disco '{disco}' não encontrado.")

elif opcao == "2":
    arquivo_maquina1 = input("Informe o caminho do arquivo TXT da máquina 1: ")
    arquivo_maquina2 = input("Informe o caminho do arquivo TXT da máquina 2: ")
    if os.path.exists(arquivo_maquina1) and os.path.exists(arquivo_maquina2):
        dlls_maquina1 = carregar_lista_de_txt(arquivo_maquina1)
        dlls_maquina2 = carregar_lista_de_txt(arquivo_maquina2)
        faltando = comparar_listas(dlls_maquina1, dlls_maquina2)
        gerar_relatorio_faltantes(faltando, "relatorio_faltantes.txt")
        print(f"Relatório gerado com {len(faltando)} DLLs faltantes.")
    else:
        print("Arquivos TXT não encontrados. Verifique os nomes e caminhos.")
