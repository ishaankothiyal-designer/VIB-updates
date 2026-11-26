/* Legacy sample links always open the named Swift example. Explicit choices never redirect. */
(()=>{
 'use strict';
 if(/\/sample(?:\.html)?$/.test(location.pathname)) {
  location.replace('sample-swift.html'+(location.search||'')+location.hash);
 }
})();
