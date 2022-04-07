
Meet
New meeting
Join a meeting
Hangouts

34 of 40
full completed code

Sai Ram <sairamcse01@gmail.com>
Attachments
Sun, Jan 27, 2019, 1:19 PM
to P.S.

full completed but only one in this code i have written the are two functions databasefunc and userfunc from databasefunc the subarea pixelvalues(s1[i],s2[i],......) should be passed to userfunc 
then it ll be complete 
Attachments area

Sai Ram <sairamcse01@gmail.com>
Sun, Jan 27, 2019, 5:07 PM
to P.S.

just above code create a class i think

from PIL import Image
import os
import matplotlib
import os.path
from os import path
q=[0,0,0,0,0,0,0,0,0,0]
u=[0,0,0,0,0,0,0,0,0,0]
t=[0,0,0,0,0,0,0,0,0,0]
l=[0,0,0,0,0,0,0,0,0,0]
r=[0,0,0,0,0,0,0,0,0,0]
u=[0,0,0,0,0,0,0,0,0,0]
d=[0,0,0,0,0,0,0,0,0,0]
a=[0,0,0,0,0,0,0,0,0,0]
s1q=[0,0,0,0,0,0,0,0,0,0]
s2q=[0,0,0,0,0,0,0,0,0,0]
s3q=[0,0,0,0,0,0,0,0,0,0]
s4q=[0,0,0,0,0,0,0,0,0,0]
s5q=[0,0,0,0,0,0,0,0,0,0]
s6q=[0,0,0,0,0,0,0,0,0,0]
s7q=[0,0,0,0,0,0,0,0,0,0]
s8q=[0,0,0,0,0,0,0,0,0,0]
s9q=[0,0,0,0,0,0,0,0,0,0]
s10q=[0,0,0,0,0,0,0,0,0,0]
saq=[0,0,0,0,0,0,0,0,0,0]
sbq=[0,0,0,0,0,0,0,0,0,0]
scq=[0,0,0,0,0,0,0,0,0,0]
sdq=[0,0,0,0,0,0,0,0,0,0]
seq=[0,0,0,0,0,0,0,0,0,0]
sfq=[0,0,0,0,0,0,0,0,0,0]
sgq=[0,0,0,0,0,0,0,0,0,0]
swq=[0,0,0,0,0,0,0,0,0,0]
suq=[0,0,0,0,0,0,0,0,0,0]
soq=[0,0,0,0,0,0,0,0,0,0]
srq=[0,0,0,0,0,0,0,0,0,0]
s123q=[0,0,0,0,0,0,0,0,0,0]
s086q=[0,0,0,0,0,0,0,0,0,0]
s093q=[0,0,0,0,0,0,0,0,0,0]
s1234q=[0,0,0,0,0,0,0,0,0,0]
s0866q=[0,0,0,0,0,0,0,0,0,0]
s0933q=[0,0,0,0,0,0,0,0,0,0]
s09331q=[0,0,0,0,0,0,0,0,0,0]
uq=[0,0,0,0,0,0,0,0,0,0]
dq=[0,0,0,0,0,0,0,0,0,0]
lq=[0,0,0,0,0,0,0,0,0,0]
rq=[0,0,0,0,0,0,0,0,0,0]
user=0
def databasefunc():
     print("enter the user no")
     user=input()
     i=0
     os.mkdir(user)
     while i<10:
          print("enter name of image to be cropped")
          image=Image.open(input())
          #0kimage.show()
          image = image.resize((600, 300))
          image.show()
          box=(400,150,580,280)
          image = image.crop(box)
          print("enter name of cropped image")
          x=input()
          gray = image.convert('L')
          image = gray.point(lambda x: 0 if x<128 else 255, '1')
          os.chdir(user)
          image.save(x)
          image=Image.open(x)
          width,height=image.size
          a[i]=width/height
          cx=width/2
          cy=height/2
          q[i]=sum(image.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          t[i]=height*width
          print("size of image in width and height")
          print(image.size)
          print("centre point of x is")
          print(cx)
          print("centre point of y is")
          print(cy)
          print("total pixels are")
          print(t[i])
          print("aspect ratio is")
          print(a[i])
          print("black pixels in image is")
          print(q[i])
          image.show()
          image=Image.open(x)
          box=(0,0,cx,height)
          im = image.crop(box)
          im.save('-1.jpg')
          im=Image.open('-1.jpg')
          l[i]=sum(im.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("left pixels are")
          print(l[i])
          os.remove('-1.jpg')
          image=Image.open(x)
          box=(cx,0,width,height)
          im1 = image.crop(box)
          im1.save('-12.jpg')
          im1=Image.open('-12.jpg')
          r[i]=sum(im1.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("right pixels are")
          print(r[i])
          os.remove('-12.jpg')
          image=Image.open(x)
          box=(0,0,width,cy)
          im2 = image.crop(box)
          im2.save('-13.jpg')
          im2=Image.open('-13.jpg')
          u[i]=sum(im2.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("up pixels are")
          print(u[i])
          os.remove('-13.jpg')
          image=Image.open(x)
          box=(0,cy,width,height)
          im3 = image.crop(box)
          im3.save('-14.jpg')
          im3=Image.open('-14.jpg')
          d[i]=sum(im3.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("down pixels are")
          print(d[i])
          os.remove('-14.jpg')
          image=Image.open(x)
          box=(0,0,cx,cy)
          im4 = image.crop(box)
          im4.save('-15.jpg')
          im4=Image.open('-15.jpg')
          s1=[0,0,0,0,0,0,0,0,0,0]
          s1[i]=sum(im4.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea1 pixels are")
          print(s1[i])
          os.remove('-15.jpg')
          image=Image.open(x)
          box=(cx,0,width,cy)
          im5 = image.crop(box)
          im5.save('-16.jpg')
          im5=Image.open('-16.jpg')
          s2=[0,0,0,0,0,0,0,0,0,0]
          s2[i]=sum(im5.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea2 pixels are")
          print(s2[i])
          os.remove('-16.jpg')
          image=Image.open(x)
          box=(0,cy,cx,height)
          im6 = image.crop(box)
          im6.save('-17.jpg')
          im6=Image.open('-17.jpg')
          s3=[0,0,0,0,0,0,0,0,0,0]
          s3[i]=sum(im6.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea3 pixels are")
          print(s3[i])
          os.remove('-17.jpg')
          image=Image.open(x)
          box=(cx,cy,width,height)
          im7 = image.crop(box)
          im7.save('-18.jpg')
          im7=Image.open('-18.jpg')
          s4=[0,0,0,0,0,0,0,0,0,0]
          s4[i]=sum(im7.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea4 pixels are")
          print(s4[i])
          os.remove('-18.jpg')
          image=Image.open(x)
          box=(0,0,cx/2,cy)
          im8 = image.crop(box)
          im8.save('-19.jpg')
          im8=Image.open('-19.jpg')
          s5=[0,0,0,0,0,0,0,0,0,0]
          s5[i]=sum(im8.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea5 pixels are")
          print(s5[i])
          os.remove('-19.jpg')
          image=Image.open(x)
          box=(cx/2,0,cx,cy)
          im9 = image.crop(box)
          im9.save('-20.jpg')
          im9=Image.open('-20.jpg')
          s6=[0,0,0,0,0,0,0,0,0,0]
          s6[i]=sum(im9.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea6 pixels are")
          print(s6[i])
          os.remove('-20.jpg')
          image=Image.open(x)
          box=(cx,0,cx+(cx/2),cy)
          ima = image.crop(box)
          ima.save('-21.jpg')
          ima=Image.open('-21.jpg')
          s7=[0,0,0,0,0,0,0,0,0,0]
          s7[i]=sum(ima.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea7 pixels are")
          print(s7[i])
          os.remove('-21.jpg')
          image=Image.open(x)
          box=(cx/2,0,width,cy)
          imaa = image.crop(box)
          imaa.save('-22.jpg')
          imaa=Image.open('-22.jpg')
          s8=[0,0,0,0,0,0,0,0,0,0]
          s8[i]=sum(imaa.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea8 pixels are")
          print(s8[i])
          os.remove('-22.jpg')
          image=Image.open(x)
          box=(0,cy,cx/2,height)
          imaa1 = image.crop(box)
          imaa1.save('-23.jpg')
          imaa1=Image.open('-23.jpg')
          s9=[0,0,0,0,0,0,0,0,0,0]
          s9[i]=sum(imaa1.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea9 pixels are")
          print(s9[i])
          os.remove('-23.jpg')
          image=Image.open(x)
          box=(cx/2,cy,cx,height)
          imaa2 = image.crop(box)
          imaa2.save('-24.jpg')
          imaa2=Image.open('-24.jpg')
          s10=[0,0,0,0,0,0,0,0,0,0]
          s10[i]=sum(imaa2.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea10 pixels are")
          print(s10[i])
          os.remove('-24.jpg')
          image=Image.open(x)
          box=(cx,cy,cx+(cx/2),height)
          imaa3 = image.crop(box)
          imaa3.save('-25.jpg')
          imaa3=Image.open('-25.jpg')
          sa=[0,0,0,0,0,0,0,0,0,0]
          sa[i]=sum(imaa3.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea11pixels are")
          print(sa[i])
          os.remove('-25.jpg')
          image=Image.open(x)
          box=(cx/2,cy,width,height)
          imaa4= image.crop(box)
          imaa4.save('-26.jpg')
          imaa4=Image.open('-26.jpg')
          sb=[0,0,0,0,0,0,0,0,0,0]
          sb[i]=sum(imaa4.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea12 pixels are")
          print(sb[i])
          os.remove('-26.jpg')
          image=Image.open(x)
          box=(0,0,cx/2,cy/2)
          imaa5= image.crop(box)
          imaa5.save('-27.jpg')
          imaa5=Image.open('-27.jpg')
          sc=[0,0,0,0,0,0,0,0,0,0]
          sc[i]=sum(imaa5.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea13 pixels are")
          print(sc[i])
          os.remove('-27.jpg')
          image=Image.open(x)
          box=(0,cy/2,cx/2,cy)
          imaa6= image.crop(box)
          imaa6.save('-28.jpg')
          imaa6=Image.open('-28.jpg')
          sd=[0,0,0,0,0,0,0,0,0,0]
          sd[i]=sum(imaa6.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea14 pixels are")
          print(sd[i])
          os.remove('-28.jpg')
          image=Image.open(x)
          box=(0,cy,cx/2,cy+(cy/2))
          imaa7= image.crop(box)
          imaa7.save('-29.jpg')
          imaa7=Image.open('-29.jpg')
          se=[0,0,0,0,0,0,0,0,0,0]
          se[i]=sum(imaa7.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea15 pixels are")
          print(se[i])
          os.remove('-29.jpg')
          image=Image.open(x)
          box=(0,cy+(cy/2),cx/2,height)
          imaa8= image.crop(box)
          imaa8.save('-30.jpg')
          imaa8=Image.open('-30.jpg')
          sf=[0,0,0,0,0,0,0,0,0,0]
          sf[i]=sum(imaa8.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea16 pixels are")
          print(sf[i])
          os.remove('-30.jpg')
          image=Image.open(x)
          box=(cx/2,0,cx,cy/2)
          imaa9= image.crop(box)
          imaa9.save('-31.jpg')
          imaa9=Image.open('-31.jpg')
          sg=[0,0,0,0,0,0,0,0,0,0]
          sg[i]=sum(imaa9.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea17 pixels are")
          print(sg[i])
          os.remove('-31.jpg')
          image=Image.open(x)
          box=(cx/2,cy/2,cx,cy)
          imaa10= image.crop(box)
          imaa10.save('-32.jpg')
          imaa10=Image.open('-32.jpg')
          sw=[0,0,0,0,0,0,0,0,0,0]
          sw[i]=sum(imaa10.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea18 pixels are")
          print(sw[i])
          os.remove('-32.jpg')
          image=Image.open(x)
          box=(cx/2,cy,cx,cy+(cy/2))
          imaa11= image.crop(box)
          imaa11.save('-33.jpg')
          imaa11=Image.open('-33.jpg')
          su=[0,0,0,0,0,0,0,0,0,0]
          su[i]=sum(imaa11.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea19 pixels are")
          print(su[i])
          os.remove('-33.jpg')
          image=Image.open(x)
          box=(cx/2,cy+(cy/2),cx,height)
          imaa12= image.crop(box)
          imaa12.save('-34.jpg')
          imaa12=Image.open('-34.jpg')
          so=[0,0,0,0,0,0,0,0,0,0]
          so[i]=sum(imaa12.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea20 pixels are")
          print(so[i])
          os.remove('-34.jpg')
          image=Image.open(x)
          box=(cx,0,cx+(cx/2),cy/2)
          imaa13= image.crop(box)
          imaa13.save('-35.jpg')
          imaa13=Image.open('-35.jpg')
          sr=[0,0,0,0,0,0,0,0,0,0]
          sr[i]=sum(imaa13.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea21 pixels are")
          print(sr[i])
          os.remove('-35.jpg')
          image=Image.open(x)
          box=(cx,cy/2,cx+(cx/2),cy)
          imaa14= image.crop(box)
          imaa14.save('-36.jpg')
          imaa14=Image.open('-36.jpg')
          s123=[0,0,0,0,0,0,0,0,0,0]
          s123[i]=sum(imaa14.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea22 pixels are")
          print(s123[i])
          os.remove('-36.jpg')
          image=Image.open(x)
          box=(cx,cy,cx+(cx/2),cy+(cy/2))
          imaa15= image.crop(box)
          imaa15.save('-37.jpg')
          imaa15=Image.open('-37.jpg')
          s086=[0,0,0,0,0,0,0,0,0,0]
          s086[i]=sum(imaa15.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea23 pixels are")
          print(s086[i])
          os.remove('-37.jpg')
          image=Image.open(x)
          box=(cx,cy+(cy/2),cx+(cx/2),height)
          imaa16= image.crop(box)
          imaa16.save('-38.jpg')
          imaa16=Image.open('-38.jpg')
          s093=[0,0,0,0,0,0,0,0,0,0]
          s093[i]=sum(imaa16.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea24 pixels are")
          print(s093[i])
          os.remove('-38.jpg')
          image=Image.open(x)
          box=(cx+(cx/2),0,width,cy/2)
          imaa17= image.crop(box)
          imaa17.save('-39.jpg')
          imaa17=Image.open('-39.jpg')
          s1234=[0,0,0,0,0,0,0,0,0,0]
          s1234[i]=sum(imaa17.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea25pixels are")
          print(s1234[i])
          os.remove('-39.jpg')
          image=Image.open(x)
          box=(cx+(cx/2),cy/2,width,cy)
          imaa18= image.crop(box)
          imaa18.save('-40.jpg')
          imaa18=Image.open('-40.jpg')
          s0866=[0,0,0,0,0,0,0,0,0,0]
          s0866[i]=sum(imaa18.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea26 pixels are")
          print(s0866[i])
          os.remove('-40.jpg')
          image=Image.open(x)
          box=(cx+(cx/2),cy,width,cy+(cy/2))
          imaa19= image.crop(box)
          imaa19.save('-41.jpg')
          imaa19=Image.open('-41.jpg')
          s0933=[0,0,0,0,0,0,0,0,0,0]
          s0933[i]=sum(imaa19.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea27 pixels are")
          print(s0933[i])
          os.remove('-41.jpg')
          image=Image.open(x)
          box=(cx+(cx/2),cy+(cy/2),width,height)
          imaa20= image.crop(box)
          imaa20.save('-42.jpg')
          imaa20=Image.open('-42.jpg')
          s09331=[0,0,0,0,0,0,0,0,0,0]
          s09331[i]=sum(imaa20.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
          print("subarea28 pixels are")
          print(s09331[i])
          os.remove('-42.jpg')
          os.chdir(os.path.dirname(os.getcwd()))
          i=i+1
def userfunc():
        print("enter the details of image u want to compare")
        print("enter the user no")
        uuser=input()
        print("enter name of image to be cropped")
        image=Image.open(input())
        image.show()
        image = image.resize((600, 300))
        image.show()
        box=(400,150,580,280)
        image = image.crop(box)
        gray = image.convert('L')
        image = gray.point(lambda x: 0 if x<128 else 255, '1')
        os.chdir(uuser)
        print("enter name of image to be saved")
        x=input()
        image.save(x)
        image=Image.open(x)
        width,height=image.size
        ua=width/height
        cx=width/2
        cy=height/2
        uq=sum(image.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        ut=height*width
        print("size of image in width and height")
        print(image.size)
        print("centre point of x is")
        print(cx)
        print("centre point of y is")
        print(cy)
        print("total pixels are")
        print(ut)
        print("aspect ratio is")
        print(ua)
        print("black pixels in image is")
        print(uq)
        image.show()
        box=(0,0,cx,height)
        im = image.crop(box)
        im.save('-1.jpg')
        im=Image.open('-1.jpg')
        ul=sum(im.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("left pixels are")
        print(ul)
        os.remove('-1.jpg')
        image=Image.open(x)
        box=(cx,0,width,height)
        im1 = image.crop(box)
        im1.save('-12.jpg')
        im1=Image.open('-12.jpg')
        ur=sum(im1.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("right pixels are")
        print(ur)
        os.remove('-12.jpg')
        image=Image.open(x)
        box=(0,0,width,cy)
        im2 = image.crop(box)
        im2.save('-13.jpg')
        im2=Image.open('-13.jpg')
        uu=sum(im2.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("up pixels are")
        print(uu)
        os.remove('-13.jpg')
        image=Image.open(x)
        box=(0,cy,width,height)
        im3 = image.crop(box)
        im3.save('-14.jpg')
        im3=Image.open('-14.jpg')
        ud=sum(im3.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("down pixels are")
        print(ud)
        os.remove('-14.jpg')
        image=Image.open(x)
        box=(0,0,cx,cy)
        im4 = image.crop(box)
        im4.save('-15.jpg')
        im4=Image.open('-15.jpg')
        us1=sum(im4.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea1 pixels are")
        print(us1)
        os.remove('-15.jpg')
        image=Image.open(x)
        box=(cx,0,width,cy)
        im5 = image.crop(box)
        im5.save('-16.jpg')
        im5=Image.open('-16.jpg')
        us2=sum(im5.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea2 pixels are")
        print(us2)
        os.remove('-16.jpg')
        image=Image.open(x)
        box=(0,cy,cx,height)
        im6 = image.crop(box)
        im6.save('-17.jpg')
        im6=Image.open('-17.jpg')
        us3=sum(im6.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea3 pixels are")
        print(us3)
        os.remove('-17.jpg')
        image=Image.open(x)
        box=(cx,cy,width,height)
        im7 = image.crop(box)
        im7.save('-18.jpg')
        im7=Image.open('-18.jpg')
        us4=sum(im7.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea4 pixels are")
        print(us4)
        os.remove('-18.jpg')
        image=Image.open(x)
        box=(0,0,cx/2,cy)
        im8 = image.crop(box)
        im8.save('-19.jpg')
        im8=Image.open('-19.jpg')
        us5=sum(im8.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea5 pixels are")
        print(us5)
        os.remove('-19.jpg')
        image=Image.open(x)
        box=(cx/2,0,cx,cy)
        im9 = image.crop(box)
        im9.save('-20.jpg')
        im9=Image.open('-20.jpg')
        us6=sum(im9.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea6 pixels are")
        print(us6)
        os.remove('-20.jpg')
        image=Image.open(x)
        box=(cx,0,cx+(cx/2),cy)
        ima = image.crop(box)
        ima.save('-21.jpg')
        ima=Image.open('-21.jpg')
        us7=sum(ima.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea7 pixels are")
        print(us7)
        os.remove('-21.jpg')
        image=Image.open(x)
        box=(cx/2,0,width,cy)
        imaa = image.crop(box)
        imaa.save('-22.jpg')
        imaa=Image.open('-22.jpg')
        us8=sum(imaa.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea8 pixels are")
        print(us8)
        os.remove('-22.jpg')
        image=Image.open(x)
        box=(0,cy,cx/2,height)
        imaa1 = image.crop(box)
        imaa1.save('-23.jpg')
        imaa1=Image.open('-23.jpg')
        us9=sum(imaa1.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea9 pixels are")
        print(us9)
        os.remove('-23.jpg')
        image=Image.open(x)
        box=(cx/2,cy,cx,height)
        imaa2 = image.crop(box)
        imaa2.save('-24.jpg')
        imaa2=Image.open('-24.jpg')
        us10=sum(imaa2.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea10 pixels are")
        print(us10)
        os.remove('-24.jpg')
        image=Image.open(x)
        box=(cx,cy,cx+(cx/2),height)
        imaa3 = image.crop(box)
        imaa3.save('-25.jpg')
        imaa3=Image.open('-25.jpg')
        usa=sum(imaa3.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea11pixels are")
        print(usa)
        os.remove('-25.jpg')
        image=Image.open(x)
        box=(cx/2,cy,width,height)
        imaa4= image.crop(box)
        imaa4.save('-26.jpg')
        imaa4=Image.open('-26.jpg')
        usb=sum(imaa4.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea12 pixels are")
        print(usb)
        os.remove('-26.jpg')
        image=Image.open(x)
        box=(0,0,cx/2,cy/2)
        imaa5= image.crop(box)
        imaa5.save('-27.jpg')
        imaa5=Image.open('-27.jpg')
        usc=sum(imaa5.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea13 pixels are")
        print(usc)
        os.remove('-27.jpg')
        image=Image.open(x)
        box=(0,cy/2,cx/2,cy)
        imaa6= image.crop(box)
        imaa6.save('-28.jpg')
        imaa6=Image.open('-28.jpg')
        usd=sum(imaa6.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea14 pixels are")
        print(usd)
        os.remove('-28.jpg')
        image=Image.open(x)
        box=(0,cy,cx/2,cy+(cy/2))
        imaa7= image.crop(box)
        imaa7.save('-29.jpg')
        imaa7=Image.open('-29.jpg')
        use=sum(imaa7.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea15 pixels are")
        print(use)
        os.remove('-29.jpg')
        image=Image.open(x)
        box=(0,cy+(cy/2),cx/2,height)
        imaa8= image.crop(box)
        imaa8.save('-30.jpg')
        imaa8=Image.open('-30.jpg')
        usf=sum(imaa8.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea16 pixels are")
        print(usf)
        os.remove('-30.jpg')
        image=Image.open(x)
        box=(cx/2,0,cx,cy/2)
        imaa9= image.crop(box)
        imaa9.save('-31.jpg')
        imaa9=Image.open('-31.jpg')
        usg=sum(imaa9.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea17 pixels are")
        print(usg)
        os.remove('-31.jpg')
        image=Image.open(x)
        box=(cx/2,cy/2,cx,cy)
        imaa10= image.crop(box)
        imaa10.save('-32.jpg')
        imaa10=Image.open('-32.jpg')
        usw=sum(imaa10.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea18 pixels are")
        print(usw)
        os.remove('-32.jpg')
        image=Image.open(x)
        box=(cx/2,cy,cx,cy+(cy/2))
        imaa11= image.crop(box)
        imaa11.save('-33.jpg')
        imaa11=Image.open('-33.jpg')
        usu=sum(imaa11.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea19 pixels are")
        print(usu)
        os.remove('-33.jpg')
        image=Image.open(x)
        box=(cx/2,cy+(cy/2),cx,height)
        imaa12= image.crop(box)
        imaa12.save('-34.jpg')
        imaa12=Image.open('-34.jpg')
        uso=sum(imaa12.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea20 pixels are")
        print(uso)
        os.remove('-34.jpg')
        image=Image.open(x)
        box=(cx,0,cx+(cx/2),cy/2)
        imaa13= image.crop(box)
        imaa13.save('-35.jpg')
        imaa13=Image.open('-35.jpg')
        usr=sum(imaa13.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea21 pixels are")
        print(usr)
        os.remove('-35.jpg')
        image=Image.open(x)
        box=(cx,cy/2,cx+(cx/2),cy)
        imaa14= image.crop(box)
        imaa14.save('-36.jpg')
        imaa14=Image.open('-36.jpg')
        us123=sum(imaa14.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea22 pixels are")
        print(us123)
        os.remove('-36.jpg')
        image=Image.open(x)
        box=(cx,cy,cx+(cx/2),cy+(cy/2))
        imaa15= image.crop(box)
        imaa15.save('-37.jpg')
        imaa15=Image.open('-37.jpg')
        us086=sum(imaa15.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea23 pixels are")
        print(us086)
        os.remove('-37.jpg')
        image=Image.open(x)
        box=(cx,cy+(cy/2),cx+(cx/2),height)
        imaa16= image.crop(box)
        imaa16.save('-38.jpg')
        imaa16=Image.open('-38.jpg')
        us093=sum(imaa16.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea24 pixels are")
        print(us093)
        os.remove('-38.jpg')
        image=Image.open(x)
        box=(cx+(cx/2),0,width,cy/2)
        imaa17= image.crop(box)
        imaa17.save('-39.jpg')
        imaa17=Image.open('-39.jpg')
        us1234=sum(imaa17.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea25pixels are")
        print(us1234)
        os.remove('-39.jpg')
        image=Image.open(x)
        box=(cx+(cx/2),cy/2,width,cy)
        imaa18= image.crop(box)
        imaa18.save('-40.jpg')
        imaa18=Image.open('-40.jpg')
        us0866=sum(imaa18.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea26 pixels are")
        print(us0866)
        os.remove('-40.jpg')
        image=Image.open(x)
        box=(cx+(cx/2),cy,width,cy+(cy/2))
        imaa19= image.crop(box)
        imaa19.save('-41.jpg')
        imaa19=Image.open('-41.jpg')
        us0933=sum(imaa19.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea27 pixels are")
        print(us0933)
        os.remove('-41.jpg')
        image=Image.open(x)
        box=(cx+(cx/2),cy+(cy/2),width,height)
        imaa20= image.crop(box)
        imaa20.save('-42.jpg')
        imaa20=Image.open('-42.jpg')
        us09331=sum(imaa20.point(lambda x: 255 if x else 0).convert("L").point(bool).getdata())
        print("subarea28 pixels are")
        print(us09331)
        os.remove('-42.jpg')
        pm=0
        pnm=0
        pc=0
        print("enter user number of image to be compared")
        zz=input()
        i=0
        while i<10:
            if s1[i]==us1:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s2[i]==us2:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s3[i]==us3:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s4[i]==us4:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s5[i]==us5:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s6[i]==us6:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s7[i]==us7:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s8[i]==us8:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s9[i]==us9:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sa[i]==usa:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sb[i]==usb:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sc[i]==usc:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sd[i]==usd:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if se[i]==use:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sf[i]==usf:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sg[i]==usg:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sw[i]==usw:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if su[i]==usu:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if so[i]==uso:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if sr[i]==usr:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s123[i]==us123:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s086[i]==us086:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s093[i]==us093:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s1234[i]==us1234:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s0866[i]==us0866:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if s0933[i]==us0933:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if u[i]==uu:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if d[i]==ud:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if r[i]==ur:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            if l[i]==ul:
                pm=pm+1
                pc=pc+1
            else:
                pnm=pnm+1
            pp[i]=(pm/(pnm+pc))*100
            print("percentage of images matching")
            print(pp[i])
            i=i+1
        count=0    
        while i<5:
            if pp[i]>=70:
               count=count+1
            else:
               count=count
            i=i+1
        count1=0
        while (i>5)&(i<10):
            if pp[i]>=70:
              count1=count1+1
            else:
              count1=count1
            
            i=i+1
        scmp=count*count1
        scmp1=count*2
        scmp2=scmp-scmp1
        if scmp2>=0:
         print("the signature is valid")
        else:
         print("the signature is not valid")  
def callfunc():
    print("enter ur choic")
    print("1:database storing/2:comparing for detection")
    choice=int(input())
    if choice==0:
        databasefunc()
    else:
       userfunc()
    print("press 1 to continue")
    ssx=int(input())
    while ssx==1:
       callfunc()
callfunc()
