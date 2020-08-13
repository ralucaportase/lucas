// @flow

import React from 'react';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';

import LucasInput from './lucasInput';
import CrawlButton from './crawlButton';
import CrawlTable from './crawlTable';
import AlertError from './alertError';
import LoadCrawlResults from './loadCrawlResults';
import styles from './styles/crawl.scss';

const Crawl = () => {
    const [url, setUrl] = React.useState('http://quotes.toscrape.com/');

    return (
        <>
            <LoadCrawlResults />
            <div className={styles.root}>
                <Paper className={styles.paper}>
                    <Grid container spacing={2}>
                        <Grid item xs={10}>
                            <LucasInput value={url} onChange={(value) => setUrl(value)} label={'URL'} />
                        </Grid>
                        <Grid item xs={2}>
                            <CrawlButton className={styles.button} url={url} />
                        </Grid>
                    </Grid>
                </Paper>
                <AlertError selector={(state) => state.crawl.task} />
                <CrawlTable />
            </div>
        </>
    );
};

export default Crawl;
