from argparse import ArgumentParser
from os import walk
from os.path import dirname, join, realpath
from pprint import pprint
from sys import exit

from models.population import Population


#TODO use an argument parser to pass values as arguments
if __name__ == '__main__':
  parser= ArgumentParser()
  options = {
    "parent_selection" : None, 
    "recombination" : None, 
    "mutation": None, 
    "survivor_selection" : None
  }
  
  for option in options:
    for _, dirnames, filenames in walk(join(dirname(realpath(__file__)), option)):
      filenames.remove('__init__.py')
      filenames.remove(option + '.py')
      option_names = [f.replace('.py', '') for f in filenames]
      parser.add_argument('-' + option[0], '--' + option, choices=option_names, required=True)

  parser.add_argument("-psize", "--population_size", type=int, metavar='x', required=True)
  parser.add_argument("-isize", "--individual_size", type=int, metavar='y', required=True)

  args = parser.parse_args()
  pprint(dir(args))
  populationSize = args.population_size
  individualSize = args.individual_size
  population = Population(populationSize=populationSize, individualSize=individualSize)
  
  # Run the EA