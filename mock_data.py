"""
mock_data.py
------------
Data simulasi yang merepresentasikan hasil scraping Wikipedia.
Digunakan untuk testing & demo tanpa koneksi internet.
Di komputer lokal, ganti dengan run_scraper() yang asli.
"""

Mock_articles = [
    {
        "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "title": "Python (programming language)",
        "summary": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected.",
        "categories": ["Programming languages", "High-level programming languages", "Object-oriented programming languages"],
        "links": [
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Guido_van_Rossum",
            "https://en.wikipedia.org/wiki/Java_(programming_language)",
            "https://en.wikipedia.org/wiki/Data_science",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
        ],
        "_link_titles": ["Machine learning", "Guido van Rossum", "Java (programming language)", "Data science", "Artificial intelligence"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Machine_learning",
        "title": "Machine learning",
        "summary": "Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data. Machine learning approaches have been applied to many fields including natural language processing, computer vision, and robotics.",
        "categories": ["Machine learning", "Artificial intelligence", "Computer science"],
        "links": [
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Neural_network_(machine_learning)",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Data_science",
            "https://en.wikipedia.org/wiki/Statistics",
        ],
        "_link_titles": ["Artificial intelligence", "Deep learning", "Neural network (machine learning)", "Python (programming language)", "Data science", "Statistics"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Guido_van_Rossum",
        "title": "Guido van Rossum",
        "summary": "Guido van Rossum is a Dutch programmer who created the Python programming language. He was Python's Benevolent Dictator for Life (BDFL) until stepping down in 2018.",
        "categories": ["Dutch programmers", "Python (programming language)", "Computer scientists"],
        "links": [
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Netherlands",
            "https://en.wikipedia.org/wiki/Dropbox_(service)",
            "https://en.wikipedia.org/wiki/Google",
        ],
        "_link_titles": ["Python (programming language)", "Netherlands", "Dropbox (service)", "Google"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "title": "Artificial intelligence",
        "summary": "Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of research in computer science that develops and studies methods and software which enable machines to perceive their environment.",
        "categories": ["Artificial intelligence", "Computer science", "Emerging technologies"],
        "links": [
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Natural_language_processing",
            "https://en.wikipedia.org/wiki/Computer_vision",
            "https://en.wikipedia.org/wiki/Robotics",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
        ],
        "_link_titles": ["Machine learning", "Deep learning", "Natural language processing", "Computer vision", "Robotics", "Python (programming language)"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Deep_learning",
        "title": "Deep learning",
        "summary": "Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning. Learning can be supervised, semi-supervised or unsupervised.",
        "categories": ["Deep learning", "Machine learning", "Artificial neural networks"],
        "links": [
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Neural_network_(machine_learning)",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/TensorFlow",
            "https://en.wikipedia.org/wiki/PyTorch",
        ],
        "_link_titles": ["Machine learning", "Artificial intelligence", "Neural network (machine learning)", "Python (programming language)", "TensorFlow", "PyTorch"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Data_science",
        "title": "Data science",
        "summary": "Data science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processing, scientific visualization, algorithms and systems to extract or extrapolate knowledge and insights from noisy, structured, or unstructured data.",
        "categories": ["Data science", "Statistics", "Computer science"],
        "links": [
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Statistics",
            "https://en.wikipedia.org/wiki/Big_data",
            "https://en.wikipedia.org/wiki/Data_mining",
        ],
        "_link_titles": ["Python (programming language)", "Machine learning", "Statistics", "Big data", "Data mining"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Natural_language_processing",
        "title": "Natural language processing",
        "summary": "Natural language processing (NLP) is an interdisciplinary subfield of computer science and artificial intelligence. It is primarily concerned with providing computers with the ability to process data encoded in natural language.",
        "categories": ["Natural language processing", "Artificial intelligence", "Computational linguistics"],
        "links": [
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Linguistics",
        ],
        "_link_titles": ["Artificial intelligence", "Machine learning", "Deep learning", "Python (programming language)", "Linguistics"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Neural_network_(machine_learning)",
        "title": "Neural network (machine learning)",
        "summary": "In machine learning, a neural network (also artificial neural network or neural net, abbreviated ANN or NN) is a model inspired by the structure and function of biological neural networks in animal brains.",
        "categories": ["Artificial neural networks", "Machine learning", "Deep learning"],
        "links": [
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Backpropagation",
        ],
        "_link_titles": ["Machine learning", "Deep learning", "Artificial intelligence", "Backpropagation"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Statistics",
        "title": "Statistics",
        "summary": "Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. In applying statistics to a scientific, industrial, or social problem, it is conventional to begin with a statistical population or a statistical model to be studied.",
        "categories": ["Statistics", "Mathematics", "Data analysis"],
        "links": [
            "https://en.wikipedia.org/wiki/Data_science",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Mathematics",
            "https://en.wikipedia.org/wiki/Probability",
        ],
        "_link_titles": ["Data science", "Machine learning", "Mathematics", "Probability"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/TensorFlow",
        "title": "TensorFlow",
        "summary": "TensorFlow is a free and open-source software library for machine learning and artificial intelligence. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks.",
        "categories": ["Machine learning software", "Google software", "Python (programming language)"],
        "links": [
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Google",
            "https://en.wikipedia.org/wiki/PyTorch",
            "https://en.wikipedia.org/wiki/Keras",
        ],
        "_link_titles": ["Deep learning", "Python (programming language)", "Google", "PyTorch", "Keras"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/PyTorch",
        "title": "PyTorch",
        "summary": "PyTorch is a machine learning library based on the Torch library, used for applications such as computer vision and natural language processing. It was originally developed by Meta AI.",
        "categories": ["Machine learning software", "Meta Platforms", "Python libraries"],
        "links": [
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/TensorFlow",
            "https://en.wikipedia.org/wiki/Computer_vision",
            "https://en.wikipedia.org/wiki/Natural_language_processing",
        ],
        "_link_titles": ["Deep learning", "Python (programming language)", "TensorFlow", "Computer vision", "Natural language processing"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Computer_vision",
        "title": "Computer vision",
        "summary": "Computer vision is an interdisciplinary field that deals with how computers can gain high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that the human visual system can do.",
        "categories": ["Computer vision", "Artificial intelligence", "Image processing"],
        "links": [
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Deep_learning",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/PyTorch",
        ],
        "_link_titles": ["Artificial intelligence", "Deep learning", "Machine learning", "PyTorch"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Java_(programming_language)",
        "title": "Java (programming language)",
        "summary": "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let programmers write once, run anywhere.",
        "categories": ["Programming languages", "Object-oriented programming languages", "Class-based programming languages"],
        "links": [
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Object-oriented_programming",
            "https://en.wikipedia.org/wiki/C_(programming_language)",
            "https://en.wikipedia.org/wiki/JavaScript",
        ],
        "_link_titles": ["Python (programming language)", "Object-oriented programming", "C (programming language)", "JavaScript"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Robotics",
        "title": "Robotics",
        "summary": "Robotics is an interdisciplinary branch of computer science and engineering. Robotics involves the design, construction, operation, and use of robots.",
        "categories": ["Robotics", "Artificial intelligence", "Engineering"],
        "links": [
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Computer_vision",
        ],
        "_link_titles": ["Artificial intelligence", "Machine learning", "Computer vision"]
    },
    {
        "url": "https://en.wikipedia.org/wiki/Big_data",
        "title": "Big data",
        "summary": "Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software. Data with many entries (rows) offer greater statistical power.",
        "categories": ["Big data", "Data management", "Information technology"],
        "links": [
            "https://en.wikipedia.org/wiki/Data_science",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Statistics",
            "https://en.wikipedia.org/wiki/Data_mining",
        ],
        "_link_titles": ["Data science", "Machine learning", "Statistics", "Data mining"]
    },
]