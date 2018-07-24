import re
import sys

def add_kw_prefix(data):
    regex = r"^(?!(^\S+\s+-))(.+)$"
    subst = "KW  - \\2"
    newdata = re.sub(regex, subst, data, 0, re.MULTILINE)
    return newdata

def main(argv):

    # if not len(argv) == 2:
    #     print "Please input the source RIS filename!"
    assert len(argv) == 2, "Please input the source RIS filename!" 
        
    with open(argv[1], encoding='utf8') as f:
        data = f.read()

    data = add_kw_prefix(data)
    outfile = "output.ris"
    with open(outfile, 'w', encoding='utf8') as f:
        f.write(data)

if __name__ == "__main__":
    main(sys.argv)
