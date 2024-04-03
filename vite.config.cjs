import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    include: ['linked-dep'],
  },
  build: {
    rollupOptions: {
      app: './notebook/templates/layout.html',
    },
    commonjsOptions: {
      include: [/linked-dep/, /node_modules/],
    },
  },
});
