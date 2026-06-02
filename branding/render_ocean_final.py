# -*- coding: utf-8 -*-
"""Ocean World icon: tropical turquoise sea + sand islet + palm + foam. Style matches sky/mountain."""
import os
from PIL import Image, ImageDraw
SS=4; MASTER=512; N=MASTER*SS
HERE=os.path.dirname(__file__); RES=os.path.abspath(os.path.join(HERE,"..","src","main","resources"))
SKY=(151,213,240); SEA=(28,170,205); SEA_DK=(16,116,150); SAND=(232,216,168); SAND_DK=(204,186,140)
FOAM=(240,248,252); PALM=(80,158,74); PALM_DK=(60,128,56); SUN=(255,240,176)
def render():
    img=Image.new("RGB",(N,N),SKY); d=ImageDraw.Draw(img)
    wl=int(N*0.40)                                  # waterline
    d.ellipse([int(N*0.74),int(N*0.08),int(N*0.92),int(N*0.26)],fill=SUN)  # sun
    d.rectangle([0,wl,N,N],fill=SEA)                # sea
    d.rectangle([0,int(N*0.74),N,N],fill=SEA_DK)    # deeper band
    # sand islet (mound) centered on waterline
    iw=int(N*0.46); cx=int(N*0.50); top=int(wl-N*0.05)
    d.ellipse([cx-iw//2,top,cx+iw//2,top+int(N*0.30)],fill=SAND)
    d.ellipse([cx-iw//2,top+int(N*0.12),cx+iw//2,top+int(N*0.30)],fill=SAND_DK)
    d.ellipse([cx-iw//2,top,cx+iw//2,top+int(N*0.14)],fill=SAND)
    # palm tuft
    px=cx; py=top+int(N*0.02)
    d.rectangle([px-int(N*0.012),py-int(N*0.10),px+int(N*0.012),py],fill=PALM_DK)
    for ang in (-1,-0.4,0.4,1):
        d.polygon([(px,py-int(N*0.10)),(px+int(ang*N*0.13),py-int(N*0.16)),(px+int(ang*N*0.10),py-int(N*0.09))],fill=PALM)
    # foam strokes
    for (fx,fy,fw) in [(0.16,0.52,0.16),(0.78,0.50,0.14),(0.30,0.66,0.18),(0.66,0.68,0.16)]:
        d.ellipse([int(N*fx),int(N*fy),int(N*(fx+fw)),int(N*(fy+0.03))],outline=FOAM,width=int(SS*5))
    return img
m=render().resize((MASTER,MASTER),Image.LANCZOS)
m.save(os.path.join(HERE,"ocean_world_icon_512.png"))
for sz in (256,128,64): m.resize((sz,sz),Image.LANCZOS).save(os.path.join(HERE,f"ocean_world_icon_{sz}.png"))
os.makedirs(RES,exist_ok=True); m.resize((256,256),Image.LANCZOS).save(os.path.join(RES,"ocean_world.png"))
print("ocean icon written")
