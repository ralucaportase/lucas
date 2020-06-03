// @flow

import * as React from 'react';
import { TextField } from '@material-ui/core';

type Props = {
    value: string,
    onChange: (value: string) => null,
    label: string,
};

const LucasInput = (props: Props) => {
    const { value, onChange, label } = props;

    const onInputChange = React.useCallback(
        (event: any) => {
            if (onChange) {
                onChange(event.target.value);
            }
        },
        [onChange],
    );

    return (
        <TextField
            value={value}
            onChange={onInputChange}
            fullWidth
            size="small"
            label={label || ''}
            variant="filled"
        />
    );
};

export default LucasInput;
