from flask import Flask, render_template_string

app = Flask(__name__)

# This is our single "Template" shared across all pages
# It includes the CSS and the structure so you don't need a static folder
BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Single File Flask App</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; margin: 0; background-color: #f4f4f4; }
        nav { background: #333; color: #fff; padding: 1rem; text-align: center; }
        nav a { color: #fff; margin: 0 15px; text-decoration: none; font-weight: bold; }
        .container { max-width: 800px; margin: 20px auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        footer { text-align: center; margin-top: 20px; font-size: 0.8rem; color: #777; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
    <div class="container">
        {{ content | safe }}
    </div>
    <footer>Powered by a single app.py file</footer>
</body>
</html>
"""

@app.route('/')
def home():
    page_content = """
        <h1>Welcome to the Homepage</h1>
        <p>This entire website is running from a single Python file.</p>
        <p>No <code>templates/</code> folder, no <code>static/</code> folder—just pure Flask logic.</p>
    """
    return render_template_string(BASE_HTML, content=page_content)

@app.route('/about')
def about():
    page_content = """
        <h1>About This Project</h1>
        <p>This is a demonstration of how Flask can render HTML strings directly.</p>
        <ul>
            <li><strong>Route 1:</strong> Home</li>
            <li><strong>Route 2:</strong> About</li>
        </ul>
    """
    return render_template_string(BASE_HTML, content=page_content)

@app.route('/contact')
def contact():
    page_content = "<h1>Contact</h1><p>Email us at: flask@example.com</p>"
    return render_template_string(BASE_HTML, content=page_content)

if __name__ == '__main__':
    app.run(debug=True)