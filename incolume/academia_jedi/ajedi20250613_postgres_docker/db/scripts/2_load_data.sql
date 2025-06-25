COPY tb_brasileiro_2022(
    classificacao,
    time,
    pontos,
    jogos,
    vitorias,
    empates,
    derrotas,
    gols_pro,
    gols_contra,
    saldo_gols,
    aproveitamento, -- Porcentagem sem o símbolo de %
    cartoes_amarelos,
    cartoes_vermelhos
 )
 FROM '/data/brasileiroA2022.csv'
 DELIMITER ','
 CSV HEADER;
