from flask import Flask, jsonify, request
import torch
import os
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

list=[] 
a=os.listdir("content/yolov5/runs/detect/exp5/labels")
a1="content/yolov5/runs/detect/exp5/labels"
for i in range(len(a)):
    b=os.path.join(a1,a[i])
    with open(b, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        list.append([b,num_lines])
column=['image path','number of memories']
df=pd.DataFrame(list,columns=column)

@app.route('/mytable')
def mytable():

    html_table = df.to_html()

    # Return HTML table as part of the Flask response
    return f'<html><body>{html_table}</body></html>'

if __name__ == '__main__':
    app.run(debug=True)


