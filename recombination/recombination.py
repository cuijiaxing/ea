
"""An interface to represent possible recombination operators of arbitrary arity
"""
class Recombination(object):
  
  @classmethod
  def recombine(cls, individuals):
    raise NotImplementedError