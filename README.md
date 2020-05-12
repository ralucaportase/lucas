## Lucas one cute web crawler

![Lucas](https://i.insider.com/5b1aae9d1ae66220008b4e20?width=1200&format=jpeg)

### Setup Lucas

1. Open a terminal and navigate to the `backend` directory:
2. Create a new virtual environment:

    ```
    λ virtualenv env --python python3
    ```
3. Activate virtual environment:

    ```
    λ source env/bin/activate
    ```
4. Install requirements:
    ```
    λ pip install -r requirements.txt
    ```
    
### Make Lucas do the hard work

Go into the crawler directory and use:
```
λ scrapy crawl lucas_crawl_spider -t csv -o links.csv
```

```
λ scrapy crawl [crawler_name] -t [output-format] -o [output-file-path]
```