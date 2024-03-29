// @flow

import cookie from 'cookie';

const extractResponse = (response) => {
    if (!response) {
        return { data: null, status: 500 };
    }

    return response.text().then((text) => {
        let data = text;
        try {
            data = text.length > 0 ? JSON.parse(text) : text;
        } catch (e) {
            console.error('Getting the response failed!');
        }

        return { data, status: response.status };
    });
};

const getCSRFToken = () => {
    return cookie.parse(document.cookie).csrftoken;
};

const post = (url: string, body: any): Promise<*> => {
    return fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
    }).then(extractResponse);
};

const buildQueryParams = (params: any): string => {
    if (!params) {
        return '';
    }
    return `?${Object.entries(params)
        .map(([key, value]) => (typeof value === 'string' ? `${key}=${value}` : ''))
        .join('&')}`;
};

const get = (url: string, params: any): Promise<*> => {
    return fetch(`${url}${buildQueryParams(params)}`, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json',
        },
    }).then(extractResponse);
};

const startCrawlTask = ({ url }: { url: ?string }) => post('/api/crawl/', { url });

const getCrawlResults = ({ taskID, uniqueID }: { taskID: ?string, uniqueID: ?string }) =>
    get('/api/crawl/', { taskID, uniqueID });

export { startCrawlTask, getCrawlResults };
