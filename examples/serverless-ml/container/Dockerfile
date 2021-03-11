FROM gcr.io/deeplearning-platform-release/tf2-cpu

RUN python3 -m pip install --upgrade --quiet cloudml-hypertune

COPY trainer /trainer

ENTRYPOINT ["python3", "/trainer/model.py"]



