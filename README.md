![Alt text](./Dashboard_Sample)

FMCG Recommendation System using Apriori Algorithm
This project is a recommendation system for Fast-Moving Consumer Goods (FMCG), built using the Apriori algorithm. It analyzes transaction data to identify frequent item sets and generate recommendations for products that are often purchased together. The system is designed to provide insights for inventory management, cross-selling, and enhancing customer experience.

Features
Frequent Itemset Mining: Identifies frequent product combinations in transaction data.
Association Rules: Generates rules to suggest related items based on historical purchase data.
Support, Confidence, and Lift Metrics: Evaluates the strength of associations to prioritize recommendations.
Scalability: Capable of handling large datasets typical in FMCG environments.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Apriori.git



Run the Apriori Algorithm:

Place your transaction data 
Execute the app script to generate association rules:

View Results: The results, including frequent itemsets and association rules, will be outputted to the console or saved to a results file if configured.

Project Structure
bash
Copy code
Apriori/
├── IPython Notebook/         # EDA                   
├── app.py                    # Main script to run Apriori
├── Apriori.py                # Helper functions for data processing
├── Dashboard_Sample.png      # Picture of dashboard
├── README.md                 # Project documentation
└── requirements.txt          # Python package dependencies
Customization
Adjust Minimum Support and Confidence: In Apriori.py, you can set the minimum support and confidence thresholds to filter results.

Dependencies
Python 3.x
pandas: For data manipulation
Install the dependencies by running:

bash
Copy code
pip install -r requirements.txt
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any new features or bug fixes.

