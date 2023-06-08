# oraculum
Um projeto simples para estudos e aplicação de SQLAlchemy e PyTest, seguindo os padrões de código limpo e arquitetura limpa.

# TODO
Separar "Base" e as entidades (em models.py) em arquivos próprios. Por ora não foi possível, pois "target_metadata = Base.metadata" (em alembic/env.py) não reconhece as entidades quando "Base" e as entidades estão em arquivos próprios.