from numpy import concatenate, zeros, ones, hamming, convolve
import matplotlib.pyplot as plt

digital = concatenate((zeros(20), ones(25), zeros(20)))
norm_hamming = hamming(80)/sum(hamming(80))
res = convolve(digital, norm_hamming)
plt.figure(figsize=(10,10))
plt.ylim(0, 0.6)
plt.plot(res, color='r', linewidth=2)
plt.plot(digital, color='b', linewidth=3)
plt.plot(norm_hamming, color='g', linewidth=4)
plt.show()
plt.savefig('datavis/hamming-convolve')