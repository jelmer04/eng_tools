from IPython.display import display, Math, HTML

def MathJax(text=False):
  script = "<script src='https://cdnjs.cloudflare.com/ajax/libs/" +\
           "mathjax/2.7.3/latest.js?config=default'></script>"
  
  if text:
    return script
  else:
    display(HTML(script))
