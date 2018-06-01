# opens a netscape bookmark file (format that chrome uses) bookmarks.html, assumes one line = 1 bookmark, and removes any duplicate urls, outputting to bookmarksout.html

import re


def main():
    with open('bookmarks.html', encoding='utf8') as infile:
        urlset = set()
        linelist = []
        urlre = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        for line in infile:
            finds = urlre.findall(line)
            if finds:
                found = False
                for find in set(finds):
                    find = find.replace(
                        'http://', '').replace('https://', '').strip()
                    if find in urlset:
                        found = True
                        print(find)
                    else:
                        urlset.add(find)
                if not found:
                    linelist.append(line)
            else:
                linelist.append(line)
        with open('bookmarksout.html', 'w', encoding='utf8') as outfile:
            outfile.writelines(linelist)


if __name__ == '__main__':
    main()
