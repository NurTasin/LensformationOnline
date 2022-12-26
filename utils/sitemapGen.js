const SitemapGenerator = require('sitemap-generator');

// create generator
var generator = SitemapGenerator('https://lensformation.tech', {
  maxDepth: 5,
  filepath: './sitemap.xml',
  maxEntriesPerFile: 50000,
  stripQuerystring: true
});

// register event listeners
generator.on('done', () => {
  console.log("Sitemap Generated")
});

// start the crawler
generator.start();