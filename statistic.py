import pandas as pd                    ## importing Python Pandas library
import numpy as np                    ## importing Python Numpy library
df = pd.read_csv('OECD_Health.csv')   ## reading data from dowlanded CSV file

df.head()             ##  Exposing CSV data to DataFrames table


##################################################################

import pandas as pd    ## importing Python Pandas library
import numpy as np     ## importing Python Numpy library 
pandas_bokeh.output_notebook()  ## outputing data inline JN

my_chart = pd.DataFrame({
    'x': np.random.randn(500)+1,
    'y': np.random.randn(500),     ## Using random numbers
    'z': np.random.randn(500)-1
}, columns=['x','y','z'])

my_chart.plot_bokeh.hist(      #
    bins=np.linspace(-5,5,45),  # 
    histogram_type="stacked",    ## Customising histogram chart
    vertical_xlabel=True,       #
    hovertool=True,
    title="Histogram example (Stacked)",
    line_color="black",
    
)


#########################################################



import numpy as np
import pandas as pd
import geopandas as gpd
import pandas_bokeh
pandas_bokeh.output_notebook()
df_mapplot = pd.read_csv(r"https://raw.githubusercontent.com/PatrikHlobil/Pandas-Bokeh/master/docs/Testdata/populated%20places/populated_places.csv")
df_mapplot.head()

df_mapplot["size"] = df_mapplot["pop_max"] / 1000000
df_mapplot.plot_bokeh.map(
    x="longitude",
    y="latitude",
    hovertool_string="""<h2> @{name} </h2> 
    
                        <h3> Population: @{pop_max} </h3>""",
    tile_provider="STAMEN_TERRAIN_RETINA",
    size="size", 
    figsize=(900, 600),
    title="World cities with more than 1.000.000 inhabitants")