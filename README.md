# Hello World Web Application

A simple Flask-based Hello World web application.

## Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python3 app.py
```

3. Open your browser and visit: `http://localhost:5000`

## Making It Accessible Over the Internet

### Option 1: Using ngrok (Easiest for Testing)
1. Download and install [ngrok](https://ngrok.com/)
2. Run your Flask app: `python3 app.py`
3. In another terminal, run: `ngrok http 5000`
4. ngrok will provide a public URL (e.g., https://abc123.ngrok.io)

### Option 2: Deploy to Cloud Platforms

#### Deploy to Heroku:
1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: python app.py
   ```
3. Deploy:
   ```bash
   heroku create
   git push heroku main
   ```

#### Deploy to Render/Railway/Vercel:
- Connect your GitHub repository
- These platforms will auto-detect Flask and deploy

#### Deploy to PythonAnywhere (Free):
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your code
3. Configure a web app pointing to `app.py`

### Option 3: Use Your Own Server
If you have a VPS or server:
1. Install dependencies
2. Run with Gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
3. Set up a reverse proxy with Nginx
4. Configure your domain to point to your server

## Files

- `hello_world.py` - Simple command-line Hello World
- `app.py` - Flask web application
- `requirements.txt` - Python dependencies
