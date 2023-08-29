# Processamento de Arquivos .fas para Pesquisa em Bioinformática

Este é um script Python desenvolvido para auxiliar a pesquisa de doutorado em Bioinformática da Raquel Santos. O objetivo do script é processar arquivos no formato .fas, reduzindo o tamanho das linhas contidas nesses arquivos e salvando os resultados em um diretório de saída.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. O script foi desenvolvido e testado em um ambiente que suporta a execução de scripts Python.

## Uso

1. Coloque os arquivos .fas que você deseja processar na mesma pasta onde o script está localizado.

2. Execute o script através do terminal ou de um ambiente de desenvolvimento Python.

   ```bash
   python col_script.py 
   ```

3. O script processará os arquivos .fas encontrados na pasta e criará um diretório chamado "output" (se ainda não existir) para armazenar os resultados processados.

4. O script lerá cada arquivo .fas, identificará as espécies e seus genes correspondentes e reduzirá o tamanho das linhas dos genes.

5. Os resultados processados serão salvos em arquivos individuais no diretório "output".

## Detalhes do Processamento

O script funciona da seguinte maneira:

- Ele busca por todos os arquivos .fas na pasta onde está sendo executado.
- Para cada arquivo .fas, ele lê as linhas e identifica as espécies e seus genes associados.
- Ele reduz o tamanho das linhas dos genes, garantindo que cada linha tenha no máximo 60 caracteres.
- Os resultados são salvos em arquivos individuais dentro do diretório "output".

## Observações

Este script foi desenvolvido especificamente para atender às necessidades da pesquisa de doutorado em Bioinformática da Raquel Santos. Se você deseja usá-lo para outros fins, pode ser necessário adaptá-lo conforme necessário.

 
