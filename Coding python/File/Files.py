
#file openning and closing 
file_obj=open('data_file.txt','r')# creat file object

file_obj.close()

#file read()

file_obj=open('data_file.txt','r')
content=file_obj.read()
print(content)
print(type(content))
print(len(content))
print(content.count('r'))
file_obj.close()

#readline()
file_obj=open('data_file.txt','r')
line=file_obj.readline()
print(line)
print(type(line))
file_obj.close()

#readlines()
file_obj=open('data_file.txt','r')
line=file_obj.readlines()
print(line[0:-1])
print(type(line))
file_obj.close()
for i in line:
    print(i.strip())
for i in line[0:5]: 
    print(i.strip())
    
file_obj=open('data_file.txt','r')
for i in file_obj:
    print(i.strip())
file_obj.close() 

f = open('data_file.txt','r')
print(f)
print(f.fileno())

#Check if the file is connected to a terminal device:
f = open("demofile.txt", "r")
print(f.isatty())

#Check if the file is readable:
f = open("demofile.txt", "r")
print(f.readable())

#Change the current file position to 4, and return the rest of the line:
f = open('data_file.txt','r')
f.seek(4)
print(f.readline())

#Find the current file position:
f = open('data_file.txt','r')
print(f.readline())
print(f.tell())

#Truncate() method 
f = open("data_file.txt", "a")
f.truncate(5)
f.close()
#read the truncate file:
f = open("data_file.txt", "r")
print(f.read())
file_obj1=open('multiple.txt', 'w')
for i in range(10):
    temp=i*10
    file_obj1.writelines(str(temp)+'\n')
    
file_obj1.close()
    
#writeline function 
f = open("demofile3.txt", "w")
f.writelines(["See you soon!", "Over and out."])
f.close()

f = open("demofile3.txt", "r")
print(f.read())

#read and write file
with open("demofile3.txt", 'w') as file_obj1:
    file_obj1.write('100')
    #file_obj1.write('100'+'\n')
    file_obj1.write('100'+'\n')
    for i in range(100):
        file_obj1.write(str(i)+'\n')
            
with open("demofile3.txt", 'r') as file_obj1:
    
    print(file_obj1.read()[0:2])
    print(file_obj1.readlines()[0:2])
    
    
       
    
    
     
    
    
    
    


















