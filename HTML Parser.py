from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print("-> " + str(attr[0]) + " > " +  str(attr[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for attr in attrs:
                print("-> " + str(attr[0]) + " > " +  str(attr[1]))

if __name__ == '__main__':
    input_html = []
    parser = MyHTMLParser() # instantiate the parser and fed it some HTML

    for _ in range(int(input())):
        input_html.append(input())

    for i in input_html:
        parser.feed(i)