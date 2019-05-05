import os
import argparse
import subprocess


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--dir_path', type=str, help='Path to the directory whose files should be categorized')
arg_parser.add_argument('--op_type', type=str, help='undo to revert to default')
args = arg_parser.parse_args()

# some check ups before using specified path
assert (args.dir_path is not None), "You have to input a valid path to a directory first by setting --dir_path"
assert (len(os.listdir(args.dir_path)) != 0), "No files to categorize here. Must be a dir with FiLEs"



# get the extension of a file
def getExtension(file_name):
    dot_split = file_name.split('.')
    return dot_split[len(dot_split) - 1]

# move to specified directory
os.chdir(args.dir_path)

# check if a file has extension
def hasExtension(file_name):
    return len(file_name.split('.')) > 1

#file to store name of new folders created 
memory = '.febvyrfrehfeyrfevfka3434ufdemeoy.txt' 
def categorize(dir_path):
    print("\nCategorizing... chill for some millisecs\n")
    for current_file in os.listdir(dir_path):  
        if hasExtension(current_file):
            new_dir = getExtension(current_file) + " files"
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
                #write name of current created directory to memory
                o=open(memory,"a")
                o.write(new_dir+'\n')
                o.close()
            #prevent from categorizing memory file
            if current_file != memory:    
                os.rename(current_file, new_dir +'/'+ current_file)
    #hide the memory file            
    subprocess.check_call(["attrib","+H",memory])            
    print("Files categorized!..")
  
    
def undo( root_dir_path):
    #check if memory file is present.(If it's present, that folder has been categorized before.
    if memory in os.listdir(root_dir_path):    
        o=open(memory,"r")
        newly_created_dir = o.readlines()  
        for new in newly_created_dir:
            new_name = new.strip('\n')
            for current_file in os.listdir(args.dir_path+'\\'+new_name):
                os.rename(new_name+'/' +current_file, current_file)
            os.rmdir(new_name)   
        o.close()
        os.remove(memory)
        print("Undo Successful!..")
    else:
        print('undo not enabled yet')
#checks whether the operation type argument is 'undo'        
if args.op_type == 'undo' :
    undo( args.dir_path)             
else:    
    categorize(args.dir_path)            
    
     
