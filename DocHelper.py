import os
import glob
import shutil
import sys
import zipfile
import urllib.request



def md_to_pdf(file_name):
    os.system(f"pandoc --pdf-engine=xelatex  -V mainfont=LXGWWenKaiMono-Regular.ttf -V geometry:margin=0.5in  -V geometry:a2paper --template eisvogel.tex  {file_name} -o {file_name.replace('.md', '.pdf')}")

if __name__ == '__main__':
    print(f"🚀 开始执行打包脚本...(By Cai 😋)")
    # 获取文件夹中所有的md文件，并按文件名排序
    file_list = sorted([f for f in os.listdir("Document") if f.endswith('.md')])

    # 创建或打开README.md文件
    with open('README.md', 'r+') as outfile:
        for fname in file_list:
            with open(os.path.join("Document", fname)) as infile:
                # 将每个文件的内容写入README.md
                outfile.write(infile.read())
                outfile.write("\n\n")
    os.rename("README.md","TShock插件编写从入门到跑路.md")
    shutil.copytree("Document/Resourse","Resourse")
    

    print("🔄 准备转换PDF...")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/fonts/TTF/LXGWWenKaiMono-Regular.ttf", "LXGWWenKaiMono-Regular.ttf")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex", "eisvogel.tex")
    directory = '/usr/share/texmf/fonts/opentype/public/lm/'
    specified_file = 'LXGWWenKaiMono-Regular.ttf'
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            shutil.copy2(specified_file, os.path.join(directory, filename))
    md_to_pdf(f"TShock插件编写从入门到跑路.md")
    print("✅ PDF转换完成！")
    print("🎉 插件打包成功！")
