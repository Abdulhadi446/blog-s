(function() {
  var form = document.getElementById('blogForm');
  if (!form) return;

  function formatDate(dateStr) {
    if (!dateStr) return "";
    var d = new Date(dateStr);
    return d.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
  }

  function buildMeta() {
    var slug = document.getElementById('slug').value;
    var title = document.getElementById('title').value;
    var author = document.getElementById('author').value || "Anonymous";
    var desc = document.getElementById('description').value;
    var keywords = document.getElementById('keywords').value;
    var tags = document.getElementById('tags').value;
    var published = document.getElementById('publishedDate').value;
    var modified = document.getElementById('modifiedDate').value;
    var image = document.getElementById('image').value;

    var lines = [];
    if (title) { lines.push('title: ' + JSON.stringify(title)); }
    if (slug) { lines.push('slug: ' + slug); }
    if (author) { lines.push('author: ' + JSON.stringify(author)); }
    if (desc) { lines.push('description: ' + JSON.stringify(desc)); }
    if (published) { lines.push('published: ' + published); }
    if (modified) { lines.push('modified: ' + modified); }
    if (image) { lines.push('image: ' + image); }
    if (keywords) { lines.push('keywords: ' + keywords.split(',').map(function(k) { return k.trim(); }).join(', ')); }
    if (tags) { lines.push('tags: ' + tags.split(',').map(function(t) { return t.trim(); }).join(', ')); }

    return lines.join('\n');
  }

  function updatePreview() {
    var preview = document.getElementById('markdownPreview');
    if (!preview) return;
    var meta = buildMeta();
    preview.innerHTML = '<div class="preview-label">Metadata Preview</div>\n' + (meta || '(fill in the form to see preview)');
  }

  var inputs = document.querySelectorAll('input, textarea');
  for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('input', updatePreview);
  }
  updatePreview();

  var now = new Date();
  var local = now.toISOString().slice(0, 16);
  var pubEl = document.getElementById('publishedDate');
  var modEl = document.getElementById('modifiedDate');
  if (pubEl && !pubEl.value) pubEl.value = local;
  if (modEl && !modEl.value) modEl.value = local;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    function getVal(id) { return document.getElementById(id).value; }

    var tags = getVal('tags');
    var tagObjects = tags
      ? tags.split(',').map(function(t) { return t.trim(); }).filter(Boolean).map(function(t) {
          return "{'name': '" + t + "', 'slug': '" + t.toLowerCase().replace(/\s+/g, '-') + "'}";
        }).join(',')
      : '';

    var params = new URLSearchParams({
      slug: getVal('slug'),
      title: getVal('title'),
      author: getVal('author'),
      description: getVal('description'),
      content: getVal('content'),
      publishedDate: getVal('publishedDate'),
      formattedDate: formatDate(getVal('publishedDate')),
      modifiedDate: getVal('modifiedDate'),
      image: getVal('image'),
      keywords: getVal('keywords'),
      tags: tagObjects
    });

    window.location.href = '/upload?' + params.toString();
  });
})();
