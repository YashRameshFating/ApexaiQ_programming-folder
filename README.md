# ApexaiQ_programming-folder

# API Research & Implementation Project

## 📌 Overview

This project presents a concise research study on modern API architectures and demonstrates practical API handling using FastAPI. It covers key concepts such as REST, GraphQL, gRPC, authentication methods, rate limiting, versioning, and security practices, along with working API examples.

---

## 🚀 Tech Stack

* Python
* FastAPI
* Uvicorn
* Requests
* JWT (for authentication)

---

## 📖 Research Summary

### 🔹 REST vs GraphQL vs gRPC

* **REST**: Simple, resource-based, uses multiple endpoints
* **GraphQL**: Client decides data structure, single endpoint
* **gRPC**: High-performance, binary communication (Protobuf)

👉 REST is best for general APIs, GraphQL for flexible frontend needs, and gRPC for high-speed microservices.

---

### 🔹 API Authentication Methods

* API Key → Simple but less secure
* Basic Auth → Username & password (Base64)
* JWT (Bearer Token) → Secure and widely used
* OAuth 2.0 → Used for third-party login systems

---

### 🔹 Rate Limiting Algorithms

* Fixed Window
* Sliding Window
* Token Bucket (most practical)
* Leaky Bucket

---

### 🔹 API Versioning

* URI Versioning → `/api/v1/users`
* Header Versioning
* Query Params

---

### 🔹 API Security Best Practices

* Use HTTPS
* Validate inputs
* Implement authentication
* Apply rate limiting
* Log and monitor requests

---

## 🛠️ FastAPI Implementation

### 📂 Project Structure

```
project/
    │── main.py
    │── routes.py
    │── database.py
    │── models.py
    |__ frontend -|
              |- script.js
              |- style.css
              |- index.html
```

---

## 🔑 Authentication Example (JWT)

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "mysecret"

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/secure")
def secure_route(token=Depends(security)):
    return {"message": "Access granted"}
```

---

## 📊 Rate Limiting Example (Simple)

```python
from fastapi import Request, HTTPException
import time

requests_log = {}

def rate_limiter(request: Request):
    ip = request.client.host
    current_time = time.time()

    if ip not in requests_log:
        requests_log[ip] = []

    requests_log[ip] = [t for t in requests_log[ip] if current_time - t < 60]

    if len(requests_log[ip]) >= 5:
        raise HTTPException(status_code=429, detail="Too many requests")

    requests_log[ip].append(current_time)
```

---

## 🔄 Versioning Example

```python
@app.get("/api/v1/users")
def get_users_v1():
    return {"version": "v1", "data": ["user1", "user2"]}

@app.get("/api/v2/users")
def get_users_v2():
    return {"version": "v2", "data": [{"name": "user1"}, {"name": "user2"}]}
```

---

## 🔐 Basic Secure API Example

```python
@app.get("/data")
def get_data():
    return {"status": "secure data"}
```

---

## ▶️ Running the Project

```bash
pip install fastapi uvicorn pyjwt
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Key Learnings

* Different API architectures serve different use cases
* Security and authentication are critical in real-world APIs
* Rate limiting prevents abuse
* Versioning ensures backward compatibility
* FastAPI simplifies API development with high performance

---

## 📎 Conclusion

This project combines theoretical understanding with practical implementation of APIs. It demonstrates how modern backend systems are designed with scalability, security, and performance in mind.

---


