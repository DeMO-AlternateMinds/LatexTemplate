def create(fileName):
    file = open(fileName + ".tex", "w+")

    # Creates Header

    file.write("\\documentclass[12pt]{article}\n\n")
    title = input("Title: ")
    file.write("\\title{" + title + "}\n")
    author = input("Author: ")
    file.write("\\author{" + author + "}\n")

    # Creates Body
    file.write("\\begin{document}\n")
    sopUser = input("Would you like sections or paragraphs?(s/p)")

    number = int(input("How many sections?"))

    num = range(0, number)

    if sopUser == "s" or sopUser == "S":
        for x in num:
            file.write("\\section{Problem " + str(x + 1) + "}\n\n")

    if sopUser == "p" or sopUser == "P":
        for x in num:
            file.write("\\paragraph{Problem " + str(x + 1) + "}\n\n")
    if sopUser == "a" or sopUser == "A":
        for x in range(0, number):
            file.write("\\section{Problem " + str(x + 1) + "}\n\n")
            secondary = 0
            secondary = int(input(str(x + 1) + ").How many subsections?"))
            char = "a"
            i = ord(char[0])

            for x in range(0, secondary):
                char = chr(i)
                file.write("\\subsection{" + char + ".)}\n\n")
                i += 1
    file.write("\\end{document}")
    file.close()

