FROM grimoirelab/sortinghat:1.5.0

COPY settings.py /opt/venv/lib/python3.9/site-packages/sortinghat/config/settings_bap.py

RUN . /opt/venv/bin/activate && \
    pip install sortinghat-openinfra
