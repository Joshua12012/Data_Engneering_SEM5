# Data Engineering Portfolio

This repository demonstrates practical implementations of data engineering concepts through multiple experiments and projects.

## Core Components

### 1. Data Cleaning and Preprocessing
- Email validation and standardization
- Handling missing values and duplicates
- Data type validation and conversion
- Statistical analysis and imputation

### 2. Database Operations
- SQLite and PostgreSQL implementations
- Schema design and table relationships
- CRUD operations
- Transaction management
- Foreign key constraints

### 3. Weather Data Pipeline
**Implementation 1 (exp4):**
- JSON data handling
- Configuration management
- Basic ETL pipeline
- File-based data storage

**Implementation 2 (exp5):**
- Improved modular architecture
- Enhanced error handling
- Structured logging
- Database persistence

### 4. API Integration
- REST API consumption
- Environment variable management
- Data transformation
- Database integration

### 5. Web Application Development
**Streamlit Applications (exp6, exp7):**
- Database models
- API endpoints
- Connection pooling
- ORM implementation

### 6. Data Analysis
- PostgreSQL integration
- DataFrame operations
- Statistical analysis
- Data visualization
- Sample data generation

## Technical Requirements

### Dependencies
```
pandas
numpy
requests
python-dotenv
flask
sqlalchemy
psycopg2-binary
matplotlib
seaborn
faker
```

### Environment Setup
1. Create `.env` file:
```ini
WEATHER_API_KEY=your_key
DB_HOST=localhost
DB_USER=postgres
DB_PASS=your_password
DB_NAME=your_database
```

2. Install requirements:
```bash
pip install -r requirements.txt
```
