# ProFiler

<h3>Descrição do Projeto</h3>
<p>
O ProFiler é uma aplicação de linha de comando (CLI) projetada para analisar diretórios e arquivos, gerando relatórios detalhados sobre as informações contidas nos caminhos especificados. A aplicação foi desenvolvida para ser intuitiva e fácil de usar, permitindo que os usuários obtenham rapidamente insights sobre seus arquivos.
</p>

<h3>Tecnologias Utilizadas</h3>
<ul>
<li>Python 3.x</li>
<li>pytest para testes automatizados</li>
<li>Virtualenv para gerenciamento de ambientes virtuais</li>
<li>Linters para garantir a qualidade do código</li>
</ul>

<h3>Objetivos do Projeto</h3>
<p>
O principal objetivo do ProFiler é fornecer uma ferramenta eficiente para a análise de arquivos e diretórios, resolvendo problemas de bugs e aumentando a cobertura de testes. O projeto enfatiza a importância do debugging e da implementação de testes automatizados, garantindo que a aplicação funcione corretamente e livre de erros.
</p>

<h3>Funcionalidades</h3>
<ul>
<li>
<strong>Geração de Relatórios:</strong> A aplicação gera relatórios informativos sobre arquivos e diretórios, incluindo detalhes como tamanho, tipo e data de modificação.
</li>
<li>
<strong>Correção de Bugs:</strong> O projeto inclui a identificação e correção de bugs nas funções principais, melhorando a confiabilidade da aplicação.
</li>
<li>
<strong>Testes Automatizados:</strong> Implementação de testes para as principais funcionalidades da aplicação, utilizando o pytest para garantir que o código esteja sempre funcionando conforme o esperado.
</li>
<li>
<strong>Interface de Linha de Comando:</strong> A aplicação permite aos usuários interagir facilmente via terminal, tornando a análise de arquivos acessível e rápida.
</li>
<li>
<strong>Auto-complete:</strong> A funcionalidade de auto-complete foi integrada, facilitando o uso da aplicação e melhorando a experiência do usuário.
</li>
</ul>

<h3>Requisitos de Implementação</h3>
<ul>
<li>Correção dos bugs nas funções <code>show_deepest_file</code> e <code>find_file_by_name</code>.</li>
<li>Criação de testes para as funções <code>show_preview</code>, <code>show_details</code>, <code>show_disk_usage</code> e <code>find_duplicate_files</code>.</li>
</ul>

<h3>Como Executar a Aplicação</h3>
<p>
Para utilizar o ProFiler, siga os passos abaixo:
</p>
<ol>
<li>Crie um ambiente virtual:</li>
<pre><code>python3 -m venv .venv</code></pre>
<li>Ative o ambiente virtual:</li>
<pre><code>source .venv/bin/activate</code></pre>
<li>Instale as dependências:</li>
<pre><code>python3 -m pip install -r dev-requirements.txt</code></pre>
<li>Configure o auto-complete:</li>
<pre><code>pro-filer --install-completion</code></pre>
<li>Execute o comando:</li>
<pre><code>pro-filer [caminho] [ação]</code></pre>
</ol>

<h3>Executando Testes</h3>
<p>
Para garantir que a aplicação funcione corretamente, execute os testes com o seguinte comando:
</p>
<pre><code>python3 -m pytest</code></pre>
<p>
Para uma saída mais detalhada, utilize:
</p>
<pre><code>python3 -m pytest -s -vv --continue-on-collection-errors</code></pre>

