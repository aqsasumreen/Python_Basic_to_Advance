# async is a programming pattern allows a high performance  I/O  operations
# in a concurrent and non-blocking manner ,
import asyncio
import time
import requests

async def func1():
    URL = "https://www.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_40965130.htm#query=4k%20wallpaper&position=0&from_view=keyword&track=ais&uuid=f1bf2709-34e2-4198-a331-a0fe1f80fc6a"
    response = requests.get(URL)
    open("insta1.jpg", "wb").write(response.content)
    print("Fun1")


async def func2():
    URL = "https://www.freepik.com/free-photo/reflection-lights-mountain-lake-captured-parco-ciani-lugano-switzerland_11505614.htm#query=4k%20wallpaper&position=2&from_view=keyword&track=ais&uuid=4c2dfb0e-00e4-4742-ad23-c940eb6ddd49"
    response = requests.get(URL)
    open("insta2.jpg", "wb").write(response.content)
    print("Fun2")


async def func3():
    URL = "https://www.google.com/search?sca_esv=f4e79416cdeea533&rlz=1C1VDKB_enPK996PK996&sxsrf=ACQVn0-tlUFjWH0MZN_fAERMaOrH7xg7Jw:1712572094714&q=Wallpapers+4k&uds=AMwkrPt31fsGLmLKAVISgr3EM-eJ7lSEAw3VSJJlEH8U_hlR_2BaHm6rLbfKMnQDYZe-KLZhUSPSq0WHKmbOcWed0Q9IIdxBaOmwfeHmavtuR8cjFMcRBEhXr8l1ctdUvdXjZwZZdjJOhs7KPrBrdyXFfwpZjXIu-mkWqJ2h8i_e_K2FvlkfS5o-CZL0NTye67gn_hT3FQkQ9C4oePn5a0LVgerThg78U9vf5QIzSMYkHyPM4VR8nm1HjrHk5esAQWftraiOrU5RY9dixs67N63JVAMv1-OmPmOOycOoRaaFV-He_xkyI2c&udm=2&prmd=isvnbz&sa=X&ved=2ahUKEwjl4O2atLKFAxV-AdsEHVYFDWsQtKgLegQIFBAB&biw=664&bih=575&dpr=1.5#vhid=YY3Tnp9WJFYIEM&vssid=mosaic"
    response = requests.get(URL)
    open("insta3.jpg", "wb").write(response.content)
    print("Fun3")

async def main():
    # await func1()
    # await func2()
    # await func3()

    # aik sath chalany kaliye
    pp = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(pp)

asyncio.run(main())
