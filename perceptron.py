import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# X holds N-by-d samples
#   - N is number of samples
#   - d is dimension
X = np.ndarray((0,2))

# Y holds N labels of -1 or 1
Y = np.array([])

# w is the d-dimensional estimator
w = np.array((0,0))

# Set up the plotting
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()
plt.axis([-4,4,-4,4])
ax.axis([-4,4,-4,4])

while (True):
    # Get a new point from the user
    # Ordinarily will be read from some large file
    x1, x2, y = input("Enter a point and label: (x y) +/-1\n").split()
    #x1, x2, y = input("Enter a point and label: x x x\n") # for python 2.7
    x1, x2, y = [float(x1), float(x2), float(y)]

    # Make input into an np.array and add to the data set
    x = np.array((x1,x2))
    X = np.append(X, [x], axis=0)
    Y = np.append(Y, y)

    # perceptron update step
    if np.sign(np.dot(x,w)) != y:
        # if x is of class -1, subtract, otherwise add
        w = w + y*x

    # Update the plot
    ax.clear()
    p_x, p_y = (X[np.where(Y==1)]).T
    ax.plot(p_x, p_y, 'or')
    p_x, p_y = (X[np.where(Y==-1)]).T
    ax.plot(p_x, p_y, 'ob')
    ax.plot([-4,4],[4*w[0]/w[1],-4*w[0]/w[1]], 'k-')
    ax.axis([-4,4,-4,4])
    fig.canvas.draw()

    # Print some info to stdout
    print("Current w: ")
    print(w)
    print("Current X: ")
    print(X)
    print("Current Y: ")
    print(Y)

    im_x = np.arange(-4,4,0.05)
    im_y = np.arange(-4,4,0.05)
    im_X, im_Y = np.meshgrid(im_x, im_y)

    im_Z = np.zeros(im_X.shape)

    # do zipping and mapping for this
    for i in range(0,im_Z.shape[0]):
        for j in range(0,im_Z.shape[1]):
            # swap i and j to compesate for pixel layout
            #vals = np.append(vals, [forward_step(w_in, w_out, w_hidden, [step[j] step[i]])])
            res = np.dot(np.array([im_y[j], im_x[i]]), w)
            im_Z[i][j] = res

    # draw the old one

    #fig = plt.figure()

    levels = np.arange(-2.0, 1.601, 0.4)
    norm = cm.colors.Normalize(vmax=abs(im_Z).max(), vmin=-abs(im_Z).max())
    cmap = cm.PRGn

    cset1 = plt.contourf(im_X, im_Y, im_Z, levels, norm=norm, cmap=cm.get_cmap(cmap, len(levels) - 1))
    #plt.show()
    fig.canvas.draw()

# At this stage, we say that w has been "trained" to fit the training data
# To use w to make a prediction, take a new point x and compute x*w, returning
# the sign of the result.
# To measure the quality of the estimator, we would run prediction (without update)
# over part of the data that was *not* used for training, and see how many it gets
# correct.
