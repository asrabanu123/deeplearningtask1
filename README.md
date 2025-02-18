Food Classification Using Deep Learning
Overview
This project is a deep learning-based food classification system that categorizes images into 34 different food classes. The solution involves dataset preprocessing, training three models (Custom CNN, VGG16, and ResNet), model evaluation, and deployment via a Flask web interface.
Features
•	Dataset Handling: Balanced dataset with 200 images per class.
•	Model Training: Custom CNN, VGG16, and ResNet architectures.
•	Evaluation Metrics: Accuracy, Precision, Recall, F1-Score.
•	Deployment: Flask API with an HTML frontend for user-friendly interaction.
•	Nutritional Data: JSON file containing nutritional information for each class.
Technologies Used
•	Python
•	TensorFlow/Keras
•	Flask
•	HTML, CSS, Bootstrap
•	JSON
•	GitHub
Installation Instruction
1.	Install dependencies: 
2.	Run the Flask application: 
3.	python app.py
4.	Access the web interface at http://127.0.0.1:5000
Usage
•	Upload an image of food.
•	Select a model (Custom CNN, VGG16, ResNet).
•	Click "Predict" to get classification results and model evaluation metrics.
File Structure
/food-classification
│── /models                # Trained models (.h5 files)
│── /static                # Static assets (CSS, images)
│── /templates             # HTML templates
│── app.py                 # Flask backend
│── ectraction.py          # Dataset preprocessing
│── nutrition.py               # Model training script
│── nutrition.json    # Nutritional information
│── README.md              # Project documentation
│─       # Required dependencies
Contributors
•	[asrabanu bagvan]
License
This project is licensed under the MIT License. See LICENSE for details.

# deeplearningtask1
