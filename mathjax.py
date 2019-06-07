from IPython.display import display, Math, HTML

def load_mathjax_in_cell_output():
  display(HTML("<script src='https://www.gstatic.com/external_hosted/"
               "mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>"))
get_ipython().events.register('post_run_cell', load_mathjax_in_cell_output)
