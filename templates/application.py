{% extends "layout.html" %}

{% block title %}
    Home
{% endblock %}

{% block main %}
<div class="container-fluid">
        <div> TEACHER </div>
        {% for row in results %}
        <div class="question-card">
<!-- row[0] = title | row[1] = username | row[2] = post date | row[3] = question | row[4] = theadid -->
                <div class="question-card-title">
                        <h4> {{ row[0] }}</h4>
                        <h6> {{ row[1] }} asked on {{ row[2] }}.</h5>
                </div>
                <div class="question-card-description">
                        <p> {{ row[3] }}</p>
                        <form action="{{ url_for('answer') }}" method="post">
                                <div class="form-group">
                                        <button class="btn btn-default" type="submit" name="thread_id" value={{ row[4] }}>Answer Question</button>
                                </div>
                        </form>
                </div>
        </div>
        {% endfor %}
</div>
{% endblock %}
