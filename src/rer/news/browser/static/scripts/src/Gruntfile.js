module.exports = function(grunt) {
  'use strict';
  require('load-grunt-tasks')(grunt);
  grunt.initConfig({
    uglify: {
      tooltipRelatedImage: {
        options: {
          sourceMap: true,
          sourceMapIncludeSources: false,
        },
        files: {
          '../tooltip-related-image.min.js': ['./bundle-compiled.js'],
        },
      },
    },
    requirejs: {
      'tooltip-related-image-plugin': {
        options: {
          baseUrl: './',
          generateSourceMaps: true,
          preserveLicenseComments: false,
          paths: {
            jquery: 'empty:',
            'mockup-patterns-modal': 'empty:',
          },
          wrapShim: false,
          name: './tooltip-related-image.js',
          exclude: ['jquery', 'mockup-patterns-modal'],
          out: './bundle-compiled.js',
          optimize: 'none',
        },
      },
    },
  });

  grunt.registerTask('compile', ['requirejs', 'uglify']);
};
