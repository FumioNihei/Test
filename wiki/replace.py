
import re
import urllib.parse
import glob
import os
import shutil

wiki_uri = "https://github.com/FumioNihei/Test/wiki/"

def readme_to_sidebar( src, dest ):
    
    with open( src, "r", encoding='utf-8' ) as tf:
        lines = tf.readlines()

    def replace( line ):
        # # こういうのがマッチ -> "- [test](./contents/test.md)"
        result = re.match( r"\s*- \[.+\]\((.+)\)", line )
        print( result )

        if result is None:
            return line
        
        # # markdownのパスを変数pathに代入
        path = str( result.groups()[0] )

        replaced_path = path.replace( "./contents/", "" ).replace( ".md", "" )
        replaced_path = urllib.parse.quote( replaced_path )
        replaced_path = f"{wiki_uri}{replaced_path}"

        result = re.sub( path, replaced_path, line )
        return result

    lines = [ replace(line) for line in lines ]

    with open( dest, 'w', encoding='utf-8' ) as f:        
        f.writelines( lines )





def replace_link( src_dir, dest_dir ):
    files = glob.glob( f"{src_dir}*.md" )

    for src in files:

        with open( src, "r", encoding='utf-8' ) as tf:
            s = tf.read()

        results = re.findall( r"\[(.+)\]\((.+)\)", s )
        results = [ (text, path) for text, path in results if not path.startswith( "http" ) ]

        if len(results) == 0:
            continue

        for text, path in results:
            name = path.replace( "./", "" ).replace( ".md", "" )
            s = s.replace( f"[{text}]({path})", f"[[{name}]]" )
        
        with open( src, 'w', encoding='utf-8' ) as f:        
            f.write( s )




dest_dir = "./docs/"

shutil.copytree( "./wiki/contents/", dest_dir, dirs_exist_ok=True )
replace_link( src_dir=dest_dir, dest_dir=dest_dir )
readme_to_sidebar( src="./wiki/README.md", dest='./docs/_Sidebar.md' )