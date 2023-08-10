sample = {1,2,3,4,5,6,5}
sample.add(7)
print(sample)

sample.remove(3)
print(sample)

sample.discard(5)
print(sample)

new_sample = sample.copy()
print(new_sample)

sample = sample.pop()
print(sample)

new_sample.update([6,7,8])
print(new_sample)

sample.clear()
print(sample)