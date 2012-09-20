<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{{name}}</title>
        
        <!-- styles -->
        <link href="/static/css/bootstrap.css" rel="stylesheet">
        <style>
            body {
                padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
            }
        </style>
        <link href="/static/css/bootstrap-responsive.css" rel="stylesheet">
    </head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Pywebase</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">
      <h1>Pywebase starter template</h1>
      <p>Use this document as a way to quick start any new project.<br> All you get is this message and a barebones HTML document.</p>
      
      <h1> About Pywebase</h1>
      <p>Small platform for local web applications. It's based on the next components:
      <ul>
        <li><a href="http://bottlepy.org/">bottle.py</a> is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.</li>
        <li><a href="https://github.com/ownport/pyservice">pyservice</a> is simple library to make service on python more easy</li>
        <li><a href="https://github.com/twitter/bootstrap">bootstrap</a> is HTML, CSS, and JS toolkit from Twitter</li>
      </ul>
      </p>

      <h1> Contact </h1>
      <p>Pywebase is available on GitHub <a href="https://github.com/ownport/pywebase">ownport/pywebase</a></p>

    </div> <!-- /container -->
    
    <!-- javascript -->
    <script src="/static/js/jquery.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    
</body>
</html>
