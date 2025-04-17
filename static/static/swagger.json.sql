{
  "swagger": "2.0",
  "info": {
    "title": "API Oficina Mecânica",
    "version": "1.0"
  },
  "basePath": "/",
  "schemes": ["http"],
  "paths": {
    "/clientes": {
      "get": {
        "summary": "Listar clientes",
        "responses": {
          "200": {
            "description": "Lista de clientes"
          }
        }
      },
      "post": {
        "summary": "Cadastrar cliente",
        "parameters": [{
          "in": "body",
          "name": "cliente",
          "required": true,
          "schema": {
            "type": "object",
            "properties": {
              "nome": { "type": "string" },
              "cpf": { "type": "string" },
              "telefone": { "type": "string" },
              "endereco": { "type": "string" }
            }
          }
        }],
        "responses": {
          "201": { "description": "Cliente criado com sucesso" }
        }
      }
    },
    "/clientes/{id}": {
      "put": {
        "summary": "Atualizar cliente",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "type": "integer"
          },
          {
            "in": "body",
            "name": "cliente",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "nome": { "type": "string" },
                "cpf": { "type": "string" },
                "telefone": { "type": "string" },
                "endereco": { "type": "string" }
              }
            }
          }
        ],
        "responses": {
          "200": { "description": "Cliente atualizado com sucesso" }
        }
      },
      "delete": {
        "summary": "Deletar cliente",
        "parameters": [{
          "name": "id",
          "in": "path",
          "required": true,
          "type": "integer"
        }],
        "responses": {
          "200": { "description": "Cliente deletado com sucesso" }
        }
      }
    },
    "/veiculos": {
      "post": {
        "summary": "Cadastrar veículo",
        "parameters": [{
          "in": "body",
          "name": "veiculo",
          "required": true,
          "schema": {
            "type": "object",
            "properties": {
              "cliente_id": { "type": "integer" },
              "marca": { "type": "string" },
              "modelo": { "type": "string" },
              "placa": { "type": "string" },
              "ano_fabricacao": { "type": "integer" }
            }
          }
        }],
        "responses": {
          "201": { "description": "Veículo cadastrado com sucesso" }
        }
      }
    },
    "/veiculos/cliente/{cliente_id}": {
      "get": {
        "summary": "Listar veículos por cliente",
        "parameters": [{
          "name": "cliente_id",
          "in": "path",
          "required": true,
          "type": "integer"
        }],
        "responses": {
          "200": { "description": "Lista de veículos do cliente" }
        }
      }
    },
    "/ordens": {
      "post": {
        "summary": "Cadastrar ordem de serviço",
        "parameters": [{
          "in": "body",
          "name": "ordem",
          "required": true,
          "schema": {
            "type": "object",
            "properties": {
              "veiculo_id": { "type": "integer" },
              "data_abertura": { "type": "string" },
              "descricao": { "type": "string" },
              "status": { "type": "string" },
              "valor_estimado": { "type": "number" }
            }
          }
        }],
        "responses": {
          "201": { "description": "Ordem cadastrada com sucesso" }
        }
      }
    },
    "/ordens/veiculo/{veiculo_id}": {
      "get": {
        "summary": "Listar ordens por veículo",
        "parameters": [{
          "name": "veiculo_id",
          "in": "path",
          "required": true,
          "type": "integer"
        }],
        "responses": {
          "200": { "description": "Lista de ordens de serviço" }
        }
      }
    },
    "/ordens/status/{status}": {
      "get": {
        "summary": "Listar ordens por status",
        "parameters": [{
          "name": "status",
          "in": "path",
          "required": true,
          "type": "string"
        }],
        "responses": {
          "200": { "description": "Lista de ordens com o status especificado" }
        }
      }
    }
  }
}
