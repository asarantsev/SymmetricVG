import numpy

sigma = numpy.array([[0.5, numpy.sqrt(2), 4.5],
                     [numpy.sqrt(2), 5, 27/numpy.sqrt(2)],
                     [4.5, 27/numpy.sqrt(2), 171/2]])

def cov(u):
    return numpy.dot(numpy.transpose(u), numpy.dot(sigma, u))

# used to compute limiting variance for a hat first modified MME
v = numpy.array([-3*numpy.sqrt(2), -3, numpy.sqrt(2)])
print('variance for a first modified MME = ', cov(v))
# used to compute limiting variance for b hat first modified MME
w = numpy.array([-3*numpy.sqrt(2), -2, numpy.sqrt(2)])
print('variance for b first modified MME = ', cov(w))
# used to compute limiting variance for a hat second modified MME
y = (numpy.log(4) - 1.5)**(-1)*numpy.array([-numpy.sqrt(2), 0.5, 0])
print('variance for a second modified MME = ', cov(y))
# used to compute limiting variance for b hat second modified MME
z = numpy.array([numpy.sqrt(2), 1 - 1/(numpy.log(4) - 1.5), 0])
print('variance for b second modified MME = ', cov(z))



# def amoment(delta, m):
#     return 2**(0.5*m)*math.pi**(-0.5)*math.gamma(0.5*(m+1))*math.gamma(1 + 0.5*m)
# 
# def covmoment(delta, m1, m2):
#     return amoment(delta, m1+m2) - amoment(delta, m1) * amoment(delta, m2)
# 
# def var(delta):
#     Sigma = numpy.array([[covmoment(delta, 1, 1), covmoment(delta, 1, 2), covmoment(delta, 1, 3)],
#                         [covmoment(delta, 2, 1), covmoment(delta, 2, 2), covmoment(delta, 2, 3)],
#                         [covmoment(delta, 3, 1), covmoment(delta, 3, 2), covmoment(delta, 3, 3)]])
#     vector = numpy.array([-amoment(delta, 3)/(amoment(delta, 2)*amoment(delta, 1)**2),
#                           -amoment(delta, 3)/(amoment(delta, 1)*amoment(delta, 2)**2),
#                           1/(amoment(delta, 1)*amoment(delta, 2))])
#     variance = numpy.dot(numpy.transpose(vector), numpy.dot(Sigma, vector))
#     return 4*variance*((delta*(delta+1))**(-2))
# 
# allDelta = numpy.arange(0.01, 2, 0.01)
# allVar = [var(delta) for delta in allDelta]
# pyplot.plot(allDelta, allVar)
# pyplot.show()

