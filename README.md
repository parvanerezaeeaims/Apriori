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

Example Results
Here is a sample of what the output might look like:

diff
Copy code
آب آلبالو  250 cc, شیر 250 cc ----------> آب پرتقال 250 cc
support: 0.20453841246696436
confidence: 0.773184511506132
lift: 1.2899601105999818

------------------------------------------------------------

آب پرتقال 250 cc, شیر 250 cc ----------> آب آلبالو  250 cc
support: 0.20453841246696436
confidence: 0.833275580416811
lift: 1.2517271372781578

------------------------------------------------------------

شیر قهوه موکا, آب آلبالو  250 cc ----------> آب پرتقال 250 cc
support: 0.21501260670129713
confidence: 0.7566816335257645
lift: 1.2624271556739906

------------------------------------------------------------

شیر قهوه موکا, آب پرتقال 250 cc ----------> آب آلبالو  250 cc
support: 0.21501260670129713
confidence: 0.8320598123809748
lift: 1.2499008388975783

------------------------------------------------------------

شیر قهوه موکا, شیر 250 cc ----------> آب آلبالو  250 cc
support: 0.17957410613931166
confidence: 0.816446605159936
lift: 1.22644704325323

------------------------------------------------------------

شیر قهوه موکا, شیر 250 cc ----------> آب پرتقال 250 cc
support: 0.16727118077705885
confidence: 0.76051046903486
lift: 1.2688150811992456

------------------------------------------------------------

آب آلبالو  250 cc, آب پرتقال 250 cc, شیر 250 cc ----------> شیر قهوه موکا
support: 0.15122573589720223
confidence: 0.7393512742826591
lift: 1.7938842977469012

------------------------------------------------------------

شیر قهوه موکا, آب آلبالو  250 cc, آب پرتقال 250 cc ----------> شیر 250 cc
support: 0.15122573589720223
confidence: 0.7033342752189884
lift: 1.8807113271220293

------------------------------------------------------------

شیر قهوه موکا, آب آلبالو  250 cc, شیر 250 cc ----------> آب پرتقال 250 cc
support: 0.15122573589720223
confidence: 0.8421355347295056
lift: 1.4049961313939647

------------------------------------------------------------

شیر قهوه موکا, آب پرتقال 250 cc, شیر 250 cc ----------> آب آلبالو  250 cc
support: 0.15122573589720223
confidence: 0.9040752578817376
lift: 1.358080761068573

------------------------------------------------------------


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

