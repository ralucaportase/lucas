// @flow

const extractResponse = (response) => {
    if (!response) {
        return { data: null, status: 500 };
    }

    return response.text().then((text) => {
        let data = text;
        try {
            data = text.length > 0 ? JSON.parse(text) : text;
        } catch (e) {}

        return { data, status: response.status };
    });
};

const post = (url: string, body: any): Promise<*> => {
    return fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
    }).then(extractResponse);
};

const startCrawl = (crawlUrl: string) => {
    return post('/api/crawl/', { url: crawlUrl });
};

export { startCrawl };
