// @flow

import * as React from 'react';
import { useDispatch } from 'react-redux';
import Button from '@material-ui/core/Button';
import { crawl } from './state';

type Props = {
    className?: string,
    url: ?string,
};

const CrawlButton = (props: Props) => {
    const { className, url } = props;
    const dispatch = useDispatch();

    const onClick = React.useCallback(() => dispatch(crawl(url)), [dispatch, url]);
    return (
        <Button
            onClick={onClick}
            className={className}
            size="large"
            fullWidth
            variant="contained"
            color="primary"
        >
            CRAWL
        </Button>
    );
};

export default CrawlButton;
