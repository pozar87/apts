import io
import matplotlib.pyplot as plt

class MatplotlibSVGWrapper:
    def __init__(self, fig):
        self.fig = fig

    def _repr_svg_(self):
        output = io.StringIO()
        self.fig.savefig(
            output,
            format="svg",
            facecolor=self.fig.get_facecolor(),
            edgecolor="none",
            transparent=False,
        )
        plt.close(self.fig)
        return (output.getvalue(),)
