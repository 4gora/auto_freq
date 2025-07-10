
# Auto Freq

> **Este repositório foi criado com objetivos de estudo de testes automatizados.**

O objetivo é demonstrar como automatizar o acesso e o registro de frequência no portal Univirtus da Uninter utilizando ferramentas modernas de automação de browser.



## Tecnologias utilizadas
- **Python 3.11+** — linguagem principal do projeto
- **Selenium** — automação de browser para testes e interações automatizadas
- **Webdriver Manager** — gerenciamento automático do driver do navegador
- **PyYAML** — leitura de arquivos de configuração YAML
- **Google Chrome** — navegador utilizado para automação


## Instalação
1. Clone o repositório:
   ```sh
   git clone <url-do-repositorio>
   cd auto_freq
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```


## Configuração
Crie um arquivo `config.yaml` na raiz do projeto com o seguinte conteúdo:
```yaml
username: seu_usuario
password: sua_senha
```


## Uso
Execute o script principal:
```sh
python main.py
```

O script irá abrir o navegador, fazer login e navegar até a área de frequência automaticamente.


## Observações
- Não compartilhe seu `config.yaml` com outras pessoas.
- O script depende da estrutura do site Univirtus. Mudanças no site podem exigir ajustes no código.
- Este projeto é apenas para fins de estudo e demonstração de automação de testes.

> **Atenção:** Os resultados e o tempo de execução podem variar de acordo com a velocidade da sua internet, o desempenho do seu hardware e a disponibilidade dos servidores do site alvo.