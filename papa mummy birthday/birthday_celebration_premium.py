from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#21151d">
  <title>HAPPY BRITHDAY TO ME QUEEN GEETA MANOJ ROY</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --ink: #21151d; --wine: #54283d; --rose: #bd7b88;
      --blush: #f3dfe0; --cream: #fbf6ef; --gold: #c9a66b;
      --muted: #8e777d; --glass: rgba(255,250,246,.075);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; color: var(--cream); font-family: "DM Sans", sans-serif;
      background: radial-gradient(ellipse at 50% -15%, #704257 0, transparent 48%),
                  linear-gradient(145deg, #1c121a 0%, #30202a 52%, #1c141b 100%);
      min-height: 100vh; overflow-x: hidden;
    }
    body::before {
      content: ""; position: fixed; inset: 0; pointer-events: none; opacity: .12;
      background-image: radial-gradient(#fff 0.65px, transparent .65px);
      background-size: 23px 23px; z-index: -1;
    }
    button, input { font: inherit; }
    button {
      border: 1px solid rgba(226,194,153,.55); border-radius: 999px;
      padding: 13px 22px; color: var(--cream); background: rgba(201,166,107,.13);
      cursor: pointer; transition: .25s ease; letter-spacing: .02em;
    }
    button:hover { transform: translateY(-2px); background: rgba(201,166,107,.25); }
    button:focus-visible, input:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; }
    .primary { color: #241820; background: linear-gradient(110deg,#e7c99b,#c99b75); border: 0; font-weight: 700; }
    .primary:hover { background: linear-gradient(110deg,#f0d8b3,#d4a783); }
    .hero { min-height: 82vh; display: grid; place-items: center; text-align: center; padding: 86px 20px 58px; position: relative; }
    .hero-inner { max-width: 850px; }
    .eyebrow { color: #dfbd91; text-transform: uppercase; letter-spacing: .32em; font-size: 11px; font-weight: 700; }
    h1, h2, h3 { font-family: "Playfair Display", Georgia, serif; font-weight: 500; }
    h1 { font-size: clamp(3.3rem, 9vw, 7.2rem); line-height: 1.02; margin: 23px 0 18px; color: #f5e8d9; }
    .hero-copy { color: #e5cfd0; font-size: clamp(1rem,2.2vw,1.25rem); line-height: 1.8; max-width: 600px; margin: 0 auto 28px; }
    .ornament { color: var(--gold); font-size: 24px; letter-spacing: .45em; margin: 25px 0; }
    .hero-actions { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
    .live-clock { color: #c9afb2; font-size: 12px; letter-spacing: .12em; margin-top: 36px; }
    .container { width: min(1050px, calc(100% - 34px)); margin: 0 auto 80px; }
    .section-intro { text-align: center; margin: 0 auto 28px; max-width: 620px; }
    .section-intro h2 { color: #f1dfcf; font-size: clamp(2rem,5vw,3rem); margin: 12px 0; }
    .section-intro p { color: #c7b4b8; line-height: 1.8; }
    .grid { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 20px; }
    .card {
      padding: clamp(24px,4vw,38px); border: 1px solid rgba(225,197,168,.18);
      border-radius: 22px; background: linear-gradient(145deg,rgba(255,250,246,.09),rgba(255,250,246,.035));
      box-shadow: 0 18px 55px rgba(0,0,0,.18); backdrop-filter: blur(12px);
    }
    .card h2 { color: #e7c99b; font-size: 1.75rem; margin: 0 0 14px; }
    .card p { color: #d4c2c4; line-height: 1.85; }
    .wide { grid-column: 1 / -1; }
    .cake-wrap { text-align: center; padding: 28px 10px 10px; }
    .cake { cursor: pointer; display: inline-block; animation: float 3s ease-in-out infinite; }
    .flame { font-size: 29px; min-height: 42px; animation: flicker .7s infinite alternate; }
    .tier { margin: auto; box-shadow: inset 0 -7px rgba(100,40,62,.12); }
    .tier.top { width: 92px; height: 28px; background: #e9b7b8; border-radius: 50% 50% 8px 8px; }
    .tier.middle { width: 145px; height: 43px; background: #c9828e; border-radius: 8px 8px 14px 14px; }
    .tier.bottom { width: 198px; height: 48px; background: #e7c6b2; border-radius: 10px 10px 16px 16px; }
    .cake-caption { color: #d9c3c2; font-size: 13px; margin-top: 17px; }
    @keyframes float { 50% { transform: translateY(-8px); } }
    @keyframes flicker { to { transform: scale(1.12); } }
    .wish-reveal { min-height: 30px; color: #e7c99b; font-family: "Playfair Display",serif; font-size: 1.35rem; margin-top: 15px; }
    .envelope {
      width: 150px; height: 105px; margin: 25px auto; display: grid; place-items: center;
      border-radius: 8px; background: linear-gradient(140deg,#d69ba0,#9f586e);
      cursor: pointer; position: relative; box-shadow: 0 14px 30px #0004; font-size: 35px;
    }
    .envelope::before { content:""; position:absolute; inset:0; background: linear-gradient(35deg,transparent 49%,#edc0bd 50%,transparent 52%),linear-gradient(-35deg,transparent 49%,#edc0bd 50%,transparent 52%); }
    .letter { display:none; text-align:left; padding:23px; margin-top:20px; border-left:2px solid var(--gold); background:rgba(255,255,255,.045); color:#e8d8d4; line-height:1.95; animation: fade .5s ease; }
    .letter h3 { color:#e7c99b; font-size:1.6rem; margin-top:0; }
    @keyframes fade { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:none; } }
    .field-row { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:20px 0; }
    label { display:block; color:#d9c2c0; font-size:12px; margin-bottom:8px; letter-spacing:.06em; }
    input[type="date"],input[type="time"] { width:100%; padding:13px; border:1px solid rgba(225,197,168,.25); border-radius:10px; color:#f7ece5; background:rgba(0,0,0,.18); color-scheme:dark; }
    .result { color:#e7c99b; line-height:1.9; margin-top:18px; }
    .countdown { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin-top:24px; }
    .time-unit { padding:17px 8px; border:1px solid rgba(225,197,168,.2); border-radius:14px; background:rgba(0,0,0,.12); }
    .time-unit strong { display:block; color:#f0d7b8; font: 2rem "Playfair Display",serif; }
    .time-unit span { color:#bca6a9; font-size:10px; letter-spacing:.14em; text-transform:uppercase; }
    .gallery { min-height:280px; border:1px dashed rgba(225,197,168,.4); border-radius:16px; display:grid; place-items:center; overflow:hidden; background:rgba(0,0,0,.12); }
    .gallery img { width:100%; height:100%; max-height:480px; object-fit:contain; }
    .gallery-tools { display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:9px; margin-top:16px; }
    .upload-label { display:inline-block; border-radius:999px; padding:12px 18px; border:1px solid rgba(226,194,153,.55); cursor:pointer; color:#f0dfd1; font-size:13px; }
    input[type=file] { display:none; }
    .memory-count { color:#bca6a9; font-size:12px; margin-top:12px; }
    .birthday-note { text-align:center; font: clamp(1.1rem,2.4vw,1.35rem)/2 "Playfair Display",serif; color:#e8d8d4; max-width:700px; margin:auto; }
    .birthday-note em { color:#e7c99b; font-style:normal; }
    footer { text-align:center; padding:35px 15px 50px; color:#a99198; font-size:12px; letter-spacing:.08em; }
    .floating { position:fixed; bottom:-40px; pointer-events:none; z-index:5; animation: rise 8s linear forwards; opacity:.75; }
    @keyframes rise { to { transform:translateY(-115vh) rotate(35deg); opacity:0; } }
    @media(max-width:700px) { .grid { grid-template-columns:1fr; } .wide { grid-column:auto; } .hero { min-height:75vh; } .field-row { grid-template-columns:1fr; } .countdown { gap:6px; } .time-unit { padding:13px 3px; } .time-unit strong { font-size:1.55rem; } .card { border-radius:18px; } }
    @media(prefers-reduced-motion:reduce) { *,*::before,*::after { animation-duration:.01ms!important; animation-iteration-count:1!important; scroll-behavior:auto!important; } }
    
/* ===== HERO PHOTO SLIDESHOW ===== */

.hero {
  min-height: 90vh;
  position: relative;
  display: grid;
  place-items: center;
  text-align: center;
  padding: 90px 20px 70px;
  overflow: hidden;
  isolation: isolate;
  background: linear-gradient(135deg, #21151d, #54283d);
}

.hero-slides {
  position: absolute;
  inset: 0;
  z-index: -2;
  overflow: hidden;
}

.hero-slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transform: scale(1.04);
  transition: opacity 1.2s ease, transform 5s ease;
}

.hero-slide.active {
  opacity: 1;
  transform: scale(1);
}

.hero-overlay {
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(
      90deg,
      rgba(25, 12, 22, .82),
      rgba(35, 15, 28, .52),
      rgba(25, 12, 22, .82)
    );
}

.hero-inner {
  position: relative;
  z-index: 2;
  width: min(850px, 100%);
  padding: 25px;
}

.hero h1 {
  text-shadow: 0 5px 25px rgba(0,0,0,.45);
}

.hero-copy {
  text-shadow: 0 2px 10px rgba(0,0,0,.7);
}

.hero-photo-controls {
  position: relative;
  z-index: 3;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 28px;
}

.hero-upload-label {
  display: inline-block;
  padding: 12px 19px;
  border: 1px solid rgba(226,194,153,.7);
  border-radius: 999px;
  color: #f5e8d9;
  background: rgba(40,20,30,.55);
  cursor: pointer;
  font-size: 13px;
  transition: .25s ease;
}

.hero-upload-label:hover {
  background: rgba(201,166,107,.3);
  transform: translateY(-2px);
}

.hero-photo-controls button {
  background: rgba(40,20,30,.65);
  backdrop-filter: blur(8px);
}

.hero-photo-count {
  width: 100%;
  color: #f0d9d5;
  font-size: 12px;
  text-shadow: 0 2px 8px #000;
  margin-top: 3px;
}

#heroPhotoUpload {
  display: none;
}

@media(max-width:700px) {
  .hero {
    min-height: 85vh;
    padding: 75px 12px 45px;
  }

  .hero-inner {
    padding: 12px;
  }

  .hero-photo-controls {
    gap: 7px;
  }

  .hero-photo-controls button,
  .hero-upload-label {
    padding: 10px 13px;
    font-size: 12px;
  }
}

@media(prefers-reduced-motion:reduce) {
  .hero-slide {
    transition: none;
  }
}


/* ===== LUXURY GOLDEN BIRTHDAY DATE CARD ===== */

.birthday-date-card {
    position: relative;
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    margin: 25px auto 20px;
    padding: 22px 42px;
    min-width: 275px;

    /* Transparent glass-like background */
    background: rgba(20, 10, 15, 0.08);
    backdrop-filter: blur(2px);

    /* Glowing golden border */
    border: 1.5px solid #e9c16e;
    border-radius: 18px;

    box-shadow:
        0 0 8px rgba(255, 207, 112, 0.85),
        0 0 18px rgba(255, 190, 75, 0.65),
        0 0 35px rgba(255, 180, 55, 0.35),
        inset 0 0 12px rgba(255, 204, 112, 0.12);

    animation: goldenBorderGlow 2.5s ease-in-out infinite alternate;
}

/* Special day heading */
.birthday-date-label {
    color: #ffe6ae;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 14px;

    text-shadow:
        0 0 6px #ffd77d,
        0 0 14px rgba(255, 193, 70, 0.9);
}

/* Date layout */
.birthday-date-main {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 17px;
}

/* Bright golden date */
.birthday-day {
    font-family: 'Playfair Display', serif;
    font-size: 76px;
    line-height: 1;
    font-weight: 700;
    color: #fff0c2;

    text-shadow:
        0 0 5px #fff8df,
        0 0 12px #ffe19a,
        0 0 22px #ffc44d,
        0 0 40px #ffb52e,
        0 0 65px rgba(255, 174, 35, 0.9);

    animation: goldenDateGlow 2s ease-in-out infinite alternate;
}

/* Month and year */
.birthday-date-details {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 5px;
}

.birthday-month {
    color: #fff0ca;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 3px;

    text-shadow:
        0 0 6px #ffe3a0,
        0 0 14px #ffc44d,
        0 0 25px rgba(255, 177, 43, 0.85);
}

.birthday-year {
    color: #f9d99b;
    font-size: 15px;
    letter-spacing: 4px;

    text-shadow:
        0 0 7px #ffd77d,
        0 0 17px rgba(255, 190, 70, 0.85);
}

/* Footer */
.birthday-date-footer {
    color: #ffe1a9;
    font-size: 9px;
    letter-spacing: 2px;
    margin-top: 16px;

    text-shadow:
        0 0 7px #ffc75e,
        0 0 16px rgba(255, 177, 43, 0.8);
}

/* Golden border animation */
@keyframes goldenBorderGlow {
    from {
        border-color: #d8ae61;
        box-shadow:
            0 0 6px rgba(255, 207, 112, 0.65),
            0 0 15px rgba(255, 190, 75, 0.45),
            0 0 28px rgba(255, 180, 55, 0.25),
            inset 0 0 10px rgba(255, 204, 112, 0.08);
    }

    to {
        border-color: #fff0bd;
        box-shadow:
            0 0 12px rgba(255, 224, 153, 1),
            0 0 25px rgba(255, 190, 75, 0.85),
            0 0 48px rgba(255, 180, 55, 0.55),
            inset 0 0 18px rgba(255, 204, 112, 0.2);
    }
}

/* Golden date animation */
@keyframes goldenDateGlow {
    from {
        text-shadow:
            0 0 5px #fff8df,
            0 0 12px #ffe19a,
            0 0 22px #ffc44d,
            0 0 40px #ffb52e;
    }

    to {
        text-shadow:
            0 0 8px #ffffff,
            0 0 18px #fff0bd,
            0 0 32px #ffd16c,
            0 0 55px #ffb52e,
            0 0 75px rgba(255, 174, 35, 1);
    }
}

/* Mobile responsive */
@media(width: 280px) {
    .birthday-date-card {
        width: 280px;
        max-width: 85%;
        margin: 18px auto;
        padding: 14px 18px;
    }

    .birthday-day {
        font-size: 62px;
    }

    .birthday-month {
        font-size: 17px;
    }
}
/* Heartbeat golden glow around the date box */
.birthday-date-card {
    background: transparent;
    border: 1.5px solid #ffd76a;
    box-shadow:
        0 0 8px rgba(255, 215, 106, 0.6),
        0 0 18px rgba(255, 193, 70, 0.4);
    animation: goldenHeartbeat 1.8s infinite ease-in-out;
}

/* Golden date glow */
.birthday-day {
    color: #ffe7a3;
    animation: dateHeartbeat 1.8s infinite ease-in-out;
}

@keyframes goldenHeartbeat {
    0%, 100% {
        box-shadow:
            0 0 6px rgba(255, 215, 106, 0.4),
            0 0 12px rgba(255, 193, 70, 0.3);
        border-color: #d9ad54;
    }

    15% {
        box-shadow:
            0 0 15px #ffd76a,
            0 0 30px rgba(255, 193, 70, 0.8),
            0 0 45px rgba(255, 193, 70, 0.5);
        border-color: #fff0b0;
    }

    30% {
        box-shadow:
            0 0 6px rgba(255, 215, 106, 0.4),
            0 0 12px rgba(255, 193, 70, 0.3);
        border-color: #d9ad54;
    }

    45% {
        box-shadow:
            0 0 18px #ffd76a,
            0 0 35px rgba(255, 193, 70, 0.9),
            0 0 55px rgba(255, 193, 70, 0.5);
        border-color: #fff4c4;
    }
}

@keyframes dateHeartbeat {
    0%, 100% {
        text-shadow: 0 0 6px #d9ad54;
    }

    15%, 45% {
        text-shadow:
            0 0 10px #ffe7a3,
            0 0 22px #ffd76a,
            0 0 40px #ffbd45,
            0 0 55px rgba(255, 193, 70, 0.8);
    }
}


   </style>
</head>
<body>
  
<header class="hero">

  <!-- Background slideshow -->
  <div class="hero-slides" id="heroSlides">
    <!-- Photos will appear here automatically -->
  </div>

  <!-- Dark overlay for readable text -->
  <div class="hero-overlay"></div>

  <!-- Birthday content -->
  <div class="hero-inner">

    <div class="eyebrow">
      A day made a little more magical
    </div>

    <div class="ornament">
      ✦ &nbsp; ♡ &nbsp; ✦
    </div>

    <h1>Happy Birthday</h1>
    
<div class="birthday-date-card">
    <div class="birthday-date-label">
        ✦ THE MOST SPECIAL DAY ✦
    </div>

    <div class="birthday-date-main">
        <span class="birthday-day" id="birthdayDay">21</span>

        <div class="birthday-date-details">
            <span class="birthday-month" id="birthdayMonth">
                OCTOBER
            </span>
            <span class="birthday-year" id="birthdayYear">
                2001
            </span>
        </div>
    </div>

    <div class="birthday-date-footer">
        ♡ A DAY WORTH CELEBRATING FOREVER ♡
    </div>
</div>


    <p class="hero-copy">
      For someone who makes ordinary moments feel extraordinary.
      May today bring the kind of happiness that stays long after
      the candles go out.
    </p>

    <div class="hero-actions">
      <a href="#surprise">
        <button class="primary">
          Discover your surprise
        </button>
      </a>

      <button id="musicButton" onclick="toggleMusic()">
        ♫ Play the melody
      </button>
    </div>

    <!-- Photo slideshow controls -->
    <div class="hero-photo-controls">

      <label for="heroPhotoUpload" class="hero-upload-label">
        ＋ Add Multiple Photos
      </label>

      <input
        type="file"
        id="heroPhotoUpload"
        accept="image/*"
        multiple
      >

      <button type="button" onclick="heroPrevious()">
        ❮ Previous
      </button>

      <button
        type="button"
        id="heroSlideshowButton"
        onclick="heroToggleSlideshow()"
      >
        Pause Slideshow
      </button>

      <button type="button" onclick="heroNext()">
        Next ❯
      </button>

      <div
        class="hero-photo-count"
        id="heroPhotoCount"
        aria-live="polite"
      >
        Add your favourite photographs to begin the slideshow ♡
      </div>

    </div>

    <div class="live-clock" id="clock"></div>

  </div>
</header>


  <main class="container">
    <div class="section-intro">
      <div class="eyebrow">A little celebration, just because</div>
      <h2>Made of wishes & warm memories</h2>
      <p>A small digital keepsake filled with thoughtful words, favourite photographs and a few birthday surprises.</p>
    </div>

    <section class="card wide cake-wrap">
      <div class="eyebrow">Make a wish</div>
      <div class="cake" role="button" tabindex="0" aria-label="Blow out the candles" onclick="blowCandles()" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();blowCandles()}">
        <div class="flame" id="flames">✦ 🕯 🕯 ✦</div>
        <div class="tier top"></div><div class="tier middle"></div><div class="tier bottom"></div>
      </div>
      <p class="cake-caption">Tap the cake to blow out the candles</p>
      <div class="wish-reveal" id="cakeWish" aria-live="polite"></div>
    </section>

    <div class="grid" id="surprise">
      <section class="card">
        <div class="eyebrow">A note from the heart</div>
        <h2>A little letter</h2>
        <p>Some wishes are better opened slowly. There is a note waiting for you.</p>
        <div class="envelope" role="button" tabindex="0" aria-label="Open your letter" onclick="openLetter()" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();openLetter()}">✉</div>
        <p style="text-align:center;font-size:12px">Tap to open your letter</p>
        <div class="letter" id="letter">
          <h3>To someone truly special for me "MY WIFEY",</h3>
          May your days be gentle, your dreams be brave and your heart always find reasons to smile. I hope life surprises you with beautiful people, meaningful moments and opportunities that make you proud.
          <br><br>
          You deserve a love that feels peaceful, laughter that comes easily and memories you will want to revisit forever.
          <br><br>
          You are more than my wife; you are my happiness,
  my strength and my home. Life may not always be perfect,
  but having you by my side makes every moment special.

  <br><br>

  I promise to keep choosing you, respecting you and
  loving you through every season of life. My greatest
  wish is to grow old with you, holding your hand and
  creating beautiful memories together.

  <br><br>

  <em>You are, and always will be, my favourite part of life.
  Forever yours. ♡</em>
          <em>Wishing you a beautiful birthday and a year as lovely as your heart.</em> ♡
        </div>
      </section>

      <section class="card">
        <div class="eyebrow">A moment in time</div>
        <h2>Birthday details</h2>
        <p>Enter a date and time to discover the little details of this life journey.</p>
        <div class="field-row">
          <div><label for="dob">DATE OF BIRTH</label><input id="dob" type="date"></div>
          <div><label for="tob">TIME OF BIRTH (OPTIONAL)</label><input id="tob" type="time"></div>
        </div>
        <button class="primary" onclick="calculateAge()">Calculate age</button>
        <div class="result" id="ageResult" aria-live="polite"></div>
      </section>

      <section class="card wide">
        <div class="eyebrow">The next chapter</div>
        <h2>Countdown to your birthday</h2>
        <p>Set the date of birth above to see the time until the next celebration.</p>
        <div class="countdown" id="countdown">
          <div class="time-unit"><strong>--</strong><span>Days</span></div>
          <div class="time-unit"><strong>--</strong><span>Hours</span></div>
          <div class="time-unit"><strong>--</strong><span>Minutes</span></div>
          <div class="time-unit"><strong>--</strong><span>Seconds</span></div>
        </div>
      </section>

      <section class="card wide">
        <div class="eyebrow">Keep the moments close</div>
        <h2>Your memory gallery</h2>
        <p>Choose photographs from your device. They appear here as a private, local slideshow and are not uploaded to a server.</p>
        <div class="gallery" id="gallery"><p>✧ Your favourite moments will live here ✧</p></div>
        <div class="gallery-tools">
          <label class="upload-label" for="photoUpload">＋ Add photographs</label>
          <input id="photoUpload" type="file" accept="image/*" multiple>
          <button onclick="previousPhoto()">Previous</button><button onclick="nextPhoto()">Next</button>
        </div>
        <div class="memory-count" id="photoCount"></div>
      </section>

      <section class="card wide">
  <div class="eyebrow">Birthday wishes for the year ahead</div>
  <h2 style="text-align:center">A Beautiful Year Awaits</h2>
  <div class="birthday-note">
    May this new year of your life bring you
    <em>endless happiness, good health, peace and success.</em>
    May all your dreams come true, and may every day bring you
    new reasons to smile.
    <br><br>
    Keep shining, keep smiling and never stop being the
    wonderful person you are.
    <br><br>
    <em>Happy Birthday, My Love! ♡</em>
  </div>
  <div style="text-align:center;margin-top:28px">
    <button class="primary" onclick="celebrate()">Send a little sparkle</button>
  </div>
</section>
    </div>
  </main>

  <footer>CRAFTED WITH CARE & A LITTLE MAGIC &nbsp; ✦ &nbsp; HAPPY BIRTHDAY</footer>

<script>


// ===== BIRTHDAY DATE DISPLAY =====

const birthdayDate = new Date(1971, 10, 15);

document.getElementById("birthdayDay").textContent =
    String(birthdayDate.getDate()).padStart(2, "0");

document.getElementById("birthdayMonth").textContent =
    birthdayDate.toLocaleDateString("en-IN", {
        month: "long"
    }).toUpperCase();

document.getElementById("birthdayYear").textContent =
    birthdayDate.getFullYear();

  const $ = (id) => document.getElementById(id);
  
// ==========================================
// HERO MULTIPLE PHOTO SLIDESHOW
// ==========================================

let heroPhotos = [];
let heroPhotoIndex = 0;
let heroSlideshowTimer = null;
let heroSlideshowPlaying = false;

const heroUpload = $("heroPhotoUpload");
const heroSlidesContainer = $("heroSlides");
const heroPlayButton = $("heroSlideshowButton");
const heroPhotoCount = $("heroPhotoCount");

// Add multiple photos without removing previous photos
heroUpload.addEventListener("change", function(event) {

  const selectedFiles = Array.from(event.target.files || []);

  const imageFiles = selectedFiles.filter(file =>
    file.type.startsWith("image/")
  );

  imageFiles.forEach(file => {
    const imageURL = URL.createObjectURL(file);
    heroPhotos.push(imageURL);
  });

  if (imageFiles.length > 0) {

    // Start from the first newly added photograph
    heroPhotoIndex = heroPhotos.length - imageFiles.length;

    displayHeroPhoto();

    startHeroSlideshow();
  }

  // Allows selecting the same files again
  heroUpload.value = "";

});

// Display the selected photograph
function displayHeroPhoto() {

  heroSlidesContainer.replaceChildren();

  if (heroPhotos.length === 0) {
    heroPhotoCount.textContent =
      "Add your favourite photographs to begin the slideshow ♡";
    return;
  }

  const image = document.createElement("img");

  image.src = heroPhotos[heroPhotoIndex];

  image.className = "hero-slide active";

  image.alt = `Birthday memory ${heroPhotoIndex + 1}`;

  heroSlidesContainer.appendChild(image);

  heroPhotoCount.textContent =
    `♡ Memory ${heroPhotoIndex + 1} of ${heroPhotos.length}`;
}

// Next photograph
function heroNext() {

  if (heroPhotos.length === 0) return;

  heroPhotoIndex =
    (heroPhotoIndex + 1) % heroPhotos.length;

  displayHeroPhoto();
}

// Previous photograph
function heroPrevious() {

  if (heroPhotos.length === 0) return;

  heroPhotoIndex =
    (heroPhotoIndex - 1 + heroPhotos.length) % heroPhotos.length;

  displayHeroPhoto();
}

// Start automatic slideshow
function startHeroSlideshow() {

  if (heroSlideshowTimer) {
    clearInterval(heroSlideshowTimer);
  }

  if (heroPhotos.length === 0) return;

  heroSlideshowPlaying = true;

  heroPlayButton.textContent = "Pause Slideshow";

  heroSlideshowTimer = setInterval(() => {

    heroNext();

  }, 4000);
}

// Pause slideshow
function pauseHeroSlideshow() {

  if (heroSlideshowTimer) {
    clearInterval(heroSlideshowTimer);
  }

  heroSlideshowTimer = null;

  heroSlideshowPlaying = false;

  heroPlayButton.textContent = "Play Slideshow";
}

// Play/Pause button
function heroToggleSlideshow() {

  if (heroPhotos.length === 0) {
    heroPhotoCount.textContent =
      "Please add some photographs first ♡";
    return;
  }

  if (heroSlideshowPlaying) {
    pauseHeroSlideshow();
  } else {
    startHeroSlideshow();
  }
}

// Release browser memory when leaving the page
window.addEventListener("beforeunload", () => {

  heroPhotos.forEach(url => URL.revokeObjectURL(url));

});


  function updateClock() {
    $('clock').textContent = new Date().toLocaleString(undefined, {
      weekday:'long', year:'numeric', month:'long', day:'numeric',
      hour:'2-digit', minute:'2-digit', second:'2-digit'
    });
  }
  updateClock();
  setInterval(updateClock, 1000);

  function openLetter() {
    const letter = $('letter');
    letter.style.display = letter.style.display === 'block' ? 'none' : 'block';
    if (letter.style.display === 'block') letter.scrollIntoView({behavior:'smooth', block:'nearest'});
  }

  function calculateAge() {
    const value = $('dob').value;
    if (!value) { $('ageResult').textContent = 'Please select a date of birth first.'; return; }
    const [year, month, day] = value.split('-').map(Number);
    const now = new Date();
    const birth = new Date(year, month - 1, day);
    if (birth > now || birth.getFullYear() !== year || birth.getMonth() !== month - 1 || birth.getDate() !== day) {
      $('ageResult').textContent = 'Please enter a valid date that is not in the future.'; return;
    }
    let years = now.getFullYear() - year;
    let months = now.getMonth() - (month - 1);
    let days = now.getDate() - day;
    if (days < 0) {
      months--;
      days += new Date(now.getFullYear(), now.getMonth(), 0).getDate();
    }
    if (months < 0) { years--; months += 12; }
    const timeText = $('tob').value ? ` · Birth time: ${$('tob').value}` : '';
    $('ageResult').textContent = `${years} years, ${months} months and ${days} days${timeText}`;
    updateCountdown();
  }

  function updateCountdown() {
    const value = $('dob').value;
    if (!value) return;
    const [, month, day] = value.split('-').map(Number);
    const now = new Date();
    let target = new Date(now.getFullYear(), month - 1, day);
    if (target <= now) target = new Date(now.getFullYear() + 1, month - 1, day);
    const diff = Math.max(0, target - now);
    const units = [
      Math.floor(diff / 86400000),
      Math.floor(diff % 86400000 / 3600000),
      Math.floor(diff % 3600000 / 60000),
      Math.floor(diff % 60000 / 1000)
    ];
    $('countdown').innerHTML = units.map((n, i) =>
      `<div class="time-unit"><strong>${String(n).padStart(2,'0')}</strong><span>${['Days','Hours','Minutes','Seconds'][i]}</span></div>`
    ).join('');
  }
  $('dob').addEventListener('change', updateCountdown);
  setInterval(updateCountdown, 1000);

  let photos = [], photoIndex = 0;
  $('photoUpload').addEventListener('change', (event) => {
    photos.forEach(URL.revokeObjectURL);
    photos = Array.from(event.target.files || []).filter(file => file.type.startsWith('image/')).map(URL.createObjectURL);
    photoIndex = 0;
    showPhoto();
  });
  function showPhoto() {
    const gallery = $('gallery');
    gallery.replaceChildren();
    if (!photos.length) {
      const message = document.createElement('p');
      message.textContent = '✧ Your favourite moments will live here ✧';
      gallery.append(message);
      $('photoCount').textContent = '';
      return;
    }
    const image = document.createElement('img');
    image.src = photos[photoIndex];
    image.alt = `Memory ${photoIndex + 1}`;
    gallery.append(image);
    $('photoCount').textContent = `Memory ${photoIndex + 1} of ${photos.length}`;
  }
  function nextPhoto() { if (photos.length) { photoIndex = (photoIndex + 1) % photos.length; showPhoto(); } }
  function previousPhoto() { if (photos.length) { photoIndex = (photoIndex - 1 + photos.length) % photos.length; showPhoto(); } }
  setInterval(nextPhoto, 5000);

  let audioContext = null, musicPlaying = false, musicTimer = null, noteIndex = 0;
  const melody = [
    [523.25,.32],[659.25,.32],[783.99,.55],[659.25,.32],[587.33,.32],[698.46,.65],
    [659.25,.32],[587.33,.32],[523.25,.75],[440,.32],[523.25,.32],[659.25,.8],
    [783.99,.32],[698.46,.32],[659.25,.55],[587.33,.32],[523.25,.9]
  ];
  function playNote() {
    if (!musicPlaying) return;
    const [frequency, duration] = melody[noteIndex++ % melody.length];
    const oscillator = audioContext.createOscillator();
    const gain = audioContext.createGain();
    oscillator.type = 'sine';
    oscillator.frequency.value = frequency;
    oscillator.connect(gain); gain.connect(audioContext.destination);
    const start = audioContext.currentTime;
    gain.gain.setValueAtTime(.0001, start);
    gain.gain.exponentialRampToValueAtTime(.075, start + .04);
    gain.gain.exponentialRampToValueAtTime(.0001, start + duration);
    oscillator.start(start); oscillator.stop(start + duration + .03);
    musicTimer = setTimeout(playNote, duration * 1000 + 90);
  }
  async function toggleMusic() {
    const button = $('musicButton');
    if (musicPlaying) {
      musicPlaying = false; clearTimeout(musicTimer);
      button.textContent = '♫ Play the melody'; return;
    }
    try {
      audioContext ||= new (window.AudioContext || window.webkitAudioContext)();
      await audioContext.resume();
      musicPlaying = true; button.textContent = 'Ⅱ Pause the melody'; playNote();
    } catch (error) { button.textContent = 'Music unavailable in this browser'; }
  }

  function celebrate() {
    const symbols = ['✦','♡','✧','❀'];
    for (let i = 0; i < 34; i++) {
      const element = document.createElement('span');
      element.className = 'floating';
      element.textContent = symbols[Math.floor(Math.random() * symbols.length)];
      element.style.left = Math.random() * 100 + 'vw';
      element.style.fontSize = (14 + Math.random() * 18) + 'px';
      element.style.color = Math.random() > .5 ? '#e7c99b' : '#e6b8c1';
      document.body.append(element);
      setTimeout(() => element.remove(), 8200);
    }
  }
  function blowCandles() {
    $('flames').textContent = '♡  ✧  ♡';
    $('cakeWish').textContent = 'May every beautiful wish find its way to you.';
    celebrate();
  }
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
