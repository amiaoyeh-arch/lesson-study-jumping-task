import os
import base64

def get_base64_image(img_path):
    if os.path.exists(img_path):
        ext = os.path.splitext(img_path)[1].lower().replace(".", "")
        if ext == "jpg": ext = "jpeg"
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/{ext};base64,{b64}"
    return ""

def generate_interactive_deck_html(title, slides_html, output_path):
    """
    Generates a single standalone HTML file with 16:9 90% layout, countdown timers, and full screen.
    """
    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Microsoft JhengHei', sans-serif; }}
        body {{ background: #eef5f9; color: #2c3e50; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 15px; }}
        #deck-container {{ width: 95vw; max-width: 1400px; aspect-ratio: 16 / 9; background: #fff; border-radius: 18px; box-shadow: 0 12px 36px rgba(0,35,70,0.12); border: 2px solid #e1e8ed; position: relative; overflow: hidden; display: flex; flex-direction: column; }}
        .slides-wrapper {{ flex: 1; position: relative; width: 100%; height: calc(100% - 64px); }}
        .slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; padding: 35px 45px; display: none; flex-direction: column; background: linear-gradient(135deg, #fff 0%, #f7fafc 100%); animation: fadeIn 0.35s ease-in-out; overflow-y: auto; }}
        .slide.active {{ display: flex; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .controls-bar {{ height: 64px; background: #fff; border-top: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; padding: 0 30px; }}
        .timer-zone {{ display: flex; align-items: center; gap: 12px; background: #edf2f7; padding: 6px 16px; border-radius: 30px; }}
        .timer-display {{ font-size: 1.35rem; font-family: monospace; font-weight: 800; color: #2c5282; min-width: 65px; }}
        .timer-btn {{ background: #3182ce; color: white; border: none; padding: 5px 12px; font-size: 0.95rem; border-radius: 6px; cursor: pointer; }}
        .nav-btn {{ background: #2b6cb0; color: white; border: none; padding: 8px 18px; font-size: 1.05rem; font-weight: bold; border-radius: 8px; cursor: pointer; }}
    </style>
</head>
<body>
    <div id="deck-container">
        <div class="slides-wrapper">
            {slides_html}
        </div>
        <div class="controls-bar">
            <div class="timer-zone">
                <span style="font-weight:bold;">⏱️ 階段計時：</span>
                <span class="timer-display" id="timer">00:00</span>
                <button class="timer-btn" id="startBtn" onclick="toggleTimer()">開始</button>
                <button class="timer-btn" style="background:#a0aec0;" onclick="resetTimer()">重設</button>
            </div>
            <div style="display:flex; gap:15px; align-items:center;">
                <button class="nav-btn" id="prevBtn" onclick="prevSlide()">◀ 上一頁</button>
                <span id="slideNum" style="font-weight:bold;">1 / 1</span>
                <button class="nav-btn" id="nextBtn" onclick="nextSlide()">下一頁 ▶</button>
                <button class="nav-btn" style="background:#4a5568;" onclick="toggleFullScreen()">⛶ 全螢幕</button>
            </div>
        </div>
    </div>
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        const slideNumDisplay = document.getElementById('slideNum');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const timerDisplay = document.getElementById('timer');
        const startBtn = document.getElementById('startBtn');
        let timerSeconds = 0, timerInterval = null, isRunning = false;

        function updateSlide() {{
            slides.forEach((s, idx) => s.classList.toggle('active', idx === currentSlide));
            slideNumDisplay.textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
            prevBtn.disabled = (currentSlide === 0);
            nextBtn.disabled = (currentSlide === totalSlides - 1);
            resetTimer(parseInt(slides[currentSlide].getAttribute('data-time')) || 0);
        }}
        function nextSlide() {{ if (currentSlide < totalSlides - 1) {{ currentSlide++; updateSlide(); }} }}
        function prevSlide() {{ if (currentSlide > 0) {{ currentSlide--; updateSlide(); }} }}
        function formatTime(s) {{ return `${{Math.floor(s/60).toString().padStart(2,'0')}}:${{(s%60).toString().padStart(2,'0')}}`; }}
        function toggleTimer() {{
            if (isRunning) {{ clearInterval(timerInterval); startBtn.textContent = '繼續'; isRunning = false; }}
            else {{
                if (timerSeconds <= 0) return;
                isRunning = true; startBtn.textContent = '暫停';
                timerInterval = setInterval(() => {{
                    if (timerSeconds > 0) {{ timerSeconds--; timerDisplay.textContent = formatTime(timerSeconds); }}
                    else {{ clearInterval(timerInterval); isRunning = false; startBtn.textContent = '開始'; alert('⏰ 時間到！'); }}
                }}, 1000);
            }}
        }}
        function resetTimer(sec) {{
            clearInterval(timerInterval); isRunning = false; startBtn.textContent = '開始';
            timerSeconds = (sec !== undefined) ? sec : (parseInt(slides[currentSlide].getAttribute('data-time')) || 0);
            timerDisplay.textContent = formatTime(timerSeconds);
        }}
        document.addEventListener('keydown', (e) => {{
            if (['ArrowRight','PageDown',' '].includes(e.key)) nextSlide();
            else if (['ArrowLeft','PageUp'].includes(e.key)) prevSlide();
        }});
        function toggleFullScreen() {{
            if (!document.fullscreenElement) document.documentElement.requestFullscreen();
            else document.exitFullscreen();
        }}
        updateSlide();
    </script>
</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return output_path
