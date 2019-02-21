import math
import numpy

n = 10
Ox = numpy.zeros((n, 1))
Red = numpy.zeros((n, 1))
S = numpy.zeros((n, 1))
P = numpy.zeros((n, 1))

k1 = 1
k2 = 1
k3 = 1

for i in range(0, n):
    Red[i] = 100
    S[i] = 10000

E = 3
dt = 0.01
D = 0.00001
for i in range(0, 10000):
    if (i > 5000):
        E = E + (6. / 5000)
    else:
        E = E - (6. / 5000)
    #print(E)
    new_ox = numpy.array(Ox)
    new_red = numpy.array(Red)
    new_s = numpy.array(S)
    new_p = numpy.array(P)

    p = numpy.exp(E)
    q = Ox[0] + Red[0]
    new_ox[0] = q - (q / (p + 1))
    new_red[0] = q / (p+1)
    I = Red[0] - new_red[0]

    

    # And now change other things
    #
    # Diffusion;
    for p in range(0, n-2):
        diff_ox = D * (Ox[p] - Ox[p+1]) * Ox[p]
        diff_red = D * (Red[p] - Red[p+1]) * Red[p]
        diff_s = D * (S[p] - S[p+1]) * S[p]
        diff_p = D * (P[p] - P[p+1]) * P[p]
        new_ox[p] = new_ox[p] - diff_ox
        new_ox[p+1] = new_ox[p+1] + diff_ox
        new_red[p] = new_red[p] - diff_red
        new_red[p+1] = new_red[p+1] + diff_red
        new_s[p] = new_s[p] - diff_s
        new_s[p+1] = new_s[p+1] + diff_s
        new_p[p] = new_p[p] - diff_p
        new_p[p+1] = new_p[p] + diff_p

    # Reaction;
    #for p in range(0, n-1):
     #   if (Red[p] > 0 and S[p] > 0):
      #      dP = dt * k3 * Red[p] * S[p]
       #     new_ox[p] = new_ox[p] + dP
        #    new_red[p] = new_red[p] - dP
         #   new_s[p] = new_s[p] - dP
          #  new_p[p] = new_p[p] + dP

    # Calculate current for each position
    currents = numpy.zeros((n, 1))
    for p in range(0, n - 1):
        currents[p] = Red[p] - new_red[p]
        
    Ox = numpy.array(new_ox)
    Red = numpy.array(new_red)
    S = numpy.array(new_s)
    P = numpy.array(new_p)

    print("%f, %f, %f, %f, %f, %f" % (currents[0], E, Ox[0], Red[0], S[0], P[0]))
    if (i % 1 == 0):
        with open(str(i)+".file", "w") as f:
            for l in range(0, n - 1):
                f.write("%d, %f, %f, %f, %f, %f\n" % (l, Ox[l], Red[l], S[l], P[l], currents[l]))


#print(Ox[1])
