# 🏠 Bangalore Home Price Prediction (Dockerized)

![App UI](BHP_website.PNG)

This project is a complete machine learning web application that predicts real estate prices in Bangalore, India. It includes model training, a Flask-based REST API, and a frontend UI – all containerized using Docker.

---

## 📚 Project Overview

This end-to-end Data Science project covers:

1. **Model Building** – Clean and prepare data, train a Linear Regression model.
2. **API Server** – Expose the model using Flask as a REST API.
3. **Frontend** – Use HTML, CSS, and JavaScript to create a responsive UI.
4. **Docker Deployment** – Run the full app in an isolated Docker container.

We apply various data science concepts such as:
- Data cleaning
- Outlier removal
- Feature engineering
- Dimensionality reduction
- Hyperparameter tuning with GridSearchCV
- K-Fold cross-validation

---

## 💻 Technologies Used

- Python
- NumPy & Pandas – Data processing
- Matplotlib – Data visualization
- Scikit-learn – Model building
- Jupyter Notebook – EDA and training
- Flask – API development
- HTML/CSS/JavaScript – Frontend UI
- Docker – Containerization
- Nginx – Reverse proxy (for production)

---

## 🚀 Run Locally with Docker

### 🔁 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- Git

### 📦 Clone the Repository

```bash
git clone https://github.com/<your-username>/bangalore-home-price-prediction.git
cd bangalore-home-price-prediction

docker build -t bhp-app .
docker run -d -p 5000:5000 bhp-app

/etc/nginx/sites-available/bhp.conf
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

sudo ln -s /etc/nginx/sites-available/bhp.conf /etc/nginx/sites-enabled/
sudo unlink /etc/nginx/sites-enabled/default
sudo systemctl restart nginx


bangalore-home-price-prediction/
│
├── client/                 # Frontend (HTML, JS, CSS)
│   ├── app.html
│   └── app.js
│
├── server/                 # Flask backend
│   ├── server.py
│   ├── util.py
│   └── artifacts/          # Trained model + columns
│
├── model/                  # Jupyter notebook and training script
│   ├── Bangalore_House_Data.ipynb
│   └── train_model.py
│
├── Dockerfile
├── requirements.txt
└── README.md
