# Start with the Airbyte Python connector base image
FROM airbyte/python-connector-base:1.1.0

# Set the working directory inside the container
WORKDIR /airbyte

# Copy the Python connector code into the container
COPY . .

# Install any additional dependencies your connector requires
# If your connector has a requirements.txt or poetry.lock, you should copy it over and install the dependencies
# Example if you are using requirements.txt:
RUN pip install --no-cache-dir -r requirements.txt

# If using poetry:
RUN pip install poetry
RUN poetry install --no-dev --no-root

# Install the connector itself
RUN pip install .

# Set the command to run the connector
# The entrypoint for Airbyte connectors is usually the main function of the module
ENTRYPOINT ["python", "main.py"]

# Set the default command to run when the container starts
CMD ["discover","--config","source_exnaton_api/secrets/config.json"]
