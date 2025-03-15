from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
import os.path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
def init_db():
    if not os.path.exists('site.db'):
        with sqlite3.connect('site.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
            c.execute('''CREATE TABLE stories (id INTEGER PRIMARY KEY, title TEXT, content TEXT, user_id INTEGER)''')
            c.execute('''CREATE TABLE contributions (id INTEGER PRIMARY KEY, content TEXT, user_id INTEGER, story_id INTEGER)''')
            conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('site.db') as conn:
            c = conn.cursor()
            # Check if the username already exists
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            if c.fetchone():
                flash('Username already exists. Please choose a different username.', 'danger')
                return redirect(url_for('register'))
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('site.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = c.fetchone()
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('homepage'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with sqlite3.connect('site.db') as conn:
        c = conn.cursor()
        # Get stories created by the user
        c.execute('SELECT * FROM stories WHERE user_id = ?', (user_id,))
        user_stories = c.fetchall()
        # Get stories the user has contributed to (excluding stories created by the user)
        c.execute('''SELECT DISTINCT stories.id, stories.title
                     FROM stories
                     JOIN contributions ON stories.id = contributions.story_id
                     WHERE contributions.user_id = ? AND stories.user_id != ?''', (user_id, user_id))
        contributed_stories = c.fetchall()
        # Get stories the user can edit (not created or contributed to)
        c.execute('''SELECT DISTINCT stories.id, stories.title
                     FROM stories
                     LEFT JOIN contributions ON stories.id = contributions.story_id
                     WHERE stories.user_id != ?
                     AND stories.id NOT IN (SELECT story_id FROM contributions WHERE user_id = ?)''', (user_id, user_id))
        editable_stories = c.fetchall()
    return render_template('homepage.html', user_stories=user_stories, contributed_stories=contributed_stories, editable_stories=editable_stories, username=session['username'])

@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        with sqlite3.connect('site.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO stories (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
            conn.commit()
        return redirect(url_for('homepage'))
    return render_template('new_story.html')

@app.route('/add_to_story/<int:story_id>', methods=['GET', 'POST'])
def add_to_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with sqlite3.connect('site.db') as conn:
        c = conn.cursor()
        # Check if the user has already contributed to the story
        c.execute('SELECT * FROM contributions WHERE user_id = ? AND story_id = ?', (user_id, story_id))
        if c.fetchone():
            flash('You have already contributed to this story.', 'danger')
            return redirect(url_for('homepage'))
        if request.method == 'POST':
            content = request.form['content']
            c.execute('INSERT INTO contributions (content, user_id, story_id) VALUES (?, ?, ?)', (content, user_id, story_id))
            conn.commit()
            return redirect(url_for('homepage'))
        # Get the latest contribution to the story
        c.execute('SELECT content FROM contributions WHERE story_id = ? ORDER BY id DESC LIMIT 1', (story_id,))
        latest_contribution = c.fetchone()
        if not latest_contribution:
            # If no contributions, show the initial story content
            c.execute('SELECT content FROM stories WHERE id = ?', (story_id,))
            latest_contribution = c.fetchone()
    return render_template('add_to_story.html', story_id=story_id, latest_contribution=latest_contribution)

@app.route('/view_story/<int:story_id>')
def view_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with sqlite3.connect('site.db') as conn:
        c = conn.cursor()
        # Check if the user has contributed to the story or is the author
        c.execute('SELECT * FROM stories WHERE id = ? AND user_id = ?', (story_id, user_id))
        story = c.fetchone()
        if not story:
            c.execute('SELECT * FROM contributions WHERE user_id = ? AND story_id = ?', (user_id, story_id))
            contribution = c.fetchone()
            if not contribution:
                flash('You can only view the full story after contributing to it.', 'danger')
                return redirect(url_for('homepage'))
        # Get the full story content and contributions
        c.execute('SELECT content FROM stories WHERE id = ?', (story_id,))
        story_content = c.fetchone()[0]
        c.execute('SELECT content FROM contributions WHERE story_id = ?', (story_id,))
        contributions = c.fetchall()
        full_story = story_content + ' '.join([contribution[0] for contribution in contributions])
    return render_template('view_story.html', full_story=full_story)

if __name__ == "__main__":
    app.run(debug=True)
