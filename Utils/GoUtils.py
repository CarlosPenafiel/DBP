#!/usr/bin/python3
import re
import sys
import gzip
class GoUtils():
    " Docstring"
    def __init__(self,filename):
        self.filename = filename
    def extractNames(self,outfile=''):
        if outfile != '':
            fout = open(outfile, 'w')
            fout.write("GoId\tGoName\tGoNamespace\n")        
        else:
            print("GoId\tGoName\tGoNamespace")
        f = gzip.open(self.filename, 'rt')
        for line in f:
            mid=re.search("^id: (GO:[0-9]{7})",line)
            mnm=re.search("^name: (.+)",line)
            nsp=re.search("^namespace: (.+)",line)
            last=re.search("^id: negatively_regulates",line)
            if last:
                break
            elif mid:
                id=mid.group(1)
            elif mnm:
                nm=mnm.group(1)
            elif nsp:
              if outfile != '':
                 fout.write(""+id+"\t"+nm+"\t"+nsp.group(1)+"\n")
              else:
                 print(""+id+"\t"+nm+"\t"+nsp.group(1))
        if outfile != '':
               fout.close
                    
    def extractGoTree(self,outfile=''):
        if outfile != '':
            fout = open(outfile, 'w')
            fout.write("GoId\tGoParentType\tGoParentId\n")        
        else:
            print("GoId\tGoParentType\tGoParentId\n")
        f = gzip.open(self.filename, 'rt')
        for line in f:
            mid=re.search("^id: (GO:[0-9]{7})",line)
            isa=re.search("^is_a: (GO:[0-9]{7})",line)
            rls=re.search("^relationship: ([^GO:0-9]+) (GO:[0-9]{7})",line)
            last=re.search("^id: negatively_regulates",line)
            if last:
                break
            elif mid:
                id=mid.group(1)
            elif isa:
                if outfile != '':
                     fout.write(""+id+"\tis_a\t"+isa.group(1)+"\n")
                else:
                     print(""+id+"\tis_a\t"+isa.group(1))
            elif rls:
              if outfile != '':
                 fout.write(""+id+"\t"+rls.group(1)+"\t"+rls.group(2)+"\n")
              else:
                 print(""+id+"\t"+rls.group(1)+"\t"+rls.group(2))
        if outfile != '':
               fout.close
    def extractGoObsoletes(self,outfile=''):
        if outfile != '':
            fout = open(outfile, 'w')
            fout.write("GoId\tGoConsiderId\n")        
        else:
            print("GoId\tGoConsiderId\n")
        f = gzip.open(self.filename, 'rt')
        for line in f:
            mid=re.search("^id: (GO:[0-9]{7})",line)
            consider=re.search("^consider: (GO:[0-9]{7})",line)
            last=re.search("^id: negatively_regulates",line)
            if last:
                break
            elif mid:
                id=mid.group(1)
            elif consider:
                if outfile != '':
                     fout.write(""+id+"\t"+consider.group(1)+"\n")
                else:
                     print(""+id+"\t"+consider.group(1))
        if outfile != '':
               fout.close
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: GoUtils.py obofile.gz command outfile.tab")
        print("       commands: gonames|gotree|goobsoletes")
        sys.exit(0)
    else:
        go = GoUtils(sys.argv[1])
        if len(sys.argv) == 4:
            if sys.argv[2] == "gonames":
                go.extractNames(outfile=sys.argv[3])
            if sys.argv[2] == "gotree":
                go.extractGoTree(outfile=sys.argv[3])
            if sys.argv[2] == "goobsoletes":
                go.extractGoObsoletes(outfile=sys.argv[3])
        else:
            go.extractNames()


