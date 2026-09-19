# -*- coding: utf-8 -*-
"""
illustration_helper.py - Prompt generator for Japanese watercolor anime style classroom illustrations.
"""

def get_illustration_prompt(scene_type, details=""):
    base_style = "Japanese watercolor anime illustration, Studio Ghibli aesthetic, soft warm pastel colors, bright peaceful classroom lighting, elementary school setting"
    
    prompts = {
        "thinking_kid": f"{base_style}, a cute 6th-grade elementary school student thinking thoughtfully, holding chin with hand, curious and focused expression, sparkling math thoughts in background, clean light background",
        "group_discuss": f"{base_style}, 4 elementary school students (2 boys and 2 girls) sitting closely around a wooden classroom desk, enthusiastically discussing a geometry math problem sheet, holding pencils and pointing at paper, smiling and listening attentively",
        "listening_pair": f"{base_style}, two elementary school students sitting side by side at wooden desks. One student is speaking gently while explaining, and the other student is turning their body towards them, looking with a warm, gentle, focused and caring gaze, actively listening with empathy",
        "step2_group": f"{base_style}, 4 elementary school students huddled close over a shared worksheet, pointing and talking softly with friendly smiles, learning community group work",
        "step3_present": f"{base_style}, an elementary school student standing confidently at the front of the classroom by the green blackboard, explaining a math geometry problem with chalk, classmates seated and listening attentively",
        "step4_reflect": f"{base_style}, a cute elementary school student sitting smiling happily while writing a reflection note in a notebook, feeling enlightened and accomplished",
        "quiet_writing": f"{base_style}, elementary school students sitting peacefully and quietly at their classroom desks, calmly writing thoughtful math reflections in their notebooks with pencils, serene quiet reflection time, warm golden sunlight streaming through windows"
    }
    
    return prompts.get(scene_type, f"{base_style}, {details}")

if __name__ == '__main__':
    for key in ["thinking_kid", "group_discuss", "listening_pair", "quiet_writing"]:
        print(f"[{key}]:\n{get_illustration_prompt(key)}\n")
