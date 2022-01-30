from distutils.command.upload import upload
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image
import os


# def spline(image_name, 
#            t=[0.,   0. ,  0.,  0.,   0.25, 0.5,  0.75, 1.,   1.,   1.,   1.  ],
#            ctr=[(839 , 216), (588, 205), (427, 8), (304, 159),(265, 100), (203, 175),(0,135)],
#            k=3):
def spline(image_name, t, ctr, k):
    # ctr =np.array( [(839 , 216), (588, 205), (427, 8), (304, 159),(265, 100), (203, 175),(0,135)])
    ctr = np.array(ctr)
    x=ctr[:,0]
    y=ctr[:,1]
    im = Image.open(os.getcwd()+ "/static/uploads/"+image_name)
    print(os.getcwd())
    # uncomment both lines for a closed curve
    #x=np.append(x,[x[0]])  
    #y=np.append(y,[y[0]])

    l=len(x)  

    # t=np.linspace(0,1,l-2,endpoint=True)
    # t=np.append([0,0,0],t)
    # t=np.append(t,[1,1,1])
    # print(t)
    # [0.   0.   0.   0.   0.25 0.5  0.75 1.   1.   1.   1.  ]
    tck=[t,[x,y],k]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    # real size of image
    # dpi = mpl.rcParams['figure.dpi']
    dpi = 80
    height = im.height
    width = im.width
   

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(im)
    # plt.imshow(im)
    ax.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='yellow')
    #plt.plot(x,y,'ro',label='Control points only')
    ax.plot(out[0],out[1],'r',linewidth=2.0,label='B-spline curve')
    # ax.legend(loc='best')
    # plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    # plt.title('Cubic B-spline curve evaluation')
    plt.axis('off')
    plt.savefig('static/uploads/'+image_name, bbox_inches='tight', pad_inches=0) 
    # plt.show()



# if __name__ == "__main__":
#     spline()