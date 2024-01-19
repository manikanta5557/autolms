FROM cypress/browsers:latest
RUN apt-get install -y chromium-browser
ENV PATH /home/root/.local/bin:${PATH}
