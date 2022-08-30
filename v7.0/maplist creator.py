import glob
from tqdm import tqdm

osupath = "C:\\Users\\Utilisateur\\AppData\\Local\\osu!\\Songs" #input('Please enter the path to your osu songs folder for training: ') # 
verbose = "n" #input('Show verbose output? y/n: ')
files = glob.glob(osupath + '/**/*.osu', recursive = True) 
numwritten = 0
f = open('maplist.txt','w+')

tags_in_map = ["cametek"]# ["another", "leggendaria", "maximum", "vivid"]
#words_in_map = ["nanahira"]

def word_in_map_name(lst, string, mode=1):
    string = string.lower()
    if mode==1: # all words must be in file name
        for word in lst:
            if word not in string:
                return False
        return True
    
    elif mode==2: # at least one word must be in file name
        for word in lst:
            if word in string:
                return True
        return False


def tag_in_map(lst,string,mode=1):
    tags = []
    
    with open(string, 'r') as f:
        try:
            f = f.readlines()[:40]
        except UnicodeDecodeError:
            return False

        
        for line in f:
            if "Tags:" in line:
                tags = line.split(":")[-1].lower().strip("\n").split(" ")
    
    if mode==1: # all tags must be included
    
        for word in lst:
            if word not in tags:
                return False
        return True
    elif mode==2: # at least one tag must be included

        for word in lst:
            if word in tags:
                print(tags)
                return True
                
        return False




for filename in tqdm(sorted(glob.iglob(osupath + '/**/*.osu', recursive = True))):

    if tag_in_map(tags_in_map,filename,2):# or word_in_map_name(words_in_map, filename, 2):

        notrainer = [speed not in filename.lower() for speed in (f"1.{spd}x" for spd in range(10))]
        if len(set(notrainer)) == 1 and notrainer[0]:
            if(verbose == 'y' or verbose == 'Y' or verbose == 'Yes' or verbose == 'YES'):
                print(filename) 
            f.write('\n' + filename)
            numwritten+=1


print('#######################################################################################')
print('Wrote ' + str(numwritten) + ' map paths to maplist.txt')
#input('maplist.txt generated in the same directory as this script, press enter to exit')
