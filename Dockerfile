FROM python:3.12-bookworm 

WORKDIR /mgc_test

# Copy your application code into the container
COPY . /mgc_test

 # Create virtual environment
RUN apt update && apt install -y python3-venv
RUN python3 -m venv .venv
RUN . .venv/bin/activate

# Install required packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# # Copy the requirements file and install Python dependencies
# FROM python_base_image
# COPY --from=python_base_image /.venv /.venv
# ENV PATH="/.venv/bin:$PATH"