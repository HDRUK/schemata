# Dataset Version Schema

```txt
#/properties/version#/properties/version
```

Dataset metadata version

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [dataset.schema.json*](../../../schema/dataset/latest/dataset.schema.json "open original schema") |

## version Type

`string` ([Dataset Version](dataset-properties-dataset-version.md))

## version Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([0-9]+)\.([0-9]+)\.([0-9]+)$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B0-9%5D%2B\)%5C.\(%5B0-9%5D%2B\)%5C.\(%5B0-9%5D%2B\)%24 "try regular expression with regexr.com")

## version Examples

```json
"1.1.0"
```
