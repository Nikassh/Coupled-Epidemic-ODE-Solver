import numpy as np

class NextGenMatrixR0:
    """
    Next-Generation Matrix (NGM) R0 Spectral Radius Solver.
    """
    @staticmethod
    def compute_r0(F_matrix: np.ndarray, V_matrix: np.ndarray) -> float:
        """
        Calculates R0 as spectral radius rho(F * V^(-1)).
        """
        V_inv = np.linalg.inv(V_matrix)
        next_gen_matrix = np.matmul(F_matrix, V_inv)
        eigenvalues = np.linalg.eigvals(next_gen_matrix)
        r0 = float(np.max(np.abs(eigenvalues)))
        return r0
