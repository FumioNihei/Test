
import re
import urllib.parse
import glob
import os
import shutil

uri = "https://github.com/FumioNihei/Test/wiki/"

def readme_to_sidebar( src, dest ):
    
    with open( src, "r", encoding='utf-8' ) as tf:
        # lines = tf.read().split( "\n" )
        lines = tf.readlines()

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

    # with open( './docs/_Sidebar.md', 'w', encoding='utf-8' ) as f:
    with open( dest, 'w', encoding='utf-8' ) as f:        
        f.writelines( [ f"{line}\n" for line in lines ] )





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
            s = s.replace( f"[{text}]({path})", f"[[{text}]]" )
        
        with open( src, 'w', encoding='utf-8' ) as f:        
            f.write( s )




def copy_wikicontents_to( src_dir, dest_dir ):
    files = glob.glob( f"{src_dir}*.md" )

    for src in files:
        dest = os.path.join( dest_dir, os.path.split(src)[1] )
        print( f"{src} -> {dest}" )
        shutil.copyfile( src, dest )





dest_dir = "./docs/"

if not os.path.exists( dest_dir ):
    os.mkdir( dest_dir )

copy_wikicontents_to( src_dir="./wiki/contents/", dest_dir=dest_dir )
replace_link( src_dir=dest_dir, dest_dir=dest_dir )
readme_to_sidebar( src="./wiki/README.md", dest='./docs/_Sidebar.md' )