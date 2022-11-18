from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.a7l8csh.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta

import random



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates/<username>')
def get_templates(username):
    return render_template(username)



# 팀페이지 댓글 기능
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
    return jsonify({'msg': '수정완료!'})
# 삭제 <- remove(num)
@app.route("/test/remove", methods=["POST"])
def remove():
    num1_receive = request.form['num1_give']
    num2_receive = request.form['num2_give']
    num3_receive = request.form['num3_give']
    db.test.delete_one({'num1': int(num1_receive), 'num2': int(num2_receive), 'num3': int(num3_receive)})
    return jsonify({'msg': '삭제!'})





# 범석페이지 댓글 기능

@app.route("/beom", methods=["POST"])
def beeom_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.beom.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@app.route("/beom", methods=["GET"])
def beom_get():
    comment_list = list(db.beom.find({},{'_id':False}))
    return jsonify({'comments':comment_list})

# 승준 페이지 댓글 기능
@app.route("/seungjun", methods=["POST"])
def seungjun_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    comment_list = list(db.seungjun.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }

    db.seungjun.insert_one(doc)
    return jsonify({'msg': '작성완료'})

@app.route("/seungjun", methods=["GET"])
def seungjun_get():
    comment_list = list(db.seungjun.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/seungjun/delete', methods=['POST'])
def seungjun_delete():
    num_receive = request.form['num_give']
    db.seungjun.update_one({'num': int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '삭제 완료!'})


# 기민 페이지 댓글 기능
@app.route("/gimin", methods=["POST"])
def gimin_post():
   name_receive = request.form['name_give']
   comment_receive = request.form['comment_give']

   doc = {
      'name':name_receive,
      'comment':comment_receive
   }

   db.gimin.insert_one(doc)


   return jsonify({'msg': '응원 완료!'})

@app.route("/gimin", methods=["GET"])
def gimin_get():
   comment_list = list(db.gimin.find({}, {'_id': False}))
   return jsonify({'comments': comment_list})



# 학수 페이지 댓글 기능
@app.route("/haksoo", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.haksoo.insert_one(doc)
    return jsonify({'msg': '댓글작성 완료!'})


@app.route("/haksoo", methods=["GET"])
def comment_get():
    haksoo_list = list(db.haksoo.find({}, {'_id': False}))
    return jsonify({'haksoos': haksoo_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5555, debug=True)

