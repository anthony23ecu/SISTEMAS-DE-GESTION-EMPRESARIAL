from flask import Flask

aplication = Flask(__name__)

@aplication.route("/")

def raiz():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Estilo Apple</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: #f5f5f7;
      color: #1d1d1f;
      line-height: 1.6;
      text-align: center;
    }

    header {
      background: #fff;
      padding: 15px 20px;
      border-bottom: 1px solid #d2d2d7;
      position: sticky;
      top: 0;
    }

    nav a {
      margin: 0 15px;
      text-decoration: none;
      color: #1d1d1f;
      font-weight: 500;
      font-size: 14px;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #0071e3;
    }

    section {
      padding: 80px 20px;
    }

    section h1 {
      font-size: 3rem;
      font-weight: 600;
      margin-bottom: 20px;
    }

    section p {
      font-size: 1.2rem;
      max-width: 700px;
      margin: 0 auto;
      color: #515154;
    }

    .btn {
      display: inline-block;
      margin-top: 30px;
      padding: 12px 24px;
      background: #0071e3;
      color: #fff;
      font-size: 1rem;
      border-radius: 50px;
      text-decoration: none;
      transition: background 0.3s ease;
    }

    .btn:hover {
      background: #005bb5;
    }

    footer {
      padding: 30px 20px;
      background: #f5f5f7;
      border-top: 1px solid #d2d2d7;
      font-size: 14px;
      color: #6e6e73;
    }
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="#inicio">Inicio</a>
      <a href="#productos">Productos</a>
      <a href="#soporte">Soporte</a>
    </nav>
  </header>

  <section id="inicio">
    <h1>Diseño simple. Potente.</h1>
    <p>Una web inspirada en el estilo Apple: minimalismo, claridad y un enfoque en la experiencia.</p>
    <a href="#productos" class="btn">Ver más</a>
  </section>

  <section id="productos">
    <h1>Productos</h1>
    <p>Presenta tus proyectos como si fueran joyas tecnológicas. Cada detalle cuenta.</p>
  </section>

  <section id="soporte">
    <h1>Soporte</h1>
    <p>Información clara, directa y útil. Porque lo simple es lo que mejor funciona.</p>
  </section>

  <footer>
    <p>&copy; 2025 Inspirado en Apple. Proyecto Demo.</p>
  </footer>
</body>
</html>
'''

if __name__ == "__main__":
    aplication.run(debug=True)
