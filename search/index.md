---
layout: page
title: Search
---

This page provides a basic search of IntTheory content.
*Note: it may take a few seconds to load!* 
(p.s. you can also try [Google CSE]({{ "/search/google.html" | absolute_url }}))

<script src="https://unpkg.com/lunr/lunr.js"></script>

<input type="text" size="15" id="lunr-search" placeholder="Search..." aria-label="search">
<input class="button-all" type="button" onclick="lunr_search();" value=" Search ">

<ul id="search-results"></ul>

<hr>

Built using [Lunr.js](https://lunrjs.com/).

<script>
// add documents
var documents = { 
    {% for post in site.documents %}
    "{{ post.url | absolute_url | xml_escape }}": 
    { 
      "url": "{{ post.url | absolute_url | xml_escape }}",
      "title": "{{ post.title | xml_escape }}",
      "text": {{ post.content | strip_html | jsonify | replace: "\n"," " }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
};
// create index
var idx = lunr(function () {
  this.ref('url')
  this.field('title')
  this.field('text')
  for (var key in documents) {
    this.add(documents[key])
  }
});
// do search
function displayResults(results) {
  var searchResults = document.getElementById('search-results');
  if (results.length) { // Are there any results?
    var appendString = '';
    for (var i = 0; i < results.length; i++) {  // Iterate over the results
      var link = results[i].ref;
      var title = documents[results[i].ref].title;
      var preview = documents[results[i].ref].text.substring(0,150);
      appendString += '<li><a href="' + link + '">' + title + '</a><br>' + preview + '... </li>';
    }
    searchResults.innerHTML = appendString;
  } else {
    searchResults.innerHTML = '<li>No results found</li>';
  }
}
function lunr_search() {
    var query = document.getElementById("lunr-search").value;
    var results = idx.search(query);
    displayResults(results);
}
</script>
