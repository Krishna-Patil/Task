# Setup Instructions to Run the IMDb Content Upload & Review System
Note: Current Directory should be flask_assignment/

Follow these steps to set up and run the application successfully.

## **1️⃣ Set Up Virtual Environment**
It is recommended to use a virtual environment to manage dependencies.

### **For Ubuntu/Linux & macOS:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### **For Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

## **2️⃣ Install Required Dependencies**
Ensure you have Python installed (preferably Python 3.8+). Then, install dependencies:
```sh
pip install -r requirements.txt
```

## **3️⃣ Install and Start MongoDB**
Ensure MongoDB is installed and running.

### **For Ubuntu/Linux:**
```sh
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

### **For macOS (using Homebrew):**
```sh
brew tap mongodb/brew
brew install mongodb-community@6.0
brew services start mongodb/brew/mongodb-community
```

### **For Windows:**
- Download MongoDB from [here](https://www.mongodb.com/try/download/community)
- Install and start the MongoDB service.

## **4️⃣ Install and Start Redis (Required for Celery)**

### **For Ubuntu/Linux:**
```sh
sudo apt update
sudo apt install -y redis-server
sudo systemctl start redis
sudo systemctl enable redis
```

### **For macOS (using Homebrew):**
```sh
brew install redis
brew services start redis
```

### **For Windows:**
- Download Redis from [here](https://github.com/microsoft/redis/releases)
- Install and start the Redis service.

## **5️⃣ Start the Celery Worker**
In a new terminal window, navigate to the project directory and run:
```sh
celery -A app.celery worker --loglevel=info
```

## **6️⃣ Start the Flask Application**
Run the following command in the project directory:
```sh
python run.py
```

## **7️⃣ Upload a CSV File**
Use an API tool like Postman or `curl` to upload a CSV file.
```sh
curl -X POST -F "file=@movies.csv" http://127.0.0.1:5000/upload
```

## **8️⃣ Fetch Movies with Pagination, Filtering & Sorting**
Use the following API to fetch movies:
```sh
curl "http://127.0.0.1:5000/movies?page=1&per_page=10&sort_by=release_date&order=1"