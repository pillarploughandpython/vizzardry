
Colors:
Light blue: #b3c4d6
Dark blue: #517ca7
Gray: #767682

pylab.legend !!!

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
fig, ax1 = plt.subplots()
ax1.plot(x, y)
ax1.set_title('bottom-left spines')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
alpha=0.5)
ax1.set_axisbelow(True)

plt.title('Développés et fabriqués')
plt.xlabel("réactivité nous permettent d'être sélectionnés et adoptés")
plt.ylabel('André was here!')
plt.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)

txt = '''
    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.'''
fig.text(.1,.1,txt)

plt.show()


# A yummy Donut Chart

# Basic simpleton of a bar chart

# Beyond the Horizonzal Bar

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Chinas Wirtschaftswachstum')
plt.tick_params(bottom="off", top="off")
plt.show()

# Line up of a line chart

"""
Only horizontal grid

ax.xaxis.grid(False)
"""

c1 = '#f4666c'
c2 = '#ed679f'
c3 = '#edb567'
c4 = '#e2ed67'
c5 = '#67e2ed'
c6 = '#679fed'

def make_pie(sizes, text,colors,labels):
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    ax.axis('equal')
    width = 0.35
    kwargs = dict(colors=[c1, c2, c3, c4, c5, c6], startangle=180, autopct='%1.1f%%')
    outside, _, _ = ax.pie(sizes, radius=1, pctdistance=1-width/2,labels=labels,**kwargs)
    plt.setp( outside, width=width, edgecolor='white')
    kwargs = dict(size=20, fontweight='bold', va='center')
    ax.text(0, 0, text, ha='center', **kwargs)
    plt.show()

make_pie([29,29,6,4,26,6], "Herkunft\nenglischer\nWörter",[c1,c2,c3,c4,c5,c6],['Latein','Französisch','Griechisch','Eigennamen','Germanisch','Rest'])
