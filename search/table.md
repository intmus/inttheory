---
layout: page
title: Search TOC
---

<link href="{{ site.baseurl }}/assets/css/vanilla-dataTables.min.css" rel="stylesheet" type="text/css">
<table id="index-table" class="display">
    <thead>
        <tr>
            <th>Chapter</th>
            <th>Section</th>
            <th>Type</th>
            <th>Title</th>
        </tr>
    </thead>
    <tbody>
<!-- Overview Examples Lesson -->
{% for chapter in site.collections %}{% if chapter.label != 'posts' %}
{% for lesson in chapter.docs %}
{% assign parts = lesson.slug | split: "-" %} {% assign t = lesson.title | split: "-" %}
    <tr>
        <td>{{ chapter.name }}</td>
        <td>{{ parts[0] }}</td>
        <td>{{ parts[1] }}</td>
        <td><a href="{{ lesson.url | absolute_url }}">{{ t[1] }}</a></td>
    </tr>
{% endfor %}
{% endif %}{% endfor %}
    </tbody>
</table>
<script src="{{ site.baseurl }}/assets/js/vanilla-dataTables.min.js" type="text/javascript"></script>

<script>
    var dataTable = new DataTable("#index-table", {
        perPage: 20,
        fixedColumns: true,
        layout: {
            top: "{info}{search}",
            bottom: "{select}{pager}"
        },
        columns: [
            { select: 0, sort: "desc" }
        ]
    });
</script>