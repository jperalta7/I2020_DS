def main(strings):
        html_output = open("output.html", "w+")
        html_output.write("<body>\n")
        for string_ in strings:
            html_output.write(string_)
            html_output.write(" ")
        html_output.write("\n</body>")
        html_output.close()
   
if __name__ == '__main__':
    import sys
    main(sys.argv[1:])