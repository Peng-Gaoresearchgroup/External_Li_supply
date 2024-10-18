import time
import DrissionPage.errors
from loguru import logger
from DrissionPage import ChromiumPage, ChromiumOptions
import requests
import os

def main():
    #检查输出文件，获得已处理的pdf目录，避免重复----Check the output file, get the processed PDF directory, avoid duplicates
    old_pdf_files = set()
    if os.path.exists('Code\Output.txt'):
        with open('Code\Output.txt', encoding='utf-8') as f:
            for text in f.read().strip().split('\n\n'):
                old_pdf_file = text.split('\n----')[0]
                old_pdf_files.add(old_pdf_file)
    
    #登录ChatGPT----Log in to ChatGPT
    co = ChromiumOptions()
    co.use_system_user_path()
    cp = ChromiumPage(co)
    cp.get('https://chatgpt.com/')
    if cp.ele('登录', timeout=2):
        raise '没有登录chatgpt，无法使用，请在浏览器上登录后重新启动\nNot logged into chatgpt, not working, please log in on your browser and restart it.'
    #如果此处报错，请尝试手动打开Chrome浏览器，登录chatgpt后，关闭所有Chrome浏览器，再重新运行----If an error is reported here, please try to open Chrome manually and close all Chrome browsers after logging in to chatgpt，finally rerun the code
    
    #读取待处理文件----Read the pending file
    #将所有需要处理的pdf文件用纯数字命名，放于py2文件夹下，详见Readme.md----Name all the pdf files that need to be processed in a pure number and put them in the py2 folder, see Readme.md for details
    pdf_files = os.listdir('Code\py2')
    pdf_files.sort(key=lambda x: int(x.split('.')[0]))
    for pdf_file in pdf_files:
        if pdf_file in old_pdf_files:
            continue
        pdf_abs_path = os.getcwd() + os.sep + 'Code\py2' + os.sep + pdf_file
        # 判断文件大小----Determine the file size
        with open(pdf_abs_path, 'rb') as f:
            file_size = len(f.read())
        if file_size < 3000:
            #3000是经验判断可调整----3000 is based on experience and can be adjusted
            with open('Code\Output.txt', 'a', encoding='utf-8') as f:
                f.write(f'{pdf_file}\n----Irregular documents\n\n')
        else:
            while True:
                logger.info(f'Processing：{pdf_file}')
                # 切换到gpt4-all----Switch to gpt4-all
                cp.get('https://chatgpt.com/?model=gpt-4-all')
                try:
                    cp.ele('tag:input').input(pdf_abs_path)
                except DrissionPage.errors.ElementLostError:
                    time.sleep(10)
                    cp.ele('tag:input').input(pdf_abs_path)
                #自定义提示词----Define the prompt word
                text = """
                “假设你是有机电化学领域的专家，请帮我总结一下这篇文献里所有研究的分子以及发生的反应过程，用英文严格按照以下格式回复（被[]圈起来的是变量，需要你从pdf中提取，如果提取不到的留空处理，请勿回复其他内容）：、\n(1)[化合物A][CAS号]在[xxx]条件下发生反应，产物为[化合物B][CAS号]”
                """
                cp.ele('#prompt-textarea').input(text)
                while True:
                    if 'disabled' in cp.ele('@data-testid=send-button').attrs:
                        time.sleep(1)
                        continue
                    cp.ele('@data-testid=send-button').click()
                    break
                if '无法上传' in cp.html:
                    continue
                reply_text = cp.ele('.markdown prose w-full break-words dark:prose-invert light', timeout=50).text
                with open('Code\Output.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{pdf_file}\n----{reply_text}\n\n')
                break


if __name__ == '__main__':
    main()
