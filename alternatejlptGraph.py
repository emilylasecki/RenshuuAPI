import pandas as pd
from matplotlib import pyplot as plt
import json


f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

YAxis = ['N5 Vocab', 'N5 Kanji', 'N5 Grammar', 'N5 Sentences', '']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5'], 0]

# Figure Size
fig, ax = plt.subplots(figsize =(9, 4))

# Horizontal Bar Plot
ax.barh(YAxis, XAxis)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
#ax.xaxis.set_tick_params(pad = 5)
#ax.yaxis.set_tick_params(pad = 10)

# Add x, y gridlines
"""ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)"""

# Show top values 
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')



# Show Plot
plt.show()