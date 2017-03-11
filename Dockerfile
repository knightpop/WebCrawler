FROM continuumio/anaconda3

ADD ./ /root/WebCrawler
WORKDIR /root/WebCrawler
RUN conda install -y -c conda-forge scrapy=1.3.2
VOLUME        ["/root/WebCrawler/images"]
ENTRYPOINT python __main__.py