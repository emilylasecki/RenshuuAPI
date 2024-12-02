import matplotlib.pyplot as plt
import json
import pandas as pd


f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

YAxis = ['Vocab', 'Kanji', 'Grammar', 'Sentences']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5']]
XAxis2 = [profile['level_progress_percs']['vocab']['n4'], profile['level_progress_percs']['kanji']['n4'],profile['level_progress_percs']['grammar']['n4'],profile['level_progress_percs']['sent']['n4']]
XAxis3 = [profile['level_progress_percs']['vocab']['n3'], profile['level_progress_percs']['kanji']['n3'],profile['level_progress_percs']['grammar']['n3'],profile['level_progress_percs']['sent']['n3']]
XAxis4 = [profile['level_progress_percs']['vocab']['n2'], profile['level_progress_percs']['kanji']['n2'],profile['level_progress_percs']['grammar']['n2'],profile['level_progress_percs']['sent']['n2']]
XAxis5 = [profile['level_progress_percs']['vocab']['n1'], profile['level_progress_percs']['kanji']['n1'],profile['level_progress_percs']['grammar']['n1'],profile['level_progress_percs']['sent']['n1']]

fid, axs = plt.subplots(5, sharex=True)

bar0 = axs[0].barh(YAxis, XAxis)
bar1 = axs[1].barh(YAxis, XAxis2)
bar2 = axs[2].barh(YAxis, XAxis3)
bar3 = axs[3].barh(YAxis, XAxis4)
bar4 = axs[4].barh(YAxis, XAxis5)

fid.set_size_inches(7,7)

#axs[4] = plt.sharex(axs[0])

axs[0].bar_label(bar0, labels=[f"{x:.0f}%" for x in bar0.datavalues], color='white', padding = 3)
axs[1].bar_label(bar1, labels=[f"{x:.0f}%" for x in bar1.datavalues], color='white', padding=3)
axs[2].bar_label(bar2, labels=[f"{x:.0f}%" for x in bar2.datavalues], color='white', padding=3)
axs[3].bar_label(bar3, labels=[f"{x:.0f}%" for x in bar3.datavalues], color='white', padding=3)
axs[4].bar_label(bar4, labels=[f"{x:.0f}%" for x in bar4.datavalues], color='white', padding=3)

axs[0].invert_yaxis()
axs[1].invert_yaxis()
axs[2].invert_yaxis()
axs[3].invert_yaxis()
axs[4].invert_yaxis()



axs[0].barh(YAxis, XAxis)
axs[1].barh(YAxis, XAxis2)
axs[2].barh(YAxis, XAxis3)
axs[3].barh(YAxis, XAxis4)
axs[4].barh(YAxis, XAxis5)

for s in ['top', 'bottom', 'left', 'right']:
    axs[0].spines[s].set_visible(False)
    axs[1].spines[s].set_visible(False)
    axs[2].spines[s].set_visible(False)
    axs[3].spines[s].set_visible(False)
    axs[4].spines[s].set_visible(False)

axs[0].set_facecolor('#201c1c')
axs[1].set_facecolor('#201c1c')
axs[2].set_facecolor('#201c1c')
axs[3].set_facecolor('#201c1c')
axs[4].set_facecolor('#201c1c')
fid.patch.set_facecolor('#201c1c')

"""for i in axs[4].patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2))+ '%',
             fontsize = 10, fontweight ='bold',
             color ='white') # add percent label here
    
for i in axs[0].patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2))+ '%',
             fontsize = 10, fontweight ='bold',
             color ='white') # add percent label here"""
    
axs[0].set_title('N5', color='white')
axs[1].set_title('N4', color='white')
axs[2].set_title('N3', color='white')
axs[3].set_title('N2', color='white')
axs[4].set_title('N1', color='white')

#for i, v in enumerate(XAxis):
   # axs[0].text(i, v, f'{v:.1f}%', ha='right', va='bottom', color='white')

axs[1].xaxis.set_ticks_position('none')
axs[1].yaxis.set_ticks_position('none')
#axs[1].set_xticklabels('none')
axs[1].set_yticklabels(YAxis, fontsize=10, color='white')
axs[0].xaxis.set_ticks_position('none')
axs[0].yaxis.set_ticks_position('none')
#axs[0].set_xticklabels('none')
axs[0].set_yticklabels(YAxis, fontsize=10, color='white')
axs[2].xaxis.set_ticks_position('none')
axs[2].yaxis.set_ticks_position('none')
#axs[2].set_xticklabels('none')
axs[2].set_yticklabels(YAxis, fontsize=10, color='white')
axs[3].xaxis.set_ticks_position('none')
axs[3].yaxis.set_ticks_position('none')
#axs[3].set_xticklabels('none')
axs[3].set_yticklabels(YAxis, fontsize=10, color='white')
axs[4].xaxis.set_ticks_position('none')
axs[4].yaxis.set_ticks_position('none')
#axs[4].set_xticklabels('none')
axs[4].set_yticklabels(YAxis, fontsize=10, color='white')
axs[4].axes.get_xaxis().set_visible(False)

colorsValue = []
for value in XAxis:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
axs[0].barh(YAxis, XAxis, color = colorsValue)
colorsValue = []
for value in XAxis2:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
axs[1].barh(YAxis, XAxis2, color = colorsValue)
colorsValue = []
for value in XAxis3:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
axs[2].barh(YAxis, XAxis3, color = colorsValue)
colorsValue = []
for value in XAxis4:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
axs[3].barh(YAxis, XAxis4, color = colorsValue)
colorsValue =[]
for value in XAxis5:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
axs[4].barh(YAxis, XAxis5, color = colorsValue)

#axs[0].barh(YAxis, XAxis, color = colorsValue)

plt.savefig('graph.png', bbox_inches='tight')
plt.show()