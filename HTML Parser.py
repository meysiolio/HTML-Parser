from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser1(HTMLParser):
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

class MyHTMLParser2(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment\n" + data)
        else:
            print(">>> Single-line Comment\n" + data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data\n" + data)


if __name__ == '__main__':
    if int(input('Parser1 or Parser2?!')) == 1:
        input_html = []
        parser = MyHTMLParser1() # instantiate the parser and fed it some HTML

        for _ in range(int(input())):
            input_html.append(input())

        for i in input_html:
            parser.feed(i)
    else:
        html = ""
        for i in range(int(input())):
            html += input().rstrip()
            html += '\n'
    
        parser = MyHTMLParser2()
        parser.feed(html)
        parser.close()