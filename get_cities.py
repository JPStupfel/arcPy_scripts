import arcpy
my_countries = r'C:\Users\johnp\code\geodata\arcPy\data\ne_10m_admin_0_countries.shp'
my_points = r'C:\Users\johnp\code\geodata\arcPy\data\ne_10m_populated_places.shp'
my_outputs = r'C:\Users\johnp\OneDrive\Documents\ArcGIS\Projects\ArcPyTutorial\outputs'
my_sql_sub_select = "NAME = 'United States of America' "

my_output_filename_points = 'brand_new_cities'
my_output_filename_country = 'USA_new_bounds'

# points file to clip, countries file and sql_sub_select the boundary with sql for a specific feature , outputs folder where you want info saved
def clip_file(points, countries, outputs, sql_sub_select, output_filename_points, output_filename_country):

    arcpy.MakeFeatureLayer_management(points, "points_lyr")
    arcpy.MakeFeatureLayer_management(countries, "countries_lyr", sql_sub_select)
    arcpy.SelectLayerByAttribute_management("countries_lyr", "SUBSET_SELECTION", sql_sub_select)
    bounds = arcpy.conversion.FeatureClassToFeatureClass('countries_lyr', outputs, output_filename_country)

    arcpy.SelectLayerByLocation_management('points_lyr', "WITHIN", bounds)
    arcpy.conversion.FeatureClassToFeatureClass('points_lyr', outputs, output_filename_points)

clip_file(points=my_points, countries=my_countries, outputs=my_outputs, sql_sub_select=my_sql_sub_select, 
output_filename_points=my_output_filename_points, output_filename_country=my_output_filename_country)