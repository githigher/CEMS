import os
import random
import shutil
import string
import datetime
from PIL import Image
from io import BytesIO

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pymysql
from pydantic import BaseModel

app = FastAPI()
# 解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class LoginClass(BaseModel):
    id: str
    password: str


@app.post("/login")
async def login(lc: LoginClass):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                           db='student_evaluation_and_management_system', charset='utf8')
    # 创建游标对象
    cursor = conn.cursor()
    cursor.execute("select * from admin where id = %s and password = %s", (lc.id, lc.password))
    conn.commit()
    results = cursor.fetchall()
    if len(results) != 0:
        return {"code": "003", "id": results[0][0], "msg": "登陆成功"}
    cursor.execute("select * from student where id = %s and password = %s", (lc.id, lc.password))
    conn.commit()
    results = cursor.fetchall()
    # 关闭游标对象
    cursor.close()
    # 关闭连接
    conn.close()
    if len(results) != 0:
        return {"code": "001", "id": results[0][0], "msg": "登陆成功"}
    else:
        return {"code": "002", "msg": "账号密码错误"}


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


# 上传图片时，把照片保存在本地
@app.post("/imgs/upload")
def upload_image(file: UploadFile = File(...)):
    # 获取当前文件所在的目录路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建目标文件夹路径
    target_folder = os.path.join(current_dir, "img")
    # 确保目标文件夹存在
    os.makedirs(target_folder, exist_ok=True)
    # 生成随机字符串作为文件名
    file_name = generate_random_string(8)
    # 获取文件的扩展名
    extension = os.path.splitext(file.filename)[1]
    # 构建文件的完整路径
    file_path = os.path.join(target_folder, f"{file_name}{extension}")
    # 保存文件到目标路径
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # 返回文件的名字
    return {"data": {"url": f"{file_name}{extension}"}}


class SubmitClass(BaseModel):
    id: str
    picture: str
    type: str
    summary: str
    score: str
    unit: str
    grade: str
    people: str


# 提交表单
@app.post("/submit")
async def upload(sc: SubmitClass):
    try:
        now = datetime.datetime.now()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        sql = "insert into record values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '正在审核', '')".format(
            sc.id, str(now), sc.picture, sc.type, sc.summary, sc.score, sc.unit, sc.grade, sc.people)
        cursor.execute(sql)
        conn.commit()
        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001"}
    except Exception as err:
        return {"code": "002"}


from fastapi.responses import FileResponse


@app.get('/img')
def get_image(name):
    # 获取与 Python 文件同级的目录路径
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # 构建图片文件路径
    image_path = os.path.join(base_dir, "img", name)
    print(image_path)
    if os.path.exists(image_path):
        # 返回图片作为响应
        return FileResponse(image_path, media_type="image/jpeg")
    else:
        # 如果图片不存在，返回错误信息
        return {"error": "Image not found."}


class GetSubmit(BaseModel):
    id: str


# 得到提交列表
@app.post("/getSubmit")
async def get_submit(gs: GetSubmit):
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        # 按照提交时间先后进行排序
        sql = "select * from record where id = '{}' order by record_time desc".format(gs.id)
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()

        # 返回userId的提交记录
        my_list = []
        for i in results:
            tmp_dist = {'date': i[1], 'evidence': 'http://127.0.0.1:8000/img?name=' + i[2], 'category': i[3],
                        'summary': i[4], 'score': i[5],
                        'unit': i[6], 'grade': i[7], 'people': i[8], 'state': i[9], 'notes': i[10]}
            my_list.append(tmp_dist)

        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001", "res": my_list}
    except Exception as err:
        return {"code": "002"}


# 综合能力展示
@app.post("/GetComprehensiveCapability")
async def get_comprehensive_capability(gs: GetSubmit):
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        sql = "select * from record where id = '{}' and state = '已通过'".format(gs.id)
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()
        my_list = []
        for i in range(7):
            # 思想政治与道德素养
            # 学科竞赛与技能培训
            # 社会实践与志愿服务
            # 文化活动
            # 学生干部任职
            # 体育活动
            # 劳育活动
            tmp_dist = {'value': 0}
            my_list.append(tmp_dist)
        for i in results:
            if i[3] == '思想政治与道德素养':
                my_list[0]['value'] += eval(i[5])
            elif i[3] == '学科竞赛与技能培训':
                my_list[1]['value'] += eval(i[5])
            elif i[3] == '社会实践与志愿服务':
                my_list[2]['value'] += eval(i[5])
            elif i[3] == '文化活动':
                my_list[3]['value'] += eval(i[5])
            elif i[3] == '学生干部任职':
                my_list[4]['value'] += eval(i[5])
            elif i[3] == '体育比赛' or i[3] == '军训阅兵' or i[3] == '参加学校田径运动会开幕式、团体啦啦操和百里毅行' or i[3] == '裁判证':
                my_list[5]['value'] += eval(i[5])
            else:
                my_list[6]['value'] += eval(i[5])

        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001", "res": my_list}
    except Exception as err:
        return {"code": "002"}


# 加分情况展示
@app.post("/GetBonusPoints")
async def get_bonus_points(gs: GetSubmit):
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        sql = "select * from record where id = '{}' and state = '已通过'".format(gs.id)
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()

        my_list = []
        for i in range(3):
            # 劳育
            # 体育
            # 德育
            tmp_dist = {'value': 0}
            my_list.append(tmp_dist)
        for i in results:
            if i[3] == '思想政治与道德素养' or i[3] == '学科竞赛与技能培训' or i[3] == '社会实践与志愿服务' or i[3] == '文化活动' or i[3] == '学生干部任职':
                my_list[2]['value'] += eval(i[5])
            elif i[3] == '体育比赛' or i[3] == '军训阅兵' or i[3] == '参加学校田径运动会开幕式、团体啦啦操和百里毅行' or i[3] == '裁判证':
                my_list[1]['value'] += eval(i[5])
            else:
                my_list[0]['value'] += eval(i[5])

        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001", "res": my_list}
    except Exception as err:
        return {"code": "002"}


class ChangePassword(BaseModel):
    id: str
    new_password: str
    again_password: str


# 修改密码
@app.post("/ChangePassword")
async def change_password(cp: ChangePassword):
    try:
        if cp.new_password != cp.again_password:
            return {"code": "003"}
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        sql = "update student set password='{}' where id = '{}'".format(cp.new_password, cp.id)
        cursor.execute(sql)
        conn.commit()
        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001"}
    except Exception as err:
        return {"code": "002"}


# 获取审核列表
@app.post("/examine")
async def get_submit():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()
        # 按照提交时间先后进行排序
        sql = "select * from record where state = '正在审核' order by record_time desc"
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()

        # 返回userId的提交记录
        my_list = []
        for i in results:
            tmp_dist = {'date': i[1], 'evidence': 'http://127.0.0.1:8000/img?name=' + i[2], 'category': i[3],
                        'summary': i[4], 'score': i[5],
                        'unit': i[6], 'grade': i[7], 'people': i[8], 'notes': i[10]}
            my_list.append(tmp_dist)

        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001", "res": my_list}
    except Exception as err:
        return {"code": "002"}


class ExamineSubmit(BaseModel):
    date: str
    evidence: str
    score: str
    notes: str


from urllib.parse import parse_qs, urlparse


# 审核通过
@app.post("/ExamineSubmit")
async def c(es: ExamineSubmit):
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456',
                               db='student_evaluation_and_management_system', charset='utf8')
        # 创建游标对象
        cursor = conn.cursor()

        # 根据url获取图片名
        parsed_url = urlparse(es.evidence)
        query_params = parse_qs(parsed_url.query)
        es.evidence = query_params.get('name')[0] if query_params.get('name') else None

        sql = "update record set state='已通过', score='{}', notes='{}' where record_time = '{}' and picture = '{}'".format(es.score, es.notes, es.date, es.evidence)
        cursor.execute(sql)
        conn.commit()
        # 关闭游标对象
        cursor.close()
        # 关闭连接
        conn.close()
        return {"code": "001"}
    except Exception as err:
        return {"code": "002"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
