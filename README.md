![frontend](https://github.com/ralucaportase/lucas/workflows/frontend/badge.svg)
![backend](https://github.com/ralucaportase/lucas/workflows/backend/badge.svg)

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
    λ pip setup.py local
    ```
    If your terminal gets filled with red text, don't freak out, it's because of psycopg2 run this commands, and try again 
    ```
    λ xcode-select --install
    λ export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
    ```
    
### Make Lucas do the hard work

#### Start a single spider

Go into the crawler directory and use:
```
λ scrapy crawl lucas_crawl_spider -t csv -o links.csv
```

```
λ scrapy crawl [crawler_name] -t [output-format] -o [output-file-path]
```

#### Scrapyd

We use scrapyd to execute the spiders. Scrapyd is an application (typically run as a daemon) that listens to requests for spiders to run and spawns a process for each one.

To run scrapyd go to the `crawler` directory and run:
```
λ scrapyd
```
If everything works, you will be able to see scrapyd web console at http://127.0.0.1:6800/

### Django

For django we use postgresql, if you don't have it installed run:
```
λ brew install postgresql
```

The database url is taken from `DATABASE_URL` env variable, and if the variable is empty it will use `lucas` db.
To create it just run:
```
λ createdb lucas
```

After that you can go in `backend/lucas` and run
```
λ python manage.py migrate
λ python manage.py runserver
```
The django app will be available on localhost:8000

### Frontend

The frontend is build with react. And served by django. 
To run the frontend run:
```
λ yarn install
λ yarn start
```
The frontend will be available on localhost:3000

To run code formatting and flow run:
```
λ yarn fix
```

If you want to see the frontend served by django, run:
```
λ yarn build
```
This will create the build directory in frontend, and django will serve the files from there.
Now you should see the frontend on: localhost:8000

### In production

We run scrapyd and django under the same dyno, with nginx on top.
Nginx will send the traffic to django and scrapyd depending on the routes.

Scrapyd web console should be available under `/scrapyd/` route.  


### Code formatting
Use `python setup.py format` in the `backend` dir to format the python code.

Use `yarn format` in `frontend` for js code.
