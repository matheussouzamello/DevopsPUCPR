# DevOps Somativa 1

Projeto simples em Python com Flask para cumprir as atividades formativas e a atividade somativa da disciplina de DevOps.

## Objetivos atendidos

- Aplicacao web simples versionada em Git
- Testes automatizados para CI
- Workflows de CI e CD com GitHub Actions
- Dockerfile para executar a aplicacao em container
- Documentacao com evidencias esperadas para entrega

## Endpoints

- `GET /`: retorna status, nome do projeto e versao
- `GET /health`: health check
- `GET /about`: resumo da stack usada

## Estrutura

- `app.py`: aplicacao Flask
- `tests/test_app.py`: testes automatizados
- `.github/workflows/ci.yml`: pipeline de integracao continua
- `.github/workflows/cd.yml`: pipeline de entrega continua
- `Dockerfile`: build da imagem Docker
- `docker-compose.yml`: execucao local simplificada

## Executar localmente com Docker

```powershell
docker build -t devops-somativa1 .
docker run -d -p 8000:8000 --name devops-somativa1-container devops-somativa1
docker ps
```

Acesse:

- `http://localhost:8000`
- `http://localhost:8000/health`
- `http://localhost:8000/about`

## Executar com Docker Compose

```powershell
docker compose up --build -d
docker ps
```

## Pipelines do GitHub Actions

### CI

- instala dependencias
- executa os testes unitarios

### CD

- gera a imagem Docker
- exporta a imagem como artefato do workflow

## Evidencias para o AVA

Voce precisa entregar pelo menos quatro imagens:

1. Repositorio publico com a URL visivel e o conteudo do projeto
2. Pull request com os workflows `CI` e `CD` aprovados
3. Terminal com `docker ps` mostrando o container em execucao
4. Arquivo `Dockerfile` aberto no repositorio

## Fluxo sugerido para publicar no GitHub

```powershell
git init -b main
git add .
git commit -m "chore: initial project structure"
git branch feature/ci-cd
git remote add origin <URL_DO_SEU_REPOSITORIO>
git push -u origin main
git push -u origin feature/ci-cd
```
