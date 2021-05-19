exec(s:='''
from matplotlib.pyplot import figure, show
from PIL import ImageDraw
from numpy import array, linspace, meshgrid, pi, cos, sin
def f(x):
    w,h=(len(max(x.split("\\n"),key=len))+1)*6,(x.count("\\n")+1)*15
    im=ImageDraw.Image.new("L",(w,h))
    ImageDraw.Draw(im).text((0,0),x,fill=1)
    THETA,Z=meshgrid(linspace(0,2*pi,w),linspace(0,1,h))
    X,Y,C=cos(THETA),sin(THETA),[[[i]*3 for i in j] for j in array(im)[::-1]]
    subplot=figure().add_subplot(projection="3d")
    subplot.plot_surface(X,Y,Z,rstride=1,cstride=1,facecolors=C)
    show()
separated=("exec(s:=''%r'')"%s).split("\\\\\\\\n")
f("\\\\\\\\n".join([i.replace("\\\\n", "\\n") for i in separated]))''')
