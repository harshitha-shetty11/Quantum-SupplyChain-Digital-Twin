# 🚛 Quantum Supply Chain Digital Twin – Walmart Sparkathon Submission

> A quantum-enhanced digital twin solution to simulate, visualize, and optimize modern retail supply chains under disruptions.

---

## 📌 Problem Statement

Retail supply chains are prone to unexpected disruptions such as:
- Supplier failures
- Sudden demand surges
- Inventory shortages

These challenges lead to inefficient logistics and delays in last-mile delivery. Traditional simulation tools struggle to handle the complexity of large, dynamic networks.

---

## ✅ Solution Overview

This project introduces a **Digital Twin** of the supply chain that:
- Simulates disruption scenarios
- Visualizes the impact in real-time
- Optimizes routes using **quantum-inspired algorithms**

> 🔍 Built to support rapid decision-making for supply chain resilience and agility.
---

## 🧰 Tech Stack

Frontend:  Streamlit                 For building the interactive dashboard and scenario visualizations

Backend:  FastAPI                    Lightweight and high-performance REST API server

Modeling & Simulation: NetworkX      For graph-based modeling of supply chain networks

Quantum Optimization: AWS Braket     Used for running quantum-inspired optimization tasks (optional)

Deployment: Docker                   For containerizing the application Docker Compose – For orchestrating multi-service deployment locally



## 🧪 How to Run Locally

### 1️⃣ Install Dependencies

pip install -r requirements.txt

### 2️⃣ Start the Backend (FastAPI)
bash
Copy
Edit
uvicorn src.api.main:app --reload

### 3️⃣ Start the Frontend Dashboard (Streamlit)
bash
Copy
Edit
streamlit run src/visualization/dashboard/main_dashboard.py

## 🎥 Demo
📺 Watch my project walkthrough on YouTube:
https://youtube.com/shorts/fICzsxZhaCU?si=WvFtKHTXsOpGwXUq

## 📸 Screenshot
<img width="1908" height="907" alt="image" src="https://github.com/user-attachments/assets/1fcbbf3b-dc8e-4b77-bfaa-b406bcf93a61" />


