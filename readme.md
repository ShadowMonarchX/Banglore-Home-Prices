Here is your **completely rewritten `README.md`** for a **Dockerized Bangalore Home Price Prediction** project, suitable for uploading to GitHub:

---

# 🏠 Bangalore Home Price Prediction (Dockerized)

![App UI](BHP_website.PNG)

This project is a full-stack machine learning web application that predicts real estate prices in Bangalore, India. It consists of:

* A **trained ML model** (Linear Regression)
* A **Flask REST API** for inference
* A **frontend UI** built with HTML, CSS, and JavaScript
* Entirely **containerized using Docker** for easy local deployment

---

## 📚 Project Features

This end-to-end data science pipeline covers:

1. ✅ **Data Preprocessing & Cleaning**
2. ✅ **Model Training & Evaluation**
3. ✅ **Flask API to Serve Predictions**
4. ✅ **Frontend UI to Accept User Input**
5. ✅ **Dockerized Setup for Local Deployment**
6. ✅ **Nginx Setup for Production Deployment (Optional)**

---

## 💻 Tech Stack

| Layer         | Technology                       |
| ------------- | -------------------------------- |
| Data Handling | Python, NumPy, Pandas            |
| Visualization | Matplotlib                       |
| Model         | Scikit-learn (Linear Regression) |
| API Server    | Flask                            |
| Frontend      | HTML, CSS, JavaScript, jQuery    |
| Container     | Docker                           |
| Web Server    | Nginx (for production)           |
| IDEs Used     | Jupyter, VS Code, PyCharm        |

---

## 📦 Project Structure

```
bangalore-home-price-prediction/
│
├── client/                 # Frontend code (HTML/CSS/JS)
│   ├── app.html
│   └── app.js
│
├── server/                 # Flask backend
│   ├── server.py
│   ├── util.py
│   └── artifacts/          # Trained model + columns info
│
├── model/                  # Model training files
│   ├── Bangalore_House_Data.ipynb
│   └── train_model.py
│
├── Dockerfile              # Docker setup
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Run Locally with Docker

### 🔧 Prerequisites

* [Docker](https://www.docker.com/products/docker-desktop) installed
* Git installed

### 🛠️ Setup Steps

1. **Clone the Repository**

```bash
git clone https://github.com/<your-username>/bangalore-home-price-prediction.git
cd bangalore-home-price-prediction
```

2. **Build Docker Image**

```bash
docker build -t bhp-app .
```

3. **Run Docker Container**

```bash
docker run -d -p 5000:5000 bhp-app
```

4. **Access the App**

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🌐 (Optional) Production Deployment with Nginx (Linux Server or EC2)

1. **Install Nginx**

```bash
sudo apt update
sudo apt install nginx
```

2. **Create config file**

`/etc/nginx/sites-available/bhp.conf`:

```nginx
server {
    listen 80;
    server_name bhp;

    root /home/ubuntu/bangalore-home-price-prediction/client;
    index app.html;

    location /api/ {
        rewrite ^/api(.*) $1 break;
        proxy_pass http://127.0.0.1:5000;
    }
}
```

3. **Enable the config**

```bash
sudo ln -s /etc/nginx/sites-available/bhp.conf /etc/nginx/sites-enabled/
sudo unlink /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

4. **Start Flask app inside Docker (already running)**

App will be available on the public IP of your EC2 instance or server.

---

## 🧪 Sample Inputs for Testing

* **Total Sqft**: `1000`
* **BHK**: `2`
* **Bathrooms**: `2`
* **Location**: Any from dropdown (e.g., Whitefield)

---

## 📈 Model Training (Optional)

If you want to retrain the model:

```bash
cd model
python3 train_model.py
```

---

## 📬 Contact

Have questions or want to contribute?

* GitHub: [@your-username](https://github.com/your-username)
* Issues: Use GitHub Issues tab to report bugs or request features

---

Let me know if you'd like:

* A GitHub Actions workflow for automatic deployment,
* A `docker-compose.yml` file for separating frontend/backend,
* Or integration with AWS S3, EC2, or GitHub Pages!
