import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.append("../")
import engcom.engcom.tufte as tufte
import engcom.engcom.data as data

wn = 1  # (rad/s) Natural frequency
time = np.linspace(0, 10, 101)
damping_ratios = np.linspace(1.6, 0.0001, 9)
responses = np.full((len(damping_ratios), len(time)), np.nan)
legend = []
for i, zeta in enumerate(damping_ratios):
    responses[i,:] = data.step_response(
        time=None,
        noisy=False,
        system_order=2,
        damping_ratio=zeta,
        natural_freq=wn,
    )["output"]
    legend.append(f"$\\zeta = {zeta:.1f}$")

fig, ax = tufte.plot(
    time*wn/(2*np.pi),
    responses,
    axis=1,
    xlabel="Normalized time $\\dfrac{\\omega_n}{2\\pi} t$",
    ylabel="Step response",
    legend=legend,
    legendloc="outside right",
    save="dynamic_system_responses.pgf",
    figsize=(4.8,4.8/1.68),
    color="map",
    points=False,
    xticks=np.linspace(0, 1.5, 4),
)
plt.show()