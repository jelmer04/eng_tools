import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.offline import iplot

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 

from plotly.colors import DEFAULT_PLOTLY_COLORS as colors
import plotly.tools as tls

cf.go_offline()

init_notebook_mode(connected=False)

plotly_version = '1.3.0'

def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML(f'''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({{
            paths: {{
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-{plotly_version}.min.js?noext',
            }},
          }});
        </script>
        '''))
        
get_ipython().events.register('pre_run_cell', configure_plotly_browser_state)
