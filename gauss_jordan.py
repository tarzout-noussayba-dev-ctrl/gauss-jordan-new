# gauss_jordan_new.py
MAX = 10
def gauss_jordan(A, B, N):
    """Solve a system of linear equations A * X = B by Gauss-Jordan."""
    for k in range(N):
        # Partial Pivoting
        if abs(A[k][k]) < 1e-9:
            for i in range(k + 1, N):
                if abs(A[i][k]) > abs(A[k][k]):
                    A[k], A[i] = A[i], A[k]
                    B[k], B[i] = B[i], B[k]
                    break
        # Check for zero pivot
        if abs(A[k][k]) < 1e-9:
            print("Error: Singular matrix (zero pivot detected).")
            return None
        # Division of pivot row
        pivot = A[k][k]
        for j in range(N):
            A[k][j] /= pivot
        B[k] /= pivot
