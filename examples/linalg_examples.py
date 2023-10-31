import numpy as np

from goph419 import linalg


def main():
    A = np.array(
        [
            [15, -10, 0],
            [-10, 25, -15],
            [0, -15, 15],
        ],
        dtype=float,
    )
    print(f"A.shape = {A.shape}")
    print(A)

    b = np.array([5.0, 4.0, 2.0])
    print(f"b.shape = {b.shape}")
    print(b)

    x = np.linalg.solve(A, b)
    print(f"x.shape = {x.shape}")
    print(x)

    x419 = linalg.solve(A, b)
    print(f"x419.shape = {x419.shape}")
    print(x419)

    Ap = np.array(
        [
            [0, -10, 0],
            [-10, 2, -15],
            [0, -15, 15],
        ],
        dtype=float,
    )
    print(f"Ap.shape = {Ap.shape}")
    print(Ap)

    xp = np.linalg.solve(Ap, b)
    print(f"xp.shape = {xp.shape}")
    print(xp)

    xp419 = linalg.solve(Ap, b)
    print(f"xp419.shape = {xp419.shape}")
    print(xp419)


if __name__ == "__main__":
    main()
