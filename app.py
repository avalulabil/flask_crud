from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Sederhana sebagai pengganti database
books = []

# Read - Menampilkan daftar buku
@app.route('/')
def index():
    return render_template('index.html', books=books)

# Create - Menambah buku baru
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published_date = request.form['published_date']
        books.append({'title': title, 'author': author, 'published_date': published_date})
        return redirect(url_for('index'))
    return render_template('create.html')

# Update - Mengupdate data buku
@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    book = books[index]
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['published_date'] = request.form['published_date']
        return redirect(url_for('index'))
    return render_template('update.html', book=book, index=index)

# Delete - Menghapus buku
@app.route('/delete/<int:index>', methods=['GET', 'POST'])
def delete(index):
    if request.method == 'POST':
        books.pop(index)
        return redirect(url_for('index'))
    return render_template('delete.html', book=books[index])

if __name__ == '__main__':
    app.run(debug=True)
