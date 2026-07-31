# 🛡️ MetaShield - File Metadata Detector

## 📌 Project Overview

**MetaShield** is a cybersecurity-based file metadata analysis tool developed using Python and Flask. The application extracts hidden metadata from digital files such as images and PDF documents to identify potential privacy risks and information leakage.

Metadata can reveal sensitive information like camera details, location data, author information, and timestamps. MetaShield helps users analyze and understand this hidden information.

---

## 🎯 Objectives

* Detect hidden metadata from digital files.
* Identify possible privacy risks.
* Analyze image EXIF information.
* Extract PDF document properties.
* Improve awareness about information leakage.

---

## ✨ Features

### 🖼️ Image Metadata Detection

MetaShield can extract:

* File Name
* File Size
* Image Format
* Image Width and Height
* Camera Information (EXIF)
* Date Taken (if available)
* GPS Location (if available)
* Other EXIF Metadata

---

### 📄 PDF Metadata Detection

MetaShield extracts:

* File Name
* File Size
* File Type
* Number of Pages
* Author
* Creator
* Producer
* Creation Date
* Modification Date

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Framework

* Flask

### Frontend

* HTML
* CSS

### Libraries

* Flask → Web application framework
* Pillow → Image processing
* ExifRead → EXIF metadata extraction
* PyPDF → PDF metadata extraction

---

## 📂 Project Structure

```
MetaShield/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone <repository-url>
```

### 2. Navigate to Project Folder

```
cd MetaShield
```

### 3. Create Virtual Environment

```
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

### 5. Install Dependencies

```
pip install -r requirements.txt
```

### 6. Run Application

```
python app.py
```

### 7. Open Browser

```
http://127.0.0.1:5000
```

---

## 🔄 Working Flow

```
User Uploads File
        |
        ↓
File Type Detection
        |
        ↓
Metadata Extraction
        |
        ↓
Information Analysis
        |
        ↓
Metadata Report Generation
```

---

## 🔐 Cybersecurity Concepts Used

* Digital Forensics
* Metadata Analysis
* Information Leakage Detection
* Privacy Protection
* Secure File Handling
* File Analysis

---

## 📸 Screenshots

(Add your project screenshots here)

Example:

```
screenshots/
│
├── homepage.png
└── metadata_report.png
```

---

## 🚀 Future Enhancements

* Add DOCX metadata extraction
* Add Video metadata analysis
* Add metadata risk scoring
* Export reports as PDF
* Add metadata removal feature
* Add user authentication

---

## 👨‍💻 Author

**Vishal Tewatia**

B.Tech Computer Science Engineering

Cybersecurity Internship Project

---

## 📜 License

This project is developed for educational and cybersecurity learning purposes.
