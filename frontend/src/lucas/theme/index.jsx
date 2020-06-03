// @flow

import { createMuiTheme } from '@material-ui/core';
import { green } from '@material-ui/core/colors';

const darkTheme = createMuiTheme({
    palette: {
        type: 'dark',
        primary: green,
    },
});

export { darkTheme };
