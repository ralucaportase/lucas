// @flow
import * as React from 'react';
import Head from 'next/head';

const Header = (): React.Node => {
    return (
        <Head>
            <title>Create Next App</title>
            <link rel="icon" href="/favicon.ico" />
        </Head>
    );
};

export default Header;
