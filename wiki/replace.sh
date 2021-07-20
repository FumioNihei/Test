
# uri="https:\/\/github.com\/IUI-Lab\/Readme\/wiki\/"
uri="https:\/\/github.com\/FumioNihei\/Test\/wiki\/"

# cat ./wiki/README.md | sed -e "s/.\/contents\//$uri/g" > ./wiki/_Sidebar.md
# cat ./wiki/_Sidebar.md | sed -e "s/.md//" > ./wiki/_Sidebar.md

# cat ./wiki/README.md | sed -e "s/.\/contents\/(\.\+).md/$uri\1/g" > ./wiki/_Sidebar.md
cat ./wiki/README.md | sed -r "s/.\/contents\/(.+).md/$uri\1/g" > ./wiki/_Sidebar.md
cat ./wiki/_Sidebar.md
