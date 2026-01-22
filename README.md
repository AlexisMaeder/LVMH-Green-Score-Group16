```markdown
# 🌿 LVMH AI Green Score

> **Operational Decision Support Tool for AI Projects (GO / NO-GO)**
> *Alberthon 2025*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Prototype_Validated-success)

## 🎯 Project Overview

**LVMH AI Green Score** is a governance tool designed to estimate the environmental footprint of AI initiatives **before** development. It transforms technical complexity into a clear business decision (**GO / NO-GO**).

In a context where AI adoption is accelerating, this tool ensures that LVMH's sustainability commitments are respected by:
1.  **Aggregating** Training and Inference costs.
2.  **Visualizing** the impact of multimodal features (Video/Images).
3.  **Delivering** an operational certificate for budget approval.

---

## ✨ Key Features

* **🌍 Location-Aware Analysis:** Dynamic adjustment of CO2 emissions based on the server's energy mix (France vs USA vs Global).
* **📸 Multimodal Impact:** Advanced estimation of energy consumption for Image & Video generation (high impact features).
* **🚦 Nutri-Score Logic:** Immediate rating from **A (Sustainable)** to **E (Critical)** based on LVMH internal thresholds.
* **📄 Official Certificate:** One-click generation of a downloadable report for project auditing and governance.
* **🔍 Transparent Methodology:** Full visibility on calculation formulas and assumptions directly within the app.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.8 or higher
* Git

### Step 1: Clone the repository
*Replace [VOTRE_NOM_UTILISATEUR] below with your actual GitHub username*

```bash
git clone [https://github.com/](https://github.com/)[VOTRE_NOM_UTILISATEUR]/LVMH-Green-Score.git
cd LVMH-Green-Score

```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt

```

### Step 3: Run the application

```bash
streamlit run app.py

```

*The application will open automatically in your web browser at `http://localhost:8501`.*

---

## 📊 Methodology (Data & Assumptions)

This tool is built upon **LVMH Business Case data** and industry benchmarks to ensure robustness.

### 1. The Formula

We consider the Total Cost of Ownership (Carbon) over the project duration:

### 2. Key Metrics

| Metric | Value | Source |
| --- | --- | --- |
| **Inference (Text)** | 0.31g CO2eq / 100 tokens | Internal LVMH Data |
| **Water Usage** | 12mL / 100 tokens | Internal LVMH Data |
| **Training (Scratch)** | ~19.2 tons CO2eq | Estimated for LLM |
| **Video Gen** | ~15.0g CO2eq / second | Industry Benchmark |

### 3. Scoring Thresholds (Annual)

* 🟢 **GO (Score A/B):** < 10 tons CO2eq
* 🟠 **WARNING (Score C):** < 50 tons CO2eq
* 🔴 **NO-GO (Score D/E):** > 50 tons CO2eq

---

## 📂 Repository Structure

```
LVMH-Green-Score/
├── app.py              # Main application script (Engine & UI)
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation

```

---

## 👥 Team Members

Developed for the **LVMH Alberthon 2025**.

* **Alexis Maeder**
* **Colin Pietri**
* **Cristian Larrain**

---

*Disclaimer: This prototype was developed for educational purposes as part of the Albert School x LVMH Hackathon.*

```

```