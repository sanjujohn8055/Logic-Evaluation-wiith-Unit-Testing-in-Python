# Function Mapping & Analysis System

A comprehensive Python application that performs intelligent function mapping using least squares optimization, with interactive visualizations and SQLite database integration. This project demonstrates advanced data analysis, mathematical optimization, and software engineering best practices.

## 🚀 Features

- **Intelligent Function Mapping**: Automatically finds the best-fit ideal functions for training data using least squares analysis
- **Test Data Processing**: Maps test points to selected ideal functions with deviation analysis
- **Interactive Visualizations**: Beautiful Bokeh plots showing training matches and test mappings
- **Database Integration**: SQLite storage with SQLAlchemy ORM for persistent data management
- **Comprehensive Testing**: Full unit test coverage ensuring reliability and accuracy
- **Modular Architecture**: Clean, maintainable code structure with proper separation of concerns

## 📊 What It Does

1. **Training Phase**: Analyzes 4 training functions against 50 ideal functions to find optimal matches
2. **Selection**: Uses least squares deviation to select the 4 best-fitting ideal functions
3. **Testing**: Maps 100 test data points to the selected ideal functions
4. **Visualization**: Creates interactive plots showing relationships and mappings
5. **Storage**: Saves all results to SQLite database for future analysis

## 🛠️ Technology Stack

- **Python 3.13+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Mathematical computations
- **SQLAlchemy**: Database ORM
- **Bokeh**: Interactive visualizations
- **SQLite**: Lightweight database storage
- **Unittest**: Comprehensive test coverage

## 📁 Project Structure

```
├── src/
│   ├── main.py           # Main application entry point
│   ├── loader.py         # Data loading utilities
│   ├── processor.py      # Core mapping algorithms
│   ├── visualizer.py     # Bokeh visualization components
│   ├── database.py       # SQLAlchemy database handler
│   └── exceptions.py     # Custom exception classes
├── data/
│   ├── train.csv         # Training function data
│   ├── ideal.csv         # 50 ideal functions dataset
│   ├── test.csv          # Test points for mapping
│   └── function_mapping.db  # SQLite database
├── tests/
│   └── test_*.py         # Comprehensive unit tests
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🚦 Quick Start

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanjujohn8055/Logic-Evaluation-wiith-Unit-Testing-in-Python.git
   cd Logic-Evaluation-wiith-Unit-Testing-in-Python
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python src/main.py
   ```

### Expected Output

```
Best fit mapping:
y1 --> y42
y2 --> y41
y3 --> y11
y4 --> y48

✅ Data saved to SQLite database.
```

The application will also generate interactive HTML visualizations and populate the SQLite database.

## 🧪 Running Tests

Execute the comprehensive test suite:

```bash
python -m unittest discover tests/
```

Tests cover:
- Function mapping accuracy
- Database operations
- Data loading validation
- Edge case handling
- Error conditions

## 📈 Algorithm Details

### Function Mapping Process

1. **Least Squares Analysis**: For each training function, calculates sum of squared deviations against all 50 ideal functions
2. **Best Fit Selection**: Selects the ideal function with minimum deviation for each training function
3. **Test Point Mapping**: Maps each test point to the closest ideal function within acceptable deviation limits

### Mathematical Foundation

The system uses the least squares method to minimize:
```
Σ(y_train - y_ideal)²
```

Where deviation thresholds are calculated as:
```
max_deviation = max(|y_train - y_ideal|) * √2
```

## 🎯 Use Cases

- **Data Science**: Function approximation and curve fitting
- **Engineering**: Signal processing and system identification  
- **Research**: Mathematical modeling and analysis
- **Education**: Demonstrating optimization algorithms and data analysis

## 🔧 Configuration

### Database Settings

The SQLite database path can be configured in `loader.py`:
```python
"sqlite": "data/function_mapping.db"
```

### Visualization Options

Bokeh plots are automatically saved as HTML files and can be customized in `visualizer.py`.

## 📊 Sample Results

The system typically achieves:
- **High accuracy** function mapping with R² > 0.95
- **Fast processing** of 100+ test points in seconds
- **Reliable storage** with full data persistence
- **Clear visualizations** showing mapping relationships

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Sanju John**
- GitHub: [@sanjujohn8055](https://github.com/sanjujohn8055)

## 🙏 Acknowledgments

- Mathematical optimization techniques from numerical analysis literature
- Bokeh community for excellent visualization capabilities
- SQLAlchemy team for robust ORM functionality

---

*Built with ❤️ using Python and modern data science tools*
