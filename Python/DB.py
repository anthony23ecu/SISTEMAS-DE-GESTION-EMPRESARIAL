from flask import Flask, request
import sqlite3
 
app = Flask(__name__)
 
@app.route("/")
def index():
    # Obtiene la tabla desde la URL (por defecto 'clientes')
    tabla = request.args.get("tabla", "clientes")
 
    html = '''
<style>
      body {
        display: flex;
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f3f4f6;
        color: #333;
      }
 
      nav {
        flex: 1;
        background: #4b0082;
        color: white;
        padding: 20px;
        min-height: 100vh;
        box-shadow: 2px 0 10px rgba(0,0,0,0.15);
      }
 
      nav h1 {
        font-size: 1.4em;
        text-align: center;
        margin-bottom: 20px;
        color: #f9fafb;
      }
 
      nav a {
        display: block;
        background: #ffffff;
        color: #4b0082;
        text-decoration: none;
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 6px;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
      }
 
      nav a:hover {
        background: #ece9ff;
        transform: translateX(4px);
      }
 
      main {
        flex: 5;
        padding: 40px;
      }
 
      h2 {
        color: #4b0082;
        border-bottom: 3px solid #4b0082;
        padding-bottom: 5px;
        margin-bottom: 20px;
      }
 
      table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-radius: 8px;
        overflow: hidden;
      }
 
      th {
        background: #4b0082;
        color: white;
        text-align: left;
        padding: 12px;
        font-weight: 600;
      }
 
      td {
        padding: 10px 12px;
        border-bottom: 1px solid #eee;
      }
 
      tr:hover td {
        background: #f9f5ff;
      }
 
      footer {
        margin-top: 40px;
        text-align: center;
        color: #777;
        font-size: 0.9em;
      }
 
      @media (max-width: 900px) {
        body {
          flex-direction: column;
        }
        nav {
          min-height: auto;
          box-shadow: none;
        }
      }
</style>
 
    <body>
<nav>
<h1>📊 Tablas</h1>
    '''
 
    # Conexión a la base de datos SQLite
    con = sqlite3.connect('empresa1.db')
    cur = con.cursor()
    
    # Listar todas las tablas (excluyendo la interna 'sqlite_sequence')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence'")
    tablas = cur.fetchall()
 
    for t in tablas:
        nombre_tabla = t[0]
        activo = "style='background:#e0d4ff; font-weight:bold;'" if nombre_tabla == tabla else ""
        html += f'<a href="/?tabla={nombre_tabla}" {activo}>{nombre_tabla}</a>'
 
    html += f'''
</nav>
<main>
<h2>Tabla: {tabla}</h2>
<table>
<tr>
    '''
 
    # Mostrar columnas y datos de la tabla seleccionada
    try:
        cur.execute(f"PRAGMA table_info({tabla});")
        columnas = cur.fetchall()
        for col in columnas:
            html += f"<th>{col[1]}</th>"
        html += "</tr>"
 
        cur.execute(f"SELECT * FROM {tabla};")
        filas = cur.fetchall()
        for fila in filas:
            html += "<tr>"
            for valor in fila:
                html += f"<td>{valor}</td>"
            html += "</tr>"
    except Exception as e:
        html += f"<tr><td colspan='100%'>⚠️ Error al cargar la tabla '{tabla}': {e}</td></tr>"
 
    html += '''
</table>
<footer>
          Hecho con ❤️ usando <strong>Flask</strong> + <strong>SQLite</strong>
</footer>
</main>
</body>
    '''
 
    con.close()
    return html
 
 
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5003)
