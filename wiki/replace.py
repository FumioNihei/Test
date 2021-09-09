
import re
import urllib.parse

def readme_to_sidebar():
    with open( "./wiki/README.md", "r", encoding='utf-8' ) as tf:
        lines = tf.read().split( "\n" )

    uri = "https://github.com/FumioNihei/Test/wiki/"

    def replace( line ):
        # # こういうのがマッチ -> "- [test](./contents/test.md)"
        result = re.match( r"\s*- \[.+\]\((.+)\)", line )
        print( result )

        # # マッチしなかったら何もしない
        if result is None:
            return line
        
        # # markdownのパスを変数pathに代入
        path = str( result.groups()[0] )

        replaced_path = path.replace( ".md", "" )
        replaced_path = replaced_path.replace( "./contents/", "" )
        replaced_path = urllib.parse.quote( replaced_path )
        replaced_path = f"{uri}{replaced_path}"

        result = re.sub( path, replaced_path, line )
        return result


    lines = [ replace(line) for line in lines ]
    print( lines )

    with open( './wiki/_Sidebar.md', 'w', encoding='utf-8' ) as f:
        f.writelines( [ f"{line}\n" for line in lines ] )



def copy_wikicontents_to_docs():
    import glob
    import os
    import shutil

    src_dir = "./wiki/contents/"
    dest_dir = "./docs/"
    os.mkdir( dest_dir )

    files = glob.glob( f"{src_dir}*.md" )

    for src in files:
        dest = os.path.join( dest_dir, os.path.split(src)[1] )
        print( f"{src} -> {dest}" )
        shutil.copyfile( src, dest )



readme_to_sidebar()
copy_wikicontents_to_docs()