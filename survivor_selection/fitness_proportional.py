from survivor_selection import SurvivorSelection


class FitnessProportional(SurvivorSelection):

    @classmethod
    def select(cls, population, offspring):
        return offspring
