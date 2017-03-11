##Web Crawler For Study

###Anaconda Setting
```bash
$ conda create -n webcrawler python=3.5 anaconda
$ source activate webcrawler
```

###Dependencies
```bash
$ conda install -y -c conda-forge scrapy=1.3.2
$ conda install -y opencv
```

###Docker
```bash
$ docker run -v {mount}:/root/WebCrawler/images knightpop/webcrawlerexample:0.0.2
```