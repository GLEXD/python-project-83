import os
import psycopg2
from psycopg2.extras import DictCursor
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urlparse
import validators

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret')
DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=DictCursor)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls')
def urls_list():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM urls ORDER BY id DESC')
            urls = cur.fetchall()
    return render_template('urls.html', urls=urls)


@app.route('/urls', methods=['POST'])
def add_url():
    url = request.form.get('url')

    if not url or not validators.url(url):
        flash('Некорректный URL', 'danger')
        return render_template('index.html'), 422

    normalized_url = urlparse(url).scheme + '://' + urlparse(url).netloc

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT id FROM urls WHERE name = %s', (normalized_url,))
            existing = cur.fetchone()
            if existing:
                flash('Страница уже существует', 'info')
                return redirect(url_for('url_page', id=existing['id']))

            cur.execute(
                'INSERT INTO urls (name, created_at) VALUES (%s, %s) RETURNING id',
                (normalized_url, datetime.now())
            )
            conn.commit()
            new_id = cur.fetchone()['id']
            flash('Страница успешно добавлена', 'success')
            return redirect(url_for('url_page', id=new_id))


@app.route('/urls/<int:id>')
def url_page(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM urls WHERE id = %s', (id,))
            url_data = cur.fetchone()
            if not url_data:
                flash('Страница не найдена', 'warning')
                return redirect(url_for('urls_list'))
    return render_template('url.html', url=url_data)
