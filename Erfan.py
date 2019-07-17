import os

while True:
                files=[]
                folders=[]
                for i in os.listdir():
                                if os.path.isdir(i):
                                                folders.append(i)
                                else:
                                                files.append(i)

                if files==[] and folders==[]:
                                print("any file or directory")
                else:
                                if files==[]:
                                                print("any file")
                                                print("\nfolders:",','.join(folders))
                                elif folders==[]:
                                                print("files:",','.join(files))
                                                print("\nany folders")
                                else:
                                                print("files:",','.join(files))
                                                print("\nfolders:",','.join(folders))
                                                
                os.chdir(input("go to: "))
                                                
                          