from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.gslmzb6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import random


@app.route('/')
def home():
    return render_template('index.html')


# 댓글 작성 <- save_comment()
@app.route("/test", methods=["POST"])
def save_comment():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    num1 = random.randint(1, 255)
    num2 = random.randint(1, 255)
    num3 = random.randint(1, 255)



    doc = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'name': name_receive,
        'comment': comment_receive
    }
    db.test.insert_one(doc)

    return jsonify({'msg': '댓글 등록!'})


# 댓글목록 조회 <- show_comment()
@app.route("/test", methods=["GET"])
def test_get():

    test_list = list(db.test.find({},{'_id':False}))
    return jsonify({'tests': test_list})


# 수정된 댓글 저장 <- save(num)
@app.route("/test/edit", methods=["POST"])
def save_edit():
    edit_receive = request.form['edit_give']
    num1_receive = request.form['num1_give']
    num2_receive = request.form['num2_give']
    num3_receive = request.form['num3_give']
    db.test.update_one({'num1': int(num1_receive), 'num2': int(num2_receive), 'num3': int(num3_receive)}, {'$set': {'comment': edit_receive}})

    return jsonify({'msg': '수정기능 테스트 완료!'})


# 삭제 <- remove(num)
@app.route("/test/remove", methods=["POST"])
def remove():
    num1_receive = request.form['num1_give']
    num2_receive = request.form['num2_give']
    num3_receive = request.form['num3_give']
    db.test.delete_one({'num1': int(num1_receive), 'num2': int(num2_receive), 'num3': int(num3_receive)})

    return jsonify({'msg': '삭제!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
