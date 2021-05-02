'''
Este Script guarda vectores de un grupo específico.
'''

ng = 'api_google_maps'
ruta_shp = 'C:/Users/user/Downloads/reporte/tuto/'
root = QgsProject.instance().layerTreeRoot()
my_group = root.findGroup(ng)

layer_list = [layer.name() for layer in my_group.children()]


for layer in layer_list:
    vector = QgsProject.instance().mapLayersByName(layer)
    if vector[0].type() == 0:
        save = QgsVectorFileWriter.writeAsVectorFormat(vector[0], ruta_shp + layer + '.shp','utf-8',driverName='ESRI Shapefile')
        print('Exportado... ' + layer + '.shp')
    else:
        print(layer + 'Este layer no es un vector...')