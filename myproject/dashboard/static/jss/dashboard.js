var mes = mes|safe;
var vendas = vendas|safe ;

var trace = {
    x: mes,
    y: vendas,
    type: 'bar'
};

var layout = {
    title: 'Vendas no Mês',
    xaxis: {
        title: 'Mês'
    },
    yaxis: {
        title: 'Vendas'
    }
};

var data = [trace];

Plotly.newPlot('vendas-grafico', data, layout);
