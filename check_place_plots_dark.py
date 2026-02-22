
from apts.place import Place

# Setup mock data
place = Place(52.2297, 21.0122, "Warsaw")

def check_legend(fig, name):
    if fig is None:
        print(f"Plot: {name} - Figure is None")
        return
    for ax in fig.get_axes():
        legend = ax.get_legend()
        if legend:
            frame = legend.get_frame()
            print(f"Plot: {name}")
            print(f"  Legend facecolor: {frame.get_facecolor()}")
            print(f"  Legend edgecolor: {frame.get_edgecolor()}")
            for text in legend.get_texts():
                print(f"  Text color: {text.get_color()}")
            if legend.get_title():
                print(f"  Title color: {legend.get_title().get_color()}")
        else:
            print(f"Plot: {name} - No legend found on an axis")

# Test Sun Path - Dark Mode
fig_sun_dark = place.plot_sun_path(dark_mode_override=True).figure
check_legend(fig_sun_dark, "Sun Path Dark")

# Test Moon Path - Dark Mode
fig_moon_dark = place.plot_moon_path(dark_mode_override=True).figure
check_legend(fig_moon_dark, "Moon Path Dark")
