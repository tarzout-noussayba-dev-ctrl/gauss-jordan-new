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
        # Elimination loop
        for i in range(N):
            if i == k:
                continue
            factor = A[i][k]
            for j in range(N):
                A[i][j] -= factor * A[k][j]
            B[i] -= factor * B[k]

    return B
def main():
    N = int(input(f"Enter the number of equations (N <= {MAX}): "))
    if N > MAX or N <= 0:
        print(f"Error: N must be between 1 and {MAX}")
        return

    A = []
    print(f"Enter the coefficients of matrix A ({N}x{N}):")
    for i in range(N):
        row = []
        for j in range(N):
            value = float(input(f"A[{i+1}][{j+1}] = "))
            row.append(value)
        A.append(row)

    B = []
    print(f"\nEnter the constants vector B ({N} values):")
    for i in range(N):
        value = float(input(f"B[{i+1}] = "))
        B.append(value)
    result = gauss_jordan(A, B, N)

    print("\nThe transformed matrix (A):")
    for i in range(N):
        for j in range(N):
            print(f"{A[i][j]:.4f}", end="\t")
        print()

    if result is not None:
        print("\nThe solution (X):")
        for i in range(N):
            print(f"x{i+1} = {result[i]:.6f}")

if __name__ == "__main__":
    main()
