<p align="center">
 <img border="5px" width="220px" src="https://res.cloudinary.com/sigbel/image/upload/v1672948566/projects/zaturi_discord_bot/Zaturi_1_dn5t3a.png" align="center" alt="Entrance" />
 <h2 align="center">Zaturi (Discord Bot)</h2>
 <p align="center">Bot de discord para um monitoramento efetivo de investimentos e criptoativos</p>
</p>

<p align="center">
<a href="https://github.com/Sigbel/Zaturi_Discord_Bot/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/sigbel/Zaturi_Discord_Bot?color=0088ff" />
</a>
<a href="https://github.com/Sigbel/Zaturi_Discord_Bot/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/sigbel/Zaturi_Discord_Bot?color=0088ff" />
</a>

</p>
<p align="center">
<a href="#demonstração">Ver demonstração</a>
·
<a href="https://github.com/sigbel/Zaturi_Discord_Bot/issues/new/choose">Reportar erros</a>
·
<a href="https://github.com/sigbel/Zaturi_Discord_Bot/issues/new/choose">Solicitar recursos</a>
</p>

# Tópicos

- [Cuidados Iniciais](#cuidados-iniciais)
- [Comandos](#comandos)
- [Demonstrativo](#demonstrativo)

## Cuidados Iniciais

Antes de prosseguir com a utilização do bot, certifique-se de instalar todas as dependências presentes no arquivo **requirements.txt**.

Para a devida utilização do bot, faz-se necessário o uso de um token único, disponibilizado após a criação de uma aplicação no [Portal de Desenvoldores](https://discord.com/developers/applications) do Discord.

Com o token em mãos, acesse o arquivo **setup**.

- Em `BOT_TOKEN=` acrescente o token fornecido.

## Comandos 

- `help`: Informa ao usuário uma lista de comandos possíveis;
- `help (comando)`: Informa ao usuário a funcionalidade do comando e sua forma de uso;
- `price`: Busca o preço atual de um determinado criptoativo e retorna o valor na moeda especificada;
- `market`: Informa todas as informações de mercado de um criptoativo, assim como um gráfico de preços nos últimos 7 dias;
- `history`: Informa o valor do criptoativo na data especificada em todos as moedas possíveis;
- `mchart`: Apresenta um gráfico de preços a partir da data especificada até a data atual;
- `mrange`: Apresenta um gráfico de preços a partir de uma data inicial até uma final especificadas;
- `search`: Busca pelas informações de um dado criptoativo (id, nome, simbolo, rank);
- `tickers`: Busca por todos os mercados e pares possíveis para o criptoativo informado;
- `trending`: Informa uma lista dos 7 criptoativos mais procurados;
- `vsc`: Informa uma lista com todas as moedas suportadas;

## Demonstrativo:

Abaixo, alguns exemplos ilustrativos dos comandos disponíveis.

|<b>_Figura 1 - Lista de comandos_</b>|
|:--:|
|![img_1.png](https://res.cloudinary.com/sigbel/image/upload/v1672962591/projects/zaturi_discord_bot/help_aqrltu.png)|

|<b>_Figura 2 - Mercado atual do criptoativo_</b>|
|:--:|
|![img_2.png](https://res.cloudinary.com/sigbel/image/upload/v1672962591/projects/zaturi_discord_bot/market_cms8mp.png)|

|<b>_Figura 3 - Busca por um criptoativo_</b>|
|:--:|
|![img_3.png](https://res.cloudinary.com/sigbel/image/upload/v1672962994/projects/zaturi_discord_bot/search_2_y94okz.png)|


