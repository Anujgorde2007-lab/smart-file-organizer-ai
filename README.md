🚀 Smart File Organizer AI

Lightweight Intelligent System for Automated File Management

---

## AI Concept
This project simulates AI-based classification using rule-based logic and keyword detection. It demonstrates how intelligent systems can be built in low-resource environments without heavy models.

---

📌 Overview

Smart File Organizer AI is a lightweight automation system designed to automatically classify and organize files into structured directories.

The project focuses on solving a common real-world problem — manual file management inefficiency — by applying rule-based logic inspired by foundational concepts in artificial intelligence and data classification.

---

❗ Problem Statement

As digital data grows, managing files manually becomes increasingly inefficient.
Students and professionals often struggle with cluttered folders, leading to wasted time and reduced productivity.

This project addresses this issue by introducing an automated, low-resource file organization system that improves efficiency without requiring heavy computational power.

---

✨ Key Features

- 📂 Automatic File Categorization
  Organizes files into folders such as Images, Documents, Code, and Videos

- ⚡ Lightweight & Fast Execution
  Designed to run efficiently on low-resource systems

- 🧠 Rule-Based Intelligent Logic
  Uses file extension mapping to simulate classification behavior

- 🧪 CLI-Based Interaction
  Simple command-line interface for real-time execution

- 🧩 Modular and Extendable Design
  Easy to upgrade with machine learning models in future

---

🤖 How It Works

1. User provides a folder path
2. System scans all files in the directory
3. File extensions are matched to predefined categories
4. Category folders are created automatically (if not existing)
5. Files are moved into their respective folders

---

🔄 Workflow

Input Folder → Scan Files → Classify by Type → Create Folders → Move Files

---

📁 Project Structure

smart-file-organizer-ai/
│── organizer.py     # Core logic for file classification and movement
│── README.md        # Project documentation

---

▶️ How to Run

1. Install Python (if not already installed)
2. Clone or download this repository
3. Open terminal in the project folder
4. Run the following command:

python organizer.py

5. Enter the target folder path when prompted

---

🌍 Why This Project Matters

Efficient file management is essential in modern digital environments.
This project demonstrates how simple, scalable automation systems can significantly improve productivity.

By focusing on lightweight and accessible solutions, this approach is particularly valuable in environments with limited computational resources.

---

🧠 Technical Insight

This system uses rule-based classification by mapping file extensions to predefined categories.
While simple, it reflects the fundamental concept of feature-based classification used in machine learning.

This serves as a foundational step toward implementing more advanced approaches such as:

- Supervised learning models
- Content-based file classification
- Intelligent data organization systems

--- 

👩‍🔧 Machine Learning Integration

This project extends rule-based logic by integrating a Naive Bayes classification model trained on file name data. 

The model predicts file categories based on learned patterns, demonstrating a transition from heuristic-based systems to data-driven approaches. 

This reflects an important step toward building scalable and intelligent file management systems.

---

⚠️ Limitations

- Relies on file extensions rather than content analysis
- Cannot understand file context or semantics
- Limited adaptability without manual rule updates

---

🚀 Future Improvements

- Integrate machine learning models for intelligent classification
- Implement content-based analysis using NLP and computer vision
- Build a graphical user interface (GUI) for ease of use
- Expand support for additional file types
- Optimize performance for large-scale datasets

---

👤 Author

Anuj Gorde
Aspiring AI Engineer | Focused on building efficient and scalable intelligent systems

---

📄 License

This project is open-source and available for learning and educational use.

===

## Example
Input:
- resume.pdf
- invoice.jpg

Output:
- Career/resume.pdf
- Finance/invoice.jpg
