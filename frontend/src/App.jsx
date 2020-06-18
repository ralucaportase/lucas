// @flow

import * as React from 'react';
import { Provider } from 'react-redux';
import { ThemeProvider } from '@material-ui/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

import store from 'lucas/state';
import Crawl from 'lucas/crawl/crawl';
import { darkTheme } from 'lucas/theme';

const App = () => (
    <Provider store={store}>
        <ThemeProvider theme={darkTheme}>
            <CssBaseline />
            <Crawl />
        </ThemeProvider>
    </Provider>
);

export default App;
