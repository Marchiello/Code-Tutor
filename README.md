<h1 align="center">Code Tutor</h1>

## Sobre:

O projeto `Code Tutor` visa permitir com que o usuário faça exercícios de programação em diversas linguagens e tenha um feedback sobre a solução criada, permitindo com que ele veja pontos de melhora no seu código enquanto exercita sua lógica de programação.

## Considerações Importantes:
* Como o projeto faz uso de modelos de LLM locais, é recomendado ter uma placa de vídeo dedicada(melhor caso) no seu computador ou até uma integrada, desde que essa seja potente. 

* Documentação da API ( Swagger ): http://0.0.0.0:8000/docs

## Como Executar o Projeto?

### Ativar a API:

#### 1. Crie um .venv

Dentro da raíz do projeto, abra o terminal e nele, digite o comando 

`python -m venv .venv`.

#### 2. Ativar o .venv

Após criar a pasta `.venv`, caso ela não tenha sido ativada( para verificar se está ativa, veja se há algo escrito `(.venv)` na linha atual do seu terminal), digite o seguinte comando no terminal:

* No Linux:
    
    `source .venv/bin/activate`

* No Windows:
    
    `.venv\Scripts\activate.bat`

> Caso estes comandos não funcionem, pesquise outras formas de ativar seu .venv.

#### 3. Instalar as Dependências

No seu terminal com o .venv ativado, digite o comando:

`pip install -r requirements.txt`.

#### 4. Ativar a API

No seu terminal, insira:

`fastapi run main.py`

---

### Ativar o LLM Local:

O presente projeto faz uso de modelos locais de LLM para avaliação e criação de execicios/enunciados. Atualmente utilizamos o modelos com o `Ollama`. Caso desconheça o Ollama, recomendo dar uma pesquisada antes.

* Documentação Ollama: 
    - https://docs.ollama.com/

    - https://ollama.com/library/gemma4 *( Modelo utilizado atualmente )*

    - No código do projeto fui deixando as URLs das documentações que utilizei para criar o código. Para duvidas mais especificas recomendo consultar os mesmos.

**Posteriormente pretendo facilitar a utilização de APIs oficiais de LLM no projeto. Mas por enquanto segue assim:**

#### 1. Instale o Ollama no seu computador:

Link: https://ollama.com/download

#### 2. Baixe o modelo de LLM desejado:

Atualmente o projeto utiliza o modelo `gemma4:e2b`. Para instalá-lo, após baixar e configurar o ollama, digite no seu terminal:

`ollama run gemma4:e2b`

Após inserir esse comando, o modelo será baixado e, após a conclusão, começará a rodar no seu terminal.

Você pode fechar o terminal. Apenas instalar é necessário para o funcionamento da aplicação.

---

### Iniciar Frontend: