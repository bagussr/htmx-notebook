import * as htmx from 'htmx.org';

htmx.onLoad(() => {
  const search = htmx.find('#default-search');

  const searchFunction = () => {
    var url = new URL(location);
    console.log(url);
    url.searchParams.set('search', search.value);
    if (search.value === '') {
      url.searchParams.set('search', '*');
    }
    history.pushState({}, '', url);
  };

  const renderFunction = evt => {};

  search.addEventListener('htmx:before-request', searchFunction);
  search.addEventListener('htmx:after-request', renderFunction);

  const x = htmx.findAll('.custom-ellipsis');
  x.forEach(item => {
    item.style['-webkit-line-clamp'] = item.getAttribute('ellipsis');
  });
});
