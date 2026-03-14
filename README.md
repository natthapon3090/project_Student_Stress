## ขั้นตอนก่อนรันโปรเจค

1. Clone โปรเจค

git clone <repository-url>
cd <project-folder>


2. สร้าง Virtual Environment

python -m venv venv


3. เปิดใช้งาน Virtual Environment

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate


4. ติดตั้ง Library

pip install -r requirements.txt


5. Train Machine Learning Model

python train_model.py


6. รัน Dashboard

python app.py


7. เปิดเว็บ

http://127.0.0.1:8050



clone → venv → install → train model → run app
