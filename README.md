# ⚡ Smart DevOps Dashboard  
📊 **Centralized Monitoring & Automation for DevOps**  

Deployed Live: [👉 Smart DevOps Dashboard](https://smart-devops-dashboard-jwtcse8jyuuihzq7ckhgr9.streamlit.app/)  

Instruction: When you open the app, it will show the Home screen. For the sidebar options, click the left side top arrow >> (⇦) to expand the menu.

## 🌍 Overview  
**Smart DevOps Dashboard** is a hands-on project built to strengthen **deployment, cloud, and automation skills**.  

💡 **AI/ML Relevance:**  
This project helped me gain **practical knowledge of deployment, containers, CI/CD, and monitoring**—key foundations for **deploying and scaling AI/ML models in the future**.  

**Skills gained relevant to AI/ML career:**  
- Hosting interactive applications on **Streamlit Cloud** ☁️  
- Managing **Docker containers** 🐳 → prepares for ML workflows  
- Automating updates with **CI/CD pipelines** 🔄  
- Monitoring system metrics and logs in **real-time dashboards** 📊  
- Understanding **infrastructure and deployment basics** ⚡  

This project shows I have **deployment knowledge**, making me better prepared for **production-ready AI/ML projects in the future**.  

---

## 📂 Key Features & How to Use  

### 1️⃣ Home  
- Shows **live system metrics** (CPU, Memory, Disk)  
- 🔄 Refresh button updates metrics  
- **Alerts:**  
  - CPU > 80% → 🔥 High CPU alert  
  - Memory > 80% → ⚠️ High memory alert  

---

### 2️⃣ Cloud (AWS)  
- Displays **EC2 instances** and **S3 buckets**  
- **Required:** `boto3` library & AWS credentials  

**How to get AWS Keys:**  
1. Login to [AWS Console](https://aws.amazon.com/console/)  
2. Go to **IAM → Users → Security Credentials**  
3. Click **Create Access Key**  
4. Copy **Access Key** & **Secret Key**  

**Inputs in Dashboard:**  
- AWS Access Key  
- AWS Secret Key  
- AWS Region (example: `us-east-1`)  

🧪 **Demo Mode:** Leave empty → shows demo EC2 & S3  

---

### 3️⃣ CI/CD (GitHub Actions)  
- Fetch latest **GitHub Actions workflow runs**  
- **Required:** GitHub token for private repos  

**How to get GitHub Token:**  
1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**  
2. Generate token with **repo** permissions  

**Inputs in Dashboard:**  
- Repository Owner  
- Repository Name  
- GitHub Token (Optional)  

🧪 **Demo Mode:** Empty → shows sample workflow runs  

---

### 4️⃣ Docker  
- Manage & view Docker containers  
- **Required:** Docker installed & running locally  

**Online Demo:** Upload `docker_demo.json` file to simulate containers  

📊 **Outputs:**  
- Container Name  
- Status (running/exited)  
- Image  

---

### 5️⃣ Terraform  
- Shows deployed infrastructure state  
- **Modes:**  
  1. Local → Reads `terraform.tfstate`  
  2. Remote (AWS S3) → Reads from S3  

**How to use AWS S3 remote:**  
1. Create S3 bucket in AWS  
2. Upload `terraform.tfstate`  
3. Generate AWS keys  
4. Provide **Access Key, Secret Key, Region, Bucket Name, Object Key**  

🧪 **Demo Mode:** Empty → shows demo state  

---

### 6️⃣ Logs  
- View recent logs (last 20 lines)  
- Supports Linux & Windows  

**Modes:**  
- Live Mode: Enter log path (e.g., `/var/log/syslog` or `C:\logs\app.log`)  
- Demo Mode: Upload log file to simulate  

⚡ **Highlights:**  
- `ERROR` → 🔴 Red  
- `WARNING` → 🟡 Yellow  
- `INFO` → 🔵 Blue  

---

## 🛠️ Skills Highlight  

- ☁️ **App Deployment:** Hosting on Streamlit Cloud  
- 🔄 **Automation:** CI/CD pipelines  
- 🐳 **Containerization:** Docker basics  
- 📊 **Monitoring & Logging:** CPU, memory, logs  
- ⚡ **Foundation for AI/ML Deployment:** Learned key deployment concepts transferable for **AI/ML projects in the future**  

---

## 🎯 Why It Matters  

Even as a **basic deployment project**, it demonstrates:  
- Practical exposure to deployment and DevOps tools  
- Ability to **work with infrastructure and monitoring**  
- Readiness to **support AI/ML model deployment in the future**  

---

## 📌 Deployment  
[Smart DevOps Dashboard – Streamlit App](https://smart-devops-dashboard-jwtcse8jyuuihzq7ckhgr9.streamlit.app/)  

---
---
## 👨‍💻 Author  
**Rupesh Kumar Shah**  
📧 Email: shahrupesh511@gmail.com  
🌐 GitHub: [iamrupesh1](https://github.com/iamrupesh1)  

---
## ⚡ Run Locally 

1. **Clone the repository:**(Python 3.8+ and docker instal required)
```bash
git clone https://github.com/iamrupesh1/smart-devops-dashboard.git
cd smart-devops-dashboard

## Install dependencies:
pip install streamlit psutil boto3 docker requests

## Run the Streamlit app:
streamlit run app.py

