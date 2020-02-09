import sys
from collections import defaultdict
from pathlib import Path

def handleDiffFile(diffFile):
    # TODO FIRST PRIMARY split by first folder
    hashFilesMap = defaultdict(list)
    f = Path(diffFile)
    with f.open() as ff:
        for l in ff.readlines():
            md5 = l[0:32]
            # 2 spaces betw md5 and path, terminated by newline
            name = l[34:-1]
            hashFilesMap[md5].append(name)
    return hashFilesMap

def findDuplicatesInOneFile(hashFilesMap):
    return dict(filter(lambda v:len(v[1])>1,hashFilesMap.items()))
def findDuplicatesInMultipleFiles(hashFilesMap1,hashFilesMap2):
    hashesInBoth=set(hashFilesMap1.keys()).intersection(set(hashFilesMap2))
    return {k:set(hashFilesMap1[k])|set(hashFilesMap2[k]) for k in hashesInBoth}

def findDuplicateFolders():
    # TODO implement
    # find folders where x = 90% of files are in the other as well
    # e.g. A contains 90% of files in B too, or A contains same files as B or B contains 90% of A files, but a lot more...
    pass

def printDict(curDict):
    # todo print size of 1, all and all-1
    for k,v in curDict.items():
        print(f"{k}")
        for vv in v:
            print(f"\t{vv}")
def main():
    fileMap={}
    for f in sys.argv[1:]:
        fileMap[f]=handleDiffFile(f)
        print(f'duplicates in {f}')
        printDict(findDuplicatesInOneFile(fileMap[f]))

    fileMapKeys=list(fileMap.keys())
    if len(fileMap)>1:
        for x in range(len(fileMapKeys)):
            for y in range(x+1,len(fileMapKeys)):
                print(f'comparing {fileMapKeys[x]} with {fileMapKeys[y]}')
                printDict(findDuplicatesInMultipleFiles(fileMap[fileMapKeys[x]],fileMap[fileMapKeys[y]]))
                # TODO next: find commonprefixes for each dup in mult files
                #a=Path('/a/b/c/d/').parts
                #b=Path('/a/b/q/d/').parts
                #os.path.commonprefix([a, b])
                # Path(*os.path.commonprefix([a,b]))
                #PosixPath('/a/b')




main()