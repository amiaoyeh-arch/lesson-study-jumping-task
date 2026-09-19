import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcMar'):
            tcPr.remove(child)
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_text(cell, text, bold=False, font_name="微軟正黑體", font_size=10, color_rgb=None, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if i > 0:
            p = cell.add_paragraph()
            p.alignment = align
        r = p.add_run(line)
        r.font.name = font_name
        r.font.size = Pt(font_size)
        r.bold = bold
        if color_rgb:
            r.font.color.rgb = color_rgb

def generate_standard_docx(data_dict, template_path, output_path):
    """
    data_dict contains:
    - school, grade, date, subject, teacher, unit_name, partners, version
    - idea_text
    - core_competencies: [(domain, text), ...]
    - curriculum_standards: (perf_text, content_text, goals_text)
    - textbook_and_student_analysis: (textbook_struct, diff_text, special_students)
    - 13_dimensions_data: [(category, item, content), ...]
    - unit_sessions_focus: text
    - 40min_process: [(phase_name, student_task, teacher_guide, time_str), ...]
    - elasticity_clause: text
    - dialogue_table: [(resp_text, diagnosis, strategy, script), ...]
    - worksheet_tasks: dict with tasks
    - attachments: text
    """
    doc = docx.Document(template_path)
    
    # 1. Update basic info paragraphs
    doc.paragraphs[0].text = f"新北市〇〇國小教學方案設計〔{data_dict.get('school', '待補：學校名稱')}〕"
    doc.paragraphs[1].text = f"授課年級：{data_dict.get('grade', '三 年 〇 班')}　　　　　　授課日期：〔{data_dict.get('date', '待補：日期')}〕"
    doc.paragraphs[2].text = f"任教學科：{data_dict.get('subject', '數學領域')}　　　　　　教 學 者（教案設計）：〔{data_dict.get('teacher', '待補：姓名')}〕"
    doc.paragraphs[3].text = f"單元名稱：{data_dict.get('unit_name', '單元名稱')}　　備課成員：〔{data_dict.get('partners', '無')}〕"
    doc.paragraphs[4].text = f"使用版本：{data_dict.get('version', '康軒版')}"
    
    # 2. Table 0: Teaching Philosophy
    set_cell_text(doc.tables[0].rows[1].cells[0], data_dict.get('idea_text', ''), font_name="微軟正黑體", font_size=10)
    
    # Save document
    doc.save(output_path)
    print(f"DOCX successfully generated at {output_path}")
    return output_path
