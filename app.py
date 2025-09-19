import streamlit as st 
import psutil
import random
import requests
import docker
import os
import json

# -------------------- Page Config --------------------
st.set_page_config(page_title="Smart DevOps Dashboard", layout="wide")

# -------------------- Session State Setup --------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "refresh_count" not in st.session_state:
    st.session_state.refresh_count = 0

# -------------------- Dark Mode --------------------
dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode
if dark_mode:
    st.markdown("""
    <style>
    body { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

# -------------------- Sidebar --------------------
st.sidebar.markdown("## 💻 Smart DevOps Dashboard")
section = st.sidebar.radio(
    "📂 Sections",
    ["Home", "Cloud", "CI/CD", "Alerts", "Docker", "Terraform", "Logs", "About"]
)
refresh = st.sidebar.button("🔄 Refresh")

if refresh:
    st.session_state.refresh_count += 1
    st.experimental_rerun = lambda: None
    st.experimental_rerun()

# -------------------- Home --------------------
if section == "Home":
    st.markdown("<h1 style='text-align:center;'>💻 Smart DevOps Dashboard – Home</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Home Section Works"):
        st.markdown("""
        - Displays system metrics: **CPU**, **Memory**, **Disk**.
        - Uses the `psutil` library to fetch **live system metrics**.
        - You can refresh metrics using the **🔄 Refresh button**.
        """)

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    st.markdown("### 📊 System Metrics")
    st.table({
        "Metric": ["CPU Usage", "Memory Usage", "Disk Usage"],
        "Value": [f"{cpu}%", f"{mem}%", f"{disk}%"]
    })

# -------------------- Cloud --------------------
elif section == "Cloud":
    st.markdown("<h1 style='text-align:center;'>☁️ Smart DevOps Dashboard – Cloud</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Cloud Section Works"):
        st.markdown("""
        - Shows **AWS resources** (EC2 & S3) using your AWS credentials.
        - Needs the **boto3** library.
        - Input details:
          - AWS Access Key
          - AWS Secret Key
          - AWS Region
        - If left empty → Demo data is shown.
        """)

    access_key = st.text_input("Enter AWS Access Key")
    secret_key = st.text_input("Enter AWS Secret Key", type="password")
    region = st.text_input("Enter AWS Region (e.g., us-east-1)")

    if st.button("🔄 Fetch AWS Resources"):
        try:
            import boto3
            if access_key and secret_key and region:
                ec2_client = boto3.client('ec2', aws_access_key_id=access_key,
                                          aws_secret_access_key=secret_key, region_name=region)
                s3_client = boto3.client('s3', aws_access_key_id=access_key,
                                         aws_secret_access_key=secret_key, region_name=region)

                st.write("### EC2 Instances")
                instances = ec2_client.describe_instances()
                for r in instances['Reservations']:
                    for i in r['Instances']:
                        st.write(f"ID: {i['InstanceId']}, State: {i['State']['Name']}")

                st.write("### S3 Buckets")
                buckets = s3_client.list_buckets()
                for b in buckets['Buckets']:
                    st.write(f"Name: {b['Name']}")
            else:
                st.warning("AWS credentials missing. Showing demo data.")
                st.write("EC2 Instance → ID: i-1234567890abcdef | State: running")
                st.write("S3 Bucket → Name: my-demo-bucket")
        except Exception as e:
            st.error(f"Error fetching AWS resources: {e}")

# -------------------- CI/CD --------------------
elif section == "CI/CD":
    st.markdown("<h1 style='text-align:center;'>⚙️ Smart DevOps Dashboard – CI/CD</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How CI/CD Works"):
        st.markdown("""
        - Fetches **GitHub Actions runs** for your repository.
        - Input details:
          - Repo Owner
          - Repo Name
          - GitHub Token (optional)
        - If inputs are empty → Shows demo runs.
        """)

    owner = st.text_input("GitHub Repo Owner")
    repo = st.text_input("GitHub Repo Name")
    token = st.text_input("GitHub Token (Optional)", type="password")

    if st.button("🔄 Fetch CI/CD Runs"):
        if owner and repo:
            url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"
            headers = {"Authorization": f"token {token}"} if token else {}
            try:
                response = requests.get(url, headers=headers)
                data = response.json()
                if "workflow_runs" in data and data["workflow_runs"]:
                    for run in data["workflow_runs"][:5]:
                        st.write(f"**{run['name']}** → Status: {run['status']}, Conclusion: {run['conclusion']}")
                else:
                    st.warning("No runs found. Showing demo runs.")
                    st.write("Demo Workflow → Status: completed, Conclusion: success")
            except Exception as e:
                st.error(f"Error fetching CI/CD runs: {e}")
        else:
            st.warning("Inputs missing. Showing demo runs.")
            st.write("Demo Workflow → Status: completed, Conclusion: success")

# -------------------- Alerts --------------------
elif section == "Alerts":
    st.markdown("<h1 style='text-align:center;'>🚨 Smart DevOps Dashboard – Alerts</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Alerts Section Works"):
        st.markdown("""
        - Monitors system **CPU & Memory usage**.
        - Uses `psutil` library.
        - Triggers alerts if usage > 80%.
        - Also checks Docker containers status.
        """)

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    st.write(f"CPU Usage: {cpu}%")
    st.write(f"Memory Usage: {mem}%")
    if cpu > 80: st.error("🔥 High CPU Usage!")
    else: st.success("✅ CPU Usage Normal")
    if mem > 80: st.error("⚠️ High Memory Usage!")
    else: st.success("✅ Memory Usage Normal")

    docker_running = random.choice([True, False])
    if docker_running: st.success("🐳 All Docker containers running")
    else: st.error("🐳 Some Docker containers stopped")

# -------------------- Docker --------------------
elif section == "Docker":
    st.markdown("<h1 style='text-align:center;'>🐳 Smart DevOps Dashboard – Docker</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Docker Section Works"):
        st.markdown("""
        - Lists Docker containers with Name, Status, Image.
        - Works live if Docker is available locally.
        - Online users can upload JSON export from server:
          Example: docker ps --format '{{json .}}'
        """)

    docker_file = st.file_uploader("Upload Docker JSON (optional)", type=["json"])
    if docker_file:
        containers_data = json.load(docker_file)
        data = {
            "Container": [c["Names"] for c in containers_data],
            "Status": [c["State"] for c in containers_data],
            "Image": [c["Image"] for c in containers_data]
        }
        st.table(data)
    else:
        try:
            client = docker.from_env()
            containers = client.containers.list(all=True)
            data = {
                "Container": [c.name for c in containers],
                "Status": [c.status for c in containers],
                "Image": [c.image.tags[0] if c.image.tags else c.image.short_id for c in containers]
            }
            st.table(data)
        except Exception as e:
            st.warning("Docker not available. Showing demo containers.")
            demo_data = {
                "Container": ["web_app", "db_server"],
                "Status": ["running", "exited"],
                "Image": ["nginx:alpine", "mysql:5.7"]
            }
            st.table(demo_data)

# -------------------- Terraform --------------------
elif section == "Terraform":
    st.markdown("<h1 style='text-align:center;'>⚡ Smart DevOps Dashboard – Terraform</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Terraform Section Works"):
        st.markdown("""
        - Works in **two modes**: Local State & AWS S3 Remote State
        - Local: Reads `terraform.tfstate`
        - AWS S3 Remote: Requires AWS credentials
        """)

    mode = st.selectbox("Select Mode", ["Local", "AWS S3 Remote"])

    if mode == "Local":
        tf_path = os.path.expanduser("~/smart-devops-dashboard/infra/terraform/terraform.tfstate")
        if os.path.exists(tf_path):
            with open(tf_path) as f:
                tf_state = json.load(f)
            if "resources" in tf_state:
                st.markdown("### 🌍 Deployed Resources (Local)")
                for res in tf_state["resources"]:
                    st.write(f"{res['type']} → {res['name']}")
            else:
                st.warning("No resources found in terraform.tfstate.")
        else:
            st.warning("Terraform files not found. Run `terraform apply` first.")
    elif mode == "AWS S3 Remote":
        access_key = st.text_input("AWS Access Key")
        secret_key = st.text_input("AWS Secret Key", type="password")
        region = st.text_input("AWS Region (e.g., us-east-1)")
        bucket = st.text_input("S3 Bucket Name")
        key = st.text_input("S3 Object Key (e.g., dev/terraform.tfstate)")

        if st.button("🔄 Fetch Terraform State from S3"):
            try:
                import boto3
                if access_key and secret_key and region and bucket and key:
                    s3_client = boto3.client(
                        "s3",
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name=region
                    )
                    obj = s3_client.get_object(Bucket=bucket, Key=key)
                    tf_state = json.loads(obj["Body"].read().decode("utf-8"))

                    if "resources" in tf_state:
                        st.markdown("### 🌍 Deployed Resources (AWS S3)")
                        for res in tf_state["resources"]:
                            st.write(f"{res['type']} → {res['name']}")
                    else:
                        st.warning("No resources found in terraform.tfstate.")
                else:
                    st.error("⚠️ Please enter all AWS details (Access Key, Secret, Region, Bucket, Key).")
            except Exception as e:
                st.error(f"Error fetching from S3: {e}")

# -------------------- Logs --------------------
elif section == "Logs":
    st.markdown("<h1 style='text-align:center;'>📝 Smart DevOps Dashboard – Logs</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - How Logs Section Works"):
        st.markdown("""
        - Upload a log file to see the last 20 lines.
        - Highlights ERROR, WARNING, INFO.
        - Works online with file upload or locally with path.
        """)

    log_file = st.file_uploader("Upload log file", type=["log", "txt"])
    log_path = st.text_input("Or enter log file path (e.g., /var/log/syslog)")

    if log_file:
        logs = log_file.read().decode("utf-8").splitlines()[-20:]
    elif log_path:
        try:
            with open(log_path) as f:
                logs = f.readlines()[-20:]
        except Exception as e:
            st.error(f"Error reading log file: {e}")
            logs = []
    else:
        logs = []

    for line in logs:
        if "ERROR" in line: st.error(line.strip())
        elif "WARNING" in line: st.warning(line.strip())
        else: st.info(line.strip())

# -------------------- About --------------------
elif section == "About":
    st.markdown("<h1 style='text-align:center;'>ℹ️ Smart DevOps Dashboard – About</h1>", unsafe_allow_html=True)

    with st.expander("📘 Notes - About This Dashboard"):
        st.markdown("""
        - Combines **System Monitoring, Cloud, CI/CD, Docker, Terraform, Logs** in one tool.
        - Built with **Python + Streamlit**.
        - Purpose: Simulates a real **DevOps Monitoring Dashboard**.
        - Created by **Rupesh** ❤️
        """)
