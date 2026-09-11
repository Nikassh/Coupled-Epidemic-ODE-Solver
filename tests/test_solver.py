import unittest
import numpy as np
from epi_tivm.intra_host import WithinHostTIVMSolver
from epi_tivm.ngm_r0 import NextGenMatrixR0

class TestEpiTIVMSolver(unittest.TestCase):
    def test_tivm_solver_execution(self):
        solver = WithinHostTIVMSolver()
        sol = solver.solve(t_span=(0, 5))
        self.assertTrue(sol.success)
        self.assertGreaterThan(len(sol.t), 0) if hasattr(self, 'assertGreaterThan') else self.assertTrue(len(sol.t) > 0)

    def test_ngm_r0_spectral_radius(self):
        F = np.array([[2.0, 1.0], [0.0, 0.0]])
        V = np.array([[0.5, 0.0], [0.0, 0.2]])
        r0 = NextGenMatrixR0.compute_r0(F, V)
        self.assertAlmostEqual(r0, 4.0, places=2)

if __name__ == '__main__':
    unittest.main()
