from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserLocation  

def location_page(request):
    return HttpResponse("""

                        
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Location App</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        body {
            background: linear-gradient(120deg, #e0ffe0, #c0f4e0);
            animation: bgShift 15s ease-in-out infinite alternate;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        @keyframes bgShift {
            0% {
                background-position: 0% 50%;
            }
            100% {
                background-position: 100% 50%;
            }
        }

        #form-section, #thank-you-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            z-index: 10;
        }

        #intro-text {
            font-size: 24px;
            color: #2e7d32;
            margin-bottom: 20px;
            animation: fadeSlide 1s ease-in-out;
        }

        @keyframes fadeSlide {
            0% {
                opacity: 0;
                transform: translateY(-30px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        input, button {
            padding: 12px 18px;
            font-size: 16px;
            border-radius: 5px;
            border: 2px solid #4CAF50;
            margin: 10px;
            transition: all 0.3s ease;
        }

        input:focus {
            outline: none;
            border-color: #388e3c;
            box-shadow: 0 0 8px #a5d6a7;
        }

        button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }

        #status {
            margin-top: 10px;
            font-weight: bold;
            color: #2e7d32;
        }

        #thank-you-section {
            display: none;
            position: absolute;
            top: 0; left: 0;
            height: 100%;
            width: 100%;
            background: linear-gradient(to top right, #e0ffe0, #b2f7b2);
            z-index: 100;
            justify-content: center;
            animation: fadeIn 1s ease-in-out forwards;
        }

        #thank-you-message {
            font-size: 32px;
            color: #2e7d32;
            margin-bottom: 20px;
        }

        .emoji {
            position: absolute;
            font-size: 28px;
            animation: floatUp 6s infinite ease-in-out;
            opacity: 0;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes floatUp {
            0% {
                transform: translateY(0);
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <!-- Floating emojis background -->
    <script>
        const bgEmojis = ['🍃', '🌿', '✨', '🌼', '💫', '🍀'];
        for (let i = 0; i < 20; i++) {
            const el = document.createElement('div');
            el.classList.add('emoji');
            el.innerText = bgEmojis[Math.floor(Math.random() * bgEmojis.length)];
            el.style.left = `${Math.random() * 100}%`;
            el.style.top = `${100 + Math.random() * 50}px`;
            el.style.animationDuration = `${4 + Math.random() * 5}s`;
            el.style.fontSize = `${18 + Math.random() * 22}px`;
            document.body.appendChild(el);
        }
    </script>

    <div id="form-section">
        <div id="intro-text">🌱 Hey there! Kindly to share your name</div>
        <input type="text" id="username" placeholder="Enter your name" />
        <button onclick="getLocation()">Submit</button>
        <p id="status"></p>
    </div>

    <div id="thank-you-section">
        <h1 id="thank-you-message">Thanks!</h1>
    </div>

    <script>
        function getLocation() {
            const status = document.getElementById('status');
            const username = document.getElementById('username').value.trim();

            if (!username) {
                status.innerText = "Please enter your name first.";
                return;
            }

            if (navigator.geolocation) {
                status.innerText = "Requesting...";
                navigator.geolocation.getCurrentPosition((pos) => {
                    const data = {
                        name: username,
                        lat: pos.coords.latitude,
                        lng: pos.coords.longitude
                    };

                    fetch('/report/', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(data)
                    }).then(res => {
                        if (res.ok) {
                            showThankYou(username);
                        } else {
                            status.innerText = "Try Again.";
                        }
                    });
                }, () => {
                    status.innerText = "Denied.";
                });
            } else {
                status.innerText = "Geolocation not supported.";
            }
        }

        function showThankYou(name) {
            document.getElementById('form-section').style.display = 'none';

            const section = document.getElementById('thank-you-section');
            section.style.display = 'flex';

            const message = document.getElementById('thank-you-message');
            const compliments = [
                "You're amazing 🌟",
                "Thanks, buddy! 💚",
                "You made our day! 🌸",
                "You're awesome 🌿",
                "Big thanks, dude! 🚀"
            ];
            const randomCompliment = compliments[Math.floor(Math.random() * compliments.length)];
            message.innerText = `Thank you, ${name}! ${randomCompliment}`;

            const emojis = ['🌼', '🌿', '🌸', '🌻', '🍀', '🌺', '💐'];
            for (let i = 0; i < 25; i++) {
                const el = document.createElement('div');
                el.classList.add('emoji');
                el.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                el.style.left = `${Math.random() * 100}%`;
                el.style.top = `${100 + Math.random() * 50}px`;
                el.style.animationDuration = `${3 + Math.random() * 4}s`;
                el.style.fontSize = `${20 + Math.random() * 25}px`;
                document.getElementById('thank-you-section').appendChild(el);
            }
        }
    </script>
</body>
</html>



    """)


@csrf_exempt
def report_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name')
            lat = data.get('lat')
            lng = data.get('lng')

            # Save to database
            UserLocation.objects.create(name=name, lat=lat, lng=lng)

            print(f"✅ Saved: {name} at Latitude={lat}, Longitude={lng}")
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': 'invalid data'}, status=400)

    return JsonResponse({'error': 'POST only'}, status=405)