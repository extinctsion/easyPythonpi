<!-- Replace this with your own banner image or animation -->

# easyPythonpi
<br>

<u>
    <h1>Introduction </h1>
</u>

**easyPythonpi** is a beginner-friendly Python library that focuses on simple calculations. It's designed to encourage open-source contributions, making it an ideal project for newcomers to programming and open source.
<br>

<u>
    <h3>Getting Started</h3>
</u>

<br>
<details>
<summary>🔍 Fork the Repository</summary>
<br>

1. Fork this repository by clicking the "Fork" button in the top-right corner of this page. Alternatively, you can fork it directly from [here](https://github.com/extinctsion/easyPy/fork).
</details>

<details>
<summary>📥 Clone the Repository</summary>
<br>

2. Clone your forked repository to your local computer using the following command. Replace `url_you_just_copied` with the URL of your forked repository.

    ```sh
    git clone url_you_just_copied
    ```
</details>

<details>
<summary>📂 Open the Repository</summary>
<br>

3. Open the cloned repository in your preferred code editor. Additionally, open a terminal within the repository directory.

    ```sh
    cd easyPythonpi
    ```
</details>

<details>
<summary>🌿 Create a New Branch</summary>
<br>

4. Create a new branch for your changes. Replace `username` with your GitHub username in the following command:

    ```sh
    git checkout -b username
    ```
</details>

<details>
<summary>🚀 Contribute Code</summary>
<br>

5. Add your new methods or functions to the `easyPythonpi.py` file within the codebase. Ensure that your code adheres to the coding style and conventions used in the existing code for consistency. For example:

    ```python
    def calculate_average(numbers):
        """Calculate the average of a list of numbers."""
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)
    ```
</details>

<details>
<summary>📝 Commit Your Changes</summary>
<br>

6. Once you've added your code, commit your changes to GitHub using the following commands. Make sure you execute them in the precise order, one after another, in your terminal.

    ```sh
    # Stage your changes
    git add .

    # Commit your changes with a descriptive message
    git commit -m "Hacktoberfest contribution"

    # Push your changes to your GitHub repository
    git push -u origin your_github_username
    ```
</details>

<details>
<summary>📢 Open a Pull Request</summary>
<br>

7. Navigate to your forked repository on GitHub. You'll see a yellow box at the top indicating that some changes have been pushed. Click the "Compare & pull request" button.

8. Submit your pull request by adding a title and description. Congratulations, you have successfully opened a pull request in this repository.

   *Note: To complete the Hacktoberfest challenge, you need to open four valid pull requests. If you've followed the above steps, you've already opened one pull request, and you need three more.*
</details>
<br>

![Library File Structure](https://github.com/extinctsion/easyPythonpi/assets/67048929/f772ba66-e2eb-4e42-b1b7-104facf6eda4)

<br>
<u>
    <h2>Running Test Cases</h2>
</u>
<br>

To ensure the reliability of your contributions and modifications, it's important to run test cases for the **easyPythonpi** library.

### Prerequisites

Before running the test cases, ensure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/): The Python programming language.

<details>
<summary>🧪 Run Test Cases</summary>
<br>

1. Install the required dependencies using pip:

    ```sh
    pip install -r requirements.txt
    ```
2. Navigate to the project directory in your terminal.
3. Run the test suite:

    ```sh
    python tests.py
    ```

   The test suite will execute, and you'll see the test results in your terminal. Ensure that all tests pass before making any contributions or modifications.
</details>
<br>

<u>
    <h2>Setting Up a Virtual Environment (Optional)</h2>
</u>
<br>

Working in a virtual environment is a good practice as it isolates project dependencies from your global Python environment.

<details>
<summary>🔮 Prerequisites</summary>
<br>

Before setting up a virtual environment, ensure you have Python installed on your system.
</details>

<details>
<summary>📦 Install and Activate a Virtual Environment</summary>
<br>

4. Create a virtual environment (you can replace `venv` with your preferred environment name):

    ```sh
    python -m venv venv
    ```

5. Activate the virtual environment:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

6. Install `unittest` (if not already installed):

    ```sh
    pip install unittest
    ```
</details>

<details>
<summary>🔬 Run the Test Cases within the Virtual Environment</summary>
<br>

7. Run the test cases as mentioned above.
</details>

<details>
<summary>🔓 Deactivate the Virtual Environment (when done)</summary>
<br>

8. When you're finished working on the project, deactivate the virtual environment:

    ```sh
    deactivate
    ```
</details>
<br>

# Hacktoberfest

Repositories with the `hacktoberfest` label are considered for the Hacktoberfest challenge. Your contributions to this project can help you achieve your Hacktoberfest goals.

Thank you for contributing to the open-source community!

</div>
