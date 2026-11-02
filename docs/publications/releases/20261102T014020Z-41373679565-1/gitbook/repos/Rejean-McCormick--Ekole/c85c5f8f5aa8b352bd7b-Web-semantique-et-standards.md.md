<!-- Frozen source: https://github.com/Rejean-McCormick/Ekole/wiki/Web-semantique-et-standards | commit: fef1626a87dbddb30df47cf9d64b75f6d49b84c3 | SHA-256: 9022c9e187f94a2a6ea486de903b27adbdbecfab81ac7b23a334591da97c2962 -->

# Web sémantique, RDF, JSON-LD et Wikidata

## L'idée de Tim Berners-Lee

L'inventeur du World Wide Web a aussi défendu le principe des **données liées (Linked Data)** : identifier les choses par des URI, rendre leurs descriptions accessibles et les relier à d'autres identifiants. Cela permet de passer d'un Web de documents à un **Web de connaissances interconnectées**.

Le modèle de référence du W3C, **RDF**, exprime des faits sous forme de triplets **sujet — propriété — objet**. Exemple conceptuel : « une fraction — possède — un dénominateur ». Les vocabulaires RDF/RDFS/OWL permettent de préciser certaines classes et propriétés. Les réalisations complexes peuvent ensuite être exportées en **JSON-LD**, une sérialisation JSON standard des données liées.

- [W3C : principes Linked Data](https://www.w3.org/wiki/LinkedData)
- [W3C : JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)

## Wikidata n'est pas Google

**Wikidata** est une base de connaissances collaborative, multilingue, structurée en entités et propriétés, capable de fournir des exports **JSON et RDF**. **Google** dispose de ses propres systèmes et de son *Knowledge Graph*; cela ne signifie pas que toutes ses réponses proviennent de Wikidata, ni que leur architecture est identique.

Pour les **données structurées des pages Web**, Google Search Central recommande généralement **JSON-LD**, avec le vocabulaire **schema.org**, lorsque ce format est approprié. Ce standard facilite l'interprétation de la page; il ne garantit pas sa visibilité dans les résultats Google.

- [Wikidata : données et exports RDF](https://www.wikidata.org/wiki/Wikidata:Database_download)
- [Google Search Central : données structurées](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=fr)

## Et Ekole ?

Les Kristals utilisent actuellement des **modèles sémantiques et fichiers JSON locaux** avec identifiants, références et relations. C'est une base favorable à une **projection** vers RDF/JSON-LD ou à des alignements avec Wikidata, **après décision de vocabulaire, mapping et validation**. Ce n'est pas un export universel déjà réalisé ou certifié.

### Exemple de forme JSON-LD envisageable

Exemple de spécification **illustrative**, non export actuel de production :

```json
{
  "@context": {
    "label": "http://www.w3.org/2000/01/rdf-schema#label",
    "requires": "https://example.org/ekole/vocab/requires"
  },
  "@id": "https://example.org/ekole/concept/fractions-equivalentes",
  "label": {"@value": "Fractions équivalentes", "@language": "fr-CA"},
  "requires": {"@id": "https://example.org/ekole/concept/parts-egales"}
}
```

Les identifiants `example.org` sont **fictifs**. En local, Ekole peut fonctionner avec des identifiants stables sans résoudre d'URL Internet au moment de la consultation. Pour publier réellement en Linked Data, une politique d'URI persistantes est nécessaire.
