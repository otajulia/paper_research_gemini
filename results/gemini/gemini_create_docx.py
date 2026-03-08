import zipfile
import os

def create_docx(file_path):
    # Minimalistic docx structure (XML based)
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>"""

    # Comprehensive and Deep Research Content
    document_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Deep Research Report: Advanced Economic Analysis of Physical Fitness and Healthcare Expenditure (2026 Update)</w:t></w:r></w:p>
    
    <w:p><w:r><w:t>1. Executive Summary: The Longitudinal Impact of NFA100</w:t></w:r></w:p>
    <w:p><w:r><w:t>Recent 2025 longitudinal data (Lee et al., 2025; KISS) reveals that participants in the National Fitness Award 100 program demonstrate an annual healthcare cost increase of only 70,000 KRW, compared to 470,000 KRW in the control group—a net preventive dividend of 400,000 KRW (~$300) per person. This report synthesizes this evidence to position the current manuscript for top-tier journals.</w:t></w:r></w:p>

    <w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>2. Methodological Superiority: Causal Inference vs. Association</w:t></w:r></w:p>
    <w:p><w:r><w:t>To meet Lancet Public Health/JAMA standards, the analysis must transition to Target Trial Emulation. Key 2026 trends emphasize:</w:t></w:r></w:p>
    <w:p><w:r><w:t>- AIPW (Augmented Inverse Probability Weighting) for double-robustness.</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Two-step TMLE (hTMLE) to address zero-inflated medical costs (point-mass at zero vs. gamma-distributed positive costs).</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Linkage Bias Correction: Utilizing IPLW to adjust for the 66% data linkage rate between NFA100 and NHIS databases.</w:t></w:r></w:p>

    <w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>3. Skill-Based Fitness: The Critical Economic Buffer for the Elderly</w:t></w:r></w:p>
    <w:p><w:r><w:t>A groundbreaking finding for 2026 is the superior predictive power of Skill-Based Fitness (SBF) over traditional Health-Related Fitness (HRF) in geriatric populations:</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Seniors in the 'Participation-only' (lowest) tier of TUG (Timed Up-and-Go) incur $308.66 USD more in annual costs due to fall-related risks.</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Chronic Disease Risk: Individuals failing to receive a grade (Participation-only) show a 2.13x higher risk of Diabetes and a 3.54x higher risk of Heart Disease compared to Grade 1 achievers.</w:t></w:r></w:p>

    <w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>4. Global Economic Context and Policy Simulation</w:t></w:r></w:p>
    <w:p><w:r><w:t>South Korea's healthcare spending is highly efficient, with a cost of $20,678 per DALY averted (JAMA Health Forum, 2025). The NFA100 program is a scalable infrastructure for this efficiency. A proposed policy simulation (Scenario: 10% shift from Participation to Tier 3) would yield projected annual savings of billions of KRW, justifying the government's 2025 expansion to 96 certification centers.</w:t></w:r></w:p>

    <w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>5. Conclusion: Strategy for High-Impact Publication</w:t></w:r></w:p>
    <w:p><w:r><w:t>The manuscript should leverage the 'Functional Threshold' narrative, arguing that maintaining fitness above the Tier 3 limit prevents catastrophic medical cost spikes. This depth exceeds prior association-only studies and provides the policy evidence demanded by top general medicine journals.</w:t></w:r></w:p>
  </w:body>
</w:document>"""

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with zipfile.ZipFile(file_path, 'w') as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', rels)
        docx.writestr('word/document.xml', document_xml)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)

if __name__ == "__main__":
    create_docx("gemini/Deep_Research_Report_20260308.docx")
    print("Deep_Research_Report_20260308.docx created successfully in gemini/ folder.")
