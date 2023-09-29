from flask import Flask, request, render_template

app = Flask(__name__)

regioes = {
    'regiao1': 'São Paulo',
    'regiao2': 'Rio de Janeiro',
    'regiao3': 'Santa Catarina',
}

fontes_energia = {
    'energia1': 'Energia Solar',
    'energia2': 'Energia Eólica',
    'energia3': 'Energia Hidrelétrica',
    'energia4': 'Energia Nuclear',
}

# Dados fictícios para emissão de CO2, desmatamento, custo de produção, produção de energia e impacto ambiental
dados_reais = {
    'regiao1': {
        'energia1': {
            'emissao_co2': 50,  # Valor real em kg/MWh
            'desmatamento': 5,  # Valor real em hectares/MWh
            'custo_producao': 100,  # Valor real em R$/MWh
            'producao_energia': 200,  # Valor real em MWh
            'impacto_ambiental': 'Baixo',  # Descrição real
        },
        'energia2': {
            'emissao_co2': 30,  # Valor real em kg/MWh
            'desmatamento': 3,  # Valor real em hectares/MWh
            'custo_producao': 90,  # Valor real em R$/MWh
            'producao_energia': 180,  # Valor real em MWh
            'impacto_ambiental': 'Moderado',  # Descrição real
        },
        'energia3': {
            'emissao_co2': 70,  # Valor real em kg/MWh
            'desmatamento': 7,  # Valor real em hectares/MWh
            'custo_producao': 120,  # Valor real em R$/MWh
            'producao_energia': 250,  # Valor real em MWh
            'impacto_ambiental': 'Moderado',  # Descrição real
        },
        'energia4': {
            'emissao_co2': 90,  # Valor real em kg/MWh
            'desmatamento': 9,  # Valor real em hectares/MWh
            'custo_producao': 150,  # Valor real em R$/MWh
            'producao_energia': 220,  # Valor real em MWh
            'impacto_ambiental': 'Alto',  # Descrição real
        },
    },
    'regiao2': {
        'energia1': {
            'emissao_co2': 60,  # Valor real em kg/MWh
            'desmatamento': 6,  # Valor real em hectares/MWh
            'custo_producao': 110,  # Valor real em R$/MWh
            'producao_energia': 220,  # Valor real em MWh
            'impacto_ambiental': 'Moderado',  # Descrição real
        },
        'energia2': {
            'emissao_co2': 40,  # Valor real em kg/MWh
            'desmatamento': 4,  # Valor real em hectares/MWh
            'custo_producao': 80,  # Valor real em R$/MWh
            'producao_energia': 160,  # Valor real em MWh
            'impacto_ambiental': 'Baixo',  # Descrição real
        },
        'energia3': {
            'emissao_co2': 80,  # Valor real em kg/MWh
            'desmatamento': 8,  # Valor real em hectares/MWh
            'custo_producao': 130,  # Valor real em R$/MWh
            'producao_energia': 270,  # Valor real em MWh
            'impacto_ambiental': 'Alto',  # Descrição real
        },
        'energia4': {
            'emissao_co2': 100,  # Valor real em kg/MWh
            'desmatamento': 10,  # Valor real em hectares/MWh
            'custo_producao': 170,  # Valor real em R$/MWh
            'producao_energia': 240,  # Valor real em MWh
            'impacto_ambiental': 'Muito Alto',  # Descrição real
        },
    },
    'regiao3': {
        'energia1': {
            'emissao_co2': 70,  # Valor real em kg/MWh
            'desmatamento': 7,  # Valor real em hectares/MWh
            'custo_producao': 120,  # Valor real em R$/MWh
            'producao_energia': 250,  # Valor real em MWh
            'impacto_ambiental': 'Moderado',  # Descrição real
        },
        'energia2': {
            'emissao_co2': 45,  # Valor real em kg/MWh
            'desmatamento': 4.5,  # Valor real em hectares/MWh
            'custo_producao': 90,  # Valor real em R$/MWh
            'producao_energia': 180,  # Valor real em MWh
            'impacto_ambiental': 'Baixo',  # Descrição real
        },
        'energia3': {
            'emissao_co2': 75,  # Valor real em kg/MWh
            'desmatamento': 7.5,  # Valor real em hectares/MWh
            'custo_producao': 110,  # Valor real em R$/MWh
            'producao_energia': 220,  # Valor real em MWh
            'impacto_ambiental': 'Moderado',  # Descrição real
        },
        'energia4': {
            'emissao_co2': 95,  # Valor real em kg/MWh
            'desmatamento': 9.5,  # Valor real em hectares/MWh
            'custo_producao': 140,  # Valor real em R$/MWh
            'producao_energia': 260,  # Valor real em MWh
            'impacto_ambiental': 'Alto',  # Descrição real
        },
    },
}


@app.route('/')
def index():
    return render_template('impacto_ambiental.html', regioes=regioes, fontes_energia=fontes_energia, resultado=None)


@app.route('/calcular', methods=['POST'])
def calcular_impacto():
    regiao = request.form.get('regiao')
    fonte_energia = request.form.get('fonte_energia')

    if regiao in dados_reais and fonte_energia in dados_reais[regiao]:
        dados = dados_reais[regiao][fonte_energia]
        resultado = {
            'emissao_co2': dados['emissao_co2'],
            'desmatamento': dados['desmatamento'],
            'custo_producao': dados['custo_producao'],
            'producao_energia': dados['producao_energia'],
            'impacto_ambiental': dados['impacto_ambiental'],
        }
    else:
        resultado = None

    return render_template('impacto_ambiental.html', regioes=regioes, fontes_energia=fontes_energia, resultado=resultado)


# ------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
