import numpy as np
import os
import templatePyMod as TPM



res = TPM.dummy.func(5.)

def test_points():
    assert (res == np.sqrt(6.))


if __name__ == '__main__':
    print(test_points())
