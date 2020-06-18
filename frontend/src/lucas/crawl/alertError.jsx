// @flow

import * as React from 'react';
import { useSelector } from 'react-redux';
import { Alert } from '@material-ui/lab';

type Props = {
    selector: (state: any) => any,
};

/**
 * Displays an alert if there are errors on the
 * selected object in the error.data field
 * @param selector
 * @returns {*}
 * @constructor
 */
const AlertError = ({ selector }: Props) => {
    const data = useSelector(selector);

    return (
        data.error &&
        data.error.data && (
            <Alert variant="filled" severity="error">
                {data.error.data}
            </Alert>
        )
    );
};

export default AlertError;
