CREATE TABLE tb_brasileiro_2022 (
    classificacao INT PRIMARY KEY,
    time VARCHAR(50) NOT NULL,
    pontos INT,
    jogos INT,
    vitorias INT,
    empates INT,
    derrotas INT,
    gols_pro INT,
    gols_contra INT,
    saldo_gols INT,
    aproveitamento INT, -- Porcentagem sem o símbolo de %
    cartoes_amarelos INT,
    cartoes_vermelhos INT
);
