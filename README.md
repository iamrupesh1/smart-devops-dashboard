# ⚡ Smart DevOps Dashboard  
📊 **Centralized Monitoring & Automation for DevOps**  
Deployed Live: [👉 Smart DevOps Dashboard](https://smart-devops-dashboard-jwtcse8jyuuihzq7ckhgr9.streamlit.app/)  

---

## 🌍 Overview  
The **Smart DevOps Dashboard** is an all-in-one platform for monitoring and managing essential **DevOps operations**.  
It integrates **system monitoring, cloud resources, CI/CD pipelines, Docker containers, Terraform states, and log analysis** into a single **Streamlit web app**.  

This project is both a **learning tool** and a **practical solution** for DevOps engineers, students, and IT professionals.  

---

## 📂 Features  

### 1️⃣ Home  
- **Purpose:** Shows **live system metrics** (CPU, Memory, Disk).  
- **Refresh:** Use the 🔄 button to update metrics.  
- **Notes:**  
  - CPU Usage above 80% → 🔥 High CPU Alert  
  - Memory Usage above 80% → ⚠️ High Memory Alert  

---

### 2️⃣ Cloud (AWS)  
- **Purpose:** Display AWS **EC2 instances** and **S3 buckets**.  
- **Requirements:** `boto3` library & AWS credentials.  

🔑 **How to get AWS Keys:**  
1. Login to [AWS Console](https://aws.amazon.com/console/)  
2. Go to **IAM → Users → Security Credentials**  
3. Click **Create Access Key**  
4. Copy **Access Key** & **Secret Key**  

📥 **Inputs in Dashboard:**  
- AWS Access Key  
- AWS Secret Key  
- AWS Region (example: `us-east-1`)  

🧪 **Demo Mode:** Leave empty → shows demo EC2 & S3.  

---

### 3️⃣ CI/CD (GitHub Actions)  
- **Purpose:** Fetch latest **GitHub Actions workflow runs**.  
- **Requirements:** GitHub token for private repos.  

🔑 **How to get GitHub Token:**  
1. Go to **GitHub → Settings → Developer Settings → Personal Access Tokens**  
2. Generate token with **repo** permissions  

📥 **Inputs in Dashboard:**  
- Repository Owner  
- Repository Name  
- GitHub Token (Optional)  

🧪 **Demo Mode:** Empty → shows sample workflow runs.  

---

### 4️⃣ Alerts  
- **Purpose:** Trigger alerts based on system health.  
- **Details:**  
  - CPU > 80% → 🔥 High CPU Usage  
  - Memory > 80% → ⚠️ High Memory Usage  
  - Docker container down → 🚨 Alert  

---

### 5️⃣ Docker  
- **Purpose:** Manage & view Docker containers.  
- **Requirements:** Docker installed & running locally.  

📥 **Online Demo:** Upload `docker_demo.json` file to simulate containers.  

📊 **Outputs:**  
- Container Name  
- Status (running/exited)  
- Image  

---

### 6️⃣ Terraform  
- **Purpose:** Show deployed infrastructure state.  
- **Modes:**  
  1. **Local State** → Reads `terraform.tfstate`  
  2. **Remote State (AWS S3)** → Reads from S3  

🔑 **How to use AWS S3 remote:**  
1. Create S3 bucket in AWS  
2. Upload `terraform.tfstate`  
3. Generate AWS keys  
4. Provide **Access Key, Secret Key, Region, Bucket Name, Object Key**  

🧪 **Demo Mode:** Shows demo state if empty.  

---

### 7️⃣ Logs  
- **Purpose:** View recent logs (last 20 lines).  
- **Supports:** Linux & Windows.  

📥 **Modes:**  
- **Live Mode:** Enter path like `/var/log/syslog` or `C:\logs\app.log`  
- **Demo Mode:** Upload log file to simulate  

⚡ **Highlights:**  
- `ERROR` → 🔴 Red  
- `WARNING` → 🟡 Yellow  
- `INFO` → 🔵 Blue  

---

### 8️⃣ About  
- **Purpose:** Info about project & creator.  
- **Credits:** Created by **Rupesh Kumar Shah** ❤️  

---

## 🌟 Future Improvements  
- 🔄 Real-time Docker & log monitoring on remote servers  
- 🔐 User authentication & credential vault  
- 📧 Email & Slack alerts for system/CI/CD issues  
- 🗺️ AWS EC2 map visualization  
- 📱 Mobile-friendly UI  

---

## 🛠️ Skills Gained  
- ☁️ **Cloud Computing (AWS)** – EC2, S3, IAM keys  
- 🔄 **CI/CD Pipelines** – GitHub Actions monitoring  
- 🐳 **Containerization** – Docker management  
- ⚡ **Infrastructure as Code (IaC)** – Terraform states  
- 📊 **Monitoring & Logging** – CPU, memory, logs  
- 🤖 **Automation** – DevOps tasks in one place  
- 🐧 **Linux SysAdmin** – process & log handling  
- 🚨 **Error Handling & Alerts** – resource health  
- 🎨 **Frontend (Streamlit)** – interactive dashboards  
- 🔗 **APIs & Integration** – AWS boto3, GitHub API, Docker SDK  

---

## ⚙️ Technologies & Tools Used  

### 🔹 Programming & Frameworks  
- Python 🐍  
- Streamlit 🎨  

### 🔹 Cloud & DevOps  
- AWS (EC2, S3, IAM) ☁️  
- Terraform ⚡  
- GitHub Actions 🔄  
- Docker 🐳  

### 🔹 Libraries & APIs  
- psutil (system monitoring)  
- boto3 (AWS SDK)  
- requests (GitHub API)  
- docker-py (Docker SDK)  
- json & logging  

### 🔹 Other Tools  
- Linux (Ubuntu/WSL) 🐧  
- Git & GitHub 🔗  
- VS Code / PyCharm 💻  
- Streamlit Cloud 🌍  

---

## 🎯 Benefits of Smart DevOps Dashboard  
✅ **Centralized DevOps Control** – All monitoring in one place  
✅ **Time-Saving** – No need to switch between AWS/Docker/GitHub  
✅ **Real-Time Monitoring** – CPU, memory, disk stats  
✅ **Error Debugging** – Log upload & analysis  
✅ **Practical Learning** – Combines Cloud, CI/CD, IaC, Containers  
✅ **Easy to Use** – Beginner-friendly UI  
✅ **Scalable** – Can extend with Jenkins, Kubernetes, etc.  
✅ **Portfolio Value** – Strong DevOps + Cloud showcase  

---

## 📌 Deployment  
Check the project online here:  
👉 [Smart DevOps Dashboard – Streamlit App](https://smart-devops-dashboard-jwtcse8jyuuihzq7ckhgr9.streamlit.app/)  

---

## 👨‍💻 Author  
**Rupesh Kumar Shah**  
📧 Email: shahrupesh511@gmail.com  
🌐 GitHub: [iamrupesh1](https://github.com/iamrupesh1)  

---
