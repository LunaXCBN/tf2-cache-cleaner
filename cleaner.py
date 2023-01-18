import glob
import os

for cache in glob.glob("**/sound.cache", recursive=True):
    if os.path.exists(cache):
        os.remove(cache)
        print("Removed %s" %cache)
