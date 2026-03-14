README.md
Programming Risk Prediction Dashboard

โปรเจคนี้เป็นระบบ Machine Learning Dashboard สำหรับพยากรณ์ความเสี่ยงที่นักศึกษาจะตกวิชา Programming โดยใช้ข้อมูลพฤติกรรมการเรียน เช่น ชั่วโมงเรียน การขาดเรียน และคะแนนสอบ

ระบบถูกพัฒนาด้วย

Python
Dash
Plotly
PyCaret
โครงสร้างโปรเจค
project
│
app.py
train_model.py
dataset.csv
model_programming.pkl
requirements.txt
README.md
│
modules
│   prediction.py
│   charts.py
│   data_cleaning.py
│
pages
│   prediction_page.py
│   analytics_page.py
│   model_page.py
│
assets
│   style.css
วิธีติดตั้งและใช้งาน
1. Clone repository
git clone https://github.com/your-repository/project-name.git
cd project-name
2. สร้าง Virtual Environment

สร้าง venv

python -m venv venv

เปิดใช้งาน venv

Windows
venv\Scripts\activate
Mac / Linux
source venv/bin/activate
3. ติดตั้ง Library

ติดตั้ง dependencies

pip install -r requirements.txt
4. Train Machine Learning Model

ก่อนใช้งาน dashboard ต้อง train โมเดลก่อน

python train_model.py

ระบบจะสร้างไฟล์

model_programming.pkl
5. รัน Dashboard
python app.py

เปิดเว็บที่

http://127.0.0.1:8050
วิธีใช้งานระบบ

ปรับค่าพารามิเตอร์ เช่น

ชั่วโมงเรียน
จำนวนครั้งขาดเรียน
คะแนนกลางภาค
คะแนนก่อนสอบปลายภาค

กดปุ่ม

พยากรณ์

ระบบจะแสดง

ผลการพยากรณ์
ระดับความเสี่ยง
คำแนะนำ
เทคโนโลยีที่ใช้
Python
Dash
Plotly
PyCaret
Pandas
Scikit-learn
Dataset

ใช้

Student Performance Dataset
UCI Machine Learning Repository
หมายเหตุ

ระบบนี้เป็น prototype สำหรับการทดลองใช้ Machine Learning ในการวิเคราะห์ความเสี่ยงของนักศึกษา
