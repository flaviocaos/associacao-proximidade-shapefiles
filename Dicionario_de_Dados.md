
# Dicionário de Dados

## Entrada

### pontos_foz.shp
- `geometry`: Geometria do ponto (medidor, ocorrência etc.)
- Outros atributos conforme o dataset original.

### lotes_foz.shp
- `geometry`: Geometria do lote
- `id` (recomendado): Identificador único do lote

## Saída

### associacao_foz.shp
- `geometry`: Geometria do ponto
- `id_lote_proximo`: ID do lote mais próximo
- `distancia_m`: Distância em metros até o lote mais próximo
