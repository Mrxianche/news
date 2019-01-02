#-*- coding:utf-8 -*-

from flask import Flask, url_for, render_template
import os
import json

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']= True
file_path = '/home/shiyanlou/files/'
file1 = 'helloshiyanlou.json'
file2 = 'helloworld.json'

@app.route('/')
def index():
    list1 = os.listdir(file_path)
    if len(list1) <2:
        return 'ERROR'
        exit(-1)
    else:
        with open(file_path + list1[0], 'r') as f:
            json_syl = json.load(f)
        with open(file_path + list1[1], 'r') as f:
            json_wd = json.load(f)
        list2 = [json_syl['title'],json_wd['title']]
        return render_template('index.html',list2 = list2)

@app.route('/files/<filename>')
def file(filename):
    list1 = os.listdir(file_path)
    if filename+'.json' not in list1:
        return render_template('404.html')
    elif filename + '.json' == 'helloshiyanlou.json':
        with open(file_path + 'helloshiyanlou.json', 'r') as f:
            json_syl = json.load(f)
        return render_template('file.html',json_dict = json_syl)
    else:
        with open(file_path + 'helloworld.json', 'r') as f:
            json_wd = json.load(f)
        return render_template('file.html',json_dict = json_wd)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html') , 404

if __name__ == '__main__':
    app.run()
