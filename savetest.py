import pickle

with open('inverted_save.pik', 'rb')as f:
    data = pickle.load(f)

print(type(data[0]),len(data[0]))