import pickle
import matplotlib.pyplot as plt
with open('data/loss.txt','rb') as f:
	data = pickle.load(f)
low = data[0]
for i in data:
	if i < low:
		low = i
print('Lowest Loss:',low)
plt.plot(data)
plt.xlabel('Iteration (100s)')
plt.ylabel('Loss')
plt.show()
