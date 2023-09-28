import numpy as np

from goph419.functions import (
    exp,
    sin,
)


def main():
    x = 1.0
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected) / expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 0.0
    expected = 1.0
    result = exp(x)
    eps = (result - expected) / expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 8.5
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected) / expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = -12.0
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected) / expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 1.0
    expected = np.sin(x)
    result = sin(x)
    eps = (result - expected) / expected
    print(f"testing sin({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 8.5
    expected = np.sin(x)
    result = sin(x)
    eps = (result - expected) / expected
    print(f"testing sin({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = -12.0
    expected = np.sin(x)
    result = sin(x)
    eps = (result - expected) / expected
    print(f"testing sin({x:0.16e})")
    print(f"expected: {expected:0.16e}")
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")


if __name__ == "__main__":
    main()
