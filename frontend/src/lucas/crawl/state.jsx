// @flow

import { startCrawl, FetchReducer } from 'lucas/api';

const fetchReducer = new FetchReducer('crawl', (params) => startCrawl(params.url));

const crawl = (url: string) => fetchReducer.fetch()({ url });

export { crawl };

export default fetchReducer.reducer();
