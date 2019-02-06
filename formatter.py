import string
import numpy as np

class EngineeringFormat(string.Formatter):
  '''Engineering formatting for Math display
  usage:  .format('{0}\t{0:eng,mm}', v)'''
  
  def format_field(self, value, format_spec):
    if format_spec.startswith('eng'):
      try:
        unit = format_spec.split(',')[1]
        unit = "\\ \\mathrm{{{}}}".format(unit)     
      except IndexError:
        unit = ''
      
      if value == 0: 
        return "{0:.0f} {1}".format(np.round(value, 3), unit)
      
      if 0.001 <= value < 10: 
        return "{0:.3f} {1}".format(np.round(value, 3), unit)
      
      if 10 <= value < 100: 
        return "{0:.2f} {1}".format(np.round(value, 3), unit)
      
      if 100 <= value < 1000: 
        return "{0:.1f} {1}".format(np.round(value, 3), unit)

      mag = np.ceil(int(np.log10(value))/3)
      rnd = np.round(value / (1000**mag), 3)
      
      if unit == '':
        return "({0:.3f} \\times {{10}}^{{{1:.0f}}})".format(rnd, mag*3)
      else:
        return "{0:.3f} \\times {{10}}^{{{1:.0f}}} {2}".format(rnd, mag*3, unit)
      
    else:
      return super().format_field(value, format_spec)
    
    
eng_format_obj = EngineeringFormat()
eng_format = eng_format_obj.format
