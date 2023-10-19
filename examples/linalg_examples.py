import numpy as np


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
    b = np.reshape(b, (len(b), 1))
    print(f"b.shape = {b.shape}")
    print(b)

    aug = np.hstack([A, b])
    print(f"aug.shape = {aug.shape}")
    print(aug)

    x = np.linalg.solve(A, b)
    print(f"x.shape = {x.shape}")
    print(x)


if __name__ == "__main__":
    main()
