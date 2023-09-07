from flask_webgoat import create_app

app = create_app()

@app.after_request
def add_csp_headers(response):
    # vulnerability: Broken Access Control
    AWS_ACCESS_KEY_ID="ASIAW375RVVHUEL2RWGF"
    response.headers['Access-Control-Allow-Origin'] = '*'
    # vulnerability: Security Misconfiguration
    response.headers['Content-Security-Policy'] = "script-src 'self' 'unsafe-inline'"
    return response

if __name__ == '__main__':
    app.run()
