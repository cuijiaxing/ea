from random import uniform

from models.population import Population
from parent_selection import ParentSelection
from utils import stochastic_universal_sampling

"""An implementation of n-roulette-wheel fitness-proportional selection
"""


class FitnessProportional(ParentSelection):

    @classmethod
    def select(cls, population, ratio):
        return stochastic_universal_sampling.sample(population, ratio * population.size())
