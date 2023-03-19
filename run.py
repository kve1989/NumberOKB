from app import app
import os

"""Проверяем на наличие папки для загрузок"""
if (not(os.path.exists(app.config['UPLOAD_FOLDER']))):
    os.mkdir(app.config['UPLOAD_FOLDER'])

if __name__ == '__main__':
    app.run(debug=True)
