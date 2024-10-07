# 🎬 Flix API

[![Django](https://img.shields.io/badge/Django-3.2+-success?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.12+-red?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-brightgreen?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=flat&logo=json-web-tokens&logoColor=white)](https://jwt.io/)

**Flix API** é uma poderosa aplicação backend desenvolvida para o gerenciamento de filmes e séries, permitindo buscar, criar, atualizar e remover registros, além de fornecer funcionalidades para avaliações e comentários. Ideal para quem deseja construir plataformas de streaming ou catálogos de filmes.

---

## 🚀 Recursos

- Gerenciamento completo de filmes e séries (CRUD).
- Busca e filtragem por título, gênero, ano de lançamento, avaliação, e mais.
- Sistema de avaliações e comentários.
- Autenticação segura com JSON Web Tokens (JWT).
- Documentação automática da API com Swagger (OpenAPI).

---

## 🛠️ Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/)** - Framework web robusto e escalável.
- **[Django Rest Framework (DRF)](https://www.django-rest-framework.org/)** - Extensão poderosa para APIs RESTful.
- **[PostgreSQL](https://www.postgresql.org/)** - Banco de dados relacional altamente escalável.
- **[Swagger](https://swagger.io/)** - Documentação interativa da API.
- **[JWT (JSON Web Tokens)](https://jwt.io/)** - Autenticação segura via tokens.

---

## 📚 Rotas da API

### Filmes

- **GET /movies/** - Lista todos os filmes.
- **POST /movies/** - Cria um novo filme.
- **GET /movies/{id}/** - Detalha um filme específico.
- **PUT /movies/{id}/** - Atualiza um filme existente.
- **DELETE /movies/{id}/** - Remove um filme.

### Séries

- **GET /series/** - Lista todas as séries.
- **POST /series/** - Cria uma nova série.

> **Nota:** A documentação completa das rotas está disponível via [Swagger](http://localhost:8000/swagger/) na aplicação rodando localmente.

---

## 🔚 Conclusão

Flix API oferece uma solução robusta e escalável para gerenciamento de filmes e séries, facilitando a criação de catálogos e plataformas de streaming. Com a combinação de Django, Django Rest Framework, PostgreSQL e autenticação JWT, esta API é altamente segura, flexível e extensível, atendendo às necessidades de diversos projetos.

A documentação clara e as funcionalidades de CRUD, busca, avaliações e mais tornam a Flix API uma base sólida para qualquer aplicação voltada para entretenimento. Sinta-se à vontade para explorar o código, contribuir com melhorias ou utilizar esta API como parte de sua próxima grande ideia no mundo dos filmes e séries!

---
