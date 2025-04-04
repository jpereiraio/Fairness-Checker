A Python-based microservice for evaluating fairness metrics on datasets using AIF360. The service reads CSV input files from an S3 bucket, compares them against normalized customer data in PostgreSQL, and writes fairness reports back to S3 in JSON format.

---

## 🛠 Features
- Supports fairness evaluation with AIF360 (e.g., Disparate Impact, Mean Difference)
- Reads input files from S3 using `boto3`
- Compares to normalized data stored in PostgreSQL
- Outputs results in JSON format to S3
- Polls S3 every 12 hours
- Fully containerized with Docker
- Deployable on Kubernetes via Helm 3

---

## 🧪 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py
```

Set required environment variables before running:
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASS`
- `S3_BUCKET`, `S3_PREFIX`, `AWS_REGION`, `OUTPUT_PREFIX`
- `CHECK_INTERVAL_SECONDS` (defaults to 43200 = 12 hours)

---

## 🐳 Docker

```bash
# Build the Docker image
docker build -t fairness-checker .

# Run container
docker run --env-file .env fairness-checker
```

---

## ⎈ Deploy with Helm 3

```bash
# Package and install the chart
helm install fairness-checker ./charts/fairness-checker \
  --set image.repository=<your-docker-repo>/fairness-checker \
  --set image.tag=latest \
  --set env.DB_HOST=your-db-host \
  --set env.DB_NAME=your-db-name \
  --set env.DB_USER=your-user \
  --set env.DB_PASS=your-password \
  --set env.S3_BUCKET=your-s3-bucket
```

Or update `values.yaml` with your defaults and run:
```bash
helm install fairness-checker ./charts/fairness-checker
```

---

## 🔐 Environment Variables via Secrets
You can refactor the deployment to use Kubernetes secrets for sensitive variables (e.g., DB_PASS, AWS credentials).

---

## 📂 Directory Structure
```
.
├── Dockerfile
├── main.py
├── fairness_checker/
│   ├── __init__.py
│   ├── config.py
│   ├── storage.py
│   ├── database.py
│   └── analyzer.py
├── requirements.txt
└── charts/
    └── fairness-checker/
```

---

## 📄 License
Apache License
Version 2.0

