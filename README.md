# ShowYourWork: Evidence-First Application Validation

ShowYourWork is an evidence-first application validation and document verification platform designed for institutional accreditation, regulatory scrutiny, and administrative compliance.

The platform enforces transparent, verifiable, and legally auditable decision support by replacing opaque black-box scoring with deterministic rule engines, tamper-evident cryptographic ledgers, and interactive evidence cards.

---

## Core Principles

1. **Rules Decide Compliance**: Statutory rules and regulatory handbook clauses determine compliance. Machine learning models assist solely by classifying documents, extracting localized text fields, and phrasing plain-language explanations.
2. **Evidence-Linked Observations**: Every anomaly flag carries concrete provenance: source document ID, page index, field key, visual bounding box coordinates, applicable handbook clause, and non-accusatory rationale.
3. **Non-Accusatory Classification**: Flags are categorized as indicators (*"Indicator: needs review"*), never branded as fraud or forgery.
4. **Maker-Checker Governance**: Automated checks assist review; no adverse administrative action occurs without an authorized scrutiny officer's formal sign-off.
5. **Synthetic, Anonymized Data**: Built strictly using synthetic test dossiers and anonymized institutional parameters with zero personal or proprietary data.

---

## Standard Verification Statuses

The platform categorizes all applications, documents, and verification checks into 6 canonical statuses:

| Status | Definition |
| :--- | :--- |
| **Verified** | All submitted documents are authenticated via trusted authority handshakes, active dates, and consistent cross-record data. |
| **Mismatch detected** | Concrete discrepancy detected between submitted documents (e.g., land acreage mismatch or entity name variation). |
| **Expired** | Statutory certificate, NOC, or accreditation validity has lapsed prior to the designated academic period. |
| **Verification pending** | Document dispatched to issuing gateway or background automated query queue awaiting response. |
| **Source unavailable** | External authority API or issuer repository returned an error, connection timeout, or maintenance code. |
| **Manual review required** | Degraded optical scan quality, corrupted QR payload, or anomalous generator metadata requiring officer inspection. |

---

## Architectural Overview

```
├── frontend/
│   ├── index.html            # Single-page administrative dashboard
│   ├── css/app.css           # Restrained administrative design system
│   ├── js/data.js            # Seed application store & regulatory norms
│   ├── js/app.js             # RBAC controller, pre-flight report & demo pipeline
│   ├── js/forensicEngine.js  # Evidence card renderer, PDF viewer & bounding boxes
│   ├── js/evidenceGraph.js   # Inter-document consistency SVG graph
│   ├── js/verificationLadder.js # 5-Tier hierarchical verification gateway
│   ├── js/complianceRules.js # Configurable statutory parameter engine
│   └── js/auditTrail.js      # SHA-256 hash-chained cryptographic ledger
├── backend/
│   ├── app/main.py           # FastAPI regulatory validation endpoints
│   ├── app/database.py       # SQLite connection manager & 10 core relational tables
│   ├── app/seed.py           # Database seeder with 8 institutions & 12 test dossiers
│   └── app/generate_synthetic_pdfs.py # ReportLab synthetic document generator
├── server.py                 # Static HTTP application server
└── run.bat                   # Desktop one-click execution script
```

---

## Roles and Access Control (RBAC)

- **Institution**: Submit regulatory dossiers, view pre-flight checklist validation reports, inspect highlighted document fields, and respond to deficiency memos.
- **Officer**: Perform deep side-by-side evidence scrutiny, evaluate cross-document contradictions, inspect 5-tier verification responses, and execute statutory Maker-Checker actions.
- **Admin**: Configure regulatory handbook thresholds (e.g., minimum land acreage, faculty-student ratios, corpus funds) and verify ledger cryptographic proofs.

---

## Quick Start & Running Locally

### Option 1: Desktop Launcher (Windows)
Double-click `run.bat` in the project root to start both the backend API and frontend portal.

### Option 2: Command Line
```powershell
# 1. Start FastAPI backend (port 8000)
& "C:\Users\acer\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000

# 2. Start static frontend server (port 8080)
& "C:\Users\acer\AppData\Local\Python\pythoncore-3.14-64\python.exe" server.py
```

Access the user interface at: **[http://localhost:8080](http://localhost:8080)**  
Access the API documentation at: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## Pre-Seeded Deliberate Test Cases

| Case | Scenario | Expected Status |
| :--- | :--- | :--- |
| **Case A** | Clean Application (All documents valid, active dates, clean OCR) | `Verified` |
| **Case B** | Expired Accreditation (Accreditation certificate expired >2.5 years ago) | `Expired` |
| **Case C** | Entity Name Discrepancy (College name varies between NOC and Affidavit) | `Mismatch detected` |
| **Case D** | Shared Document Reuse (Identical Fire NOC file hash uploaded to two institutions) | `Mismatch detected` |
| **Case E** | Generator Footprint Anomaly (Structural certificate contains non-standard export metadata) | `Manual review required` |
| **Case F** | Cryptographic QR Authentication (Embedded 2D QR decrypts to verified portal URN) | `Verified` |
| **Case G** | Corrupted QR Code (Unreadable bitmask prevents automated cryptographic verification) | `Manual review required` |
| **Case H** | Low-Quality Scan (Mobile camera capture with optical confidence < 0.70 threshold) | `Manual review required` |
