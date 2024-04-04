import plugin from 'tailwindcss/plugin';

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './notebook/**/*.{html,js,jsx,ts,tsx,vue}',
    './notebook/templates/layout.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    plugin(function ({ addComponents, theme }) {
      addComponents({
        '.btn': {
          padding: '.7rem 1rem',
          borderRadius: '.25rem',
          fontWeight: '600',
          fontSize: theme('fontSize.sm'),
          '&:hover': {
            backgroundColor: theme('colors.gray.100'),
          },
        },
        '.input': {
          padding: theme('spacing.2.5 spacing.4'),
          backgroundColor: 'white',
          border: '1px solid black',
          borderRadius: '.25rem',
          width: '100%',
          '&:focus': {
            outline: '1px solid black',
            border: '1px solid black',
            boxShadow: 'none',
          },
        },
      });
    }),
  ],
};
