names = ["Mo", "Jo", "Flo"]
data = dict.fromkeys(names) # => {"Mo": None, "Jo": None, "Flo": None}

#%% Populate Data
data["Mo"] = {}
data["Mo"]["year"] = "sophomore"
data["Mo"]["major"] = "Mechanical Engineering"
data["Mo"]["GPA"] = 3.44
data["Jo"] = {}
data["Jo"]["year"] = "junior"
data["Jo"]["major"] = "Computer Science"
data["Jo"]["GPA"] = 3.96
data["Flo"] = {}
data["Flo"]["year"] = "sophomore"
data["Flo"]["major"] = "Philosophy"
data["Flo"]["GPA"] = 3.12

#%% Data Operations and Printing
print(f"Mo is a {data['Mo']['year']}. "
      f"Jo is a {data['Jo']['year']}. "
      f"Flo is a {data['Flo']['year']}.")
data["Jo"]["GPA"] = 3.98
print(f"Jo's new GPA is {data['Jo']['GPA']}")
data.pop("Mo")
print(f"Names sans Mo: {list(data.keys())}")