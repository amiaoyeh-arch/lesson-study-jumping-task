# -*- coding: utf-8 -*-
"""
HTML Interactive Deck Builder for Learning Community (SLC) Jumping Tasks
Features:
- 16:9 widescreen fluid responsive layout (aspect-ratio: 16/9, max-width: 1400px)
- Zero-overlap cover layout (left-side visuals, right-side content)
- 50% image width layout for norms & cards
- Built-in multi-stage countdown timers with pause/resume & alert
- Fullscreen mode, keyboard navigation (Space, Arrows, PageUp/PageDown, F key)
- Base64 fully embedded images for zero-dependency offline sharing
"""
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

def generate_interactive_deck_html(title, slides_html_list, output_path):
    slides_joined = "\n".join(slides_html_list)
    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary: #1a365d;
            --secondary: #3F98DE;
            --accent: #276749;
            --highlight: #c53030;
            --bg-light: #f7fafc;
            --border-color: #cbd5e0;
            --card-bg: #ffffff;
            --text-dark: #2d3748;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Microsoft JhengHei', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
        body {{ background: #edf2f7; color: var(--text-dark); display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 10px; }}
        #deck-container {{ width: 96vw; max-width: 1400px; aspect-ratio: 16 / 9; background: var(--card-bg); border-radius: 16px; box-shadow: 0 16px 40px rgba(0, 30, 60, 0.15); border: 2px solid var(--border-color); position: relative; overflow: hidden; display: flex; flex-direction: column; }}
        .slides-wrapper {{ flex: 1; position: relative; width: 100%; height: calc(100% - 68px); }}
        .slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; padding: 22px 36px; display: none; flex-direction: column; background: linear-gradient(135deg, #ffffff 0%, #f7fafc 100%); animation: fadeIn 0.3s ease-in-out; overflow-y: auto; }}
        .slide.active {{ display: flex; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        
        .slide-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 2px solid var(--border-color); padding-bottom: 8px; }}
        .slide-title {{ font-size: 1.6rem; font-weight: 800; color: var(--primary); display: flex; align-items: center; gap: 10px; }}
        .slide-badge {{ font-size: 0.95rem; font-weight: 700; color: #fff; background: var(--secondary); padding: 4px 14px; border-radius: 20px; }}
        
        .grid-2 {{ display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 20px; flex: 1; align-items: stretch; }}
        .grid-4 {{ display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px; flex: 1; }}
        .card {{ background: #fff; border: 1.5px solid var(--border-color); border-radius: 12px; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); display: flex; flex-direction: column; justify-content: space-between; }}
        .card-highlight {{ border-color: var(--secondary); background: #ebf8ff; }}
        .card-green {{ border-color: var(--accent); background: #f0fff4; }}
        
        /* 50% Image Layout */
        .rule-card-50 {{ display: flex; gap: 16px; align-items: center; height: 100%; }}
        .rule-card-50 img {{ width: 50%; height: 95%; max-height: 180px; object-fit: cover; border-radius: 10px; border: 2px solid #cbd5e0; flex-shrink: 0; box-shadow: 0 4px 8px rgba(0,0,0,0.06); }}
        .rule-card-50-text {{ width: 50%; display: flex; flex-direction: column; justify-content: center; }}
        .rule-card-50-text h3 {{ color: var(--primary); font-size: 1.25rem; margin-bottom: 6px; font-weight: 800; }}
        .rule-card-50-text p {{ font-size: 0.98rem; line-height: 1.55; color: #2d3748; }}

        .geometry-zone {{ display: flex; flex-direction: column; align-items: center; justify-content: center; background: #ffffff; border: 2px solid #cbd5e0; border-radius: 12px; padding: 10px; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }}
        .geometry-zone img {{ max-width: 95%; max-height: 88%; object-fit: contain; border-radius: 8px; }}

        .controls-bar {{ height: 68px; background: #fff; border-top: 1.5px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; padding: 0 25px; }}
        .timer-zone {{ display: flex; align-items: center; gap: 10px; background: #edf2f7; padding: 6px 14px; border-radius: 30px; border: 1px solid var(--border-color); }}
        .timer-display {{ font-size: 1.35rem; font-family: 'Courier New', Courier, monospace; font-weight: 800; color: var(--primary); min-width: 70px; text-align: center; }}
        .timer-btn {{ background: var(--secondary); color: white; border: none; padding: 5px 12px; font-size: 0.88rem; font-weight: bold; border-radius: 6px; cursor: pointer; }}
        .timer-btn.stop {{ background: #e53e3e; }}
        .nav-btn {{ background: var(--primary); color: white; border: none; padding: 7px 16px; font-size: 0.95rem; font-weight: bold; border-radius: 8px; cursor: pointer; transition: background 0.2s; }}
        .nav-btn:hover {{ background: var(--secondary); }}
        .nav-btn:disabled {{ background: #cbd5e0; cursor: not-allowed; }}
        .fullscreen-btn {{ background: #4a5568; }}

        .formula-box {{ background: #f7fafc; border-left: 4px solid var(--secondary); padding: 10px 14px; margin: 10px 0; font-size: 1.05rem; font-weight: bold; color: var(--primary); border-radius: 0 8px 8px 0; }}
        .text-lg {{ font-size: 1.05rem; line-height: 1.6; }}
        .text-bold {{ font-weight: bold; }}
        .color-red {{ color: var(--highlight); }}
        .color-blue {{ color: var(--secondary); }}
        .color-green {{ color: var(--accent); }}

        /* Cover Layout - Zero Overlap */
        .cover-layout {{ display: grid; grid-template-columns: 290px 1fr; gap: 28px; width: 100%; height: 100%; align-items: center; background: radial-gradient(circle at center, #ebf8ff 0%, #ffffff 80%); border-radius: 12px; padding: 24px 32px; border: 2px solid #bee3f8; }}
        .cover-left-visual {{ display: flex; flex-direction: column; gap: 14px; align-items: center; justify-content: center; height: 100%; }}
        .cover-img-top {{ width: 150px; height: 150px; border-radius: 50%; border: 4px solid #3F98DE; box-shadow: 0 6px 16px rgba(63, 152, 222, 0.25); object-fit: cover; }}
        .cover-img-bot {{ width: 270px; height: 180px; border-radius: 12px; border: 3px solid #276749; box-shadow: 0 8px 20px rgba(39, 103, 73, 0.2); object-fit: cover; }}
        .cover-right-content {{ display: flex; flex-direction: column; justify-content: center; padding-left: 10px; }}

        /* Reflection Image */
        .reflect-img-box {{ margin-top: 10px; width: 100%; height: 120px; border-radius: 8px; overflow: hidden; border: 1.5px solid #cbd5e0; box-shadow: 0 3px 8px rgba(0,0,0,0.05); }}
        .reflect-img-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    </style>
</head>
<body>

<div id="deck-container">
    <div class="slides-wrapper">
        {slides_joined}
    </div>

    <!-- Controls Bar -->
    <div class="controls-bar">
        <div class="timer-zone">
            <span style="font-weight:bold; color:var(--primary); font-size:0.95rem;">⏱️ 階段倒數：</span>
            <span class="timer-display" id="timer">00:00</span>
            <button class="timer-btn" id="startBtn" onclick="toggleTimer()">開始</button>
            <button class="timer-btn" style="background:#a0aec0;" onclick="resetTimer()">重設</button>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
            <button class="nav-btn" id="prevBtn" onclick="prevSlide()">◀ 上一頁</button>
            <span id="slideNum" style="font-weight:bold; font-size:1rem; min-width:55px; text-align:center;">1 / {len(slides_html_list)}</span>
            <button class="nav-btn" id="nextBtn" onclick="nextSlide()">下一頁 ▶</button>
            <button class="nav-btn fullscreen-btn" onclick="toggleFullScreen()">⛶ 全螢幕</button>
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

    function formatTime(s) {{
        const m = Math.floor(s / 60).toString().padStart(2, '0');
        const sec = (s % 60).toString().padStart(2, '0');
        return `${{m}}:${{sec}}`;
    }}

    function toggleTimer() {{
        if (isRunning) {{
            clearInterval(timerInterval);
            startBtn.textContent = '繼續';
            startBtn.classList.remove('stop');
            isRunning = false;
        }} else {{
            if (timerSeconds <= 0) return;
            isRunning = true;
            startBtn.textContent = '暫停';
            startBtn.classList.add('stop');
            timerInterval = setInterval(() => {{
                if (timerSeconds > 0) {{
                    timerSeconds--;
                    timerDisplay.textContent = formatTime(timerSeconds);
                }} else {{
                    clearInterval(timerInterval);
                    isRunning = false;
                    startBtn.textContent = '開始';
                    startBtn.classList.remove('stop');
                    alert('⏰ 階段時間到！請同學整理手邊紀錄，準備進行下一階段。');
                }}
            }}, 1000);
        }}
    }}

    function resetTimer(sec) {{
        clearInterval(timerInterval);
        isRunning = false;
        startBtn.textContent = '開始';
        startBtn.classList.remove('stop');
        timerSeconds = (sec !== undefined) ? sec : (parseInt(slides[currentSlide].getAttribute('data-time')) || 0);
        timerDisplay.textContent = formatTime(timerSeconds);
    }}

    document.addEventListener('keydown', (e) => {{
        if (['ArrowRight', 'PageDown', ' '].includes(e.key)) nextSlide();
        else if (['ArrowLeft', 'PageUp'].includes(e.key)) prevSlide();
        else if (e.key === 'f' || e.key === 'F') toggleFullScreen();
    }});

    function toggleFullScreen() {{
        if (!document.fullscreenElement) document.documentElement.requestFullscreen();
        else document.exitFullscreen();
    }}

    updateSlide();
</script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Interactive Deck HTML generated at: {output_path}")
    return output_path
