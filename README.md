<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每句练耳</title>
</head>

<body>

<h1>🎧 每句练耳</h1>

<h2>✈️ Airport</h2>

<p id="sentence">Good morning.</p>

<button onclick="speak()">▶ 播放</button>

<script>

function speak() {

let text = document.getElementById("sentence").innerText;

let voice = new SpeechSynthesisUtterance(text);

voice.lang = "en-US";

voice.rate = 0.75;

speechSynthesis.speak(voice);

}

</script>

</body>
</html>
