
"""An interface to represent possible parent selection operators
"""
class ParentSelection(object):
  
  @classmethod
  def select(cls, population):
    raise NotImplementedError