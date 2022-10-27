import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from peeters_piper.peeter_piper import piper
from peeter_piper import piper

#filename = "GW20130314-0057-s02_additional_field.csv"
filename = "BV01K_additional_field.csv"

df = pd.read_csv(filename)

# Plot example data
# Piper plot
figureTitle = "BV01K Well (ATES Warm Well)"
fig = plt.figure()
markers = [ "*","s","X", "^", "v", "o", "+", "8", "p",
           "P", "h", "H", "x", "X", "d", "D", "<", ">"]
arrays = []
for i, (label, group_df) in enumerate(df.groupby("additional-field")):
    arr = group_df.iloc[:, 2:10].values
    arrays.append(
        [
            arr,
            {
                "label": label,
                "marker": markers[i],
                "edgecolor": "k",
                "linewidth": 0.5,
                "facecolor": "none",
            },
        ]
    )

rgb = piper(arrays, figureTitle, use_color=True, fig=fig)
plt.legend()
#fig.savefig(filename + "_piper_plot.png", dpi=120)
fig.savefig(filename + "_piper_plot1.png", dpi=120)