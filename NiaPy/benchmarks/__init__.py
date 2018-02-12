"""Module with implementations of benchmarks."""

from NiaPy.benchmarks.rastrigin import Rastrigin
from NiaPy.benchmarks.rosenbrock import Rosenbrock
from NiaPy.benchmarks.griewank import Griewank
from NiaPy.benchmarks.sphere import Sphere
from NiaPy.benchmarks.ackley import Ackley

__all__ = [
    'Rastrigin',
    'Rosenbrock',
    'Griewank',
    'Sphere',
    'Ackley'
]
