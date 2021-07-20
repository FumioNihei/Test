

with open( "./wiki/README.md", "r", encoding='utf-8' ) as tf:
    lines = tf.read().split( "\n" )
    
# for line in lines:
#     print( f"{line}++" )

uri = "https://github.com/FumioNihei/Test/wiki/"


import re

def replace( line ):
    result = re.match( r"\s*- \[.+\]\((.+)\)", line )
    print( result )

    if result is None:
        return line
    
    url = str( result.groups()[0] )

    import urllib.parse

    replaced_url = url.replace( ".md", "" )
    replaced_url = replaced_url.replace( "./contents/", "" )
    replaced_url = urllib.parse.quote( replaced_url )
    replaced_url = f"{uri}{replaced_url}"

    result = re.sub( url, replaced_url, line )
    return result


lines = [ replace(line) for line in lines ]

print( lines )


with open( './wiki/_Sidebar.md', 'w', encoding='utf-8' ) as f:
    f.writelines( [ f"{line}\n" for line in lines ] )

