import geopandas as gpd
from shapely.geometry import Point
from shapely.ops import unary_union
from scipy.spatial import cKDTree
import numpy as np
import os

# Parâmetros
pontos_path = r"G:\Meu Drive\PARANACIDADE\parana_cidade\Material Geomais\Teste\shp\pontos_foz.shp"
lotes_path = r"G:\Meu Drive\PARANACIDADE\parana_cidade\Material Geomais\Teste\shp\lotes_foz.shp"
saida_path = r"G:\Meu Drive\PARANACIDADE\parana_cidade\Material Geomais\Teste\shp\associacao_foz.shp"

# Leitura dos dados
pontos = gpd.read_file(pontos_path)
lotes = gpd.read_file(lotes_path)

# Garante projeção unificada
pontos = pontos.to_crs(epsg=31982)
lotes = lotes.to_crs(epsg=31982)

# Corrige geometrias inválidas
lotes["geometry"] = lotes["geometry"].buffer(0)

# Cria área de cobertura dos lotes com buffer de 10.000 metros
area_de_interesse = unary_union(lotes.geometry).buffer(10000)

# Filtra os pontos que estão dentro da área (com margem de 2 metros)
pontos_filtrados = pontos[pontos.geometry.within(area_de_interesse)].copy()

print(f"Selecionados {len(pontos_filtrados)} pontos dentro da área dos lotes (com buffer).")

# Calcula centróides dos lotes
lotes['centroide'] = lotes.geometry.centroid

# Cria árvore de vizinhança para busca espacial
coords_pontos = np.array([(geom.x, geom.y) for geom in pontos_filtrados.geometry])
coords_centroides = np.array([(geom.x, geom.y) for geom in lotes['centroide']])

tree = cKDTree(coords_centroides)
distancias, indices = tree.query(coords_pontos, distance_upper_bound=10000)

# Associa o lote mais próximo dentro do limite
pontos_filtrados['id_lote_proximo'] = [
    lotes.iloc[i]['id'] if i < len(lotes) and dist <10000 else None
    for i, dist in zip(indices, distancias)
]
pontos_filtrados['distancia_m'] = distancias

# Salva os pontos filtrados e associados
pontos_filtrados.to_file(saida_path)

print("Associação por proximidade (com filtro espacial) concluída com sucesso!")
