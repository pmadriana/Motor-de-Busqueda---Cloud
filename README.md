# Motor-de-Busqueda---Cloud

Motor de Búsqueda usando Hadoop y algoritmos: Índice Invertido y Page Rank

#Pre requisitos
* Tener instalado Python3
* Tener instalado Hadoop 3.2

# Preparar el Ambiente de Pruebas
* Clonar el repositorio
* Descargar el conjunto de datos del siguiente enlace https://www.kaggle.com/kmader/aminer-academic-citation-dataset
* Crear una carpeta data y colocar todos los archivos .json en esa carpeta
* Usar el siguiente comendo para colocar el conjunto de datos en el sistema de archivos de Hadoop
```
hadoop fs -mkdir /data
hadoop fs -put ./data/* /data
```
# Ejecucion de los Algoritmos de Indice Invertido y Page Rank
- Ejecutar el indice invertido
```
mapred streaming -files inverted_index_mapper.py,inverted_index_reducer.py -input /data/*.json -output /inverted_index_result -mapper inverted_index_mapper.py -reducer inverted_index_reducer.py
```
- Ejecutar el PageRank
```
mapred streaming -files page_rank_mapper.py,page_rank_reducer.py -input /data/*.json -output /page_rank_result -mapper page_rank_mapper.py -reducer page_rank_reducer.py
```
- Obtener un archivo de texto con los resultados del PageRank y del Indice Invertido
```
hadoop fs -getmerge /inverted_index_result index_result.txt && hadoop fs -getmerge /page_rank_result ank_result.txt
```

# Buscador Web
<br>
<img src="https://github.com/pmadriana/Motor-de-Busqueda---Cloud/blob/main/searchmotor.PNG" />
<br>
