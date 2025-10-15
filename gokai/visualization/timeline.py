
import matplotlib.pyplot as plt

def draw_timeline(phases):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    y = 1
    x = 0
    for name, dur in phases:
        ax.broken_barh([(x, dur)], (y, 0.8))
        ax.text(x+dur/2, y+0.4, name, ha="center", va="center")
        x += dur
    ax.set_ylim(0, 3)
    ax.set_xlim(0, x+1)
    ax.set_yticks([])
    ax.set_title("Oś czasu i cykle rozwoju")
    return fig
