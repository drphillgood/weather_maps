import os
os.environ['PROJ_LIB'] = r'C:/Users/ustro/.conda/envs/TEST/Library/share'

import plotly
plotly.__version__

from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()

import plotly as py
from plotly.graph_objs import *

import numpy as np
from scipy.io import netcdf

from mpl_toolkits.basemap import Basemap
