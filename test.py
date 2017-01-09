import subprocess, signal, os
from time import sleep
from os import listdir
from os.path import isfile, join, isdir

#######################---edit file names---#######################################################
variable_file_name = "SumClass.java"



#######################---edit file names---#######################################################

#grabs all the file names in the "students_work" directory
mypath = "/mnt/c/Users/evank/OneDrive/chico/Winter_2016/testing_script/students_work"
student_dirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]

#opens up where the output will go
output_file = open("output.txt", 'w')


for i in student_dirs:
    #prints out file names
    print(i)
    
    #deletes old test_file
    subprocess.Popen("rm sample_project/" + variable_file_name, shell=True)
    #moves new test_file into the sample_project folder
    subprocess.Popen("cp /mnt/c/Users/evank/OneDrive/chico/Winter_2016/testing_script/students_work/" + i + "/SumClass.java /mnt/c/Users/evank/OneDrive/chico/Winter_2016/testing_script/sample_project", shell=True)
    #gets list of all of the files in the students folder
    dir_list = os.listdir("/mnt/c/Users/evank/OneDrive/chico/Winter_2016/testing_script/students_work/" + i)

    #checks if the correct file is in the student folder
    in_folder = False
    for files in dir_list:
        if files == variable_file_name:
            in_folder = True
    #prints out students name
    output_file.write(i + ": \n")

    if in_folder:
        #compiles the new test file
        subprocess.Popen("javac sample_project/" + variable_file_name, shell=True)
        #compiles the whole project again with recompiled test file
        subprocess.Popen("javac -sourcepath sample_project sample_project/CorrectStudentWork.java", shell=True).wait()
        #runs the project
        output = subprocess.Popen("java -classpath sample_project/ CorrectStudentWork", shell=True, stdout=subprocess.PIPE)
        output.wait()
        #getting the output of the program
        out = output.communicate()[0]


        #getting rid of the extra characters
        output_file.write(out.decode('ascii'))
        output_file.write("\n")
    else:
        output_file.write("ERROR: missing file or incorrect file name\n")
