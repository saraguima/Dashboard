(function (){
    var el = document.gerElementById("char-data");
    if (!el) return;

    try{
        var payload = JSON.parse(el.textContent || "{}");
        var mes = payload.mes || [];
        var vendas = payload.vendas || [];

        var trace = { x: mes, y: vendas, type: "bar"};
        var layout = {
            title: "Vendas no Mês",
            xaxis: { title: "Mês"},
            yaxis: { title: "Vendas"},
            margin: { t: 50, 1: 50, r: 20, b:50}
    };

    Plotly.newPlot("vendas-grafico", [trace], layout);
} catch (e) {
    console.error("Erro ao ler chart-data:", e);
}
})();