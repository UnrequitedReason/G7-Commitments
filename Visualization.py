# Import necessary libraries

# Import data manipulation libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Import visualization libraries
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rcParams
import matplotlib.patches as mpatches
%matplotlib inline
sns.set_style('white')

# Make area coloured chart visualization

# Read in data
df3 = pd.read_csv('G7 Commitments.csv')

# Format graph colour
blue = '#1F77B4'
orange = '#FF7F0E'
green = '#2CA02C'
red = '#D62728'
purple = '#9467BD'
brown = '#8C564B'
pink = '#E377C2'
gray = '#7F7F7F'
pgreen = '#BCBD22'
pblue = '#17BECF'
dblue = '#12476d'
dorange = '#cc5f00'
dgreen = '#1b641b'
dred = '#971c1c'
dpurple = '#673e8e'
dbrown = '#53332d'
dpink = '#941e71'
dgray = '#262626'
lblue = '#A3B2F0'
lorange = '#FFD268'
lgreen = '#87de87'
lred = '#E35734'
lgray = '#CCCCCC'
cols = {'Development': blue, 'Energy': lorange, 'Health': lred, 'Terrorism': dgray, 'Trade': orange, 'Nonproliferation':
         lblue, 'Crime and Corruption': dred, 'Macroeconomic policy': dgreen, 'Food & Agriculture': purple, 'Environment':
         green, 'Gender': pink, 'Financial regulation': dpink, 'Education': dorange, 'ICT': dpurple, 'Labour & Employment':
         dbrown, 'Good governance': pblue, 'Peace & security': lgray, 'East-West Relations (Russia)': red, 'Drugs':
         brown, 'IFI/UN reform': lgreen, 'Microeconomic policy': pgreen, 'Democracy & human rights': dblue, 'Other': gray}
color = [cols[i] for i in list(df3.columns)]

sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 5})
plot = df3.plot.area(stacked=True, figsize=(30,15), title=False, legend=False, color=color)
sns.set_style('white')
plot.set_ylabel('')
plot.set_xlabel('')
plt.ylim(0,100)
sns.despine()
handles, labels = plot.get_legend_handles_labels()

plt.savefig('G7 Commitments by Year.png', bbox_inches='tight')
