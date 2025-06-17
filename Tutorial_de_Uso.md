
# Tutorial de Uso

1. Coloque os arquivos `pontos_foz.shp` e `lotes_foz.shp` no diretório `shp/`.
2. Ative o ambiente virtual:
```bash
.venv\Scripts\activate
```
3. Instale as dependências (se necessário):
```bash
pip install -r requirements.txt
```
4. Execute o script:
```bash
python associar_por_proximidade_com_mascara.py
```
5. O resultado estará em `shp/associacao_foz.shp`.

Você pode explorar os dados também pelo notebook `associar_por_proximidade_com_mascara.ipynb`.
