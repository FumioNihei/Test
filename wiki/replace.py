
import re
import urllib.parse

def readme_to_sidebar():
    with open( "./wiki/README.md", "r", encoding='utf-8' ) as tf:
        lines = tf.read().split( "\n" )

    uri = "https://github.com/FumioNihei/Test/wiki/"

    def replace( line ):
        result = re.match( r"\s*- \[.+\]\((.+)\)", line )
        print( result )

        if result is None:
            return line
        
        url = str( result.groups()[0] )

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



def copy_to_parent_dir():
    import glob
    import os
    import shutil

    src_dir = "./wiki/contents/"
    dest_dir = "./wiki/"

    files = glob.glob( f"{src_dir}*.md" )

    for src in files:
        dest = os.path.join( dest_dir, os.path.split(src)[1] )
        print( f"{src} -> {dest}" )
        shutil.copyfile( src, dest )



readme_to_sidebar()
copy_to_parent_dir()