def main():
    lines = open("README.md", encoding="utf-8").readlines()

    with open("README.md", "w", encoding="utf-8") as dest:
        for line in lines:
            dest.write(patch(line))

CYR="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
CYR+=CYR.upper()

def patch(line):
    s1 = line
    s2 = " " + s1
    s3 = " " + s2
    s4 = " " + s3

    def char(c1, c2, c3, c4):
        if c1 == ' ' and c2 in CYR and c3 in CYR and c4 not in CYR:
            return chr(160)
        elif c1 == ' ' and c2 in CYR and c3 not in CYR:
            return chr(160)
        else:
            return c1

    return "".join(map(char, s1, s2, s3, s4))

main()
