
"""An interface to represent possible survivor selection operators
"""
class SurvivorSelection(object):

  @classmethod
  def select(cls, population):
    raise NotImplementedError
