import pickle

L1 = [1, 2, 3]
L2 = [4, 5, 6]

with open("pickle_example.pickle", "wb") as f:
    pickle.dump((L1, L2), f)  # Bundle into a tuple

with open("pickle_example.pickle", "rb") as f:
    data = pickle.load(f)  # data is a tuple
