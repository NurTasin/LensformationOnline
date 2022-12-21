def template(imgPlace):
    return f"""\
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Projects - Lensformation</title>
    <meta name="description" content="Lensformation is a photography studio based in Bangladesh. We focus on capturing precious moments and try to add some creativity with it.">
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:300,400,700&amp;display=swap">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
    <link rel="stylesheet" href="assets/css/Footer-with-social-media-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pikaday/1.6.1/css/pikaday.min.css">
</head>

<body>
    <nav class="navbar navbar-light navbar-expand-lg fixed-top bg-light bg-gradient portfolio-navbar gradient">
        <div class="container"><a class="navbar-brand logo" href="/index.html">Lensformation</a><button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navbarNav"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link active" href="projects-compact-grid.html">Projects</a></li>
                    <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <main class="page projets-page">
        <section class="portfolio-block projects compact-grid">
            <div class="heading">
                <h2>Recent Work</h2>
            </div>
            <div class="row g-0">
                {imgPlace}
            </div>
        </section>
    </main>
    <footer class="page-footer">
        <div class="container">
            <div class="social-icons"><a href="https://facebook.com/lensformation"><i class="icon ion-social-facebook"></i></a><a href="https://instagram.com/lensformation"><i class="icon ion-social-instagram-outline"></i></a><a href="mailto: lensformation.ts@gmail.com"><i class="icon ion-email"></i></a></div>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pikaday/1.6.1/pikaday.min.js"></script>
    <script src="assets/js/theme.js"></script>
</body>

</html>
"""


def renderImage(href:str,src:str,heading:str,desc:str):
    return f"""\
<div class="col-md-6 col-lg-4 item zoom-on-hover position-relative"><a href="{href}"><img class="img-fluid image" src="{src}"><span class="description"><span class="description-heading">{heading}</span><span class="description-body">{desc}</span></span></a></div>
"""