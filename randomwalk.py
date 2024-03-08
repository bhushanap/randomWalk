import numpy as np
np.set_printoptions(precision=2)

steps = 20
start = 0
iterations = 1000
sd = 30
# rr = 1
# up = 1
# down = - 1


resu = 25
startu = 5
endu = 50

resd = 25
startd = 5
endd = 50



ups = np.linspace(startu,endu,resu) # [5,10,15...50]
downs = -np.linspace(startd,endd,resd) #[-5,-10...-50]
# print(ups,downs)
returns = [[None for down in range(resd)] for up in range(resu)]
ratios  = [[None for down in range(resd)] for up in range(resu)]
wins  = [[0 for down in range(resd)] for up in range(resu)]
inconclusives  = [[0 for down in range(resd)] for up in range(resu)]

for i,up in enumerate(ups):
    for j,down in enumerate(downs):
        win = 0
        lose = 0
        inconclusive = 0
        expectation = 0
        
        for iteration in range(iterations):
            position = start
            conclude = False
            for step in range(steps):
                deviate = np.random.normal()*sd
                position += deviate
                if position > up:
                    win+=1
                    expectation += up
                    conclude = True
                    break
                if position < down:
                    lose+=1
                    expectation += down
                    conclude = True
                    break
            if not conclude:
                inconclusive += 1
                expectation += position
            returns[i][j] = expectation/iterations#(up,down,win,win/iterations*100, lose/iterations*100, inconclusive/iterations*100, expectation)
            ratios[i][j] = -up/down
            wins[i][j] = win/iterations*100
            inconclusives[i][j] = inconclusive/iterations*100

returns = np.array(returns)
ratios = np.array(ratios)
wins = np.array(wins)
inconclusives = np.array(inconclusives)
print(ratios)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.colors import LogNorm

# Create subplots for side-by-side plotting
fig, axes = plt.subplots(1, 4, figsize=(12, 12))

# Plot the first array (returns)
norm_returns = Normalize(vmin=np.min(returns), vmax=np.max(returns))
im_returns = axes[0].imshow(returns, cmap='coolwarm', interpolation='nearest', norm=norm_returns)
axes[0].set_title('Returns')
cbar_returns = fig.colorbar(im_returns, ax=axes[0], orientation='vertical')

# Plot the second array (ratios)
norm_ratios = LogNorm(vmin=np.min(ratios), vmax=np.max(ratios))
im_ratios = axes[1].imshow(ratios, cmap='viridis', interpolation='nearest', norm=norm_ratios)
axes[1].set_title('Reward Risk Ratios')
cbar_ratios = fig.colorbar(im_ratios, ax=axes[1], orientation='vertical')

# Plot the second array (wins)
norm_wins = Normalize(vmin=0, vmax=100)
im_wins = axes[2].imshow(wins, cmap='RdYlGn', interpolation='nearest', norm=norm_wins)
axes[2].set_title('Win rate')
cbar_ratios = fig.colorbar(im_wins, ax=axes[2], orientation='vertical')

# Plot the second array (wins)
norm_ins = Normalize(vmin=0, vmax=100)
im_ins = axes[3].imshow(inconclusives, cmap='RdYlGn', interpolation='nearest', norm=norm_ins)
axes[3].set_title('Inconclusive results')
cbar_ratios = fig.colorbar(im_ins, ax=axes[3], orientation='vertical')

plt.show()


    