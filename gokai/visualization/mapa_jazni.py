
import matplotlib.pyplot as plt

def plot_radar(values, labels=None, title="Mapa Jaźni"):
    import numpy as np
    N = len(values)
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    values = values + values[:1]
    angles += angles[:1]
    fig = plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels or [f"C{i+1}" for i in range(N)])
    ax.set_title(title)
    return fig
