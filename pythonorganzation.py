import os
import shutil
current_dir = os.path.dirname(os.path.realpath(__file__))
##organise your images
for filename in os.listdir(current_dir):
    if filename.endswith((".png", "jpg" , 'gif' , 'jpeg')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename , "Images")
        os.remove(filename)
        print('Images  Done')
    ##organise your codes  
    if filename.endswith((".py", ".html" , '.css' , '.cpp')):
        if not os.path.exists("codes"):
            os.mkdir('codes')
        shutil.copy(filename , "codes")
        os.remove(filename)
        print('codes Done')   
        
        ##organise your videos
    if filename.endswith((".mp4", ".webm")):
        if not os.path.exists("videos"):
            os.mkdir('videos')
        shutil.copy(filename , "videos")
        os.remove(filename)
        print('Videos Done') 
            ##organise your Docs
    if filename.endswith((".pdf", ".word",'txt')):
        if not os.path.exists("Doc"):
            os.mkdir('Doc')
        shutil.copy(filename , "Doc")
        os.remove(filename)
        print('Docs Done')         
            ##organise your apps
    if filename.endswith((".exe")):
        if not os.path.exists("apps"):
            os.mkdir('apps')
        shutil.copy(filename , "apps")
        os.remove(filename)
        print('apps Done')
            ##organise your archives
    if filename.endswith((".rar" , '.zip')):
        if not os.path.exists("archive"):
            os.mkdir('archive')
        shutil.copy(filename , "archive")
        os.remove(filename)
        print('archives Done')        
    
          ##organise your Iso
    if filename.endswith((".iso")):
        if not os.path.exists("iso"):
            os.mkdir('iso')
        shutil.copy(filename , "iso")
        os.remove(filename)
        print('iso Done')        
    
    
