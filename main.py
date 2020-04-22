from GeneticAlgorithm import GeneticAlgorithm

def fitness_fn(genes):
  return sum(genes)

if __name__ == '__main__':
  ga = GeneticAlgorithm(fitness_fn)
  ga.evolve()
  print(ga.get_best_evolved_individuals()[0].get_genes())