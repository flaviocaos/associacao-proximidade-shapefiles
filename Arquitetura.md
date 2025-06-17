
# Arquitetura do Projeto

O projeto é composto por um pipeline de leitura, transformação e associação de dados geoespaciais:

1. **Entrada**: Arquivos `.shp` de pontos e polígonos
2. **Pré-processamento**: Projeção e limpeza de geometrias
3. **Filtro Espacial**: Seleção de pontos dentro da área de influência
4. **Associação**: cKDTree para determinar lote mais próximo
5. **Saída**: Novo `.shp` com os pontos associados ao lote mais próximo
