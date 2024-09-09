import basic_info
import geopandas as gpd
import matplotlib.pyplot as plt

shapefile_folder = basic_info.shapefile_folder
shapefile_file = basic_info.shapefile_file

# Load the shapefile
def create_my_shape_outline(shapefile_file):
    shape = gpd.read_file(shapefile_file)
    shape = shape[shape['PROVINCE'] == 'LIM'] # Change to the province you are working on
    shape_outline = shape.dissolve()
    shape_outline = shape_outline.to_crs(epsg=4326)
    shape_outline.plot()
    plt.show()  # Ensure the plot is displayed
    shape_outline.to_file(f'{shapefile_folder}/outline.shp')
    with open('basic_info.py', 'a') as f:
        f.write(f"\nshapefile_outline = '{shapefile_folder}/outline.shp'")
    print('Shapefile created and saved as outline.shp')