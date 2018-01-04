import re
import sys

def add_kw_prefix(data):
    regex = r"^([^-]+?)$"
    subst = "KW  - \\1"
    newdata = re.sub(regex, subst, data, 0, re.MULTILINE)
    return newdata

def main(argv):

    if not len(argv) == 2:
        print "Please input the source RIS filename!"
    else:
        with open(argv[1]) as f:
            data = f.read()

        newdata = add_kw_prefix(data)
        outfile = "output.ris"
        with open(outfile, 'w') as f:
            f.write(newdata)

if __name__ == "__main__":
    main(sys.argv)
