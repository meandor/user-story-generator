FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY user_story_generator ./user_story_generator
ENV PYTHONPATH=/usr/src/app

RUN useradd -M -s /bin/bash user_story_generator && chown -R user_story_generator:user_story_generator /usr/src/app
USER user_story_generator

CMD [ "python", "user_story_generator/main.py" ]
