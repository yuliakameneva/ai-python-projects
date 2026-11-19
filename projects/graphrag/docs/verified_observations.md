# Перевірка на реальних записах (інформаційний огляд, не повний датасет)

Дата перевірки: 16.10.2026. Цей файл не є частиною корпусу для бенчмаркінгу.

1. Без пошукових фільтрів `https://api.fda.gov/drug/label.json?limit=1` повернув продукт SILICEA з `set_id=0000025c-6dbf-4af7-a741-5cbacaed519a`. У повернутому документі є `active_ingredient` та `indications_and_usage`, але немає окремих полів `contraindications` або `drug_interactions`. Отже, такі записи непридатні для пілота зі strict constraints.
2. Запит `https://api.fda.gov/drug/label.json?search=_exists_:boxed_warning` повернув інструкцію **Naproxen**:
   - `set_id`: `000155a8-709c-44e5-a75f-cd890f3a7caf`;
   - `id`: `8c45ef1f-f708-485b-bc20-60aa87ce6289`;
   - `version`: `31`; `effective_time`: `20260129`;
   - `openfda.substance_name`: `NAPROXEN`;
   - `openfda.pharm_class_epc`: `Nonsteroidal Anti-inflammatory Drug [EPC]`;
   - наявні розділи `contraindications`, `indications_and_usage`, `drug_interactions`;
   - у розділі `drug_interactions` згадані, зокрема, warfarin та aspirin. Це текстове свідчення, а не готове графове ребро `INTERACTS_WITH`.

Важливо: оригінальні тексти і справжні масиви записів отримуються **скриптом** `01_fetch_openfda.py`. Огляд вище не замінює завантаження, не є заповненим набором із 20 препаратів і не повинен використовуватися для розрахунку метрик.

Джерела:
- https://api.fda.gov/drug/label.json?limit=1
- https://api.fda.gov/drug/label.json?search=_exists_:boxed_warning
- https://open.fda.gov/apis/drug/label/
