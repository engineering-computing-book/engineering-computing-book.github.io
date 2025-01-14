import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
import engcom.engcom.tufte as tufte
import engcom.engcom.data as data

d = data.policy_adoption()
legend = ["Average Citizens", "Economic Elites"]

fig, ax = tufte.plot(
    d["percent_favoring_policy"] - d["percent_favoring_policy"][0]/2,  # Offset to middle of bin
    100*np.stack((d["adoption_average"], d["adoption_elite"])),
    axis=1,
    xlabel="Percent favoring proposed policy change",
    ylabel="Percent predicted probability of adoption",
    legend=legend,
    save="policy_correlations.pgf",
    figsize=(3,3/1.68),
    dotsize=5,
    color="dodgerblue",
)
plt.show()