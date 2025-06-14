# FastAPI Aspire Dashboard

A demo project showcasing how to integrate a **Python FastAPI** application with the **.NET Aspire Dashboard** for observability and local service orchestration.

---

## 🌐 Technologies Used

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [.NET Aspire](https://learn.microsoft.com/en-us/dotnet/aspire/)
- [Aspire Dashboard (Standalone)](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone-for-python)

---

## 🚀 Features

- Seamless integration with Aspire Dashboard
- Service discovery & observability
- Simple FastAPI backend service
- Custom resource naming for dashboard UI

---

## 🧩 Prerequisites

- Python 3.9+
- [Docker](https://www.docker.com/) (for Aspire Dashboard)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/MusaddiqueHussainLabs/fastapi_aspire_dashboard.git
cd fastapi_aspire_dashboard
````

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate    # On Linux/macOS
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Setup Aspire Dashboard (Standalone via Docker)

You can run the Aspire Dashboard using Docker instead of installing it via .NET tools.

### 1. Run Aspire Dashboard container

```bash
docker run --rm -p 18888:18888 mcr.microsoft.com/dotnet/aspire-dashboard
```

> This will start the dashboard at: [http://localhost:18888](http://localhost:18888)

---

## ⚙️ Run FastAPI with Aspire Integration

### 1. Set environment variable to identify your service in Aspire

```bash
# On Linux/macOS
export ASPIRE_RESOURCE_NAME=fastapi_aspire_dashboard

# On Windows (CMD)
set ASPIRE_RESOURCE_NAME=fastapi_aspire_dashboard

# On Windows (PowerShell)
$env:ASPIRE_RESOURCE_NAME="fastapi_aspire_dashboard"
```

### 2. Start the FastAPI app

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🔍 Verify in Aspire Dashboard

Once your app is running and the Aspire Dashboard container is active, open:

📍 [http://localhost:18888](http://localhost:18888)

You should see:

* Your FastAPI service listed as `fastapi_aspire_dashboard`
* Health check status
* Service metadata

---

## 🧼 Cleanup

To stop the dashboard and app:

```bash
# Stop Uvicorn server
CTRL + C

# Stop Docker container
CTRL + C
```

---

## 📎 References

* [.NET Aspire Dashboard (Standalone)](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone?tabs=bash)
* [Aspire with FastAPI (Python)](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone-for-python?tabs=fastapi%2Cwindows)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Uvicorn Docs](https://www.uvicorn.org/)

---

## 📌 License

MIT License - see the [LICENSE](LICENSE) file for details.