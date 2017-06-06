FROM python:3
COPY src/checkout.py /
CMD ["python3", "checkout.py"]