import time
import numpy as np
start_time = time.time()

# Laurens Van Der Maaten Barnes-Hut TSNE

import bhtsne

X = np.loadtxt("lstm2_batch100_50.txt")
Y = bhtsne.bh_tsne(X)
output = []
for point in Y:
   output.append(point)
print("--- %s seconds ---" % (time.time() - start_time))
    
np.savetxt("bh_laurens_full_10.txt", np.array(output)) 
print("--- %s seconds ---" % (time.time() - start_time))

# Laurens Van Der Maaten Python TSNE

import time
import numpy as np
start_time = time.time()

import tsne

X = np.loadtxt("hiddens_half.txt")
Y = tsne.tsne(X)
print("--- %s seconds ---" % (time.time() - start_time))

np.savetxt("python_tsne_laurens_half.txt", np.array(Y))   
print("--- %s seconds ---" % (time.time() - start_time))

# SKLearn Barnes-Hut TSNE

import time
import numpy as np
start_time = time.time()

from sklearn import manifold

X = np.loadtxt("lstm2_batch100_50.txt")
t = manifold.TSNE()
np.set_printoptions(suppress=True)
Y = t.fit_transform(X)
print("--- %s seconds ---" % (time.time() - start_time))

np.savetxt("bh_sklearn_full_10.txt", np.array(Y)) 
print("--- %s seconds ---" % (time.time() - start_time))

