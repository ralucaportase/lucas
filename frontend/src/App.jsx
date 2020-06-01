// @flow

import * as React from 'react';
import { Provider } from 'react-redux';
import store from 'lucas/state';

const App = () => (
    <Provider store={store}>
        <span>Hello world</span>
    </Provider>
);

export default App;
