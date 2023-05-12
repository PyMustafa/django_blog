# Blog Project README

This is a Django-based blog project that I created to learn more about web development.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the project using `python manage.py runserver`.

## Running with Docker

To run the project using Docker, follow these steps:
1. Install Docker if you haven't already.
  - [Docker Desktop for Mac and Windows](https://www.docker.com/products/docker-desktop)
  - [Docker Engine for Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Pull the `django-blog` image from Docker Hub by running `docker pull mustafaa828/django-blog`.
3. Run the image using the following command: `docker run -p 8000:8000 django-blog`.
4. Open your web browser and go to `http://localhost:8000` to view the running application.

Note that if you have any environment variables or other configuration that you need to pass to the container, you can use the `-e` and `-v` options to set these values and mount any necessary volumes.



## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch with your changes.
3. Submit a pull request.

Label issues, [Bug Tracker](https://github.com/mustafaa828/django_blog/issues)
## Additional Information

Here are some additional resources that may be useful:

- [Documentation](https://docs.djangoproject.com/)
