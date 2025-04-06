// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
const { defineConfig } = require('@vue/cli-service')
const webpack = require('webpack')

module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        'process.env.VUE_APP_VERSION': JSON.stringify(require('./package.json').version)
      })
    ]
  },
  devServer: {
    client: {
      overlay: false
    }
  }
})
// const { defineConfig } = require('@vue/cli-service');
// const webpack = require('webpack');

// module.exports = defineConfig({
//   transpileDependencies: true,
//   configureWebpack: {
//     plugins: [
//       new webpack.DefinePlugin({
//         'process.env.VUE_APP_VERSION': JSON.stringify(require('./package.json').version)
//       })
//     ],
//     optimization: {
//       minimizer: [
//         {
//           test: /\.js(\?.*)?$/i,
//           chunkFilter: (chunk) => chunk.name !== 'vendor',
//           extractComments: false,
//           sourceMap: true,
//           options: {
//             // 移除 console 语句
//             drop_console: true,
//             // 移除 debugger
//             drop_debugger: true,
//           },
//         },
//       ],
//     },
//   },
//   devServer: {
//     client: {
//       overlay: false
//     }
//   }
// });