import json
import numpy as np
import time
from pathlib import Path

basename = "compare_npy_and_json"
A = np.random.rand(10_000, 5)
A_list = A.tolist()

# %% Save as JSON

json_ = {"save": {}, "load": {}}
json_["save"]["tic"] = time.time()
with open(f"{basename}.json", "w") as f:
    json.dump({"A": A_list}, f)
json_["save"]["toc"] = time.time()

# %% Load JSON

json_["load"]["tic"] = time.time()
with open(f"{basename}.json", "r") as f:
    A_json_dict = json.load(f)
A_json = np.array(A_json_dict["A"])
json_["load"]["toc"] = time.time()

# %% Save as .npy

npy_ = {"save": {}, "load": {}}
npy_["save"]["tic"] = time.time()
with open(f"{basename}.npy", "wb") as f:
    np.save(f, A, allow_pickle=False)
npy_["save"]["toc"] = time.time()

# %% Load .npy

npy_["load"]["tic"] = time.time()
with open(f"{basename}.npy", "rb") as f:
    A_npy = np.load(f)
npy_["load"]["toc"] = time.time()

# %% Compare

## Size
json_["size_MB"] = Path(f"{basename}.json").stat().st_size * 1e-6
npy_["size_MB"] = Path(f"{basename}.npy").stat().st_size * 1e-6

## Save Time
json_["save_time_s"] = json_["save"]["toc"] - json_["save"]["tic"]
npy_["save_time_s"] = npy_["save"]["toc"] - npy_["save"]["tic"]

## Load Time
json_["load_time_s"] = json_["load"]["toc"] - json_["load"]["tic"]
npy_["load_time_s"] = npy_["load"]["toc"] - npy_["load"]["tic"]

print(
    f"JSON\t size (MB): {json_['size_MB']:.3g}\t"
    f"save time (s): {json_['save_time_s']:.3g}\t"
    f"load time (s): {json_['load_time_s']:.3g}"
)
print(
    f".npy\t size (MB): {npy_['size_MB']:.3g}\t"
    f"save time (s): {npy_['save_time_s']:.3g}\t"
    f"load time (s): {npy_['load_time_s']:.3g}"
)
