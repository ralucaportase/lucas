import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import LucasInput from './lucasInput';
import CrawlButton from './crawlButton';
import CrawlTable from './crawlTable';
import AlertError from './alertError';
import LoadCrawlResults from './loadCrawlResults';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
    button: {
        height: '100%',
    },
}));

const Crawl = () => {
    const [url, setUrl] = React.useState('http://quotes.toscrape.com/');

    const classes = useStyles();
    return (
        <>
            <LoadCrawlResults />
            <div className={classes.root}>
                <Paper className={classes.paper}>
                    <Grid container spacing={2}>
                        <Grid item xs={10}>
                            <LucasInput value={url} onChange={(url) => setUrl(url)} label={'URL'} />
                        </Grid>
                        <Grid item xs={2}>
                            <CrawlButton className={classes.button} url={url} />
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
