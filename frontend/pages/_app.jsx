// @flow
import * as React from 'react';

import Header from '@lucas/header';
import Footer from '@lucas/footer';
import '../styles/globals.scss';

type Props = {
    Component: React.ComponentType<*>,
    pageProps: any,
};

const App = ({ Component, pageProps }: Props): React.Node => {
    return (
        <>
            <Header />
            <main>
                <Component {...pageProps} />
            </main>
            <Footer />
        </>
    );
};

export default App;
