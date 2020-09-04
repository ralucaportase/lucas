import * as React from 'react';

import Header from '../lucas/header';
import '../styles/globals.css';

const App = ({ Component, pageProps }): React.Node => {
    return (
        <>
            <Header />
            <main>
                <Component {...pageProps} />
            </main>
            <footer>
                <a
                    href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <img src="/vercel.svg" alt="Vercel Logo" className="logo" />
                </a>
            </footer>
        </>
    );
};

export default App;
