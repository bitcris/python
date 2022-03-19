from googlesearch import search

query = input('BUSCA: ')


result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)


print(result)

#aqui teremos um pequeno sistema de buscas no Google
