from argparse import ArgumentParser
from fnmatch import fnmatch
from os import walk
from os.path import dirname, join, realpath
from pprint import pprint
from sys import exit

from algorithms.simple_ga import SimpleGA
from models.population import Population


def underscore_to_camelcase(value):
    def camelcase():
        yield str.lower
        while True:
            yield str.capitalize

    c = camelcase()
    return "".join(c.next()(x) if x else '_' for x in value.split("_"))

#TODO use an argument parser to pass values as arguments
if __name__ == '__main__':
    parser = ArgumentParser()
    options = {
      "parent_selection": None,
      "recombination": None,
      "mutation": None,
      "survivor_selection": None
    }

    for option in options:
        for _, dirnames, filenames in walk(join(dirname(realpath(__file__)), option)):
            filenames.remove('__init__.py')
            filenames.remove(option + '.py')
            option_names = []
            for file in filenames:
                if fnmatch(file, '*.py'):
                    option_names.append(file.replace('.py', ''))
            parser.add_argument('-' + option[0], '--' + option, choices=option_names, required=True)

    parser.add_argument("-psize", "--population_size", type=int, metavar='x', required=True)
    parser.add_argument("-isize", "--individual_size", type=int, metavar='y', required=True)
    parser.add_argument("--rounds", type=int, metavar='r', required=True)

    args = parser.parse_args()
    populationSize = args.population_size
    individualSize = args.individual_size
    rounds = args.rounds

    # Load the relevant modules as specified in command-line
    # Kind of hacky but convenient
    for option in options:
        selectedOption = args.__getattribute__(option)
        className = underscore_to_camelcase(selectedOption)
        className = className[0].capitalize() + className[1:]
        _temp = __import__("{}.{}".format(option, selectedOption), globals(), locals(), [className], -1)
        locals()[underscore_to_camelcase(option)] = _temp.__getattribute__(className)

    initialPopulation = Population(populationSize=populationSize, individualSize=individualSize)

    # Initialize the algorithm
    algorithm = SimpleGA()

    # Run it!
    algorithm.run(initialPopulation, rounds, parentSelection(), recombination(), mutation(), survivorSelection())
