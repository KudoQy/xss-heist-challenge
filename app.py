from flask import Flask, request, render_template

app = Flask(__name__)

# --- The XSS Vulnerability lies here! ---
@app.route('/vault-search')
def vault_search():
    # Get the 'query' parameter from the URL (e.g., /vault-search?query=something)
    search_query = request.args.get('query', '')

    # --- THIS IS THE VULNERABLE PART ---
    # We are directly passing the user input 'search_query' to the template
    # and in the template, we will explicitly tell Jinja2 NOT to escape it.
    # This allows injected HTML/JavaScript to be rendered by the browser.
    return render_template('vault_search.html', user_input=search_query)

# --- Basic Home Page (Optional, but good for navigation) ---
@app.route('/')
def index():
    return "<h1>Welcome to the Heist CTF!</h1><p>Navigate to the <a href='/vault-search'>Vault Search</a> to begin the challenge.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
