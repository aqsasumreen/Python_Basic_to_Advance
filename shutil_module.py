import shutil
shutil.copy("first.py" , "second.py")
shutil.copytree("audio" , "sounds") #for files
shutil.move("oop/first.txt", "first.txt")
shutil.rmtree("sounds") #delete folders