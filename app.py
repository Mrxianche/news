#-*- coding:utf-8 -*-

from flask import Flask, url_for, render_template
import os
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']= True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    categorys = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__ (self,title, created_time, categorys, content):
        self.title = title
        self.created_time = created_time
        self.categorys = categorys
        self.content = content

class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
    files = db.relationship('File')
    def __init__ (self, name):
        self.name = name

'''
file_path = '/home/shiyanlou/files/'
file1 = 'helloshiyanlou.json'
file2 = 'helloworld.json'
'''
def InsertData():
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

#InsertData()

@app.route('/')
def index():
    return render_template('index.html',files = File.query.all())
    '''
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
'''

@app.route('/files/<file_id>')
def file(file_id):
    get_file = File.query.get(file_id)
    return render_template('file.html',get_file = get_file)
    '''
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
'''

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html') , 404

if __name__ == '__main__':
    app.run()
