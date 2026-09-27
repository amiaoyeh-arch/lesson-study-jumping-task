# -*- coding: utf-8 -*-
"""
16:9 Vector PDF Generator using Microsoft Edge Headless mode
"""
import os
import subprocess

def export_print_html_to_pdf(print_html_path, output_pdf_path):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        print_html_path
    ]
    print(f"Exporting 16:9 Vector PDF: {output_pdf_path}...")
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(output_pdf_path):
        size_mb = os.path.getsize(output_pdf_path) / (1024 * 1024)
        print(f"Successfully generated 16:9 PDF: {output_pdf_path} ({size_mb:.2f} MB)")
        return output_pdf_path
    return None
