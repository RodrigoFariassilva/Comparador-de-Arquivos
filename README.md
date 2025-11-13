Comparador de Arquivos DLL
Este projeto tem como objetivo listar todos os arquivos DLL de um disco ou diretório e comparar duas listas geradas em máquinas diferentes, identificando quais DLLs estão faltando. É útil para auditorias, migrações ou verificações de integridade entre ambientes Windows.

Funcionalidades

Varredura completa de disco ou diretório para localizar arquivos .dll.
Geração de arquivo TXT com a lista completa das DLLs encontradas.
Comparação entre duas listas TXT para identificar DLLs faltantes.
Geração de relatório detalhado com as DLLs ausentes e contagem total.


Como funciona
O script possui um menu interativo com duas opções:


Varrer disco e salvar lista de DLLs

Percorre o disco informado (ex.: C:\) e salva a lista em dlls_maquina.txt.



Comparar dois arquivos TXT e gerar relatório

Compara os arquivos TXT gerados em duas máquinas.
Cria relatorio_faltantes.txt com as DLLs que estão faltando na segunda máquina.




Pré-requisitos

Python 3.8+
Sistema operacional Windows (por causa das DLLs).
Permissões para leitura do disco (pode precisar executar como administrador).
