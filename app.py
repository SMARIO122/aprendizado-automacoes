import dash
from dash import html, dcc, Output, Input

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Terminal Geek"),
    
    dcc.Input(
        id='campo-comando',
        type='text',
        placeholder='Digite um comando...',
        style={'marginRight': '10px'}
    ),
    
    html.Button("Executar", id='botao-executar', n_clicks=0),

    html.Div(id='saida-terminal', style={'marginTop': '20px'})
])

@app.callback(
    Output('saida-terminal', 'children'),
    Input('botao-executar', 'n_clicks'),
    Input('campo-comando', 'value')
)
def mostrar_saida(_, comando):
    if comando:
        return f"📡 Comando executado: {comando}"
    return ""

if __name__ == "__main__":
    app.run(debug=True, port=8050)




