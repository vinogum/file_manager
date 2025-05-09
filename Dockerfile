# Step 1: Start with a Python base image
FROM python

# Step 2: Set the working directory in the container
WORKDIR /filemanager

# Step 3: Copy the requirements file into the container
COPY requirements.txt /filemanager/

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the Django project files into the container
COPY . /filemanager/

# Step 6: Expose the port Django will run on
EXPOSE 8000

# Step 7: Run migrations
RUN python manage.py migrate

# Step 8: Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
