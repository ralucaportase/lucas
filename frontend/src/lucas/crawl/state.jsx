// @flow

import { combineReducers } from 'redux';

import { startCrawlTask, FetchReducer, getCrawlResults } from 'lucas/api';

const crawlTaskFetchReducer = new FetchReducer('crawlTask', startCrawlTask);

const crawl = (url: ?string) => crawlTaskFetchReducer.fetch()({ url });

const crawlResultsFetchReducer = new FetchReducer('crawl', getCrawlResults);

const getResults = ({ taskID, uniqueID }: { taskID: ?string, uniqueID: ?string }) =>
    crawlResultsFetchReducer.fetch()({
        taskID,
        uniqueID,
    });

export { crawl, getResults };

export default combineReducers({
    task: crawlTaskFetchReducer.reducer(),
    results: crawlResultsFetchReducer.reducer(),
});
