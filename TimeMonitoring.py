#in ipython

import numpy as np
A = np.random.rand(500, 500)
%timeit A[A > 0.5] = 5
#result: 100 loops, best of 3: 2.02 ms per loop
