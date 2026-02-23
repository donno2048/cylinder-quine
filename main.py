exec(s:='''
from tqdm import tqdm
from PIL import ImageDraw, ImageFont
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation
from numpy import array,linspace as lin,meshgrid,pi,sin,newaxis
def f(x,font=ImageFont.load_default(size=15),S=2,F=100):
    X,t=x.split("\\n"),tqdm(total=F)
    w,h=int(max(map(font.getlength,X))/.7),len(X)*(font.size+S)
    im,fig,h=ImageDraw.Image.new("L",(w,h+S)),figure(),h+S
    ImageDraw.Draw(im).text((0,0),x,fill=1,font=font,spacing=S)
    def update(fr, subplot, colors):
        for c in subplot.collections: c.remove()
        subplot.set_box_aspect((1, 1, 3))
        T,Z=meshgrid(lin(2*pi*fr/F,(1+fr/F)*2*pi,w),lin(0,1,h))
        return subplot.plot_surface(sin(pi / 2-T), sin(T), - Z,
                        rstride=1,cstride=1,facecolors=colors),
    FuncAnimation(fig, update, frames = F, interval = 50, fargs
                            =(fig.add_subplot(projection="3d"),
                   (1-array(im))[...,newaxis].repeat(3,axis=-1)
             ),cache_frame_data=False).save("main.gif",dpi=400,
                       progress_callback=lambda *_:t.update(1))
sep=("exec(s:=\'\'%r\'\')"%s).split("\\\\\\\\n")
f("\\\\\\\\n".join(i.replace("\\\\n", "\\n") for i in sep))''')
