# WordToSQL App Using OpenAI's text-davinci-003 LLM

Welcome to the WordToSQL App repository! This application leverages OpenAI's powerful text-davinci-003 language model to convert natural language prompts into SQL statements. With this tool, you can easily translate your verbal instructions or queries into structured SQL commands.

## How It Works

1. **Input Prompt**: Enter a natural language prompt describing the SQL operation you want to perform.

2. **OpenAI's text-davinci-003**: The application utilizes OpenAI's state-of-the-art language model to understand and interpret your input.

3. **SQL Output**: Receive a generated SQL statement as output, reflecting the desired database operation.

## Getting Started

To use the WordToSQL App, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/WordToSQL-App.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to access the WordToSQL App.

## Example Usage

1. Enter a prompt like "Retrieve all employees from the 'employees' table."

2. Receive the generated SQL statement: 
   ```sql
   SELECT * FROM employees;
   ```

## Contributing

We welcome contributions from the community! If you find any issues or have ideas for improvements, please submit a pull request or open an issue.

## Disclaimer

Please note that the WordToSQL App is a demonstration of OpenAI's text-davinci-003 model and may not cover all SQL use cases. Use the generated SQL statements responsibly, and always verify their correctness before executing them on a production database.

Happy querying!
