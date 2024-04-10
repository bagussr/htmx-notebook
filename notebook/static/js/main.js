import 'vite/modulepreload-polyfill';
import 'htmx.org';
import '../css/styles.css';
import 'flowbite/dist/flowbite';
import 'flowbite';
import * as htmx from 'htmx.org';
import './htmx_extensions/response_target';

const getAuth = () => {
  return localStorage.getItem('token');
};

htmx.defineExtension('api-ext', {
  onEvent: function (name, evt) {
    if (name == 'htmx:configRequest') {
      if (getAuth()) {
        evt.detail.headers['Authorization'] = getAuth();
      }
    }
  },
});

globalThis.htmx = htmx;
