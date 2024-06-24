# Técnicas de Validação de Modelos

# Holdout
Divide os dados em duas partes: um conjunto de treinamento e um conjunto de teste.
Geralmente, a divisão é feita na proporção de 70%-30%, 80%-20% ou similar.
Vantagens: Simplicidade e facilidade de implementação.
Desvantagens: Pode levar a uma alta variabilidade nos resultados, dependendo de como os dados são divididos.
K-Fold Cross-Validation:

Divide os dados em K subconjuntos (ou "folds"). O modelo é treinado K vezes, cada vez usando K-1 folds para treino e 1 fold diferente para teste.
A média dos resultados de todos os K testes é usada para avaliar o desempenho do modelo.

# Técnica K-Fold Cross-Validation
Na K-Fold Cross-Validation, a base de dados é dividida em K partes iguais (folds). O processo envolve K iterações, onde em cada iteração:

O modelo é treinado com K-1 folds.
O fold restante é usado como conjunto de teste.
O processo é repetido K vezes, cada vez usando um fold diferente como conjunto de teste. A performance final do modelo é a média das K avaliações.

K=5 ou K=10 são valores comuns para K.