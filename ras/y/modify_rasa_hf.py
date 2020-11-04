import rasa , os , shutil
def copytree(src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                copytree(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)

if __name__ == "__main__":
    
    rasapath = rasa.__file__[:-11] + "nlu/utils/hugging_face/"
    
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/hugging_face"
    copytree(dir_path,rasapath)


