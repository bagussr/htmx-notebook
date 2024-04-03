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
          padding: '.5rem 1rem',
          borderRadius: '.25rem',
          fontWeight: '600',
          fontSize: theme('fontSize.sm'),
        },
      });
    }),
  ],
};
