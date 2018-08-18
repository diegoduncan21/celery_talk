FROM python:2.7
ENV PYTHONUNBUFFERED 1
# Create root folder for project
RUN mkdir /webapps
WORKDIR /webapps
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libncurses5-dev \
libxml2-dev \
libxslt1-dev \
libpq-dev \
python-dev \
build-essential \
xvfb \
binutils \
libproj-dev gdal-bin \
python-pip \
git-core \
net-tools

# install version that server have.
# RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
# RUN tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
# RUN mv wkhtmltox/bin/wkhtmlto* /usr/bin/
# RUN ln -nfs /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

# hack on https://github.com/JazzCore/python-pdfkit/wiki/Using-wkhtmltopdf-without-X-server
# RUN echo '#!/bin/sh\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh
# RUN chmod a+x /usr/bin/wkhtmltopdf.sh
# RUN rm -f /usr/local/bin/wkhtmltopdf
# RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

RUN pip install -U pip setuptools

COPY requirements.txt /webapps/
RUN pip install -r /webapps/requirements.txt

ADD . /webapps/

# Django service
EXPOSE 8000