from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://testco:sparta@cluster0.wewsxn0.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta


@app.route('/')
def home():
    return render_template('homework.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    comment_list = list(db.homework.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }

    db.homework.insert_one(doc)
    return jsonify({'msg': '작성완료'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/homework/delete', methods=['POST'])
def homework_delete():
    num_receive = request.form['num_give']
    db.homework.update_one({'num': int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)