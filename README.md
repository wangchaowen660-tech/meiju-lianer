对，伙计。👍 这次直接给你完整代码，100句已经放进去。

你现在只操作现有的 index.html：

编辑 → 全选旧代码 → 删除 → 粘贴下面全部代码 → 提交更改。

<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每句练耳 · Chaowen AI</title>
<style>
body {
    margin: 0;
    background: #f5f7fa;
    font-family: Arial, sans-serif;
    color: #222;
}
.container {
    max-width: 520px;
    margin: auto;
    padding: 22px 16px;
}
h1 {
    text-align: center;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 22px;
}
.card {
    background: white;
    border-radius: 22px;
    padding: 22px 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,.08);
}
.scene {
    text-align: center;
    color: #777;
    margin-bottom: 10px;
}
.progress {
    text-align: center;
    color: #888;
    margin-bottom: 20px;
}
.label {
    color: #777;
    font-size: 14px;
    text-align: center;
    margin: 12px 0;
}
.sentence {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
    min-height: 90px;
    display: flex;
    align-items: center;
    justify-content: center;
}
button {
    width: 100%;
    border: none;
    border-radius: 15px;
    padding: 14px;
    margin: 5px 0;
    font-size: 17px;
    font-weight: bold;
}
.play {
    background: #222;
    color: white;
}
.next {
    background: #222;
    color: white;
}
.other {
    background: #edf0f4;
}
.answer,
.chunks,
.meaning {
    display: none;
    margin-top: 12px;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}
.answer {
    background: #eef6ff;
    font-size: 20px;
    font-weight: bold;
}
.chunks {
    background: #f5f5f5;
    line-height: 1.8;
}
.meaning {
    background: #fff8e8;
}
.timer {
    text-align: center;
    color: #777;
    min-height: 25px;
    margin: 12px;
}
.status {
    text-align: center;
    color: #777;
    min-height: 25px;
}
</style>
</head>
<body>
<div class="container">
<h1>🎧 每句练耳</h1>
<div class="subtitle">
Chaowen AI · 一句一句听懂
</div>
<div class="card">
<div id="scene" class="scene"></div>
<div id="progress" class="progress"></div>
<div class="label">
🎧 对方说
</div>
<div id="sentence" class="sentence"></div>
<button class="play" onclick="playQuestion()">
▶ 播放
</button>
<button class="other" onclick="playQuestion()">
🔁 再听一次
</button>
<div id="timer" class="timer"></div>
<div class="label">
🗣️ 现在轮到你回答
</div>
<button class="other" onclick="showAnswer()">
👀 显示标准回答
</button>
<div id="answer" class="answer"></div>
<button class="other" onclick="playAnswer()">
🔊 听标准回答
</button>
<button class="other" onclick="showMeaning()">
🇨🇳 看中文意思
</button>
<div id="meaning" class="meaning"></div>
<button class="other" onclick="showChunks()">
🧩 看英语词块
</button>
<div id="chunks" class="chunks"></div>
<button class="next" onclick="nextSentence()">
➡️ 下一句
</button>
<div id="status" class="status">
准备好了
</div>
</div>
</div>
<script>
const lessons = [
/* ===== 机场 1-15 ===== */
["✈️ 机场","Good morning.","Good morning.","早上好。","Good morning"],
["✈️ 机场","May I see your passport?","Sure. Here is my passport.","可以看看你的护照吗？","May I see...? · your passport"],
["✈️ 机场","Where are you going?","I'm going to China.","你要去哪里？","Where are you going? · I'm going to..."],
["✈️ 机场","Do you have any bags to check in?","Yes, I have one bag.","你有行李要托运吗？","Do you have...? · bags to check in"],
["✈️ 机场","How many bags do you have?","I have two bags.","你有几个行李？","How many...? · do you have?"],
["✈️ 机场","Do you want a window seat?","Yes, please.","你想要靠窗的座位吗？","Do you want...? · a window seat"],
["✈️ 机场","Do you have any carry-on luggage?","Yes, I have one bag.","你有随身行李吗？","Do you have...? · carry-on luggage"],
["✈️ 机场","Here is your boarding pass.","Thank you.","这是你的登机牌。","Here is your... · boarding pass"],
["✈️ 机场","What is your flight number?","My flight number is 123.","你的航班号是多少？","What is your... · flight number"],
["✈️ 机场","What time is your flight?","My flight is at ten.","你的航班几点？","What time is... · your flight"],
["✈️ 机场","Your gate is twelve.","Thank you.","你的登机口是12号。","Your gate is..."],
["✈️ 机场","Boarding starts at ten thirty.","Okay. Thank you.","10:30开始登机。","Boarding starts at..."],
["✈️ 机场","Is this your first time here?","Yes, it is.","这是你第一次来这里吗？","Is this your first time...?"],
["✈️ 机场","Do you need any help?","Yes, please.","你需要帮助吗？","Do you need...? · any help"],
["✈️ 机场","Have a nice flight.","Thank you.","祝你旅途愉快。","Have a nice..."],
/* ===== 酒店 16-25 ===== */
["🏨 酒店","Do you have a reservation?","Yes, I have a reservation.","你有预订吗？","Do you have...? · a reservation"],
["🏨 酒店","May I see your passport?","Sure. Here you are.","可以看看你的护照吗？","May I see...? · your passport"],
["🏨 酒店","What is your name?","My name is Wang.","你叫什么名字？","What is your name?"],
["🏨 酒店","How many nights are you staying?","I'm staying for three nights.","你住几个晚上？","How many nights...? · staying"],
["🏨 酒店","What time is check-in?","Check-in is at two.","几点可以入住？","What time is check-in?"],
["🏨 酒店","What time is check-out?","Check-out is at noon.","几点退房？","What time is check-out?"],
["🏨 酒店","Where is my room?","Your room is upstairs.","我的房间在哪里？","Where is...? · my room"],
["🏨 酒店","Do you have Wi-Fi?","Yes, we do.","有无线网络吗？","Do you have...? · Wi-Fi"],
["🏨 酒店","What is the Wi-Fi password?","I'll give it to you.","Wi-Fi密码是什么？","What is the... · password"],
["🏨 酒店","Could I have another towel?","Of course.","可以再给我一条毛巾吗？","Could I have...? · another towel"],
/* ===== 餐厅 26-40 ===== */
["🍽️ 餐厅","A table for two, please.","Sure. This way, please.","请安排两个人的桌子。","A table for two"],
["🍽️ 餐厅","May I see the menu?","Of course.","可以看看菜单吗？","May I see...? · the menu"],
["🍽️ 餐厅","What do you recommend?","I recommend the fish.","你推荐什么？","What do you recommend?"],
["🍽️ 餐厅","Are you ready to order?","Yes, I'm ready.","准备好点餐了吗？","Are you ready to...?"],
["🍽️ 餐厅","I'd like some chicken.","Sure.","我想要一些鸡肉。","I'd like... · some chicken"],
["🍽️ 餐厅","Can I have some water?","Sure.","可以给我一些水吗？","Can I have...? · some water"],
["🍽️ 餐厅","Is this spicy?","No, it isn't.","这个辣吗？","Is this... · spicy?"],
["🍽️ 餐厅","Can you make it less spicy?","Sure.","可以做得不那么辣吗？","Can you make it...?"],
["🍽️ 餐厅","What comes with this?","It comes with rice.","这个配什么？","What comes with...?"],
["🍽️ 餐厅","I'd like some rice.","Sure.","我想要一些米饭。","I'd like... · some rice"],
["🍽️ 餐厅","Can I get another plate?","Of course.","可以再给我一个盘子吗？","Can I get...? · another plate"],
["🍽️ 餐厅","Could we have the bill, please?","Certainly.","请给我们账单。","Could we have...? · the bill"],
["🍽️ 餐厅","Can I pay by card?","Yes, you can.","可以刷卡吗？","Can I pay...? · by card"],
["🍽️ 餐厅","Is service included?","Yes, it is.","包含服务费吗？","Is service included?"],
["🍽️ 餐厅","Thank you for your help.","You're welcome.","谢谢你的帮助。","Thank you for..."],
/* ===== 购物 41-50 ===== */
["🛒 购物","How much is this?","It's ten dollars.","这个多少钱？","How much is...?"],
["🛒 购物","Do you have a larger size?","Yes, we do.","有大一点的尺寸吗？","Do you have...? · a larger size"],
["🛒 购物","Do you have a smaller size?","Yes, we do.","有小一点的尺寸吗？","Do you have...? · a smaller size"],
["🛒 购物","Can I try this on?","Sure.","我可以试一下吗？","Can I try...? · this on"],
["🛒 购物","Do you have another color?","Yes, we do.","有其他颜色吗？","Do you have...? · another color"],
["🛒 购物","Where can I pay?","The cashier is over there.","在哪里付款？","Where can I pay?"],
["🛒 购物","Can I pay by card?","Yes, you can.","可以刷卡吗？","Can I pay...? · by card"],
["🛒 购物","Can I have a bag?","Sure.","可以给我一个袋子吗？","Can I have...? · a bag"],
["🛒 购物","Do you have anything cheaper?","Let me check.","有没有便宜一点的？","anything cheaper"],
["🛒 购物","I'll take this one.","Okay.","我要这个。","I'll take... · this one"],
/* ===== 交通 51-60 ===== */
["🚕 交通","Where are you going?","I'm going to the airport.","你要去哪里？","Where are you going? · I'm going to..."],
["🚕 交通","How much is the fare?","It's twenty dollars.","车费多少钱？","How much is... · the fare"],
["🚕 交通","How long will it take?","About thirty minutes.","需要多长时间？","How long will it take?"],
["🚕 交通","Please take me to this address.","Sure.","请送我到这个地址。","Please take me to..."],
["🚕 交通","Can you stop here?","Sure.","可以在这里停吗？","Can you stop...?"],
["🚕 交通","Where is the bus stop?","It's over there.","公交车站在哪里？","Where is...? · the bus stop"],
["🚕 交通","Which bus should I take?","Take bus number ten.","我应该坐哪路公交？","Which bus should I take?"],
["🚕 交通","What time does the bus leave?","It leaves at eight.","公交几点出发？","What time does... leave?"],
["🚕 交通","Is this the right train?","Yes, it is.","这是正确的火车吗？","Is this the right...?"],
["🚕 交通","Where can I buy a ticket?","You can buy one over there.","在哪里可以买票？","Where can I buy...?"],
/* ===== 日常交流 61-75 ===== */
["👋 日常","How are you?","I'm good, thank you.","你好吗？","How are you?"],
["👋 日常","How is your day?","It's good.","你今天怎么样？","How is your day?"],
["👋 日常","What are you doing?","I'm working.","你在做什么？","What are you doing?"],
["👋 日常","Where do you live?","I live in Kenya.","你住在哪里？","Where do you live?"],
["👋 日常","Where are you from?","I'm from China.","你来自哪里？","Where are you from?"],
["👋 日常","What do you do?","I'm a cook.","你是做什么工作的？","What do you do?"],
["👋 日常","Do you speak English?","A little.","你会说英语吗？","Do you speak...?"],
["👋 日常","Could you speak slowly?","Sure.","你可以说慢一点吗？","Could you speak slowly?"],
["👋 日常","Could you say that again?","Of course.","可以再说一次吗？","Could you say that again?"],
["👋 日常","I don't understand.","No problem.","我不明白。","I don't understand."],
["👋 日常","What does that mean?","It means...","那是什么意思？","What does that mean?"],
["👋 日常","Can you help me?","Sure.","你可以帮我吗？","Can you help me?"],
["👋 日常","Give me a minute, please.","Okay.","请给我一分钟。","Give me a minute"],
["👋 日常","See you tomorrow.","See you.","明天见。","See you tomorrow"],
["👋 日常","Have a nice day.","You too.","祝你今天愉快。","Have a nice day"],
/* ===== 厨房工作 76-90 ===== */
["👨‍🍳 厨房","Are the vegetables ready?","Yes, they're ready.","蔬菜准备好了吗？","Are the vegetables ready?"],
["👨‍🍳 厨房","Can you clean the fish?","Sure, I can.","你可以把鱼清理好吗？","Can you clean...?"],
["👨‍🍳 厨房","Is the chicken ready?","Not yet.","鸡肉准备好了吗？","Is the chicken ready?"],
["👨‍🍳 厨房","Please wash the vegetables.","Okay.","请把蔬菜洗一下。","Please wash..."],
["👨‍🍳 厨房","Cut the onions, please.","Okay.","请切洋葱。","Cut the onions"],
["👨‍🍳 厨房","The soup is ready.","Great.","汤好了。","The soup is ready"],
["👨‍🍳 厨房","Taste the soup, please.","Okay.","请尝一下汤。","Taste the soup"],
["👨‍🍳 厨房","Is it too salty?","No, it's fine.","太咸了吗？","Is it too salty?"],
["👨‍🍳 厨房","Is it spicy enough?","Yes, it's good.","辣度够吗？","Is it spicy enough?"],
["👨‍🍳 厨房","We need more rice.","Okay.","我们需要更多米饭。","We need more..."],
["👨‍🍳 厨房","We need more vegetables.","Okay.","我们需要更多蔬菜。","We need more..."],
["👨‍🍳 厨房","Lunch is ready.","Okay.","午餐好了。","Lunch is ready"],
["👨‍🍳 厨房","Dinner starts at six.","Okay.","晚餐六点开始。","Dinner starts at..."],
["👨‍🍳 厨房","Please clean the kitchen.","Sure.","请把厨房清洁一下。","Please clean..."],
["👨‍🍳 厨房","Good job.","Thank you.","做得很好。","Good job"],
/* ===== 万能应急 91-100 ===== */
["🆘 万能句","Please wait a moment.","Okay.","请等一下。","Please wait..."],
["🆘 万能句","I'm not sure.","That's okay.","我不确定。","I'm not sure"],
["🆘 万能句","Let me check.","Okay.","让我检查一下。","Let me check"],
["🆘 万能句","Can you show me?","Sure.","你可以给我看看吗？","Can you show me?"],
["🆘 万能句","Please write it down.","Sure.","请把它写下来。","Please write it down"],
["🆘 万能句","I need some help.","Sure.","我需要一些帮助。","I need some help"],
["🆘 万能句","I don't know.","That's okay.","我不知道。","I don't know"],
["🆘 万能句","One more time, please.","Sure.","请再来一次。","One more time"],
["🆘 万能句","That's fine.","Okay.","没关系/可以。","That's fine"],
["🆘 万能句","Thank you very much.","You're welcome.","非常感谢。","Thank you very much"]
];
let current = 0;
let timerID = null;
function showSentence() {
    document.getElementById("scene").innerText =
    lessons[current][0];
    document.getElementById("sentence").innerText =
    lessons[current][1];
    document.getElementById("progress").innerText =
    "第 " + (current + 1) + " / " + lessons.length + " 句";
    document.getElementById("answer").style.display = "none";
    document.getElementById("meaning").style.display = "none";
    document.getElementById("chunks").style.display = "none";
    document.getElementById("timer").innerText = "";
    document.getElementById("status").innerText =
    "准备好了";
}
function speak(text, rate = 0.75) {
    speechSynthesis.cancel();
    let voice =
    new SpeechSynthesisUtterance(text);
    voice.lang = "en-US";
    voice.rate = rate;
    speechSynthesis.speak(voice);
}
function playQuestion() {
    clearInterval(timerID);
    speak(lessons[current][1], 0.75);
    let seconds = 5;
    document.getElementById("timer").innerText =
    "⏸️ 听完后思考 " + seconds + " 秒";
    timerID = setInterval(function() {
        seconds--;
        if(seconds > 0) {
            document.getElementById("timer").innerText =
            "⏸️ 思考中…… " + seconds + " 秒";
        } else {
            clearInterval(timerID);
            document.getElementById("timer").innerText =
            "🗣️ 现在轮到你回答！";
            document.getElementById("status").innerText =
            "先自己说，不要马上看答案";
        }
    },1000);
}
function showAnswer() {
    document.getElementById("answer").innerText =
    lessons[current][2];
    document.getElementById("answer").style.display =
    "block";
}
function playAnswer() {
    speak(lessons[current][2], 0.75);
}
function showMeaning() {
    document.getElementById("meaning").innerText =
    lessons[current][3];
    document.getElementById("meaning").style.display =
    "block";
}
function showChunks() {
    document.getElementById("chunks").innerText =
    lessons[current][4];
    document.getElementById("chunks").style.display =
    "block";
}
function nextSentence() {
    clearInterval(timerID);
    current++;
    if(current >= lessons.length) {
        current = 0;
    }
    showSentence();
}
showSentence();
</script>
</body>
</html>

这次你只做

全选旧代码 → 删除 → 粘贴上面全部代码 → 提交更改。

然后打开我们已经成功的网址：

《每句练耳》⁠￼

你应该看到：

第 1 / 100 句

然后可以一直点：

▶ 播放 → 5秒思考 → 显示回答 → 听回答 → 看中文 → 看词块 → 下一句

如果100句跑通，下一步就不是重新改程序了，而是继续把内容库扩展到800句。
