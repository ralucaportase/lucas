// @flow

import * as React from 'react';
import { useSelector } from 'react-redux';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import styles from './styles/crawlTable.scss';

const EMPTY_ARRAY = Object.freeze([]);

const CrawlTable = () => {
    const crawlResults = useSelector(
        (state) => (state.crawl.results.data || {}).crawlResults || EMPTY_ARRAY,
    );

    return (
        <TableContainer className={styles.container} component={Paper}>
            <Table className={styles.table} size="small" aria-label="a dense table">
                <TableHead>
                    <TableRow>
                        <TableCell>Address</TableCell>
                        <TableCell align="left">Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {crawlResults.map((row) => (
                        <TableRow key={row.address}>
                            <TableCell component="th" scope="row">
                                {row.address}
                            </TableCell>
                            <TableCell align="left">200</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default CrawlTable;
