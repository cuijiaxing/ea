
"""An interface to represent possible mutation operators
"""


class Mutation(object):

    @classmethod
    def mutate(cls, individual):
        raise NotImplementedError
