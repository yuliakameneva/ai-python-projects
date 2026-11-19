// The :Entity base label makes ID lookup consistent across all entity kinds.
CREATE CONSTRAINT entity_id IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE;
CREATE INDEX drug_generic IF NOT EXISTS FOR (d:Drug) ON (d.generic_name);
CREATE INDEX label_set_id IF NOT EXISTS FOR (l:DrugLabel) ON (l.set_id);
CREATE INDEX section_field IF NOT EXISTS FOR (s:TextSection) ON (s.section_type);
CREATE INDEX chunk_section IF NOT EXISTS FOR (c:TextChunk) ON (c.section_id);
