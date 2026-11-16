from pathlib import Path
import re
import tempfile
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'downloads'
OUT.mkdir(exist_ok=True)
BLACK = '000000'
GRAY = 'E6E6E6'
MID = '666666'

def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd'); tcPr.append(shd)
    shd.set(qn('w:fill'), fill)

def set_cell_margins(cell, top=95, start=95, bottom=95, end=95):
    tc = cell._tc; tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in('w:tcMar')
    if tcMar is None:
        tcMar = OxmlElement('w:tcMar'); tcPr.append(tcMar)
    for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node=tcMar.find(qn(f'w:{m}'))
        if node is None: node=OxmlElement(f'w:{m}'); tcMar.append(node)
        node.set(qn('w:w'),str(v)); node.set(qn('w:type'),'dxa')

def repeat_header(row):
    trPr=row._tr.get_or_add_trPr(); el=OxmlElement('w:tblHeader'); el.set(qn('w:val'),'true'); trPr.append(el)

def set_keep_row(row):
    trPr=row._tr.get_or_add_trPr(); el=OxmlElement('w:cantSplit'); trPr.append(el)

def add_page_field(p):
    p.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    r=p.add_run('Page '); r.font.size=Pt(8); r.font.color.rgb=RGBColor.from_string(MID)
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); p._p.append(fld)

def add_hyperlink(paragraph, text, url):
    rid=paragraph.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    link=OxmlElement('w:hyperlink'); link.set(qn('r:id'),rid)
    run=OxmlElement('w:r'); props=OxmlElement('w:rPr')
    color=OxmlElement('w:color'); color.set(qn('w:val'),'000000'); props.append(color)
    underline=OxmlElement('w:u'); underline.set(qn('w:val'),'single'); props.append(underline)
    run.append(props); node=OxmlElement('w:t'); node.text=text; run.append(node); link.append(run); paragraph._p.append(link)

def new_doc(title, subtitle, doc_code):
    d=Document(); sec=d.sections[0]
    sec.page_width=Inches(8.5); sec.page_height=Inches(11)
    d.core_properties.author='Swaraj Singh'
    d.core_properties.last_modified_by='Swaraj Singh'
    d.core_properties.title=title
    d.core_properties.subject='Fictional security governance and incident response learning project'
    d.core_properties.keywords='security, GRC, risk, incident response, fictional lab'
    d.core_properties.comments='Fictional security design and incident response case study'
    d.core_properties.created=datetime.now(timezone.utc)
    d.core_properties.modified=datetime.now(timezone.utc)
    sec.top_margin=Inches(.75); sec.bottom_margin=Inches(.75); sec.left_margin=Inches(.8); sec.right_margin=Inches(.8)
    sec.header_distance=Inches(.35); sec.footer_distance=Inches(.35)
    styles=d.styles
    normal=styles['Normal']; normal.font.name='Aptos'; normal.font.size=Pt(10.5); normal.font.color.rgb=RGBColor.from_string(BLACK)
    normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.08
    for name,size in [('Title',27),('Subtitle',12),('Heading 1',17),('Heading 2',13),('Heading 3',11)]:
        st=styles[name]; st.font.name='Aptos Display' if name!='Subtitle' else 'Aptos'; st.font.size=Pt(size); st.font.color.rgb=RGBColor.from_string(BLACK)
        if name.startswith('Heading'):
            st.font.bold=True; st.paragraph_format.space_before=Pt(13 if name=='Heading 1' else 9); st.paragraph_format.space_after=Pt(4); st.paragraph_format.keep_with_next=True
    styles['Subtitle'].font.italic=False
    # The built-in Title style carries a blue theme border in Word; explicitly remove it.
    title_ppr=styles['Title']._element.get_or_add_pPr()
    title_border=title_ppr.find(qn('w:pBdr'))
    if title_border is not None: title_ppr.remove(title_border)
    h=sec.header.paragraphs[0]; h.text=f'APEX CAPITAL  |  {doc_code}'; h.style='Caption'
    for r in h.runs: r.font.name='Aptos'; r.font.size=Pt(8); r.font.bold=True; r.font.color.rgb=RGBColor.from_string(MID)
    add_page_field(sec.footer.paragraphs[0])
    p=d.add_paragraph(style='Title'); p.paragraph_format.space_before=Pt(68); p.paragraph_format.space_after=Pt(10)
    ppr=p._p.get_or_add_pPr(); pborder=OxmlElement('w:pBdr'); bottom=OxmlElement('w:bottom'); bottom.set(qn('w:val'),'none'); pborder.append(bottom); ppr.append(pborder)
    p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    r=p.add_run(title); r.bold=True; r.font.name='Aptos Display'; r.font.size=Pt(27); r.font.color.rgb=RGBColor.from_string(BLACK)
    p=d.add_paragraph(subtitle, style='Subtitle'); p.paragraph_format.space_after=Pt(25)
    for line in ['Prepared by Swaraj Singh','Portfolio learning project','16 November 2026']:
        p=d.add_paragraph(); p.paragraph_format.space_after=Pt(4); rr=p.add_run(line); rr.font.size=Pt(10); rr.font.color.rgb=RGBColor.from_string(MID)
    d.add_paragraph('')
    p=d.add_paragraph(); r=p.add_run('DOCUMENT STATUS  '); r.bold=True; r.font.size=Pt(9)
    r=p.add_run('Fictional scenario • design proposal • no production deployment or VM tests claimed'); r.font.size=Pt(9)
    p.paragraph_format.space_before=Pt(26)
    p=d.add_paragraph(); p.paragraph_format.space_before=Pt(5)
    r=p.add_run('Companion project: '); r.font.size=Pt(9)
    add_hyperlink(p,'GitHub repository','https://github.com/dedsec-terminal/Apex-Capital-GRC')
    d.add_page_break()
    return d

def para(d, text, style=None, boldlead=None):
    p=d.add_paragraph(style=style)
    if boldlead and text.startswith(boldlead):
        p.add_run(boldlead).bold=True; p.add_run(text[len(boldlead):])
    else: p.add_run(text)
    return p

def bullets(d, items, numbered=False):
    for x in items: para(d,x,'List Number' if numbered else 'List Bullet')

def table(d, headers, rows, widths=None, font=9.3):
    t=d.add_table(rows=1, cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'
    t.autofit=False
    if widths:
        for col,w in zip(t.columns,widths): col.width=Inches(w)
    head=t.rows[0]; repeat_header(head); set_keep_row(head)
    for i,x in enumerate(headers):
        c=head.cells[i]; c.text=str(x); set_cell_shading(c,'333333'); set_cell_margins(c); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        for p in c.paragraphs:
            p.paragraph_format.space_after=Pt(0)
            for r in p.runs: r.font.name='Aptos'; r.font.size=Pt(font); r.font.bold=True; r.font.color.rgb=RGBColor.from_string('FFFFFF')
    for ri,row in enumerate(rows):
        cells=t.add_row().cells; set_keep_row(t.rows[-1])
        for i,x in enumerate(row):
            c=cells[i]; c.text=str(x); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; set_cell_margins(c)
            if ri%2: set_cell_shading(c,'F2F2F2')
            if widths and i<len(widths): c.width=Inches(widths[i])
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(1); p.paragraph_format.line_spacing=1.0
                for r in p.runs: r.font.name='Aptos'; r.font.size=Pt(font); r.font.color.rgb=RGBColor.from_string(BLACK)
    # Keep compact tables cohesive across page boundaries so a final row or a
    # form row does not become detached from its heading and column labels.
    if len(t.rows)<=9:
        for row in t.rows[:-1]:
            for cell in row.cells:
                for p in cell.paragraphs: p.paragraph_format.keep_with_next=True
    d.add_paragraph().paragraph_format.space_after=Pt(2)
    return t

def diagram(path):
    w,h=1500,560; im=Image.new('RGB',(w,h),'white'); dr=ImageDraw.Draw(im)
    try: f=ImageFont.truetype('arial.ttf',28); sm=ImageFont.truetype('arial.ttf',22); tiny=ImageFont.truetype('arial.ttf',18)
    except: f=sm=tiny=ImageFont.load_default()
    boxes=[(45,120,330,395,'WAN / UPLINK','External boundary'),(405,120,690,395,'pfSense','4 interfaces\nWAN + 3 zones'),(780,30,1080,160,'DMZ','10.0.1.0/24\nUbuntu Web .10'),(780,205,1080,335,'INTERNAL','10.0.2.0/24\nWindows .10'),(780,380,1080,510,'MANAGEMENT','10.0.3.0/24\nWazuh .10')]
    for x1,y1,x2,y2,a,b in boxes:
        dr.rectangle((x1,y1,x2,y2),outline='#111111',width=4,fill='white')
        dr.text((x1+18,y1+18),a,font=f,fill='black')
        for j,line in enumerate(b.split('\n')): dr.text((x1+18,y1+62+j*30),line,font=sm,fill='black')
    def arrow(a,b,label,yoff=0):
        x1,y1=a; x2,y2=b; dr.line((x1,y1,x2,y2),fill='#111111',width=4); dr.polygon([(x2,y2),(x2-14,y2-10),(x2-14,y2+10)],fill='#111111'); dr.text(((x1+x2)//2-42,(y1+y2)//2-28+yoff),label,font=tiny,fill='black')
    arrow((330,255),(405,255),''); arrow((690,190),(780,95),''); arrow((690,255),(780,270),''); arrow((690,320),(780,445),'')
    dr.text((45,500),'Flow intent: web 80/443; admin 22/3389 from approved sources; Wazuh 1514/1515',font=tiny,fill='#333333')
    dr.text((45,530),'Default-deny between zones; proposed design, not verified VM configuration',font=tiny,fill='#333333')
    im.save(path)

def build_capability():
    d=new_doc('Security and GRC Capability Report','A fictional financial services security lab: requirements, risk, control design, response and validation','CAPABILITY REPORT')
    d.add_heading('Executive summary',1)
    para(d,'This report demonstrates a structured approach to turning business protection needs into security requirements, risk decisions, control intent, incident response procedures and verifiable evidence. The scenario models a small financial services environment with public web access, an internal endpoint and centralized monitoring. The resulting design prioritizes segmentation, identity controls, resilience, detection and accountable risk treatment.')
    para(d,'The work product is a design proposal for a fictional four-VM lab. No virtual machines were registered during the readiness check; no controls were configured, incidents exercised, or security tests executed. Risk scores are initial scenario estimates. Framework references are proposed crosswalks, not control-effectiveness results or compliance conclusions.')
    table(d,['Decision area','Current position','Evidence required to advance'],[
        ('Architecture','Four-VM, three-zone design proposed','Build isolated lab; export firewall and host configurations'),
        ('Risk','Eight inherent scenario risks prioritized','Validate assumptions with asset/service owners; assign treatment approvals'),
        ('Frameworks','Selected NIST CSF 2.0 and ISO/IEC 27001:2022 references','Confirm scope, applicability and final mapping with control owners'),
        ('Incident response','Operational plan and tabletop design prepared','Approve roles; conduct exercise; capture decisions and timings'),
        ('Assurance','Tests and evidence are pending','Execute approved procedures; retain dated, redacted artifacts')])
    d.add_heading('1. Purpose and approach',1)
    para(d,'The report follows a traceable assurance path: define the service and its protection needs; identify threats and business consequences; assign accountable roles; map control intent to a proposed design; define response and validation procedures; collect evidence; and use findings to revise risk treatment. Each step names its inputs and the artifact needed to support a decision.')
    table(d,['Stage','Question answered','Output'],[
        ('Requirements','What must remain confidential, accurate and available?','Business and security requirements'),
        ('Risk','How could the requirement fail and what is the consequence?','Inherent scenario risk and owner role'),
        ('Control design','What safeguard is intended to reduce exposure?','Control intent and proposed framework crosswalk'),
        ('Response','Who decides, what evidence is preserved, and how is service restored?','Incident plan, decision log and recovery gates'),
        ('Validation','What would demonstrate the safeguard works?','Test procedure, evidence artifact and reviewer conclusion'),
        ('Improvement','What remains open and who owns the next action?','Treatment/action register and reassessment')])
    d.add_heading('2. Scenario and scope',1)
    para(d,'Apex Capital is a fictional scenario used to demonstrate risk-based security planning. The business profile, workforce, data categories and service dependencies are assumptions for analysis. The four virtual machines are a simplified lab abstraction; they do not represent a deployed business environment or production-scale architecture.')
    table(d,['In scope','Out of scope'],[
        ('Four-VM network and host design; firewall intent; endpoint and monitoring controls; risk register; incident response; test and evidence planning.','Real client systems or data; cloud deployment; payment-card environment; formal audit or certification; legal determination; completed supplier due diligence; executed penetration or control testing.')])
    para(d,'The fictional service is assumed to handle sensitive customer and financial information. Before applying this design to a real organization, validate data categories, critical services, business impact tolerances, supplier dependencies, operating jurisdictions and regulatory applicability with accountable owners.')
    table(d,['Service or information','Why it matters','Response priority','Decision before deployment'],[
        ('Internal records and privileged identities','Unauthorized access could affect confidentiality and business decisions','Stop suspected misuse; establish identity and data scope','Data owner confirms classification, roles and acceptable recovery point'),
        ('Public web service','An exposed service may provide an entry point or availability dependency','Contain affected service while preserving monitoring visibility','Service owner sets minimum service and restoration order'),
        ('Monitoring and administration','Responders need trustworthy telemetry and a clean recovery path','Protect logging and approved admin access during isolation','Security owner confirms retention, clock sync and responder access'),
        ('Supplier connections and evidence','A provider may affect access, data handling or recovery','Establish dependency and restrict risky access when justified','Supplier owner records criticality, contractual duties and escalation path')])
    para(d,'Recovery time and recovery point objectives are intentionally unset until a business impact review establishes them. A technical target chosen only because the lab can meet it would not demonstrate that the business requirement was met.')
    d.add_heading('3. Business requirements and traceability',1)
    table(d,['ID','Protection need','Control intent','Validation evidence'],[
        ('BR-01','Protect sensitive information in transit and at rest','Encryption selected for applicable data paths and storage; access restricted by role','Effective configuration, certificate or policy output, and approved test record'),
        ('BR-02','Restrict privileged and remote access','Separate administrative access; limit RDP/SSH to approved management sources; review access','Effective access policy, allowed/denied connectivity, access review'),
        ('BR-03','Contain compromise between network zones','Default-deny inter-zone policy with explicit, justified flows','Sanitized rule export, paired positive/negative tests, firewall logs'),
        ('BR-04','Detect and investigate suspicious activity','Collect relevant endpoint and network events; synchronize timestamps; restrict log access','Source inventory, generated event, SIEM record, timestamp and retrieval check'),
        ('BR-05','Restore trusted services after disruption','Protect backups; document recovery dependencies and integrity checks','Restore log, integrity results, measured recovery time, owner acceptance'),
        ('BR-06','Manage supplier and service-provider exposure','Tier suppliers, review relevant evidence, track exceptions and reassessment','Diligence record, decision rationale, remediation status and review date'),
        ('BR-07','Communicate and govern incident decisions','Assign incident authority, escalation, verified updates and notification assessment','Decision log, approved situation report, post-incident actions')])
    para(d,'Traceability is complete only when a requirement links to a risk, an accountable control owner, an operating procedure, a test that can falsify the control assumption, and reviewable evidence. A framework cross-reference alone does not close that chain.')
    d.add_heading('4. Proposed architecture and security rationale',1)
    with tempfile.TemporaryDirectory(prefix='apex-docx-') as td:
        img=Path(td)/'architecture.png'; diagram(img)
        d.add_picture(str(img),width=Inches(6.7))
    para(d,'Figure 1. Proposed four-interface boundary and three-zone lab. Addresses and flows are design values, not observed configuration.',None)
    table(d,['Zone / component','Address or interface','Purpose','Primary boundary'],[
        ('pfSense','WAN plus 10.0.1.1 / 10.0.2.1 / 10.0.3.1','Routing, NAT and stateful filtering','No WAN management path; explicit rules between zones'),
        ('DMZ / Ubuntu web','10.0.1.10 / 10.0.1.0/24','Simulated public service','Permit only deliberately exposed web ports; deny DMZ-to-internal by default'),
        ('Internal / Windows','10.0.2.10 / 10.0.2.0/24','Simulated business endpoint','Administrative RDP restricted to approved management clients'),
        ('Management / Wazuh','10.0.3.10 / 10.0.3.0/24','Central telemetry and alert review','Restrict dashboard to approved administrators; log collection limited to sources')])
    para(d,'Intended telemetry includes Wazuh agent traffic on TCP 1514 and controlled enrollment on TCP 1515. Optional pfSense syslog forwarding uses UDP 514 only when configured. These are proposed defaults; confirm ports, authentication and logging behavior against the deployed product version. Define outbound rules explicitly and keep the lab isolated until its upstream attachment is reviewed.')
    d.add_heading('5. Risk assessment',1)
    para(d,'The initial model multiplies likelihood and impact ratings from 1 to 5. It is a qualitative prioritization aid, not a calibrated quantitative measure. Scores are inherent scenario estimates before considering control effectiveness. No residual score is assigned because design and execution evidence have not been reviewed.')
    risks=[('R-001','DMZ host reaches internal systems',3,5,15,'High','Network security owner'),('R-002','Credential compromise exposes access',4,5,20,'Critical','IAM owner'),('R-003','Ransomware disrupts service or data',4,5,20,'Critical','Endpoint and resilience owner'),('R-004','Missing logs weaken investigation',3,4,12,'Medium','Security operations owner'),('R-005','Public service compromise',3,5,15,'High','Application / infrastructure owner'),('R-006','Insider misuse of authorized access',2,5,10,'Medium','Data owner and IAM owner'),('R-007','Supplier weakness affects the business',3,5,15,'High','Third-party risk owner'),('R-008','Firewall drift exposes a protected path',3,4,12,'Medium','Network security owner')]
    table(d,['ID','Scenario risk','L','I','Score','Band','Proposed owner'],risks,[.55,2.25,.3,.3,.5,.55,1.45],8.5)
    para(d,'Risk ownership is a proposed role assignment. Treatment decisions require evidence of the service context, threat conditions, current safeguards and business impact. Residual risk should be documented only after operation is demonstrated, exceptions are understood and an authorized owner accepts the remaining exposure.')
    d.add_heading('6. Control design and framework mapping',1)
    table(d,['Control theme','Design intent','Selected references'],[
        ('Supplier governance','Classify service criticality; review proportionate evidence; track gaps and reassess','NIST CSF 2.0 GV.SC-01/02/04/05/06/07; ISO A.5.19–A.5.21'),
        ('Identity and access','Least privilege, protected privileged access and periodic rights review','NIST PR.AA-05; ISO A.5.15, A.5.18, A.8.2'),
        ('Network security','Restrict inter-zone access and review firewall changes','NIST PR.IR-01; ISO A.8.20–A.8.22, A.8.32'),
        ('Configuration and vulnerabilities','Maintain known baselines and address technical weaknesses','NIST PR.PS-01/02; ISO A.8.8, A.8.9'),
        ('Logging and detection','Monitor endpoints, services and network activity','NIST DE.CM-01/09; ISO A.8.15, A.8.16'),
        ('Incident response','Prepare roles, coordinate response and record decisions','NIST RS.MA-01; ISO A.5.24, A.5.26'),
        ('Backups and recovery','Protect backups and verify recovery readiness','NIST PR.DS-11, RC.RP-01; ISO A.8.13, A.5.29, A.5.30')])
    para(d,'The references are analyst-selected associations between control intent and framework outcomes. NIST CSF describes cybersecurity outcomes; it does not prescribe a firewall configuration. ISO Annex A applicability depends on organizational context, risk assessment and the approved Statement of Applicability. Mapping does not establish implementation, compliance or effectiveness.')
    d.add_heading('7. Supplier assurance and GRC workflow',1)
    para(d,'Supplier risk is represented by R-007. A repeatable third-party risk process should identify the service and data access, assign criticality, request relevant evidence, assess scope and freshness, record exceptions, define treatment, obtain an authorized decision and set reassessment or offboarding triggers.')
    table(d,['Workflow step','Decision or record','Quality check'],[
        ('Intake and inventory','Legal entity, service, owner, data and access','Confirm service boundary and subcontractors'),
        ('Tiering','Criticality rationale and business dependency','Use impact and substitutability; document assumptions'),
        ('Evidence review','Evidence item, scope, period, issuer and reviewer','Verify that the evidence covers the actual service and relevant period'),
        ('Control assessment','Question, mapped reference, evidence and finding','Do not treat a policy statement or certificate as proof of every control'),
        ('Treatment','Action, accountable role, due date and retest evidence','Separate remediation intent from verified closure'),
        ('Decision','Approve, conditionally accept, defer or reject','Authorized business owner records rationale and exceptions'),
        ('Monitoring / exit','Change triggers, reassessment, access removal','Confirm closure of integrations, accounts and retained data')])
    para(d,'A decision should be supported by evidence that matches the supplier service, stated scope, relevant dates and control question. Findings should remain open until a reviewer evaluates suitable remediation evidence. A GRC platform can support workflow and records, but using a platform does not itself establish governance effectiveness.')
    d.add_heading('8. Incident response design',1)
    para(d,'The proposed incident plan assigns decision authority, severity, escalation, communications, evidence handling, recovery approval and post-incident improvement. It covers ransomware, credential compromise, web-service compromise, monitoring disruption and supplier-notified incidents. External reporting is assessed against verified facts, affected data, applicable jurisdictions and current legal advice; the plan does not invent a statutory notification deadline.')
    table(d,['Phase','Core activity','Decision record'],[
        ('Prepare','Maintain role contacts, access, logging, backups, playbooks and exercises','Readiness checklist and contact owner'),
        ('Report and triage','Validate source, scope, confidence and business impact','Incident ID, timeline, severity and activation decision'),
        ('Contain','Choose the narrowest effective isolation; preserve evidence','Approver, affected paths, rationale and time'),
        ('Investigate and eradicate','Correlate endpoint, identity, network and supplier evidence; remove cause','Evidence register, scope assessment and remediation owner'),
        ('Recover','Restore trusted baseline and verify integrity, access and monitoring','Recovery gates and business-owner acceptance'),
        ('Learn','Review decisions, evidence gaps and control failures','Corrective action, owner, due date and retest')])
    d.add_heading('9. Tabletop scenario and expected decisions',1)
    para(d,'Scenario: Wazuh produces a synthetic anomalous authentication and ransomware-style alert associated with the Windows endpoint at 10.0.2.10. This is an exercise design only. It does not describe an observed incident or completed tabletop.')
    table(d,['Inject / decision point','Expected action','Evidence to capture'],[
        ('Initial alert','Open incident record, validate host/time/source, preserve original alert, assess confidence and assign provisional severity','Alert export, event time, analyst notes and incident ID'),
        ('Corroborated encryption and spread','Escalate to response lead; isolate affected endpoint or specific path after authority check; preserve firewall and endpoint telemetry','Isolation approver/time, rule change, scope and evidence hashes'),
        ('No independent corroboration','Avoid destructive isolation; collect approved volatile and endpoint/network evidence; seek second-source confirmation','Query results, collection method, confidence and next review time'),
        ('Possible data exposure','Identify affected data and users; involve privacy/legal role to assess current obligations','Verified facts, uncertainty, jurisdiction assessment and decision owner'),
        ('Supplier may be involved','Review integration/access, preserve supplier notice and contract terms, restrict risky access when authorized','Supplier evidence request, access change, communication and decision log'),
        ('Restore requested','Require clean baseline, credential rotation, fixed entry path, integrity checks, monitoring and service-owner approval','Restore log, validation results, exceptions and acceptance decision')])
    d.add_heading('10. Evidence and evaluation',1)
    para(d,'Evidence should be attributable, time-bound, protected from alteration and sufficient to reproduce the reviewer’s conclusion. Keep originals read-only, record collection method and custody, hash exported files, synchronize timestamps and create redacted public copies separately. Avoid placing raw logs, usernames, secrets or personal data in public repositories.')
    table(d,['Measure','Definition','Record after exercise'],[
        ('Classification latency','Incident opened to severity and activation decision','Start/end timestamps; not yet measured'),
        ('Containment decision latency','Corroborated compromise inject to authorized isolation decision','Start/end timestamps; not yet measured'),
        ('Evidence completeness','Required evidence fields present ÷ required fields','Completed evidence register; not yet measured'),
        ('Decision traceability','Material decisions linked to evidence, authority and rationale','Incident log review; not yet measured'),
        ('Communication accuracy','Verified factual statements ÷ all factual statements in draft update','Reviewer check; not yet measured'),
        ('Recovery readiness','Required recovery gates correctly identified ÷ gates expected','Exercise observer record; not yet measured'),
        ('Improvement closure','Actions with accepted closure evidence ÷ actions due for review','Action register and reviewer disposition; not yet measured')])
    d.add_heading('11. Improvement register and next steps',1)
    table(d,['Priority','Action','Owner role','Closure evidence'],[
        ('1','Provision isolated four-VM lab and record interfaces, versions and baseline configs','Lab / network owner','Inventory, approved topology and sanitized exports'),
        ('2','Validate criticality, data assumptions and applicable obligations','Business and privacy/legal owners','Approved service profile and documented applicability assessment'),
        ('3','Implement and test firewall, host and logging safeguards','Infrastructure and security operations owners','Test logs, configurations, timestamps and independent review'),
        ('4','Run incident tabletop and capture actual participant decisions','Incident manager','Attendance, inject timeline, decision log, scoring and improvement actions'),
        ('5','Conduct controlled restore exercise and measure recovery','Resilience owner','Restore output, integrity check, elapsed time and acceptance'),
        ('6','Establish supplier intake, evidence review and treatment workflow','Third-party risk owner','Completed synthetic assessment, review rationale and retest record')])
    d.add_heading('Conclusion',1)
    para(d,'The report demonstrates a way to connect business needs to risk, controls, evidence and response decisions. Its strongest next step is execution in an isolated lab followed by independent review of dated evidence. Until then, the architecture, mappings, procedures and test outcomes remain proposals.')
    d.add_heading('Appendix A. Requirements-to-evidence traceability',1)
    table(d,['Requirement','Risk','Control / procedure','Validation','Evidence status'],[
        ('BR-02/03 segmentation and access','R-001, R-008','Firewall baseline; network response plan','T-01/T-02/T-08','Planned; no execution evidence'),
        ('BR-04 detection and investigation','R-004','Logging baseline; incident triage','T-05','Planned; no event evidence'),
        ('BR-05 recovery','R-003','Backup and recovery procedure','T-06','Planned; no restore evidence'),
        ('BR-06 supplier assurance','R-007','Supplier due diligence and incident interface','T-07','Planned; no assessment evidence'),
        ('BR-07 communication and governance','R-002/R-003/R-004','Severity, escalation and communications','Tabletop exercise','Designed; no exercise evidence')])
    path=OUT/'Apex_Capital_Security_and_GRC_Report.docx'; d.save(path); return path

def clean_md(s):
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',s)
    s=re.sub(r'\*\*(.*?)\*\*',r'\1',s); s=re.sub(r'(?<!\*)\*([^*]+)\*',r'\1',s); s=s.replace('`','')
    return s.strip()

def parse_table(lines):
    vals=[]
    for line in lines:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if cells and all(re.fullmatch(r':?-{3,}:?',c or '-') for c in cells): continue
        vals.append([clean_md(c) for c in cells])
    return vals

def compact_wide_table(rows, max_columns=5):
    if not rows or len(rows[0])<=max_columns: return rows
    headers=rows[0]; group=(len(headers)+max_columns-1)//max_columns
    out_headers=[]; ranges=[]
    for start in range(0,len(headers),group):
        end=min(start+group,len(headers)); ranges.append((start,end))
        out_headers.append(' / '.join(x for x in headers[start:end] if x))
    out=[out_headers]
    for row in rows[1:]:
        cells=[]
        for start,end in ranges:
            entries=[]
            for i in range(start,end):
                value=row[i] if i<len(row) else ''
                if value: entries.append(f'{headers[i]}: {value}')
            cells.append('; '.join(entries))
        out.append(cells)
    return out

def build_irp():
    md=ROOT/'07-Policies-and-Standards'/'incident-response-plan.md'
    if not md.exists(): raise FileNotFoundError(f'Required incident plan not found: {md}')
    lines=md.read_text(encoding='utf-8').splitlines()
    d=new_doc('Cyber Incident Response Plan','Fictional Apex Capital lab | operational roles, response procedures and exercise records','INCIDENT RESPONSE PLAN')
    # Preserve the detailed, scenario-specific plan content while translating Markdown structure into editable Word elements.
    i=0; first_title=True
    while i<len(lines):
        s=lines[i].strip()
        if not s: i+=1; continue
        if s.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'): block.append(lines[i].strip()); i+=1
            rows=compact_wide_table(parse_table(block))
            if rows and rows[0]:
                n=len(rows[0]); normalized=[r+['']*(n-len(r)) for r in rows[1:] if len(r)>0]
                table(d,rows[0][:n], [r[:n] for r in normalized],font=9.3)
            continue
        if s.startswith('> '):
            p=d.add_paragraph(); p.paragraph_format.left_indent=Inches(.2); r=p.add_run(clean_md(s[2:])); r.italic=True; r.font.size=Pt(9); i+=1; continue
        if s.startswith('# '):
            if first_title: first_title=False
            else: d.add_heading(clean_md(s[2:]),1)
            i+=1; continue
        if s.startswith('## '):
            heading=clean_md(s[3:])
            if heading.startswith('Appendix E. Post-incident review prompts'): d.add_page_break()
            d.add_heading(heading,1); i+=1; continue
        if s.startswith('### '):
            heading=clean_md(s[4:])
            if heading.startswith('Appendix E. Post-incident review prompts'): d.add_page_break()
            d.add_heading(heading,2); i+=1; continue
        if s.startswith('#### '): d.add_heading(clean_md(s[5:]),3); i+=1; continue
        if s.startswith(('- ','* ')):
            p=d.add_paragraph(style='List Bullet'); p.add_run(clean_md(s[2:])); i+=1; continue
        if re.match(r'^\d+[.)]\s+',s):
            p=d.add_paragraph(style='List Number'); p.add_run(clean_md(re.sub(r'^\d+[.)]\s+','',s))); i+=1; continue
        if s.startswith('```'):
            code=[]; i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'): code.append(lines[i]); i+=1
            i+=1; p=d.add_paragraph(); p.paragraph_format.left_indent=Inches(.2)
            r=p.add_run('\n'.join(code)); r.font.name='Consolas'; r.font.size=Pt(8); continue
        chunks=[s]; i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|','> ','- ','* ','```')) and not re.match(r'^\d+[.)]\s+',lines[i].strip()):
            chunks.append(lines[i].strip()); i+=1
        para(d,clean_md(' '.join(chunks)))
    path=OUT/'Apex_Capital_Incident_Response_Plan.docx'; d.save(path); return path

if __name__=='__main__':
    a=build_capability(); b=build_irp(); print(f'Created {a}\nCreated {b}')
