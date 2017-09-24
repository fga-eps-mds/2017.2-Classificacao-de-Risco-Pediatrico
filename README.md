  [![Coverage Status](https://coveralls.io/repos/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/badge.svg?branch=master)](https://coveralls.io/github/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico?branch=master)
  [![BuildStatus](https://travis-ci.org/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico.svg?branch=devel)  
# Classificação de risco na pediatria

O projeto busca melhorar a eficiência da atual classificação de risco do Hospital Materno-Infantil de Brasília, por meio de sua automatização.

O software terá como função classificar os pacientes em estados imediato,  hospitalar e ambulatorial, recomendando o local mais apropriado para o atendimento, de acordo com os sintomas verificados pelos responsáveis pela triagem.

**CRP** foi desenvolvido inicialmente por estudantes das disciplinas Métodos de Desenvolvimento de Software e Gestão de Portifólio e Projeto de Software, do curso de engenharia de software da Universidade de Brasília Faculdade do Gama.


**Se você deseja contribuir com CRP, leia a nossa [licença](https://github.com/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico/blob/master/LICENSE). Esse projeto está sob a [licença MIT](https://mit-license.org/). Ao contribuir com esse projeto, você estará de acordo com essa liceça.**


## Instalação

Para contribuir com o projeto você deve possuir o docker, docker-compose e uma conta no github, após isso clone o projeto.
  - [Download docker](https://docs.docker.com/engine/installation/)
  - [Download docker-compose](https://docs.docker.com/compose/install/)
  - Para instalar o git nos sistemas linux que utilizam o apt-get, utilize o comando

  ``` sudo apt-get install git ```

  - Para clonar o projeto, utilize o comando

  `git clone      https://github.com/fga-gpp-mds/2017.2-Classificacao-de-Risco-Pediatrico.git`

  - Após clonar o projeto entre no diretório pelo comando

  `cd 2017.2-Classificacao-de-Risco-Pediatrico`

  - Construa as imagens do docker pelo comando

  `sudo docker-compose build`

  - Faça as migrações pelo comando

  `sudo docker-compose run web python makemigrations`

  - Aplique as migrações pelo comando

  `sudo docker-compose run web python migrate`

  ## Rodando Aplicação

  - Após a realização de todos os passos suba a aplicação pelo comando

  `sudo docker-compose up`
