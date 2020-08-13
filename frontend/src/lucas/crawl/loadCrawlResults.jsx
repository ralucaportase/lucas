// @flow

import * as React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Backdrop from '@material-ui/core/Backdrop';
import CircularProgress from '@material-ui/core/CircularProgress';

import { getResults } from './state';
import styles from './styles/loadCrawlResults.scss';

// This component will start requesting crawl results right after the
// crawl task has started. This should be replaced with web sockets.
const LoadCrawlResults = () => {
    const dispatch = useDispatch();
    const crawlResultsTimer = React.useRef(null);

    const crawlTask = useSelector((state) => state.crawl.task);
    const crawlResults = useSelector((state) => state.crawl.results);

    const [crawlResultsLoading, setCrawlResultsLoading] = React.useState(false);

    const isCrawlFinished = React.useCallback(
        () =>
            (crawlResults.data && crawlResults.data.status === 'finished') || !!crawlResults.error,
        [crawlResults],
    );

    React.useEffect(() => {
        if (crawlTask.loaded) {
            crawlResultsTimer.current = setInterval(() => {
                dispatch(getResults(crawlTask.data));
                setCrawlResultsLoading(true);
            }, 2000);
        }
        return () => {
            if (crawlResultsTimer.current) {
                setCrawlResultsLoading(false);
                clearInterval(crawlResultsTimer.current);
            }
        };
    }, [crawlTask.loaded, dispatch, crawlTask.data]);

    React.useEffect(() => {
        if (isCrawlFinished()) {
            if (crawlResultsTimer.current) {
                clearInterval(crawlResultsTimer.current);
                setCrawlResultsLoading(false);
            }
        }
    }, [isCrawlFinished]);

    return (
        <Backdrop className={styles.backdrop} open={crawlResultsLoading}>
            <CircularProgress color="inherit" />
            For now you can start only one crawl session. Lucas sorry :(
            <img
                src={
                    'https://i.dailymail.co.uk/i/newpix/2018/06/07/12/4D01BD2F00000578-0-image-a-9_1528369788305.jpg'
                }
                alt={'Sad lucas'}
            />
        </Backdrop>
    );
};

export default LoadCrawlResults;
