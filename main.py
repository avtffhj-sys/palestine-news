from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    news = [
        {
            'title': 'القدس: تطورات جديدة في البلدة القديمة',
            'category': 'سياسة',
            'date': '2026-07-21',
            'comments': 34,
            'image': 'city'
        },
        {
            'title': 'أهالي غزة يطلقون حملة إغاثة',
            'category': 'مجتمع',
            'date': '2026-07-20',
            'comments': 18,
            'image': 'people-arrows'
        },
        {
            'title': 'المسجد الأقصى يستقبل المصلين',
            'category': 'دين',
            'date': '2026-07-19',
            'comments': 27,
            'image': 'kaaba'
        },
        {
            'title': 'معرض الفن التشكيلي في رام الله',
            'category': 'ثقافة',
            'date': '2026-07-18',
            'comments': 12,
            'image': 'palette'
        }
    ]
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)