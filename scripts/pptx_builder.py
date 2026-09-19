import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_16x9_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_standard_header(slide, title_text, badge_text=""):
    NAVY = RGBColor(26, 54, 93)
    BLUE = RGBColor(43, 108, 176)
    
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12.133), Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
    p = tf.paragraphs[0]
    r1 = p.add_run()
    r1.text = title_text
    r1.font.name = "微軟正黑體"
    r1.font.size = Pt(28)
    r1.font.bold = True
    r1.font.color.rgb = NAVY

    if badge_text:
        r2 = p.add_run()
        r2.text = f"   [{badge_text}]"
        r2.font.name = "微軟正黑體"
        r2.font.size = Pt(18)
        r2.font.bold = True
        r2.font.color.rgb = BLUE
