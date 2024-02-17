from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

def evolve(state):
    driver = PySCFDriver(
        atom="H 0 0 0; H 0 0 0.735",
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )
    return { "ammonia":1 }
