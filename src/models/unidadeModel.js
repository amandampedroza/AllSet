var database = require("../database/config")

// Coloque os mesmos parâmetros aqui. Vá para a var instrucaoSql  //nome, estado, cidade, bairro, contato, fkEmpresa
function cadastrar(nome, estado, cidade, bairro, contato ,fkEmpresa) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, estado, cidade, bairro, contato, fkEmpresa );
    
    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    var instrucaoSql = `
        INSERT INTO Unidade (fkEmpresa, nome, estado, cidade, bairro, contato) VALUES ('${fkEmpresa}', '${nome}','${estado}', '${cidade}', '${bairro}', '${contato}');
    `;

    // INSERT INTO Unidade (idUnidade, fkEmpresa, identificacao, estado, cidade, bairro, contato)
    // VALUES (1, 1, 'Unidade A', 'SP', 'São Paulo', 'Centro', '1234-5678');


    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

module.exports = {
    cadastrar
};