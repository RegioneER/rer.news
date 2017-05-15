const ExtractTextPlugin = require('extract-text-webpack-plugin');

const plugin = new ExtractTextPlugin({
  filename: '[name].css',
  disable: false,
});

module.exports = {
  entry: {
    rernews: require.resolve('./rernews.less'),
  },
  output: {
    path: __dirname + '/../src/rer/news/browser/static',
    publicPath: '/++resource++rer.news/',
    filename: '[name].css',
  },
  module: {
    rules: [
      {
        test: /\.less$/,
        exclude: /node_modules/,
        use: plugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader', // translates CSS into CommonJS
              options: {
                sourceMap: true,
              },
            },
            {
              loader: 'postcss-loader',
              options: {
                sourceMap: true,
                plugins: () => ([
                  require('autoprefixer')(),
                ]),
              },
            },
            {
              loader: 'less-loader', // compiles Less to CSS
              options: {
                sourceMap: true,
              },
            },
          ],
        }),
      },
    ],
  },

  // devtool: 'source-map',
  plugins: [
    plugin,
  ],
};
