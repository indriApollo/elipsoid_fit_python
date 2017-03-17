import numpy as np
from ellipsoid_fit import ellipsoid_fit as ellipsoid_fit, data_regularize
import argparse


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Get center of each axis and transformation')
    parser.add_argument('filename')
    args = parser.parse_args()

    data = np.loadtxt(args.filename)
    data2 = data_regularize(data)

    center, radii, evecs, v = ellipsoid_fit(data2)

    a,b,c = radii
    r = (a*b*c)**(1./3.)
    D = np.array([[r/a,0.,0.],[0.,r/b,0.],[0.,0.,r/c]])
    TR = evecs.dot(D).dot(evecs.T)
    
    print(center)
    print('transformation:')
    print(TR)
    
    np.savetxt('mag_cal_ellipsoid.txt', np.vstack((center.T, TR)))

