from threading import Thread


class Population(object):

    individuals = None

    def __init__(self, individuals):
        self.individuals = individuals

    def size(self):
        return len(self.individuals)

    def evaluate(self):
        threads = []
        for i in xrange(self.size()):
            thread = Thread(target=self.individuals[0].evaluateFitness)
            thread.start()
            threads.append(thread)

            if i % 8 == 0:
                for t in threads:
                    t.join()
                threads = []

        for t in threads:
            t.join()
