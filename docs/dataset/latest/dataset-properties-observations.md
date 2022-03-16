# Observations Schema

```txt
#/properties/observations#/properties/observations
```

Multiple observations about the dataset may be provided and users are expected to provide at least one observation (1..\*). We will be supporting the schema.org observation model (<https://schema.org/Observation>) with default values. Users will be encouraged to provide their own statistical populations as the project progresses. Example: \<b> Statistical Population 1 \</b> type: StatisticalPopulation populationType: Persons numConstraints: 0 \<b> Statistical Population 2 \</b> type: StatisticalPopulation populationType: Events numConstraints: 0 \<b> Statistical Population 3 \</b> type: StatisticalPopulation populationType: Findings numConstraints: 0 typeOf: Observation observedNode: \<b> Statistical Population 1 \</b> measuredProperty: count measuredValue: 32937 observationDate: “2017”

> <https://schema.org/observation>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## observations Type

an array of merged types ([Details](dataset-properties-observations-items.md))
