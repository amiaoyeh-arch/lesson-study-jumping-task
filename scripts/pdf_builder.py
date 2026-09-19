# -*- coding: utf-8 -*-
"""
pdf_builder.py - Convert HTML slide deck to 16:9 high-resolution vector PDF using Edge Headless.
"""
import os
import subprocess

def export_pdf(html_print_path, pdf_output_path):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_output_path}",
        html_print_path
    ]
    
    print(f"Exporting PDF via Edge Headless to {pdf_output_path}...")
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(pdf_output_path):
        size_mb = os.path.getsize(pdf_output_path) / (1024 * 1024)
        print(f"PDF Successfully generated: {pdf_output_path} ({size_mb:.2f} MB)")
        return True
    else:
        print("Failed to generate PDF.")
        return False
