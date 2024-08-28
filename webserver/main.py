import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()


#Con un decorador se indica la ruta para acceder al recurso List
@app.get('/')
def get_list():
    return [1,2,3,]

#Con un decorador se indica otra ruta para acceder al recurso Contact
@app.get('/contact', response_class=HTMLResponse)
async def get_list():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Server Test</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f8ff;
                color: #333;
            }
            h1 {
                color: #0073e6;
            }
            #fun-button {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                background-color: #0073e6;
                color: white;
                border: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            #fun-button:hover {
                background-color: #005bb5;
            }
            #output {
                margin-top: 20px;
                font-size: 18px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>

        <h1>Welcome to the Web Server Test!</h1>
        <p>Click the button below to see something fun happen!</p>
        <button id="fun-button" onclick="showMessage()">Click Me!</button>
        <div id="output"></div>

        <script>
            function showMessage() {
                const messages = [
                    "Hello, Web Explorer!",
                    "You're awesome!",
                    "Isn't this fun?",
                    "Your server is working perfectly!",
                    "Keep up the great work!"
                ];
                const randomMessage = messages[Math.floor(Math.random() * messages.length)];
                document.getElementById('output').innerText = randomMessage;
            }
        </script>

    </body>
    </html>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()