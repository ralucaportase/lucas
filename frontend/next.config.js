const path = require('path');

module.exports = {
    webpack(config) {
        config.resolve.alias['@lucas'] = path.join(__dirname, 'lucas');
        config.resolve.alias['@pages'] = path.join(__dirname, 'pages');
        config.resolve.alias['@public'] = path.join(__dirname, 'public');
        return config;
    },
};
